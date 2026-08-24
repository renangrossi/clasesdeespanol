#!/usr/bin/env python3
"""
Construye cada página independiente de nivel superior: index.html,
exercises.html, extras.html, dictionary.html, irregular-verbs.html,
placement-test.html, progress.html, today-review.html,
simulated-exams.html.

Uso:
    python3 scripts/build_static_pages.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = ""

STAR = site_chrome.STAR
STARS_ROW = site_chrome.STARS_ROW
ARROW = site_chrome.ARROW_SVG
CHECK = site_chrome.CHECK_SVG


def ex_block(data):
    return f'<div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(data, ensure_ascii=False)}</script></div>'


def page_header(eyebrow, h1, lede):
    return f"""<div class="page-header">
        {STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{eyebrow}</p>
                <h1>{h1}</h1>
                <p class="page-header__lede">{lede}</p>
            </div>
        </div>
    </div>"""


def write_page(path, title, description, body_sections, active_top=None, breadcrumb_label=None,
                extra_css=None, extra_scripts=None):
    breadcrumb = None
    if breadcrumb_label:
        breadcrumb = f'<li><a href="{REL}index.html">Inicio</a></li><li aria-current="page">{breadcrumb_label}</li>'
    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=extra_css))
    out.append(site_chrome.header(REL, None, breadcrumb, active_top=active_top))
    out.extend(body_sections)
    out.append(site_chrome.footer(REL, extra_scripts=extra_scripts))
    (REPO_ROOT / path).write_text("\n".join(out), encoding="utf-8")
    print(f"Built {path}")


# =======================================================================
# INDEX
# =======================================================================
def build_index():
    hero = f"""<section class="hero" id="mission">
        <div class="hero__inner">
            {STARS_ROW}
            <div class="hero__split">
                <div>
                    <p class="eyebrow hero__eyebrow">Bienvenidos</p>
                    <h1>Bienvenido a la Academia de Renan el Profesor</h1>
                    <p class="hero__lede">Un curso de español alineado al MCER, con gramática, vocabulario y ejercicios — inmersión total: explicaciones en español, ejemplos en español real.<br>¡Empecemos!</p>
                    <div class="hero__actions">
                        <a class="btn btn--accent" href="levels/pre-a1.html">Empieza con Pre-A1 {ARROW}</a>
                        <a class="btn btn--ghost-inverse" href="placement-test.html">¿Cuál es mi nivel?</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <hr class="rule">"""

    level_grammar = {
        "Pre-A1": ["Alfabeto y sonidos", "Saludos y presentaciones", "Números y la hora", "Verbos básicos"],
        "A1": ["Ser &amp; estar", "Género &amp; artículos", "Presente regular e irregular", "El verbo gustar"],
        "A2": ["Pretérito indefinido &amp; imperfecto", "Verbos con cambio de raíz", "Pronombres de objeto", "El imperativo"],
        "B1": ["Presente de subjuntivo", "Pronombres combinados", "Futuro &amp; condicional", "Voseo argentino"],
        "B2": ["Imperfecto de subjuntivo", "Condicionales con si", "Ser/estar avanzado", "Voz pasiva"],
        "C1": ["Pluscuamperfecto de subjuntivo", "Condicionales complejas", "Registro académico", "Variación dialectal"],
        "C2": ["Sintaxis compleja", "Registro literario", "Matices léxicos", "Variación regional"],
    }
    cards = []
    romans = ["I", "II", "III", "IV", "V", "VI", "VII"]
    for i, (code, topics) in enumerate(level_grammar.items()):
        roman = romans[i]
        items = "".join(f"<li>{t}</li>" for t in topics)
        level_name = {c: n for c, n, s in site_chrome.LEVELS}[code]
        cards.append(f"""<article class="lesson-card">
            <span class="lesson-card__index" aria-hidden="true">{roman}</span>
            <h3>{code} — {level_name}</h3>
            <ul style="color:var(--color-text-muted);font-size:var(--step--1);padding-left:1.1em;list-style:disc;display:flex;flex-direction:column;gap:0.25em;">{items}</ul>
            <div class="lesson-card__actions"><a class="btn btn--ghost btn--small" href="levels/{code.lower()}.html">Abrir {code} {ARROW}</a></div>
        </article>""")

    grammar_section = f"""<section id="gramatica" class="section section--surface" aria-labelledby="gramatica-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Gramática</p>
                <h2 id="gramatica-heading">La hoja de ruta de gramática española</h2>
                <p>Un recorrido completo por la gramática española a través de siete niveles del MCER, desde tu primer ser y estar hasta el registro literario — abre cualquier nivel para ver todos los temas y empezar a practicar.</p>
            </div>
            <div class="grid">{"".join(cards)}</div>
        </div>
    </section>"""

    ladder_items = []
    ladder_desc = {
        "Pre-A1": "Primer contacto con el idioma: alfabeto, sonidos y frases mínimas para sobrevivir en español.",
        "A1": "Frases básicas y expresiones cotidianas para necesidades inmediatas.",
        "A2": "Intercambios sencillos y directos sobre temas familiares y asuntos rutinarios.",
        "B1": "Uso independiente del español para el trabajo, los estudios y los viajes.",
        "B2": "Interacción fluida y espontánea, con argumentos claros y detallados.",
        "C1": "Uso flexible y eficaz del idioma para la vida académica y profesional.",
        "C2": "Dominio preciso y matizado del español en prácticamente cualquier contexto.",
    }
    for code, name, slug in site_chrome.LEVELS:
        code_cls = "ladder__code ladder__code--compact" if len(code) > 2 else "ladder__code"
        ladder_items.append(f"""<li class="ladder__rung">
            <span class="{code_cls}" aria-hidden="true">{code}</span>
            <div class="ladder__body">
                <h3>{name}</h3>
                <p>{ladder_desc[code]} <a class="ladder__link" href="levels/{slug}.html">Entra al nivel {ARROW}</a></p>
            </div>
        </li>""")

    cefr_section = f"""<section id="sobre-mcer" class="section section--surface" aria-labelledby="mcer-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">El Marco y tu Camino a Través de Él</p>
                <h2 id="mcer-heading">Sobre el MCER</h2>
                <p>El <strong>Marco Común Europeo de Referencia para las Lenguas (MCER)</strong> es el estándar internacional para describir el nivel de dominio de un idioma. Organiza este curso en siete niveles — entra en cualquiera de ellos a continuación.</p>
            </div>
            <ol class="ladder">{"".join(ladder_items)}</ol>
        </div>
    </section>"""

    skills = [
        ("Gramática", "index.html#gramatica", "M3 8 4 8v13a1 1 0 0 0 1 1h6", "Tiempos, formas y reglas estructuradas, organizadas por nivel del MCER y conectadas con ejercicios de práctica.", '<path d="M3 5.5C3 4.7 3.7 4 4.5 4H10a2 2 0 0 1 2 2v14a1.5 1.5 0 0 0-1.5-1.5H4.5A1.5 1.5 0 0 1 3 17V5.5Z"/><path d="M21 5.5c0-.8-.7-1.5-1.5-1.5H14a2 2 0 0 0-2 2v14a1.5 1.5 0 0 1 1.5-1.5h5.5a1.5 1.5 0 0 0 1.5-1.5V5.5Z"/>'),
        ("Vocabulario", None, None, "Listas de palabras por tema que crecen junto a la gramática de cada nivel, desde los primeros sustantivos hasta colocaciones más precisas.", '<path d="M4 19V6.5A2.5 2.5 0 0 1 6.5 4H8"/><path d="M4 13h4"/><path d="M14 19V6.5A2.5 2.5 0 0 1 16.5 4H20"/><path d="M14 13h4"/>'),
        ("Ejercicios", "exercises.html", None, "Práctica adicional de lectura y vocabulario, independiente del nivel, para cualquier momento.", '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>'),
        ("Lectura", "exercises.html", None, "Textos y diálogos de estilo auténtico en español que ponen en juego la gramática y el vocabulario en contexto.", '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/>'),
        ("Escucha", "exercises.html", None, "Transcripciones de diálogos y monólogos para entrenar el oído al español hablado de forma natural.", '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3Z"/><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3Z"/>'),
        ("Escritura", None, None, "Tareas de escritura guiada que crecen desde frases sueltas hasta párrafos argumentativos bien estructurados.", '<path d="M2 22c4-1 8-3 10-5"/><path d="M22 2c-8 0-16 4-16 14 0 2 2 4 4 4C20 20 22 10 22 2Z"/>'),
        ("Conversación", None, None, "Temas de conversación para practicar y debatir en cada nivel.", '<path d="M12 15a3 3 0 0 0 3-3V6a3 3 0 0 0-6 0v6a3 3 0 0 0 3 3Z"/><path d="M19 11a7 7 0 0 1-14 0"/><path d="M12 18v3"/><path d="M9 21h6"/>'),
        ("Exámenes Simulados", "simulated-exams.html", None, "Secciones de examen simulado al estilo DELE/SIELE, con claves de respuestas, para preparar la certificación.", '<circle cx="12" cy="15" r="6"/><path d="m9 10-3-7"/><path d="m15 10 3-7"/><path d="M9.5 15.5 12 17l2.5-1.5"/>'),
    ]
    skill_cards = []
    for name, href, _, desc, icon in skills:
        tag_open = f'<a class="skill-card" href="{href}">' if href else '<div class="skill-card">'
        tag_close = "</a>" if href else "</div>"
        skill_cards.append(f'{tag_open}<svg class="skill-card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icon}</svg><h3>{name}</h3><p>{desc}</p>{tag_close}')

    skills_section = f"""<section id="skills" class="section" aria-labelledby="skills-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Un Currículo Completo</p>
                <h2 id="skills-heading">Todas las destrezas, cubiertas</h2>
                <p>Cada nivel del MCER trabaja las mismas destrezas clave, para no dejar nada al azar.</p>
            </div>
            <div class="grid grid--4">{"".join(skill_cards)}</div>
        </div>
    </section>"""

    why_section = f"""<section id="why-us" class="section section--surface" aria-labelledby="why-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Por Qué Aprender con Nosotros</p>
                <h2 id="why-heading">Un curso hecho para generar confianza</h2>
            </div>
            <div class="grid grid--3" style="max-width:70rem;margin:0 auto;">
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15 9-2 6-6 2 2-6 6-2Z"/></svg></span>
                    <h3>Organizado según el MCER</h3>
                    <p>Cada lección está vinculada al Marco Común Europeo, así siempre sabes exactamente en qué punto estás y qué sigue.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></span>
                    <h3>Aprende a tu propio ritmo</h3>
                    <p>Avanza nivel por nivel o entra directamente a los ejercicios, el diccionario o el repaso de hoy cuando necesites práctica extra.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.5 4 5.7 4 9s-1.5 6.5-4 9c-2.5-2.5-4-5.7-4-9s1.5-6.5 4-9Z"/></svg></span>
                    <h3>Basado en español real</h3>
                    <p>Ejemplos y diálogos naturales, no relleno de manual artificial — y cada punto de gramática viene con los errores comunes que hay que evitar.</p>
                </div>
            </div>
        </div>
    </section>"""

    cta = f"""<section class="cta-band" aria-labelledby="cta-heading">
        {STARS_ROW}
        <p class="eyebrow" style="justify-content:center;">Empieza cuando quieras</p>
        <h2 id="cta-heading">Disfruta el camino — empieza hoy con tu nivel.</h2>
        <p>¿No sabes por dónde empezar? Haz la prueba de nivel, o simplemente empieza en Pre-A1 y avanza paso a paso.</p>
        <div class="hero__actions">
            <a class="btn btn--accent" href="levels/pre-a1.html">Explora todos los niveles {ARROW}</a>
            <a class="btn btn--ghost-inverse" href="placement-test.html">¿Cuál es mi nivel?</a>
        </div>
    </section>"""

    write_page(
        "index.html",
        "Renan el Profesor — Academia de Español",
        "Un curso de español alineado al MCER con gramática, vocabulario, lectura, escucha, escritura, conversación y exámenes simulados, organizado nivel por nivel de Pre-A1 a C2.",
        [hero, grammar_section, cefr_section, skills_section, why_section, cta],
        active_top="home",
        extra_scripts=[],
    )


# =======================================================================
# EXERCISES
# =======================================================================
def build_exercises():
    header = page_header("Práctica Independiente", "Ejercicios",
                          "Práctica adicional de lectura y vocabulario, independiente del nivel — entra cuando quieras.")

    items = [
        ("A2", "Un Correo de una Amiga", "<p>¡Hola Marta! ¿Cómo estás? Yo estoy muy bien. El sábado pasado fui al mercado con mi madre y compramos muchísima fruta fresca. Después comimos en un bar pequeño cerca de casa.</p><p>El próximo fin de semana voy a la playa con unas amigas. ¡No veo la hora! ¿Tú qué planes tienes para este fin de semana? ¡Escríbeme pronto!<br>Un abrazo,<br>Laura</p>",
         {"id": "ex-a2-correo", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
             {"id": "exa2m1", "statement": "Laura fue al mercado con su madre.", "answer": True, "explanation": "«Fui al mercado con mi madre.»"},
             {"id": "exa2m2", "statement": "Laura va a la montaña el próximo fin de semana.", "answer": False, "explanation": "Va a la playa (el mar), no a la montaña."},
         ]}),
        ("B1", "Un Anuncio de Trabajo", "<p><strong>Se busca camarero/a para restaurante en el centro de Sevilla.</strong> Se requiere experiencia mínima de un año en el sector de la hostelería. Turnos flexibles, también los fines de semana. Se valora el conocimiento de inglés. Sueldo según experiencia. Para postularse, enviar el currículum a empleo@restaurantesevilla.es antes del viernes.</p>",
         {"id": "ex-b1-anuncio", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
             {"id": "exb1a1", "prompt": "¿Cuánta experiencia se requiere?", "options": ["No se requiere experiencia", "Al menos un año", "Al menos cinco años"], "answerIndex": 1, "explanation": "«Se requiere experiencia mínima de un año.»"},
             {"id": "exb1a2", "prompt": "¿Qué se valora como un plus?", "options": ["Tener coche propio", "Saber inglés", "Vivir cerca"], "answerIndex": 1, "explanation": "«Se valora el conocimiento de inglés.»"},
         ]}),
        ("B2", "Una Reseña de Restaurante", "<p>Era escéptico antes de reservar, dado el gran número de reseñas contradictorias en internet. Sin embargo, mi experiencia fue claramente positiva. El servicio, aunque no impecable, fue amable, y los platos —en particular los primeros— estaban preparados con cuidado e ingredientes de calidad. Único punto negativo: los tiempos de espera entre un plato y otro fueron bastante largos.</p>",
         {"id": "ex-b2-resena", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
             {"id": "exb2r1", "statement": "La impresión general del autor fue positiva.", "answer": True, "explanation": "«Mi experiencia fue claramente positiva.»"},
             {"id": "exb2r2", "statement": "El plato principal se menciona como lo peor de la comida.", "answer": False, "explanation": "Los primeros platos fueron elogiados; la queja fue sobre los tiempos de espera entre platos."},
         ]}),
        ("C1", "Un Breve Artículo sobre el Día de los Muertos", "<p>El Día de los Muertos, celebrado principalmente en México cada 1 y 2 de noviembre, continúa atrayendo cada año a millones de visitantes, atraídos tanto por su inigualable riqueza simbólica como por la atmósfera única de sus altares y desfiles. A pesar de los desafíos que plantea el turismo masivo —desde la gestión de las multitudes hasta la preservación del sentido original de la festividad—, las comunidades han sabido, en los últimos años, desarrollar formas más sostenibles de compartir la tradición, animando a los visitantes a conocer también las costumbres de los pueblos menos frecuentados.</p>",
         {"id": "ex-c1-diadelosmuertos", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
             {"id": "exc1f1", "prompt": "¿Qué desafío menciona el artículo?", "options": ["La falta de altares tradicionales", "La gestión del turismo masivo", "La escasez de flores de cempasúchil"], "answerIndex": 1, "explanation": "Se menciona directamente «los desafíos que plantea el turismo masivo»."},
         ]}),
        ("Pre-A1", "Un Mensaje de Texto", "<p>Hola, soy Pedro. Estoy en la calle Mayor, cerca del banco. ¿Dónde estás tú? Yo tengo hambre, ¿comemos algo? Hay un restaurante muy bueno aquí. Te espero a las dos.</p>",
         {"id": "ex-pa1-mensaje", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "expa1a", "statement": "Pedro está cerca del banco.", "answer": True, "explanation": "El texto dice: «Estoy en la calle Mayor, cerca del banco»."},
            {"id": "expa1b", "statement": "Pedro no tiene hambre.", "answer": False, "explanation": "El texto dice: «Yo tengo hambre»."},
            {"id": "expa1c", "statement": "Pedro espera a la otra persona a las dos.", "answer": True, "explanation": "El texto dice: «Te espero a las dos»."},
         ]}),
        ("Pre-A1", "En la Cafetería de la Universidad", "<p>—Hola, ¿qué quieres tomar?<br>—Un café, por favor. ¿Y tú?<br>—Yo quiero un té con leche.<br>—Perfecto, son tres euros en total.</p>",
         {"id": "ex-pa1-cafeteria", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "expa1d", "prompt": "¿Qué pide la primera persona?", "options": ["Un té", "Un café", "Un jugo"], "answerIndex": 1, "explanation": "El texto dice: «Un café, por favor»."},
            {"id": "expa1e", "prompt": "¿Cuánto cuesta todo en total?", "options": ["Dos euros", "Tres euros", "Cuatro euros"], "answerIndex": 1, "explanation": "El texto dice: «son tres euros en total»."},
         ]}),
        ("A1", "Presentando a la Familia", "<p>Esta es mi familia. Mi padre se llama Antonio y es ingeniero. Mi madre se llama Carmen y es profesora. Tengo dos hermanos: Pablo, que tiene quince años, y Lucía, que tiene diez años. Vivimos en un piso pequeño pero muy cómodo.</p>",
         {"id": "ex-a1-familia", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa1fa1", "prompt": "¿Cuál es la profesión del padre?", "options": ["Profesor", "Ingeniero", "Médico"], "answerIndex": 1, "explanation": "El texto dice: «Mi padre se llama Antonio y es ingeniero»."},
            {"id": "exa1fa2", "prompt": "¿Cuántos años tiene Lucía?", "options": ["Diez", "Quince", "Veinte"], "answerIndex": 0, "explanation": "El texto dice: «Lucía, que tiene diez años»."},
            {"id": "exa1fa3", "prompt": "¿Cómo es el piso de la familia?", "options": ["Grande y lujoso", "Pequeño pero cómodo", "Viejo y feo"], "answerIndex": 1, "explanation": "El texto dice: «un piso pequeño pero muy cómodo»."},
         ]}),
        ("A1", "Un Anuncio de Piso Compartido", "<p>Se busca compañero de piso para apartamento en el centro. Habitación individual con ventana grande. Precio: 350 euros al mes, gastos incluidos. Cerca del metro y de muchas tiendas. Llamar solo por las tardes.</p>",
         {"id": "ex-a1-piso", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa1pi1", "statement": "El apartamento está en el centro.", "answer": True, "explanation": "El texto dice: «apartamento en el centro»."},
            {"id": "exa1pi2", "statement": "El precio no incluye los gastos.", "answer": False, "explanation": "El texto dice: «gastos incluidos»."},
            {"id": "exa1pi3", "statement": "Se puede llamar a cualquier hora.", "answer": False, "explanation": "El texto dice: «Llamar solo por las tardes»."},
         ]}),
        ("A2", "Un Fin de Semana en la Montaña", "<p>El fin de semana pasado fuimos a la montaña con unos amigos. Caminamos casi seis horas el sábado y llegamos muy cansados al refugio. Por la noche cenamos comida típica de la zona y dormimos muy bien. El domingo, antes de volver, visitamos un pequeño pueblo cercano.</p>",
         {"id": "ex-a2-montana", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa2mo1", "prompt": "¿Cuánto tiempo caminaron el sábado?", "options": ["Cuatro horas", "Seis horas", "Ocho horas"], "answerIndex": 1, "explanation": "El texto dice: «Caminamos casi seis horas el sábado»."},
            {"id": "exa2mo2", "prompt": "¿Dónde durmieron?", "options": ["En un hotel", "En el refugio", "En una tienda de campaña"], "answerIndex": 1, "explanation": "El texto dice: «llegamos muy cansados al refugio»."},
            {"id": "exa2mo3", "prompt": "¿Qué hicieron el domingo antes de volver?", "options": ["Descansaron todo el día", "Visitaron un pueblo cercano", "Caminaron otra vez seis horas"], "answerIndex": 1, "explanation": "El texto dice: «visitamos un pequeño pueblo cercano»."},
         ]}),
        ("A2", "Una Queja por un Vuelo Cancelado", "<p>Estimados señores, les escribo porque mi vuelo del pasado lunes fue cancelado sin previo aviso. Esperé cuatro horas en el aeropuerto sin recibir ninguna información. Al final, tuve que comprar otro billete con otra compañía. Solicito una compensación por los gastos adicionales.</p>",
         {"id": "ex-a2-queja", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa2q1", "statement": "El vuelo se canceló sin aviso previo.", "answer": True, "explanation": "El texto dice: «fue cancelado sin previo aviso»."},
            {"id": "exa2q2", "statement": "La persona esperó dos horas en el aeropuerto.", "answer": False, "explanation": "El texto dice que esperó cuatro horas."},
            {"id": "exa2q3", "statement": "La persona pide una compensación económica.", "answer": True, "explanation": "El texto dice: «Solicito una compensación por los gastos adicionales»."},
         ]}),
        ("B1", "El Debate sobre las Redes Sociales", "<p>Cada vez más estudios señalan los efectos del uso excesivo de las redes sociales en la salud mental de los jóvenes. Sin embargo, muchos defienden que estas plataformas también facilitan la conexión social y el acceso a la información. El verdadero reto, según los expertos, está en encontrar un equilibrio saludable.</p>",
         {"id": "ex-b1-redes", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb1re1", "prompt": "¿Qué señalan los estudios mencionados?", "options": ["Los beneficios de las redes sociales", "Los efectos del uso excesivo en la salud mental", "El precio de los teléfonos"], "answerIndex": 1, "explanation": "El texto dice: «los efectos del uso excesivo de las redes sociales en la salud mental»."},
            {"id": "exb1re2", "prompt": "¿Qué defienden algunas personas sobre las redes sociales?", "options": ["Que deberían prohibirse", "Que facilitan la conexión social", "Que no sirven para nada"], "answerIndex": 1, "explanation": "El texto dice: «facilitan la conexión social y el acceso a la información»."},
            {"id": "exb1re3", "prompt": "¿Cuál es el verdadero reto, según los expertos?", "options": ["Prohibir las redes", "Encontrar un equilibrio saludable", "Usarlas más"], "answerIndex": 1, "explanation": "El texto termina: «el verdadero reto... está en encontrar un equilibrio saludable»."},
         ]}),
        ("B1", "Una Biografía Breve", "<p>Frida Kahlo nació en Coyoacán, México, en 1907. Después de sufrir un grave accidente de autobús a los dieciocho años, empezó a pintar durante su larga recuperación. Su obra, llena de color y simbolismo, refleja tanto su dolor físico como su identidad mexicana. Hoy es una de las artistas más reconocidas del mundo.</p>",
         {"id": "ex-b1-frida", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb1fr1", "statement": "Frida Kahlo nació en 1907.", "answer": True, "explanation": "El texto dice: «nació en Coyoacán, México, en 1907»."},
            {"id": "exb1fr2", "statement": "Empezó a pintar antes del accidente.", "answer": False, "explanation": "El texto dice que empezó a pintar «durante su larga recuperación», es decir, después del accidente."},
            {"id": "exb1fr3", "statement": "Su obra refleja su identidad mexicana.", "answer": True, "explanation": "El texto dice: «refleja tanto su dolor físico como su identidad mexicana»."},
         ]}),
        ("B2", "El Auge del Turismo Sostenible", "<p>En los últimos años, cada vez más viajeros buscan opciones de turismo sostenible que minimicen el impacto ambiental de sus desplazamientos. Esta tendencia ha impulsado a numerosos hoteles y agencias a adoptar prácticas más responsables, desde la reducción de plásticos hasta el apoyo a comunidades locales. No obstante, algunos críticos advierten que ciertas iniciativas son más una estrategia de marketing que un compromiso real.</p>",
         {"id": "ex-b2-turismo", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb2tu1", "prompt": "¿Qué buscan cada vez más viajeros?", "options": ["Vuelos más baratos", "Turismo sostenible", "Hoteles de lujo"], "answerIndex": 1, "explanation": "El texto dice: «cada vez más viajeros buscan opciones de turismo sostenible»."},
            {"id": "exb2tu2", "prompt": "¿Qué prácticas han adoptado hoteles y agencias?", "options": ["Subir los precios", "Reducir plásticos y apoyar a comunidades locales", "Cerrar temporalmente"], "answerIndex": 1, "explanation": "El texto menciona «la reducción de plásticos hasta el apoyo a comunidades locales»."},
            {"id": "exb2tu3", "prompt": "¿Qué advierten algunos críticos?", "options": ["Que el turismo sostenible no existe", "Que algunas iniciativas son solo marketing", "Que cuesta demasiado dinero"], "answerIndex": 1, "explanation": "El texto dice: «ciertas iniciativas son más una estrategia de marketing que un compromiso real»."},
         ]}),
        ("B2", "La Inteligencia Artificial en el Aula", "<p>La incorporación de herramientas de inteligencia artificial en las aulas plantea tanto oportunidades como desafíos considerables. Por un lado, permite personalizar el aprendizaje según el ritmo de cada estudiante. Por otro, genera preocupación entre los docentes sobre la dependencia excesiva de la tecnología y la posible pérdida de habilidades de pensamiento crítico.</p>",
         {"id": "ex-b2-ia", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb2ia1", "statement": "La IA en el aula solo genera oportunidades, sin ningún desafío.", "answer": False, "explanation": "El texto dice que plantea «tanto oportunidades como desafíos considerables»."},
            {"id": "exb2ia2", "statement": "La IA permite personalizar el aprendizaje.", "answer": True, "explanation": "El texto dice: «permite personalizar el aprendizaje según el ritmo de cada estudiante»."},
            {"id": "exb2ia3", "statement": "Algunos docentes están preocupados por la dependencia de la tecnología.", "answer": True, "explanation": "El texto dice: «genera preocupación entre los docentes sobre la dependencia excesiva de la tecnología»."},
         ]}),
        ("C1", "Reflexiones sobre el Silencio", "<p>Vivimos en una época que parece rehuir el silencio como si fuera una amenaza. Notificaciones, música de fondo, conversaciones constantes: todo conspira para llenar cada instante de estímulo sonoro. Sin embargo, numerosos estudios sugieren que los momentos de silencio deliberado favorecen la creatividad, la memoria y el bienestar emocional, algo que las tradiciones contemplativas llevan siglos afirmando sin necesidad de evidencia científica.</p>",
         {"id": "ex-c1-silencio", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exc1si1", "prompt": "¿Cómo describe el texto la relación actual con el silencio?", "options": ["Se busca activamente", "Se rehúye, como una amenaza", "Es indiferente"], "answerIndex": 1, "explanation": "El texto dice: «Vivimos en una época que parece rehuir el silencio como si fuera una amenaza»."},
            {"id": "exc1si2", "prompt": "¿Qué favorecen los momentos de silencio deliberado, según los estudios?", "options": ["El estrés", "La creatividad, la memoria y el bienestar emocional", "El aburrimiento"], "answerIndex": 1, "explanation": "El texto dice: «favorecen la creatividad, la memoria y el bienestar emocional»."},
            {"id": "exc1si3", "prompt": "¿Qué relación establece el texto con las tradiciones contemplativas?", "options": ["Que las contradicen", "Que afirmaban esto sin evidencia científica", "Que no tienen relación"], "answerIndex": 1, "explanation": "El texto dice que estas tradiciones «llevan siglos afirmando» lo mismo «sin necesidad de evidencia científica»."},
         ]}),
        ("C1", "El Debate sobre la Traducción Literaria", "<p>Toda traducción literaria implica, inevitablemente, una serie de pérdidas y ganancias que rara vez pasan desapercibidas para el lector atento. Quienes defienden la fidelidad absoluta al original olvidan, a menudo, que cada lengua organiza la realidad de forma distinta, de modo que una traslación literal puede resultar, paradójicamente, menos fiel al espíritu del texto que una versión más libre pero más sensible al contexto cultural de llegada.</p>",
         {"id": "ex-c1-traduccion", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exc1tr1", "statement": "El texto afirma que la traducción literaria nunca implica pérdidas.", "answer": False, "explanation": "El texto dice que implica «inevitablemente, una serie de pérdidas y ganancias»."},
            {"id": "exc1tr2", "statement": "Según el texto, una traducción literal siempre es la más fiel.", "answer": False, "explanation": "El texto dice que puede resultar «paradójicamente, menos fiel al espíritu del texto»."},
            {"id": "exc1tr3", "statement": "El texto valora considerar el contexto cultural de llegada.", "answer": True, "explanation": "El texto menciona positivamente «una versión más libre pero más sensible al contexto cultural de llegada»."},
         ]}),
        ("C2", "Sobre la Memoria Colectiva", "<p>La memoria colectiva no es, como a menudo se supone ingenuamente, un mero archivo pasivo de hechos compartidos, sino una construcción activa y en permanente disputa, moldeada tanto por quienes detentan el poder de narrar el pasado como por quienes se resisten a esa narración oficial. Cada generación, en última instancia, reescribe su historia según las urgencias del presente que la interroga.</p>",
         {"id": "ex-c2-memoria", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exc2me1", "prompt": "¿Cómo describe el texto la memoria colectiva?", "options": ["Un archivo pasivo de hechos", "Una construcción activa y en disputa", "Algo que no cambia nunca"], "answerIndex": 1, "explanation": "El texto dice que es «una construcción activa y en permanente disputa»."},
            {"id": "exc2me2", "prompt": "¿Quiénes moldean esa memoria, según el texto?", "options": ["Solo los historiadores", "Quienes narran el pasado y quienes se resisten a esa narración", "Nadie en particular"], "answerIndex": 1, "explanation": "El texto menciona a «quienes detentan el poder de narrar» y a «quienes se resisten a esa narración oficial»."},
            {"id": "exc2me3", "prompt": "¿Qué hace cada generación, según el texto?", "options": ["Ignora el pasado por completo", "Reescribe su historia según el presente", "Repite exactamente la misma historia"], "answerIndex": 1, "explanation": "El texto termina: «Cada generación... reescribe su historia según las urgencias del presente»."},
         ]}),
        ("Pre-A1", "Números de Teléfono", "<p>—¿Cuál es tu número de teléfono?<br>—Es el seis, dos, cuatro, ocho, uno, cinco, cero, tres.<br>—¿Puedes repetirlo, por favor?<br>—Claro: seis, dos, cuatro, ocho, uno, cinco, cero, tres.</p>",
         {"id": "ex-pa1-telefono", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "expa1f1", "statement": "La persona repite el número dos veces.", "answer": True, "explanation": "El texto muestra el número dicho, y luego repetido tras la petición."},
            {"id": "expa1f2", "statement": "El número empieza por siete.", "answer": False, "explanation": "El número empieza por seis."},
         ]}),
        ("Pre-A1", "En la Farmacia", "<p>—Buenos días, necesito algo para el dolor de cabeza.<br>—Tenemos estas pastillas. ¿Alguna alergia?<br>—No, ninguna.<br>—Perfecto, son cinco euros.</p>",
         {"id": "ex-pa1-farmacia", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "expa1g1", "prompt": "¿Qué necesita la persona?", "options": ["Algo para dormir", "Algo para el dolor de cabeza", "Vitaminas"], "answerIndex": 1, "explanation": "El texto dice: «necesito algo para el dolor de cabeza»."},
            {"id": "expa1g2", "prompt": "¿Tiene alguna alergia?", "options": ["Sí", "No"], "answerIndex": 1, "explanation": "El texto dice: «No, ninguna»."},
         ]}),
        ("A1", "Un Correo de Bienvenida", "<p>Bienvenido a nuestra academia de español. Las clases empiezan el lunes a las nueve de la mañana. Necesitas traer un cuaderno y un bolígrafo. Si tienes dudas, puedes escribirnos a info@academia.es o llamarnos por teléfono.</p>",
         {"id": "ex-a1-bienvenida", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa1h1", "statement": "Las clases empiezan un lunes.", "answer": True, "explanation": "El texto dice: «Las clases empiezan el lunes»."},
            {"id": "exa1h2", "statement": "Hay que traer una computadora.", "answer": False, "explanation": "El texto dice que hay que traer «un cuaderno y un bolígrafo»."},
            {"id": "exa1h3", "statement": "Se puede escribir un correo si hay dudas.", "answer": True, "explanation": "El texto dice: «puedes escribirnos a info@academia.es»."},
         ]}),
        ("A1", "Mi Barrio", "<p>Vivo en un barrio tranquilo con muchas tiendas pequeñas. Hay una panadería, una farmacia y un parque muy bonito cerca de mi casa. Los vecinos son amables y siempre nos saludamos por la calle.</p>",
         {"id": "ex-a1-barrio", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa1i1", "prompt": "¿Cómo es el barrio?", "options": ["Ruidoso", "Tranquilo", "Peligroso"], "answerIndex": 1, "explanation": "El texto dice: «Vivo en un barrio tranquilo»."},
            {"id": "exa1i2", "prompt": "¿Qué hay cerca de la casa?", "options": ["Un hospital", "Un parque bonito", "Una escuela"], "answerIndex": 1, "explanation": "El texto dice: «un parque muy bonito cerca de mi casa»."},
         ]}),
        ("A2", "Una Receta Fácil", "<p>Para hacer esta ensalada, necesitas lechuga, tomate, cebolla y un poco de aceite de oliva. Primero, lava y corta todas las verduras. Después, mezcla todo en un bol grande. Por último, añade sal y un poco de vinagre al gusto.</p>",
         {"id": "ex-a2-receta", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa2rc1", "statement": "La receta lleva carne.", "answer": False, "explanation": "La receta es una ensalada con lechuga, tomate, cebolla y aceite."},
            {"id": "exa2rc2", "statement": "Primero se lavan y cortan las verduras.", "answer": True, "explanation": "El texto dice: «Primero, lava y corta todas las verduras»."},
         ]}),
        ("A2", "Un Fin de Semana Diferente", "<p>Normalmente paso los fines de semana en casa, pero este sábado decidí hacer algo diferente: fui a un concierto al aire libre con unos amigos. La música fue increíble y conocimos a mucha gente nueva. Fue una experiencia que no voy a olvidar fácilmente.</p>",
         {"id": "ex-a2-concierto", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa2co1", "prompt": "¿Qué suele hacer la persona normalmente los fines de semana?", "options": ["Ir a conciertos", "Quedarse en casa", "Viajar"], "answerIndex": 1, "explanation": "El texto dice: «Normalmente paso los fines de semana en casa»."},
            {"id": "exa2co2", "prompt": "¿Con quién fue al concierto?", "options": ["Sola", "Con unos amigos", "Con su familia"], "answerIndex": 1, "explanation": "El texto dice: «fui a un concierto al aire libre con unos amigos»."},
         ]}),
        ("A2", "Cambios en el Barrio", "<p>Cuando era pequeño, en mi calle solo había casas antiguas y un pequeño quiosco. Ahora hay varios edificios nuevos y un centro comercial grande. Aunque el barrio cambió mucho, todavía me gusta caminar por las mismas calles de mi infancia.</p>",
         {"id": "ex-a2-cambios", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exa2ca1", "statement": "Antes había un centro comercial grande.", "answer": False, "explanation": "El texto dice que antes «solo había casas antiguas y un pequeño quiosco»."},
            {"id": "exa2ca2", "statement": "A la persona le sigue gustando caminar por el barrio.", "answer": True, "explanation": "El texto dice: «todavía me gusta caminar por las mismas calles»."},
         ]}),
        ("B1", "El Impacto del Ejercicio en la Salud Mental", "<p>Numerosos estudios confirman que el ejercicio regular no solo mejora la condición física, sino que también reduce significativamente los niveles de estrés y ansiedad. Los expertos recomiendan al menos treinta minutos de actividad moderada, como caminar o nadar, varias veces por semana.</p>",
         {"id": "ex-b1-ejercicio", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb1ej1", "prompt": "¿Qué reduce el ejercicio regular, según el texto?", "options": ["El apetito", "El estrés y la ansiedad", "La memoria"], "answerIndex": 1, "explanation": "El texto dice: «reduce significativamente los niveles de estrés y ansiedad»."},
            {"id": "exb1ej2", "prompt": "¿Cuánto tiempo recomiendan los expertos?", "options": ["Quince minutos", "Treinta minutos", "Una hora"], "answerIndex": 1, "explanation": "El texto dice: «al menos treinta minutos de actividad moderada»."},
         ]}),
        ("B1", "Un Correo sobre un Malentendido", "<p>Hola Marcos, quería aclarar el malentendido de ayer. Creo que no me expliqué bien en la reunión y por eso pensaste que yo estaba en desacuerdo con tu propuesta. En realidad, me pareció una idea excelente. Espero que podamos hablarlo con calma mañana.</p>",
         {"id": "ex-b1-malentendido", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb1ma1", "statement": "La persona estaba en desacuerdo con la propuesta.", "answer": False, "explanation": "El texto dice: «me pareció una idea excelente»."},
            {"id": "exb1ma2", "statement": "El malentendido ocurrió por una mala explicación.", "answer": True, "explanation": "El texto dice: «creo que no me expliqué bien en la reunión»."},
         ]}),
        ("B1", "La Importancia de Dormir Bien", "<p>Dormir menos de seis horas por noche de forma habitual puede afectar la concentración, el estado de ánimo y hasta el sistema inmunológico. Los especialistas sugieren mantener horarios regulares para dormir y evitar las pantallas al menos una hora antes de acostarse.</p>",
         {"id": "ex-b1-dormir", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb1do1", "prompt": "¿Qué puede afectar dormir poco?", "options": ["Solo el estado de ánimo", "La concentración, el ánimo y el sistema inmunológico", "Nada importante"], "answerIndex": 1, "explanation": "El texto menciona los tres efectos."},
            {"id": "exb1do2", "prompt": "¿Qué sugieren los especialistas antes de dormir?", "options": ["Hacer ejercicio", "Evitar las pantallas", "Comer algo"], "answerIndex": 1, "explanation": "El texto dice: «evitar las pantallas al menos una hora antes de acostarse»."},
         ]}),
        ("B2", "El Regreso de los Discos de Vinilo", "<p>En una era dominada por el streaming musical, resulta llamativo el resurgimiento de los discos de vinilo entre las nuevas generaciones. Más allá de la calidad de sonido, muchos jóvenes valoran la experiencia física de poseer un objeto tangible y el ritual de escuchar un álbum completo, sin las distracciones habituales de las plataformas digitales.</p>",
         {"id": "ex-b2-vinilo", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb2vi1", "prompt": "¿Qué valoran muchos jóvenes en el vinilo, además del sonido?", "options": ["El precio bajo", "La experiencia física de un objeto tangible", "La portabilidad"], "answerIndex": 1, "explanation": "El texto dice: «valoran la experiencia física de poseer un objeto tangible»."},
            {"id": "exb2vi2", "prompt": "¿Qué evita el ritual de escuchar un vinilo, según el texto?", "options": ["El silencio", "Las distracciones digitales", "El costo"], "answerIndex": 1, "explanation": "El texto dice «sin las distracciones habituales de las plataformas digitales»."},
         ]}),
        ("B2", "El Dilema del Crecimiento Urbano", "<p>Las grandes ciudades enfrentan un dilema constante entre el crecimiento económico y la calidad de vida de sus habitantes. Mientras la expansión urbana atrae inversión y empleo, también genera problemas como la congestión del tráfico, la contaminación y el encarecimiento de la vivienda, especialmente para las familias de menores ingresos.</p>",
         {"id": "ex-b2-urbano", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exb2ur1", "statement": "El crecimiento urbano no tiene ninguna desventaja.", "answer": False, "explanation": "El texto menciona congestión, contaminación y encarecimiento de la vivienda."},
            {"id": "exb2ur2", "statement": "El encarecimiento de la vivienda afecta especialmente a las familias con menos ingresos.", "answer": True, "explanation": "El texto lo dice explícitamente al final."},
         ]}),
        ("C1", "La Paradoja de la Elección", "<p>Contrariamente a la intuición, disponer de un número excesivo de opciones no siempre facilita la toma de decisiones; con frecuencia, la abundancia de alternativas genera una parálisis decisoria que termina por generar insatisfacción, incluso cuando la elección final resulta objetivamente satisfactoria. Este fenómeno, documentado extensamente en psicología del consumidor, cuestiona la premisa de que más opciones equivalen siempre a mayor libertad.</p>",
         {"id": "ex-c1-eleccion", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exc1el1", "prompt": "¿Qué puede generar un exceso de opciones?", "options": ["Mayor satisfacción siempre", "Parálisis decisoria", "Decisiones más rápidas"], "answerIndex": 1, "explanation": "El texto dice: «genera una parálisis decisoria»."},
            {"id": "exc1el2", "prompt": "¿Qué premisa cuestiona este fenómeno?", "options": ["Que menos opciones son mejores", "Que más opciones equivalen siempre a mayor libertad", "Que las decisiones no importan"], "answerIndex": 1, "explanation": "El texto termina cuestionando exactamente esa premisa."},
         ]}),
        ("C1", "Sobre la Procrastinación", "<p>Lejos de ser un simple problema de gestión del tiempo, la procrastinación crónica suele estar vinculada a mecanismos de regulación emocional: postergar una tarea desagradable ofrece un alivio inmediato, aunque a costa de un malestar mayor a largo plazo. Comprender esta dimensión emocional resulta esencial para diseñar estrategias verdaderamente eficaces contra este hábito.</p>",
         {"id": "ex-c1-procrastinacion", "type": "true-false", "title": "Comprobación de Comprensión", "items": [
            {"id": "exc1pr1", "statement": "El texto reduce la procrastinación a un problema de gestión del tiempo.", "answer": False, "explanation": "El texto dice que está «lejos de ser un simple problema de gestión del tiempo»."},
            {"id": "exc1pr2", "statement": "Postergar una tarea ofrece un alivio inmediato.", "answer": True, "explanation": "El texto dice: «postergar una tarea desagradable ofrece un alivio inmediato»."},
         ]}),
        ("C2", "La Ilusión de la Objetividad Periodística", "<p>Pretender una objetividad absoluta en el ejercicio periodístico constituye, cuando menos, una aspiración ingenua: toda selección de qué hechos narrar, en qué orden y con qué términos, implica ya una toma de posición, por sutil que esta resulte. Reconocer esta condición no equivale a renunciar al rigor informativo, sino a asumir con honestidad intelectual los límites inherentes a cualquier narración de la realidad.</p>",
         {"id": "ex-c2-objetividad", "type": "multiple-choice", "title": "Comprobación de Comprensión", "items": [
            {"id": "exc2ob1", "prompt": "¿Cómo describe el texto la objetividad absoluta en periodismo?", "options": ["Un logro alcanzable fácilmente", "Una aspiración ingenua", "Algo irrelevante"], "answerIndex": 1, "explanation": "El texto dice: «constituye, cuando menos, una aspiración ingenua»."},
            {"id": "exc2ob2", "prompt": "¿Qué implica toda selección de hechos, según el texto?", "options": ["Nada en particular", "Ya una toma de posición", "Una mentira deliberada"], "answerIndex": 1, "explanation": "El texto dice que «implica ya una toma de posición, por sutil que esta resulte»."},
         ]}),
    ]
    sections = [header]
    for level, title, passage, ex in items:
        sections.append(f"""<section class="section section--surface" aria-labelledby="ex-{ex['id']}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level}</p>
                <h2 id="ex-{ex['id']}-heading">{title}</h2>
                <div class="card"><div class="prose">{passage}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(ex)}</div>
            </div>
        </section>""")

    write_page("exercises.html", "Ejercicios — Renan el Profesor · Curso de Español",
               "Práctica adicional de lectura y vocabulario en español, independiente del nivel, con retroalimentación instantánea.",
               sections, active_top="exercises", breadcrumb_label="Ejercicios",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


# =======================================================================
# EXTRAS
# =======================================================================
def build_extras():
    header = page_header("Más Allá de la Gramática", "Extras",
                          "Expresiones comunes, tú frente a usted (y vos), situaciones cotidianas, y breves notas culturales.")

    expressions = [
        ("¡Vale!", "De acuerdo, está bien.", "Uso muy frecuente en España para aceptar algo o confirmar un plan."),
        ("¡Qué va!", "¡Para nada! / ¡Qué dices!", "Para negar con énfasis algo que alguien acaba de decir."),
        ("Ni idea", "No lo sé en absoluto.", "Respuesta informal, muy común entre amigos."),
        ("¡Venga!", "¡Vamos! / ¡Anímate!", "Ánimo o invitación a actuar, muy usado en España en el habla diaria."),
        ("¡Ojalá!", "¡Espero que sí, con toda el alma!", "Expresa un deseo intenso; viene del árabe «law šá lla»."),
        ("No pasa nada", "No hay problema, tranquilo.", "Para quitar importancia a un error o una disculpa."),
        ("¡Qué guay!", "¡Qué genial!", "Coloquial y muy español; en América Latina se dice a menudo «qué chévere» o «qué padre»."),
        ("Ostras", "¡Vaya! (expresión de sorpresa)", "Eufemismo educado de una palabrota; se usa incluso en contextos formales."),
        ("¡Anda!", "¡Vaya! / ¡No me digas!", "Sorpresa o incredulidad; también anima a alguien a hacer algo."),
        ("Estar en las nubes", "Estar distraído, no prestar atención.", "Expresión figurada muy común en toda situación informal."),
    ]
    exp_rows = "".join(f"<tr><td><strong>{it}</strong></td><td>{sig}</td><td>{note}</td></tr>" for it, sig, note in expressions)

    expressions_section = f"""<section id="expressions" class="section section--surface" aria-labelledby="expr-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Suena Más Natural</p>
                <h2 id="expr-heading">Expresiones Comunes</h2>
                <p>Frases breves y muy frecuentes que hacen que tu español suene natural, no de manual.</p>
            </div>
            <div class="table-scroll"><table class="ref-table"><thead><tr><th>Expresión</th><th>Significado</th><th>Nota</th></tr></thead><tbody>{exp_rows}</tbody></table></div>
        </div>
    </section>"""

    formal_informal = f"""<section id="formal-informal" class="section section--tight" aria-labelledby="fi-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Registro</p>
                <h2 id="fi-heading">Tú, Usted… y Vos</h2>
                <p>Elegir tú o usted es solo el comienzo — y en gran parte de América existe una tercera opción: vos.</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Informal (tú)</h3>
                    <ul class="rules-list">
                        <li>Hola, ¿cómo estás?</li>
                        <li>Perdona, ¿tienes un minuto?</li>
                        <li>¿Puedes ayudarme?</li>
                        <li>Te quería preguntar una cosa.</li>
                        <li>¡Hasta pronto! / ¡Nos vemos!</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Formal (usted)</h3>
                    <ul class="rules-list">
                        <li>Buenos días, ¿cómo está usted?</li>
                        <li>Disculpe, ¿tendría un minuto?</li>
                        <li>¿Podría ayudarme?</li>
                        <li>Quería preguntarle una cosa.</li>
                        <li>Saludos cordiales / Hasta luego</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Regional (vos — Argentina, Uruguay…)</h3>
                    <ul class="rules-list">
                        <li>Hola, ¿cómo estás vos?</li>
                        <li>Che, ¿tenés un minuto?</li>
                        <li>¿Vos podés ayudarme?</li>
                        <li>Te quería preguntar una cosa.</li>
                        <li>¡Nos vemos, che!</li>
                    </ul>
                </div>
            </div>
            <div class="notice mt-lg"><strong>Regla general</strong><p>Usa usted con desconocidos, personas mayores, autoridades y en cualquier contexto profesional — hasta que te inviten a tutear. En Argentina, Uruguay y buena parte de Centroamérica, vos reemplaza a tú incluso en las situaciones informales cotidianas.</p></div>
        </div>
    </section>"""

    everyday = f"""<section id="everyday" class="section section--surface" aria-labelledby="everyday-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Situaciones Reales</p>
                <h2 id="everyday-heading">Español de Todos los Días</h2>
                <p>Intercambios breves y prácticos para situaciones con las que te vas a encontrar de verdad.</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>En un bar o café</h3>
                    <p><em>Un café con leche, por favor.</em></p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">En muchos bares españoles te sientas y el camarero te atiende en la mesa; en otros países hispanohablantes es más común pedir y pagar directamente en la barra.</p>
                </div>
                <div class="card">
                    <h3>En un mercado</h3>
                    <p><em>¿Cuánto cuestan estas manzanas?</em></p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">En algunos países de América Latina es habitual regatear un poco en el mercado, algo que casi nunca ocurre en España.</p>
                </div>
                <div class="card">
                    <h3>Charla trivial</h3>
                    <p><em>Qué calor/frío hace hoy, ¿no?</em></p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">El clima es un tema seguro y universal para romper el hielo, igual que en muchos otros idiomas.</p>
                </div>
            </div>
        </div>
    </section>"""

    culture = f"""<section id="culture" class="section section--tight" aria-labelledby="culture-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Notas Culturales</p>
                <h2 id="culture-heading">El Mundo Hispanohablante en Breve</h2>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Horarios de comida</h3>
                    <p>En España se suele almorzar entre las 2 y las 3 de la tarde y cenar después de las 9; en gran parte de América Latina el almuerzo es antes, entre el mediodía y la 1, y la cena suele ser bastante más temprana, alrededor de las 7 u 8.</p>
                </div>
                <div class="card">
                    <h3>La cultura del mate</h3>
                    <p>En Argentina, Uruguay y Paraguay, el mate es mucho más que una infusión: compartir la bombilla y la ronda de mate es un ritual social diario, con su propio vocabulario (cebar, lavado, amargo, dulce).</p>
                </div>
                <div class="card">
                    <h3>Un idioma, muchos acentos</h3>
                    <p>El español es lengua oficial en más de veinte países, desde España hasta Argentina, pasando por México, el Caribe y toda Sudamérica — cada región tiene su propio vocabulario, entonación y expresiones, y ninguna variante es «más correcta» que otra.</p>
                </div>
            </div>
        </div>
    </section>"""

    write_page("extras.html", "Extras — Renan el Profesor · Curso de Español",
               "Expresiones comunes, tú/usted/vos, situaciones cotidianas y breves notas culturales del mundo hispanohablante.",
               [header, expressions_section, formal_informal, everyday, culture],
               active_top="extras", breadcrumb_label="Extras", extra_css=["lessons"])


# =======================================================================
# DICTIONARY
# =======================================================================
def dict_card(name, desc, url_tmpl, sample_word, featured=True):
    cls = "card card--feature dict-card" if featured else "card dict-card"
    btn_cls = "btn btn--accent btn--small dict-card__link" if featured else "btn btn--accent btn--small dict-card__link"
    sample_url = url_tmpl.replace("{word}", sample_word)
    return f"""<div class="{cls}" data-url-template="{url_tmpl}">
        <h3>{name}</h3>
        <p>{desc}</p>
        <div class="card__foot">
            <a class="{btn_cls}" data-dict-link href="{sample_url}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>Buscar</a>
        </div>
    </div>"""


def build_dictionary():
    header = page_header("Diccionario y Referencia", "Busca Cualquier Palabra en Español",
                          "Escribe una palabra una sola vez y ábrela directamente en cualquiera de estos diccionarios en español, o usa las herramientas de pronunciación de más abajo.")

    input_section = f"""<section class="section section--surface" aria-labelledby="primary-dict-heading">
        <div class="section__inner">
            <h2 id="primary-dict-heading" class="visually-hidden">Diccionarios Principales</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-lg);">
                <label for="dict-word" class="eyebrow" style="margin-bottom:0.6em;display:block;">Tu palabra</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="dict-word" class="dict-input" placeholder="Escribe una palabra, p. ej. «ojalá»" autocomplete="off" data-dict-word>
                </div>
                <p class="notice mt-lg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Cada tarjeta de abajo se actualiza mientras escribes. Pulsa Enter para saltar a uno al azar de los cuatro diccionarios principales.</p>
            </div>
            <div class="grid">
                {dict_card("RAE — Diccionario de la lengua española", "El diccionario oficial de la Real Academia Española: la referencia definitiva para definiciones, gramática y uso correcto del español.", "https://dle.rae.es/{word}", "ojalá")}
                {dict_card("Wikcionario en español", "Diccionario colaborativo con etimología, ejemplos y variantes regionales de miles de palabras.", "https://es.wiktionary.org/wiki/{word}", "ojalá")}
                {dict_card("Fundéu BBVA", "Recomendaciones sobre el uso correcto del español: dudas frecuentes, neologismos y cuestiones de estilo.", "https://www.fundeu.es/?s={word}", "ojalá")}
                {dict_card("Sinónimos y Antónimos", "Encuentra sinónimos y antónimos para enriquecer tu vocabulario y evitar repeticiones.", "https://www.wordreference.com/sinonimos/{word}", "ojalá")}
            </div>
        </div>
    </section>"""

    more_section = f"""<section class="section" aria-labelledby="more-dict-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Si Necesitas Más</p>
                <h2 id="more-dict-heading">Más Diccionarios y Pronunciación</h2>
                <p>Para una segunda opinión, conjugar un verbo, o para escuchar cómo se pronuncia una palabra de verdad.</p>
            </div>
            <div class="grid">
                {dict_card("Conjugador de Verbos", "Tablas completas de conjugación para cualquier verbo español, en todos los tiempos y modos.", "https://www.conjugacion.es/del/verbo/{word}.php", "hablar", featured=False)}
                {dict_card("Forvo", "Pronunciaciones reales grabadas por hablantes nativos de español de distintos países.", "https://forvo.com/word/{word}/#es", "ojalá", featured=False)}
            </div>
        </div>
    </section>"""

    write_page("dictionary.html", "Diccionario y Referencia — Renan el Profesor · Curso de Español",
               "Busca cualquier palabra en español en la RAE, Wikcionario, Fundéu BBVA y más, con herramientas de sinónimos, conjugación y pronunciación.",
               [header, input_section, more_section],
               active_top="dictionary", breadcrumb_label="Diccionario y Referencia",
               extra_scripts=["dictionary.js"])


# =======================================================================
# IRREGULAR VERBS
# =======================================================================
IRREGULAR_VERBS = [
    ("ser", "existir, tener cierta identidad o cualidad permanente", "soy", "fui", "raíz totalmente irregular"),
    ("estar", "expresar ubicación, estado o condición temporal", "estoy", "estuve", "raíz irregular en el pretérito (estuv-)"),
    ("ir", "trasladarse de un lugar a otro", "voy", "fui", "raíz totalmente irregular"),
    ("tener", "poseer algo o sentir algo", "tengo", "tuve", "1ª persona irregular + raíz irregular en pretérito"),
    ("hacer", "realizar o producir algo", "hago", "hice", "1ª persona irregular + raíz irregular en pretérito"),
    ("decir", "comunicar algo con palabras", "digo", "dije", "1ª persona irregular + raíz irregular en pretérito"),
    ("poder", "tener la capacidad de hacer algo", "puedo", "pude", "diptongación o→ue + raíz irregular en pretérito"),
    ("querer", "desear algo o sentir cariño", "quiero", "quise", "diptongación e→ie + raíz irregular en pretérito"),
    ("saber", "conocer un hecho o tener información", "sé", "supe", "1ª persona irregular + raíz irregular en pretérito"),
    ("poner", "colocar algo en un lugar", "pongo", "puse", "1ª persona irregular + raíz irregular en pretérito"),
    ("venir", "trasladarse hacia el lugar donde está el hablante", "vengo", "vine", "1ª persona irregular + raíz irregular en pretérito"),
    ("salir", "irse de un lugar", "salgo", "salí", "1ª persona irregular"),
    ("dar", "entregar algo a alguien", "doy", "di", "1ª persona irregular + pretérito sin acento"),
    ("ver", "percibir algo con los ojos", "veo", "vi", "1ª persona irregular + pretérito sin acento"),
    ("haber", "verbo auxiliar de los tiempos compuestos; también «existir» (hay)", "he", "hube", "raíz totalmente irregular"),
    ("traer", "llevar algo hacia el hablante", "traigo", "traje", "1ª persona irregular + raíz irregular en pretérito"),
    ("caer", "irse hacia abajo por la fuerza de la gravedad", "caigo", "caí", "1ª persona irregular"),
    ("oír", "percibir sonidos con el oído", "oigo", "oí", "1ª persona irregular + cambio ortográfico (oyó)"),
    ("conducir", "guiar un vehículo", "conduzco", "conduje", "1ª persona irregular + raíz irregular en pretérito (-duje)"),
    ("producir", "crear o fabricar algo", "produzco", "produje", "1ª persona irregular + raíz irregular en pretérito (-duje)"),
    ("huir", "escapar de un peligro o lugar", "huyo", "huí", "cambio ortográfico i→y"),
    ("construir", "edificar o fabricar algo", "construyo", "construí", "cambio ortográfico i→y"),
    ("seguir", "continuar haciendo algo o ir detrás de alguien", "sigo", "seguí", "cambio de raíz e→i + cambio ortográfico gu→g"),
    ("pedir", "solicitar algo", "pido", "pedí", "cambio de raíz e→i"),
    ("servir", "ser útil para algo o atender a alguien", "sirvo", "serví", "cambio de raíz e→i"),
    ("dormir", "estar en estado de sueño", "duermo", "dormí", "diptongación o→ue"),
    ("morir", "dejar de vivir", "muero", "morí", "diptongación o→ue"),
    ("sentir", "experimentar una sensación o emoción", "siento", "sentí", "diptongación e→ie"),
    ("preferir", "gustar más una cosa que otra", "prefiero", "preferí", "diptongación e→ie"),
    ("jugar", "realizar una actividad de ocio o deporte", "juego", "jugué", "diptongación u→ue + cambio ortográfico g→gu"),
    ("empezar", "comenzar algo", "empiezo", "empecé", "diptongación e→ie + cambio ortográfico z→c"),
    ("pensar", "usar la mente para razonar", "pienso", "pensé", "diptongación e→ie"),
    ("volver", "regresar a un lugar", "vuelvo", "volví", "diptongación o→ue"),
    ("encontrar", "hallar algo o a alguien", "encuentro", "encontré", "diptongación o→ue"),
    ("contar", "narrar algo o decir números en orden", "cuento", "conté", "diptongación o→ue"),
    ("entender", "comprender algo", "entiendo", "entendí", "diptongación e→ie"),
    ("perder", "dejar de tener algo", "pierdo", "perdí", "diptongación e→ie"),
    ("mostrar", "hacer ver algo a alguien", "muestro", "mostré", "diptongación o→ue"),
    ("mover", "cambiar algo de lugar", "muevo", "moví", "diptongación o→ue"),
    ("recordar", "traer algo a la memoria", "recuerdo", "recordé", "diptongación o→ue"),
    ("oler", "percibir un olor", "huelo", "olí", "diptongación o→hue"),
    ("caber", "poder contenerse dentro de un espacio", "quepo", "cupe", "1ª persona irregular + raíz irregular en pretérito"),
    ("valer", "tener un precio o un mérito", "valgo", "valí", "1ª persona irregular"),
    ("andar", "caminar o moverse", "ando", "anduve", "raíz irregular en el pretérito"),
    ("cerrar", "hacer que algo deje de estar abierto", "cierro", "cerré", "diptongación e→ie"),
    ("comenzar", "empezar algo, dar inicio a algo", "comienzo", "comencé", "diptongación e→ie + cambio ortográfico z→c"),
]


def build_irregular_verbs():
    header = page_header("Referencia", "Verbos Irregulares del Español",
                          "Los verbos irregulares más comunes, con su presente (yo), pretérito (yo) y tipo de irregularidad — escribe para filtrar.")

    rows = "".join(
        f"<tr><td><strong>{inf}</strong></td><td>{meaning}</td><td>{pres}</td><td>{pret}</td><td class=\"text-muted\">{tipo}</td></tr>"
        for inf, meaning, pres, pret, tipo in IRREGULAR_VERBS
    )

    section = f"""<section class="section section--surface" aria-labelledby="verbs-heading">
        <div class="section__inner">
            <h2 id="verbs-heading" class="visually-hidden">Verbos Irregulares</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-md);">
                <label for="verb-filter" class="eyebrow" style="margin-bottom:0.6em;display:block;">Filtrar</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="verb-filter" class="dict-input" placeholder="Escribe para filtrar, p. ej. «tener» o «ser»" autocomplete="off" data-verb-filter>
                </div>
                <p class="notice mt-lg" data-verb-count><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Mostrando los {len(IRREGULAR_VERBS)} verbos.</p>
                <p class="notice mt-lg" data-verb-empty hidden>No se encontraron verbos que coincidan con «<span data-verb-empty-term></span>».</p>
            </div>
            <div class="table-scroll">
                <table class="ref-table">
                    <caption>Verbos irregulares comunes del español</caption>
                    <thead><tr><th>Infinitivo</th><th>Definición</th><th>Presente (yo)</th><th>Pretérito (yo)</th><th>Tipo de Irregularidad</th></tr></thead>
                    <tbody data-verb-tbody>{rows}</tbody>
                </table>
            </div>
        </div>
    </section>"""

    write_page("irregular-verbs.html", "Verbos Irregulares del Español — Renan el Profesor · Curso de Español",
               "Tabla de referencia de los verbos irregulares más comunes del español: presente, pretérito y tipo de irregularidad, con filtro en vivo.",
               [header, section], active_top="extras", breadcrumb_label="Verbos Irregulares",
               extra_css=["lessons"], extra_scripts=["irregular-verbs.js"])


# =======================================================================
# PLACEMENT TEST
# =======================================================================
def build_placement_test():
    header = page_header("Encuentra Tu Nivel", "Prueba de Nivel",
                          "28 preguntas, entre tres y cuatro por nivel de Pre-A1 a C2. Responde las que puedas — la sensación de dónde empieza a costarte es la mejor guía de tu nivel real.")

    blocks = [
        ("Pre-A1", [
            {"id": "pt-prea1-1", "prompt": "Buenos días, ¿cómo ___ usted?", "options": ["está", "estás", "es"], "answerIndex": 0, "explanation": "Con usted se usa la forma de él/ella: está."},
            {"id": "pt-prea1-2", "prompt": "Tengo veinte ___.", "options": ["año", "años", "anos"], "answerIndex": 1, "explanation": "La edad se expresa con el sustantivo en plural: años."},
            {"id": "pt-prea1-3", "prompt": "Son las tres de la tarde. Se dice: «___, ¿cómo estás?»", "options": ["Buenos días", "Buenas tardes", "Buenas noches"], "answerIndex": 1, "explanation": "Entre el mediodía y el anochecer se usa «buenas tardes»."},
            {"id": "pt-prea1-4", "prompt": "Yo ___ estudiante.", "options": ["soy", "eres", "es"], "answerIndex": 0, "explanation": "La primera persona del verbo ser es soy."},
        ]),
        ("A1", [
            {"id": "pt-a1-1", "prompt": "Barcelona ___ una ciudad muy bonita.", "options": ["es", "está", "son"], "answerIndex": 0, "explanation": "Cualidad permanente → ser."},
            {"id": "pt-a1-2", "prompt": "El té ___ frío ahora, no lo quiero.", "options": ["es", "está", "eres"], "answerIndex": 1, "explanation": "Estado temporal → estar."},
            {"id": "pt-a1-3", "prompt": "___ chico es mi hermano.", "options": ["El", "La", "Los"], "answerIndex": 0, "explanation": "Chico es masculino singular → el."},
            {"id": "pt-a1-4", "prompt": "Me ___ mucho las películas de terror.", "options": ["gusto", "gusta", "gustan"], "answerIndex": 2, "explanation": "Gustar concuerda con lo que gusta: «las películas» (plural) → gustan."},
        ]),
        ("A2", [
            {"id": "pt-a2-1", "prompt": "Ayer ___ (yo - comer) en un restaurante muy bueno.", "options": ["comí", "como", "comía"], "answerIndex": 0, "explanation": "Acción puntual y terminada → pretérito indefinido."},
            {"id": "pt-a2-2", "prompt": "De pequeño, ___ (yo - vivir) en un pueblo pequeño.", "options": ["viví", "vivía", "he vivido"], "answerIndex": 1, "explanation": "Descripción de una situación habitual en el pasado → imperfecto."},
            {"id": "pt-a2-3", "prompt": "Ella ___ (dormir) muy poco anoche.", "options": ["durmió", "dormió", "dormía"], "answerIndex": 0, "explanation": "Dormir cambia la raíz o→u en la tercera persona del pretérito: durmió."},
            {"id": "pt-a2-4", "prompt": "¡___ (comer, tú) toda la verdura!", "options": ["come", "comes", "comas"], "answerIndex": 0, "explanation": "Imperativo afirmativo informal de comer: come."},
        ]),
        ("B1", [
            {"id": "pt-b1-1", "prompt": "Espero que ___ (tú - venir) a mi cumpleaños.", "options": ["vienes", "vengas", "vendrás"], "answerIndex": 1, "explanation": "Esperar que exige subjuntivo presente: vengas."},
            {"id": "pt-b1-2", "prompt": "¿Me prestas tu coche? Sí, ___ presto sin problema. (te + lo)", "options": ["te lo", "te la", "se lo"], "answerIndex": 0, "explanation": "Objeto indirecto (te) + directo masculino (el coche → lo) = te lo."},
            {"id": "pt-b1-3", "prompt": "El año que viene ___ (yo - terminar) mis estudios.", "options": ["terminaré", "termino", "terminaba"], "answerIndex": 0, "explanation": "Plan futuro → futuro simple."},
            {"id": "pt-b1-4", "prompt": "En Argentina, en lugar de «tú tienes», se dice: «___ tenés».", "options": ["vos", "tú", "usted"], "answerIndex": 0, "explanation": "El voseo rioplatense reemplaza a tú por vos, con su propia forma verbal."},
        ]),
        ("B2", [
            {"id": "pt-b2-1", "prompt": "Si ___ (yo - tener) más tiempo libre, aprendería a tocar la guitarra.", "options": ["tengo", "tuviera", "tendría"], "answerIndex": 1, "explanation": "Condicional hipotético (2º tipo): si + imperfecto de subjuntivo."},
            {"id": "pt-b2-2", "prompt": "Ojalá ___ (ellos - llegar) pronto, ya es tarde.", "options": ["llegan", "lleguen", "llegaran"], "answerIndex": 1, "explanation": "Ojalá + subjuntivo presente expresa un deseo sobre algo aún posible."},
            {"id": "pt-b2-3", "prompt": "La puerta ___ abierta cuando llegué.", "options": ["es", "estaba", "fue"], "answerIndex": 1, "explanation": "Resultado de una acción anterior → estar + participio."},
            {"id": "pt-b2-4", "prompt": "El puente ___ (construir) en el siglo XIX.", "options": ["fue construido", "construyó", "ha construido"], "answerIndex": 0, "explanation": "Voz pasiva: ser + participio (concordando en género y número)."},
        ]),
        ("C1", [
            {"id": "pt-c1-1", "prompt": "Si lo ___ (yo - saber) antes, te habría avisado.", "options": ["supiera", "hubiera sabido", "sabría"], "answerIndex": 1, "explanation": "Condicional del 3er tipo (irreal en el pasado): si + pluscuamperfecto de subjuntivo."},
            {"id": "pt-c1-2", "prompt": "Me extrañó que todavía no ___ (ellos - llegar) a esa hora.", "options": ["hubieran llegado", "llegaron", "llegaran"], "answerIndex": 0, "explanation": "Pluscuamperfecto de subjuntivo: acción anterior a otra ya pasada."},
            {"id": "pt-c1-3", "prompt": "¿Cuál de estas frases pertenece a un registro académico?", "options": ["Cabe destacar que los resultados obtenidos confirman la hipótesis.", "Oye, mira lo que encontré, ¡es increíble!", "Qué fuerte lo de ayer, ¿no?"], "answerIndex": 0, "explanation": "El registro académico evita coloquialismos y usa construcciones impersonales como «cabe destacar»."},
            {"id": "pt-c1-4", "prompt": "En México, «¿qué onda?» es una forma coloquial de preguntar…", "options": ["¿cómo estás?", "¿dónde vives?", "¿cuánto cuesta?"], "answerIndex": 0, "explanation": "Es un saludo informal muy extendido en el español mexicano, equivalente a «¿qué tal?»."},
        ]),
        ("C2", [
            {"id": "pt-c2-1", "prompt": "¿Qué oración usa una estructura enfática (oración hendida)?", "options": ["El problema me preocupa mucho.", "Es el problema lo que más me preocupa.", "Me preocupa bastante el problema."], "answerIndex": 1, "explanation": "Esta es una oración hendida, que destaca «el problema» mediante «es... lo que»."},
            {"id": "pt-c2-2", "prompt": "Debo ___ una decisión importante.", "options": ["hacer", "tomar", "dar"], "answerIndex": 1, "explanation": "La colocación fija en español es «tomar una decisión»."},
            {"id": "pt-c2-3", "prompt": "«Es posible que» suele ir seguido de…", "options": ["el indicativo", "el subjuntivo", "el imperativo"], "answerIndex": 1, "explanation": "«Es posible que» presenta algo incierto, lo que exige subjuntivo."},
            {"id": "pt-c2-4", "prompt": "Trabajo mucho ___ ganar más dinero.", "options": ["por", "para", "de"], "answerIndex": 1, "explanation": "La finalidad de una acción se expresa con para."},
        ]),
    ]
    sections = [header]
    all_items = []
    for level, items in blocks:
        all_items.extend(items)
        level_slug = level.lower()
        sections.append(f"""<section class="section section--tight" aria-labelledby="pt-{level_slug}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level}</p>
                <h2 id="pt-{level_slug}-heading">Preguntas de Nivel {level}</h2>
                {ex_block({"id": f"pt-{level_slug}-block", "type": "multiple-choice", "title": f"Preguntas de Nivel {level}", "items": items})}
            </div>
        </section>""")

    guide = f"""<section class="section section--surface" aria-labelledby="pt-guide-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Cómo Leer Tus Resultados</p>
            <h2 id="pt-guide-heading">Qué Significa Tu Puntuación</h2>
            <ul class="summary-list">
                <li>Te costaron incluso las preguntas de Pre-A1 → empieza en <a href="levels/pre-a1.html">Pre-A1</a> y construye las bases desde cero.</li>
                <li>Cómodo en Pre-A1, con dificultad desde A1 → empieza en <a href="levels/a1.html">A1</a>.</li>
                <li>Cómodo hasta A2, con dificultad desde B1 → empieza en <a href="levels/b1.html">B1</a>.</li>
                <li>Cómodo hasta B1, con dificultad desde B2 → empieza en <a href="levels/b2.html">B2</a>.</li>
                <li>Cómodo hasta B2, con dificultad desde C1 → empieza en <a href="levels/c1.html">C1</a>.</li>
                <li>Acertaste todo, incluido C2 → repasa las lecciones de <a href="levels/c2.html">C2</a> para pulir detalles, o explora la página de <a href="extras.html">Extras</a>.</li>
            </ul>
        </div>
    </section>"""
    sections.append(guide)

    write_page("placement-test.html", "Prueba de Nivel — Renan el Profesor · Curso de Español",
               "Una breve prueba de nivel autoevaluable para descubrir en qué nivel del MCER empezar tu español, de Pre-A1 a C2.",
               sections, active_top=None, breadcrumb_label="Prueba de Nivel",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


# =======================================================================
# PROGRESS
# =======================================================================
def build_progress():
    header = page_header("Tu Trayectoria", "Mi Progreso",
                          "XP, rachas e insignias, guardado únicamente en este dispositivo — nada se envía nunca a ningún servidor.")

    section = f"""<section class="section section--surface" aria-labelledby="progress-heading">
        <div class="section__inner">
            <h2 id="progress-heading" class="visually-hidden">Progreso</h2>
            <div class="progress-panel__summary" id="progress-summary"></div>
        </div>
    </section>
<section class="section section--tight" aria-labelledby="progress-levels-heading">
        <div class="section__inner">
            <p class="eyebrow">Por Nivel</p>
            <h2 id="progress-levels-heading">Progreso por Nivel</h2>
            <div id="progress-levels"></div>
        </div>
    </section>
<section class="section section--surface" aria-labelledby="progress-badges-heading">
        <div class="section__inner">
            <p class="eyebrow">Logros</p>
            <h2 id="progress-badges-heading">Insignias</h2>
            <ul class="badge-grid" id="progress-badges"></ul>
        </div>
    </section>
<section class="section section--tight" aria-labelledby="progress-reset-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Empezar de Nuevo</p>
            <h2 id="progress-reset-heading">Reiniciar Progreso</h2>
            <p style="color:var(--color-text-muted);">Esto borra tu XP, tu racha y tus insignias en este dispositivo. El historial de repetición espaciada (Repaso de Hoy) se guarda por separado y no se ve afectado.</p>
            <button type="button" class="btn btn--ghost" id="progress-reset-btn">Reiniciar XP y Insignias</button>
        </div>
    </section>"""

    write_page("progress.html", "Mi Progreso — Renan el Profesor · Curso de Español",
               "Sigue tu XP, tu racha y tus insignias a lo largo del curso de español, guardado de forma privada en tu dispositivo.",
               [header, section], active_top=None, breadcrumb_label="Mi Progreso")


# =======================================================================
# TODAY'S REVIEW
# =======================================================================
def build_today_review():
    header = page_header("Repetición Espaciada", "Repaso de Hoy",
                          "Un repaso breve y diario de los ejercicios que has fallado antes — generado automáticamente a partir de tu propio historial.")

    section = f"""<section class="section section--surface" aria-labelledby="review-heading">
        <div class="section__inner">
            <h2 id="review-heading" class="visually-hidden">Repaso</h2>
            <div id="review-status-box" class="notice"><p>Cargando tu cola de repaso…</p></div>
            <div id="review-blocks" style="margin-top:var(--space-md);"></div>
        </div>
    </section>"""

    write_page("today-review.html", "Repaso de Hoy — Renan el Profesor · Curso de Español",
               "Un repaso diario de repetición espaciada de ejercicios de español que has fallado antes, generado automáticamente a partir de tu propio historial.",
               [header, section], active_top=None, breadcrumb_label="Repaso de Hoy",
               extra_css=["exercises"], extra_scripts=["exercises.js", "mastery.js", "today-review.js"])


# =======================================================================
# SIMULATED EXAMS
# =======================================================================
def build_simulated_exams():
    header = page_header("Práctica de Examen", "Exámenes Simulados",
                          "Secciones de práctica al estilo de las certificaciones oficiales de español — DELE y SIELE — con claves de respuestas.")

    intro = f"""<section class="section section--tight" aria-labelledby="exams-intro-heading">
        <div class="section__inner section__inner--narrow">
            <h2 id="exams-intro-heading" class="visually-hidden">Sobre Estos Exámenes</h2>
            <p style="color:var(--color-text-muted);">El español cuenta con dos certificaciones internacionales de referencia como lengua extranjera: el <strong>DELE</strong> (Diplomas de Español como Lengua Extranjera, del Instituto Cervantes) y el <strong>SIELE</strong> (Servicio Internacional de Evaluación de la Lengua Española, respaldado por el propio Instituto Cervantes y varias universidades). Ambos evalúan las mismas cuatro destrezas — comprensión de lectura, comprensión auditiva, expresión escrita y expresión oral — en los niveles del MCER de A1 a C2. Las secciones siguientes son práctica en ese estilo, no exámenes oficiales reales.</p>
        </div>
    </section>"""

    pa1_reading = ("<p>Hola, me llamo Sara. Soy de España y tengo veinte años. Estudio en la universidad y vivo con dos compañeras. Por las mañanas voy a clase y por las tardes trabajo en una cafetería. Los fines de semana me gusta salir con mis amigas.</p>")
    pa1_reading_ex = {"id": "sim-prea1-reading", "type": "true-false", "title": "Lectura al Estilo DELE/SIELE — Pre-A1", "items": [
        {"id": "simpa1r1", "statement": "Sara vive sola.", "answer": False, "explanation": "El texto dice: «vivo con dos compañeras»."},
        {"id": "simpa1r2", "statement": "Sara trabaja en una cafetería por las tardes.", "answer": True, "explanation": "El texto dice: «por las tardes trabajo en una cafetería»."},
        {"id": "simpa1r3", "statement": "A Sara no le gusta salir con amigas.", "answer": False, "explanation": "El texto dice: «me gusta salir con mis amigas»."},
    ]}
    pa1_grammar_ex = {"id": "sim-prea1-grammar", "type": "multiple-choice", "title": "Gramática al Estilo DELE/SIELE — Pre-A1",
                       "items": [
                           {"id": "simpa1g1", "prompt": "Yo ___ estudiante.", "options": ["soy", "eres", "es"], "answerIndex": 0, "explanation": "Yo + ser = soy."},
                           {"id": "simpa1g2", "prompt": "¿Cómo ___ tú?", "options": ["te llamas", "se llama", "me llamo"], "answerIndex": 0, "explanation": "Pregunta con tú: ¿Cómo te llamas?."},
                           {"id": "simpa1g3", "prompt": "Nosotros ___ de México.", "options": ["soy", "somos", "son"], "answerIndex": 1, "explanation": "Nosotros + ser = somos."},
                       ]}

    a1_reading = ("<p>Mi rutina diaria es bastante simple. Me levanto a las siete, desayuno rápido y voy al trabajo en autobús. A mediodía como con mis compañeros. Por la tarde estudio inglés dos horas. Antes de dormir, siempre leo un poco.</p>")
    a1_reading_ex = {"id": "sim-a1-reading", "type": "multiple-choice", "title": "Lectura al Estilo DELE/SIELE — A1", "items": [
        {"id": "sima1r1", "prompt": "¿Cómo va al trabajo la persona?", "options": ["A pie", "En autobús", "En coche"], "answerIndex": 1, "explanation": "El texto dice: «voy al trabajo en autobús»."},
        {"id": "sima1r2", "prompt": "¿Qué estudia por la tarde?", "options": ["Español", "Inglés", "Francés"], "answerIndex": 1, "explanation": "El texto dice: «estudio inglés dos horas»."},
        {"id": "sima1r3", "prompt": "¿Qué hace antes de dormir?", "options": ["Ve la televisión", "Lee un poco", "Escucha música"], "answerIndex": 1, "explanation": "El texto dice: «siempre leo un poco»."},
    ]}
    a1_grammar_ex = {"id": "sim-a1-grammar", "type": "fill-blank", "title": "Gramática al Estilo DELE/SIELE — A1",
                      "instructions": "Completa cada frase.",
                      "items": [
                          {"id": "sima1g1", "prompt": "Ella ___ (tener) veinticinco años.", "answers": [["tiene"]], "explanation": "Ella + tener (irregular en yo, regular aquí) = tiene."},
                          {"id": "sima1g2", "prompt": "Nosotros ___ (vivir) en Madrid.", "answers": [["vivimos"]], "explanation": "Nosotros + verbo en -ir = vivimos."},
                          {"id": "sima1g3", "prompt": "¿Cuántos hermanos ___ (tú - tener)?", "answers": [["tienes"]], "explanation": "Tú + tener = tienes."},
                      ]}

    a2_reading = ("<p>El verano pasado viajé a Portugal con mi familia. Visitamos Lisboa y Oporto, y comimos platos deliciosos en cada ciudad. El clima era muy agradable, ni muy caliente ni muy frío. Fue uno de los mejores viajes de mi vida, y ya estamos planeando volver el próximo año.</p>")
    a2_reading_ex = {"id": "sim-a2-reading", "type": "true-false", "title": "Lectura al Estilo DELE/SIELE — A2", "items": [
        {"id": "sima2r1", "statement": "El viaje fue a Portugal.", "answer": True, "explanation": "El texto dice: «viajé a Portugal con mi familia»."},
        {"id": "sima2r2", "statement": "El clima era muy caliente.", "answer": False, "explanation": "El texto dice que el clima «era muy agradable, ni muy caliente ni muy frío»."},
        {"id": "sima2r3", "statement": "La familia planea volver a Portugal.", "answer": True, "explanation": "El texto dice: «ya estamos planeando volver el próximo año»."},
    ]}
    a2_grammar_ex = {"id": "sim-a2-grammar", "type": "fill-blank", "title": "Gramática al Estilo DELE/SIELE — A2",
                      "instructions": "Completa cada frase con el pretérito indefinido o el imperfecto según corresponda.",
                      "items": [
                          {"id": "sima2g1", "prompt": "Ayer ___ (yo - visitar) a mis abuelos.", "answers": [["visité"]], "explanation": "Marcador de tiempo cerrado (ayer) → pretérito indefinido."},
                          {"id": "sima2g2", "prompt": "De niño, ___ (yo - vivir) en el campo.", "answers": [["vivía"]], "explanation": "Descripción de una etapa del pasado → imperfecto."},
                          {"id": "sima2g3", "prompt": "El año pasado ellos ___ (comprar) una casa nueva.", "answers": [["compraron"]], "explanation": "Marcador de tiempo cerrado → pretérito indefinido."},
                      ]}

    b1_reading = ("<p>En los últimos años, cada vez más personas en España y América Latina eligen trabajar desde casa al menos un par de días a la semana. Según una encuesta reciente, la mayoría de los trabajadores se declara más satisfecha que antes, sobre todo gracias al tiempo que ahorran en los desplazamientos. Sin embargo, algunos encuestados señalan dificultades para separar la vida personal del trabajo, y se quejan de jornadas laborales más largas de lo habitual.</p>")
    b1_reading_ex = {"id": "sim-b1-reading", "type": "true-false", "title": "Lectura al Estilo DELE/SIELE — B1", "items": [
        {"id": "simb1r1", "statement": "La mayoría de los trabajadores encuestados dice estar más satisfecha trabajando desde casa.", "answer": True, "explanation": "«La mayoría de los trabajadores se declara más satisfecha.»"},
        {"id": "simb1r2", "statement": "Nadie mencionó ninguna desventaja del teletrabajo.", "answer": False, "explanation": "Algunos mencionaron dificultades para separar el trabajo de la vida personal y jornadas más largas."},
        {"id": "simb1r3", "statement": "El ahorro en desplazamientos es una razón de la satisfacción.", "answer": True, "explanation": "El texto dice: «sobre todo gracias al tiempo que ahorran en los desplazamientos»."},
    ]}
    b1_grammar_ex = {"id": "sim-b1-grammar", "type": "fill-blank", "title": "Gramática al Estilo DELE/SIELE — B1",
                      "instructions": "Completa cada frase.",
                      "items": [
                          {"id": "simb1g1", "prompt": "De pequeño, ___ (yo - jugar) siempre en la calle.", "answers": [["jugaba"]], "explanation": "Acción habitual en el pasado → imperfecto."},
                          {"id": "simb1g2", "prompt": "Mañana ___ (nosotros - salir) muy temprano.", "answers": [["saldremos"]], "explanation": "Plan futuro → futuro simple."},
                          {"id": "simb1g3", "prompt": "¿___ (Poder - usted) ayudarme, por favor? (formal)", "answers": [["Podría"]], "explanation": "Petición formal y cortés → condicional."},
                          {"id": "simb1g4", "prompt": "Espero que ___ (tú - tener) un buen viaje.", "answers": [["tengas"]], "explanation": "Esperar que exige subjuntivo presente."},
                      ]}
    b1_listening = ("<p><strong>Recepcionista:</strong> Hotel Miramar, buenas tardes.<br><strong>Cliente:</strong> Buenas tardes, quisiera reservar una habitación doble para el fin de semana.<br><strong>Recepcionista:</strong> Por supuesto, ¿para cuántas noches?<br><strong>Cliente:</strong> Dos noches, viernes y sábado.<br><strong>Recepcionista:</strong> Perfecto, tenemos disponibilidad. ¿A nombre de quién hago la reserva?<br><strong>Cliente:</strong> A nombre de Ana Ruiz.</p>")
    b1_listening_ex = {"id": "sim-b1-listening", "type": "multiple-choice", "title": "Comprensión Auditiva al Estilo DELE/SIELE — B1",
                        "instructions": "Lee este guion como si fuera un audio y responde.",
                        "items": [
                            {"id": "simb1l1", "prompt": "¿Qué tipo de habitación reserva el cliente?", "options": ["Individual", "Doble", "Familiar"], "answerIndex": 1, "explanation": "El texto dice: «una habitación doble»."},
                            {"id": "simb1l2", "prompt": "¿Cuántas noches se queda?", "options": ["Una noche", "Dos noches", "Tres noches"], "answerIndex": 1, "explanation": "El texto dice: «Dos noches, viernes y sábado»."},
                        ]}

    b2_reading = ("<p>El debate sobre la inteligencia artificial en el mundo laboral sigue dividiendo a los expertos y a la opinión pública. Si por un lado se subrayan las ventajas en términos de eficiencia, por otro crece la preocupación por la pérdida de empleos en algunos sectores. Los economistas coinciden, sin embargo, en que la formación continua será determinante para afrontar esta transición.</p>")
    b2_reading_ex = {"id": "sim-b2-reading", "type": "multiple-choice", "title": "Lectura al Estilo DELE/SIELE — B2", "items": [
        {"id": "simb2r1", "prompt": "¿En qué coinciden los economistas?", "options": ["En que la inteligencia artificial debería prohibirse", "En que la formación continua será clave", "En que la pérdida de empleos está exagerada"], "answerIndex": 1, "explanation": "«La formación continua será determinante.»"},
        {"id": "simb2r2", "prompt": "¿Qué ventaja se subraya sobre la inteligencia artificial?", "options": ["La eficiencia", "El bajo costo", "La sencillez"], "answerIndex": 0, "explanation": "El texto dice: «se subrayan las ventajas en términos de eficiencia»."},
    ]}
    b2_grammar_ex = {"id": "sim-b2-grammar", "type": "fill-blank", "title": "Gramática al Estilo DELE/SIELE — B2",
                      "instructions": "Completa cada frase.",
                      "items": [
                          {"id": "simb2g1", "prompt": "Si ___ (yo - tener) más tiempo, estudiaría más.", "answers": [["tuviera"]], "explanation": "Condicional hipotético: si + imperfecto de subjuntivo."},
                          {"id": "simb2g2", "prompt": "Dudo que ellos ___ (llegar) a tiempo.", "answers": [["lleguen"]], "explanation": "Dudar que exige subjuntivo presente."},
                          {"id": "simb2g3", "prompt": "Si hubiera sabido la verdad, ___ (yo - actuar) diferente.", "answers": [["habría actuado"]], "explanation": "Condicional irreal de pasado: consecuencia en condicional compuesto."},
                      ]}

    c1_reading = ("<p>La proliferación de asistentes virtuales basados en inteligencia artificial ha reavivado un viejo debate filosófico: ¿puede una máquina, por sofisticada que sea su capacidad de generar lenguaje, llegar a comprender realmente el significado de lo que produce? Mientras algunos investigadores sostienen que se trata de una cuestión meramente técnica, destinada a resolverse con el tiempo, otros insisten en que la comprensión genuina exige una experiencia corporal y contextual de la que estos sistemas, por definición, carecen.</p>")
    c1_reading_ex = {"id": "sim-c1-reading", "type": "true-false", "title": "Lectura al Estilo DELE/SIELE — C1", "items": [
        {"id": "simc1r1", "statement": "El texto plantea si una máquina puede comprender realmente el lenguaje que genera.", "answer": True, "explanation": "El texto dice: «¿puede una máquina... llegar a comprender realmente el significado de lo que produce?»."},
        {"id": "simc1r2", "statement": "Todos los investigadores están de acuerdo en que es solo una cuestión técnica.", "answer": False, "explanation": "El texto dice que «otros insisten en que la comprensión genuina exige una experiencia corporal y contextual»."},
        {"id": "simc1r3", "statement": "Según algunos, la comprensión genuina requiere experiencia corporal y contextual.", "answer": True, "explanation": "El texto dice exactamente eso en la última frase."},
    ]}
    c1_grammar_ex = {"id": "sim-c1-grammar", "type": "fill-blank", "title": "Gramática al Estilo DELE/SIELE — C1",
                      "instructions": "Completa cada frase.",
                      "items": [
                          {"id": "simc1g1", "prompt": "Si hubiera llegado antes, ___ (ver) a mi hermano.", "answers": [["habría visto"], ["hubiera visto"]], "explanation": "Condicional irreal de pasado."},
                          {"id": "simc1g2", "prompt": "No conozco a nadie que ___ (saber) tanto de este tema.", "answers": [["sepa"]], "explanation": "Antecedente indefinido/inexistente (nadie) → subjuntivo."},
                          {"id": "simc1g3", "prompt": "Cabría ___ (reconsiderar) esta parte del proyecto.", "answers": [["reconsiderar"]], "explanation": "Cabría + infinitivo, forma atenuada de sugerencia."},
                      ]}
    c1_listening = ("<p><strong>Entrevistador:</strong> Su último libro aborda temas complejos como la memoria y el exilio. ¿De dónde nace esa elección?<br><strong>Autora:</strong> Nace de una pregunta personal: ¿qué queda de nosotros cuando dejamos el lugar donde crecimos? Quería explorarlo a través de una historia, no de un ensayo.<br><strong>Entrevistador:</strong> ¿Hay algo autobiográfico en la novela?<br><strong>Autora:</strong> Sin duda, aunque preferí transformarlo mediante la ficción.</p>")
    c1_listening_ex = {"id": "sim-c1-listening", "type": "multiple-choice", "title": "Comprensión Auditiva al Estilo DELE/SIELE — C1",
                        "instructions": "Lee este guion como si fuera un audio y responde.",
                        "items": [
                            {"id": "simc1l1", "prompt": "¿Qué temas aborda el último libro de la autora?", "options": ["El amor y la aventura", "La memoria y el exilio", "La ciencia ficción"], "answerIndex": 1, "explanation": "El entrevistador dice: «aborda temas complejos como la memoria y el exilio»."},
                            {"id": "simc1l2", "prompt": "¿Cómo prefirió tratar el elemento autobiográfico?", "options": ["Como un ensayo directo", "Mediante la ficción", "No lo menciona"], "answerIndex": 1, "explanation": "La autora dice: «preferí transformarlo mediante la ficción»."},
                        ]}

    c2_reading = ("<p>Resulta cuando menos paradójico que, en una era definida por la sobreabundancia informativa, la capacidad de discernimiento crítico parezca haberse erosionado en proporción inversa a la cantidad de datos disponibles. Cabría argumentar que la mera acumulación de información, lejos de traducirse automáticamente en conocimiento, exige de por sí un aparato conceptual capaz de jerarquizarla, contextualizarla y, en última instancia, cuestionarla.</p>")
    c2_reading_ex = {"id": "sim-c2-reading", "type": "true-false", "title": "Lectura al Estilo DELE/SIELE — C2", "items": [
        {"id": "simc2r1", "statement": "El texto afirma que más información siempre produce más discernimiento crítico.", "answer": False, "explanation": "El texto dice que el discernimiento crítico «parece haberse erosionado» pese a la sobreabundancia informativa."},
        {"id": "simc2r2", "statement": "Según el texto, la acumulación de información no se traduce automáticamente en conocimiento.", "answer": True, "explanation": "El texto dice: «la mera acumulación de información... no se traduce automáticamente en conocimiento»."},
        {"id": "simc2r3", "statement": "El texto sugiere que se necesita un marco conceptual para procesar la información críticamente.", "answer": True, "explanation": "El texto dice que se exige «un aparato conceptual capaz de jerarquizarla, contextualizarla... cuestionarla»."},
    ]}
    c2_grammar_ex = {"id": "sim-c2-grammar", "type": "multiple-choice", "title": "Gramática al Estilo DELE/SIELE — C2",
                      "items": [
                          {"id": "simc2g1", "prompt": "\"Quienes ___ (llegar) tarde no podrán entrar.\"", "options": ["lleguen", "llegan", "llegarán"], "answerIndex": 0, "explanation": "Quienes con antecedente indefinido exige subjuntivo."},
                          {"id": "simc2g2", "prompt": "\"Cabe la posibilidad de que esto ___ (cambiar) pronto.\"", "options": ["cambia", "cambie", "cambiará"], "answerIndex": 1, "explanation": "Cabe la posibilidad de que exige subjuntivo."},
                          {"id": "simc2g3", "prompt": "\"El que ___ (incumplir) esta norma será sancionado.\" (registro jurídico)", "options": ["incumpliere", "incumple", "incumplirá"], "answerIndex": 0, "explanation": "Futuro de subjuntivo, propio del registro jurídico formal."},
                      ]}

    exam_sections = []
    levels_data = [
        ("Pre-A1", pa1_reading, pa1_reading_ex, pa1_grammar_ex, None, None),
        ("A1", a1_reading, a1_reading_ex, a1_grammar_ex, None, None),
        ("A2", a2_reading, a2_reading_ex, a2_grammar_ex, None, None),
        ("B1", b1_reading, b1_reading_ex, b1_grammar_ex, b1_listening, b1_listening_ex),
        ("B2", b2_reading, b2_reading_ex, b2_grammar_ex, None, None),
        ("C1", c1_reading, c1_reading_ex, c1_grammar_ex, c1_listening, c1_listening_ex),
        ("C2", c2_reading, c2_reading_ex, c2_grammar_ex, None, None),
    ]
    for level, reading, reading_ex, grammar_ex, listening, listening_ex in levels_data:
        level_slug = level.lower()
        listening_html = ""
        if listening and listening_ex:
            listening_html = f"""
                <p class="eyebrow" style="margin-top:var(--space-lg);">{level} · Comprensión Auditiva</p>
                <div class="card"><div class="prose">{listening}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(listening_ex)}</div>"""
        exam_sections.append(f"""<section class="section section--surface" aria-labelledby="sim-{level_slug}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level} · Comprensión de Lectura</p>
                <h2 id="sim-{level_slug}-heading">Examen Simulado {level}</h2>
                <div class="card"><div class="prose">{reading}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(reading_ex)}</div>
                <div style="margin-top:var(--space-md);">{ex_block(grammar_ex)}</div>{listening_html}
            </div>
        </section>""")

    write_page("simulated-exams.html", "Exámenes Simulados — Renan el Profesor · Curso de Español",
               "Secciones de examen simulado al estilo DELE/SIELE en español, con comprensión de lectura y gramática, más claves de respuestas.",
               [header, intro] + exam_sections, active_top="exams", breadcrumb_label="Exámenes Simulados",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


if __name__ == "__main__":
    build_index()
    build_exercises()
    build_extras()
    build_dictionary()
    build_irregular_verbs()
    build_placement_test()
    build_progress()
    build_today_review()
    build_simulated_exams()
