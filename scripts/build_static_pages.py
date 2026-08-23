#!/usr/bin/env python3
"""
Construye cada página independiente de nivel superior: index.html,
exercises.html, extras.html, dictionary.html, irregular-verbs.html,
placement-test.html, progress.html, today-review.html,
simulated-exams.html.

Uso:
    python3 scripts/build_static_pages.py
"""
import html
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


def esc(s):
    return html.escape(s, quote=False)


def ex_block(data):
    return f'<div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(data, ensure_ascii=False)}</script></div>'


def page_header(eyebrow, h1, lede):
    return f"""<div class="page-header">
        {STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{esc(eyebrow)}</p>
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
                    <p class="hero__lede">Un curso de español alineado al MCER, con gramática, vocabulario y ejercicios &mdash; inmersión total: explicaciones en español, ejemplos en español real.<br>&iexcl;Empecemos!</p>
                    <div class="hero__actions">
                        <a class="btn btn--accent" href="levels/pre-a1.html">Empieza con Pre-A1 {ARROW}</a>
                        <a class="btn btn--ghost-inverse" href="placement-test.html">&iquest;Cu&aacute;l es mi nivel?</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <hr class="rule">"""

    level_grammar = {
        "Pre-A1": ["Alfabeto y sonidos", "Saludos y presentaciones", "N&uacute;meros y la hora", "Verbos b&aacute;sicos"],
        "A1": ["Ser &amp; estar", "G&eacute;nero &amp; art&iacute;culos", "Presente regular e irregular", "El verbo gustar"],
        "A2": ["Pret&eacute;rito indefinido &amp; imperfecto", "Verbos con cambio de ra&iacute;z", "Pronombres de objeto", "El imperativo"],
        "B1": ["Presente de subjuntivo", "Pronombres combinados", "Futuro &amp; condicional", "Voseo argentino"],
        "B2": ["Imperfecto de subjuntivo", "Condicionales con si", "Ser/estar avanzado", "Voz pasiva"],
        "C1": ["Pluscuamperfecto de subjuntivo", "Condicionales complejas", "Registro acad&eacute;mico", "Variaci&oacute;n dialectal"],
        "C2": ["Sintaxis compleja", "Registro literario", "Matices l&eacute;xicos", "Variaci&oacute;n regional"],
    }
    cards = []
    romans = ["I", "II", "III", "IV", "V", "VI", "VII"]
    for i, (code, topics) in enumerate(level_grammar.items()):
        roman = romans[i]
        items = "".join(f"<li>{t}</li>" for t in topics)
        level_name = {c: n for c, n, s in site_chrome.LEVELS}[code]
        cards.append(f"""<article class="lesson-card">
            <span class="lesson-card__index" aria-hidden="true">{roman}</span>
            <h3>{code} &mdash; {level_name}</h3>
            <ul style="color:var(--color-text-muted);font-size:var(--step--1);padding-left:1.1em;list-style:disc;display:flex;flex-direction:column;gap:0.25em;">{items}</ul>
            <div class="lesson-card__actions"><a class="btn btn--ghost btn--small" href="levels/{code.lower()}.html">Abrir {code} {ARROW}</a></div>
        </article>""")

    grammar_section = f"""<section id="gramatica" class="section section--surface" aria-labelledby="gramatica-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Gram&aacute;tica</p>
                <h2 id="gramatica-heading">La hoja de ruta de gram&aacute;tica espa&ntilde;ola</h2>
                <p>Un recorrido completo por la gram&aacute;tica espa&ntilde;ola a trav&eacute;s de siete niveles del MCER, desde tu primer ser y estar hasta el registro literario &mdash; abre cualquier nivel para ver todos los temas y empezar a practicar.</p>
            </div>
            <div class="grid">{"".join(cards)}</div>
        </div>
    </section>"""

    ladder_items = []
    ladder_desc = {
        "Pre-A1": "Primer contacto con el idioma: alfabeto, sonidos y frases m&iacute;nimas para sobrevivir en espa&ntilde;ol.",
        "A1": "Frases b&aacute;sicas y expresiones cotidianas para necesidades inmediatas.",
        "A2": "Intercambios sencillos y directos sobre temas familiares y asuntos rutinarios.",
        "B1": "Uso independiente del espa&ntilde;ol para el trabajo, los estudios y los viajes.",
        "B2": "Interacci&oacute;n fluida y espont&aacute;nea, con argumentos claros y detallados.",
        "C1": "Uso flexible y eficaz del idioma para la vida acad&eacute;mica y profesional.",
        "C2": "Dominio preciso y matizado del espa&ntilde;ol en pr&aacute;cticamente cualquier contexto.",
    }
    for code, name, slug in site_chrome.LEVELS:
        ladder_items.append(f"""<li class="ladder__rung">
            <span class="ladder__code" aria-hidden="true">{code}</span>
            <div class="ladder__body">
                <h3>{name}</h3>
                <p>{ladder_desc[code]} <a class="ladder__link" href="levels/{slug}.html">Entra al nivel {ARROW}</a></p>
            </div>
        </li>""")

    cefr_section = f"""<section id="sobre-mcer" class="section section--surface" aria-labelledby="mcer-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">El Marco y tu Camino a Trav&eacute;s de &Eacute;l</p>
                <h2 id="mcer-heading">Sobre el MCER</h2>
                <p>El <strong>Marco Com&uacute;n Europeo de Referencia para las Lenguas (MCER)</strong> es el est&aacute;ndar internacional para describir el nivel de dominio de un idioma. Organiza este curso en siete niveles &mdash; entra en cualquiera de ellos a continuaci&oacute;n.</p>
            </div>
            <ol class="ladder">{"".join(ladder_items)}</ol>
        </div>
    </section>"""

    skills = [
        ("Gram&aacute;tica", "index.html#gramatica", "M3 8 4 8v13a1 1 0 0 0 1 1h6", "Tiempos, formas y reglas estructuradas, organizadas por nivel del MCER y conectadas con ejercicios de pr&aacute;ctica.", '<path d="M3 5.5C3 4.7 3.7 4 4.5 4H10a2 2 0 0 1 2 2v14a1.5 1.5 0 0 0-1.5-1.5H4.5A1.5 1.5 0 0 1 3 17V5.5Z"/><path d="M21 5.5c0-.8-.7-1.5-1.5-1.5H14a2 2 0 0 0-2 2v14a1.5 1.5 0 0 1 1.5-1.5h5.5a1.5 1.5 0 0 0 1.5-1.5V5.5Z"/>'),
        ("Vocabulario", None, None, "Listas de palabras por tema que crecen junto a la gram&aacute;tica de cada nivel, desde los primeros sustantivos hasta colocaciones m&aacute;s precisas.", '<path d="M4 19V6.5A2.5 2.5 0 0 1 6.5 4H8"/><path d="M4 13h4"/><path d="M14 19V6.5A2.5 2.5 0 0 1 16.5 4H20"/><path d="M14 13h4"/>'),
        ("Ejercicios", "exercises.html", None, "Pr&aacute;ctica adicional de lectura y vocabulario, independiente del nivel, para cualquier momento.", '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>'),
        ("Lectura", "exercises.html", None, "Textos y di&aacute;logos de estilo aut&eacute;ntico en espa&ntilde;ol que ponen en juego la gram&aacute;tica y el vocabulario en contexto.", '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/>'),
        ("Escucha", "exercises.html", None, "Transcripciones de di&aacute;logos y monólogos para entrenar el o&iacute;do al espa&ntilde;ol hablado de forma natural.", '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3Z"/><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3Z"/>'),
        ("Escritura", None, None, "Tareas de escritura guiada que crecen desde frases sueltas hasta p&aacute;rrafos argumentativos bien estructurados.", '<path d="M2 22c4-1 8-3 10-5"/><path d="M22 2c-8 0-16 4-16 14 0 2 2 4 4 4C20 20 22 10 22 2Z"/>'),
        ("Conversaci&oacute;n", None, None, "Temas de conversaci&oacute;n para practicar y debatir en cada nivel.", '<path d="M12 15a3 3 0 0 0 3-3V6a3 3 0 0 0-6 0v6a3 3 0 0 0 3 3Z"/><path d="M19 11a7 7 0 0 1-14 0"/><path d="M12 18v3"/><path d="M9 21h6"/>'),
        ("Ex&aacute;menes Simulados", "simulated-exams.html", None, "Secciones de examen simulado al estilo DELE/SIELE, con claves de respuestas, para preparar la certificaci&oacute;n.", '<circle cx="12" cy="15" r="6"/><path d="m9 10-3-7"/><path d="m15 10 3-7"/><path d="M9.5 15.5 12 17l2.5-1.5"/>'),
    ]
    skill_cards = []
    for name, href, _, desc, icon in skills:
        tag_open = f'<a class="skill-card" href="{href}">' if href else '<div class="skill-card">'
        tag_close = "</a>" if href else "</div>"
        skill_cards.append(f'{tag_open}<svg class="skill-card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icon}</svg><h3>{name}</h3><p>{desc}</p>{tag_close}')

    skills_section = f"""<section id="skills" class="section" aria-labelledby="skills-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Un Curr&iacute;culo Completo</p>
                <h2 id="skills-heading">Todas las destrezas, cubiertas</h2>
                <p>Cada nivel del MCER trabaja las mismas destrezas clave, para no dejar nada al azar.</p>
            </div>
            <div class="grid grid--4">{"".join(skill_cards)}</div>
        </div>
    </section>"""

    why_section = f"""<section id="why-us" class="section section--surface" aria-labelledby="why-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Por Qu&eacute; Aprender con Nosotros</p>
                <h2 id="why-heading">Un curso hecho para generar confianza</h2>
            </div>
            <div class="grid grid--3" style="max-width:70rem;margin:0 auto;">
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15 9-2 6-6 2 2-6 6-2Z"/></svg></span>
                    <h3>Organizado seg&uacute;n el MCER</h3>
                    <p>Cada lecci&oacute;n est&aacute; vinculada al Marco Com&uacute;n Europeo, as&iacute; siempre sabes exactamente en qu&eacute; punto est&aacute;s y qu&eacute; sigue.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></span>
                    <h3>Aprende a tu propio ritmo</h3>
                    <p>Avanza nivel por nivel o entra directamente a los ejercicios, el diccionario o el repaso de hoy cuando necesites pr&aacute;ctica extra.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.5 4 5.7 4 9s-1.5 6.5-4 9c-2.5-2.5-4-5.7-4-9s1.5-6.5 4-9Z"/></svg></span>
                    <h3>Basado en espa&ntilde;ol real</h3>
                    <p>Ejemplos y di&aacute;logos naturales, no relleno de manual artificial &mdash; y cada punto de gram&aacute;tica viene con los errores comunes que hay que evitar.</p>
                </div>
            </div>
        </div>
    </section>"""

    cta = f"""<section class="cta-band" aria-labelledby="cta-heading">
        {STARS_ROW}
        <p class="eyebrow" style="justify-content:center;">Empieza cuando quieras</p>
        <h2 id="cta-heading">Disfruta el camino &mdash; empieza hoy con tu nivel.</h2>
        <p>&iquest;No sabes por d&oacute;nde empezar? Haz la prueba de nivel, o simplemente empieza en Pre-A1 y avanza paso a paso.</p>
        <div class="hero__actions">
            <a class="btn btn--accent" href="levels/pre-a1.html">Explora todos los niveles {ARROW}</a>
            <a class="btn btn--ghost-inverse" href="placement-test.html">&iquest;Cu&aacute;l es mi nivel?</a>
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
    header = page_header("Pr&aacute;ctica Independiente", "Ejercicios",
                          "Pr&aacute;ctica adicional de lectura y vocabulario, independiente del nivel &mdash; entra cuando quieras.")

    items = [
        ("A2", "Un Correo de una Amiga", "<p>&iexcl;Hola Marta! &iquest;C&oacute;mo est&aacute;s? Yo estoy muy bien. El s&aacute;bado pasado fui al mercado con mi madre y compramos much&iacute;sima fruta fresca. Despu&eacute;s comimos en un bar peque&ntilde;o cerca de casa.</p><p>El pr&oacute;ximo fin de semana voy a la playa con unas amigas. &iexcl;No veo la hora! &iquest;T&uacute; qu&eacute; planes tienes para este fin de semana? &iexcl;Escr&iacute;beme pronto!<br>Un abrazo,<br>Laura</p>",
         {"id": "ex-a2-correo", "type": "true-false", "title": "Comprobaci&oacute;n de Comprensi&oacute;n", "items": [
             {"id": "exa2m1", "statement": "Laura fue al mercado con su madre.", "answer": True, "explanation": "&laquo;Fui al mercado con mi madre.&raquo;"},
             {"id": "exa2m2", "statement": "Laura va a la monta&ntilde;a el pr&oacute;ximo fin de semana.", "answer": False, "explanation": "Va a la playa (el mar), no a la monta&ntilde;a."},
         ]}),
        ("B1", "Un Anuncio de Trabajo", "<p><strong>Se busca camarero/a para restaurante en el centro de Sevilla.</strong> Se requiere experiencia m&iacute;nima de un a&ntilde;o en el sector de la hosteler&iacute;a. Turnos flexibles, tambi&eacute;n los fines de semana. Se valora el conocimiento de ingl&eacute;s. Sueldo seg&uacute;n experiencia. Para postularse, enviar el curr&iacute;culum a empleo@restaurantesevilla.es antes del viernes.</p>",
         {"id": "ex-b1-anuncio", "type": "multiple-choice", "title": "Comprobaci&oacute;n de Comprensi&oacute;n", "items": [
             {"id": "exb1a1", "prompt": "&iquest;Cu&aacute;nta experiencia se requiere?", "options": ["No se requiere experiencia", "Al menos un a&ntilde;o", "Al menos cinco a&ntilde;os"], "answerIndex": 1, "explanation": "&laquo;Se requiere experiencia m&iacute;nima de un a&ntilde;o.&raquo;"},
             {"id": "exb1a2", "prompt": "&iquest;Qu&eacute; se valora como un plus?", "options": ["Tener coche propio", "Saber ingl&eacute;s", "Vivir cerca"], "answerIndex": 1, "explanation": "&laquo;Se valora el conocimiento de ingl&eacute;s.&raquo;"},
         ]}),
        ("B2", "Una Rese&ntilde;a de Restaurante", "<p>Era esc&eacute;ptico antes de reservar, dado el gran n&uacute;mero de rese&ntilde;as contradictorias en internet. Sin embargo, mi experiencia fue claramente positiva. El servicio, aunque no impecable, fue amable, y los platos &mdash;en particular los primeros&mdash; estaban preparados con cuidado e ingredientes de calidad. &Uacute;nico punto negativo: los tiempos de espera entre un plato y otro fueron bastante largos.</p>",
         {"id": "ex-b2-resena", "type": "true-false", "title": "Comprobaci&oacute;n de Comprensi&oacute;n", "items": [
             {"id": "exb2r1", "statement": "La impresi&oacute;n general del autor fue positiva.", "answer": True, "explanation": "&laquo;Mi experiencia fue claramente positiva.&raquo;"},
             {"id": "exb2r2", "statement": "El plato principal se menciona como lo peor de la comida.", "answer": False, "explanation": "Los primeros platos fueron elogiados; la queja fue sobre los tiempos de espera entre platos."},
         ]}),
        ("C1", "Un Breve Art&iacute;culo sobre el D&iacute;a de los Muertos", "<p>El D&iacute;a de los Muertos, celebrado principalmente en M&eacute;xico cada 1 y 2 de noviembre, contin&uacute;a atrayendo cada a&ntilde;o a millones de visitantes, atra&iacute;dos tanto por su inigualable riqueza simb&oacute;lica como por la atm&oacute;sfera &uacute;nica de sus altares y desfiles. A pesar de los desaf&iacute;os que plantea el turismo masivo &mdash;desde la gesti&oacute;n de las multitudes hasta la preservaci&oacute;n del sentido original de la festividad&mdash;, las comunidades han sabido, en los &uacute;ltimos a&ntilde;os, desarrollar formas m&aacute;s sostenibles de compartir la tradici&oacute;n, animando a los visitantes a conocer tambi&eacute;n las costumbres de los pueblos menos frecuentados.</p>",
         {"id": "ex-c1-diadelosmuertos", "type": "multiple-choice", "title": "Comprobaci&oacute;n de Comprensi&oacute;n", "items": [
             {"id": "exc1f1", "prompt": "&iquest;Qu&eacute; desaf&iacute;o menciona el art&iacute;culo?", "options": ["La falta de altares tradicionales", "La gesti&oacute;n del turismo masivo", "La escasez de flores de cempas&uacute;chil"], "answerIndex": 1, "explanation": "Se menciona directamente &laquo;los desaf&iacute;os que plantea el turismo masivo&raquo;."},
         ]}),
    ]
    sections = [header]
    for level, title, passage, ex in items:
        sections.append(f"""<section class="section section--surface" aria-labelledby="ex-{ex['id']}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level}</p>
                <h2 id="ex-{ex['id']}-heading">{esc(title)}</h2>
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
    header = page_header("M&aacute;s All&aacute; de la Gram&aacute;tica", "Extras",
                          "Expresiones comunes, t&uacute; frente a usted (y vos), situaciones cotidianas, y breves notas culturales.")

    expressions = [
        ("&iexcl;Vale!", "De acuerdo, est&aacute; bien.", "Uso muy frecuente en Espa&ntilde;a para aceptar algo o confirmar un plan."),
        ("&iexcl;Qu&eacute; va!", "&iexcl;Para nada! / &iexcl;Qu&eacute; dices!", "Para negar con &eacute;nfasis algo que alguien acaba de decir."),
        ("Ni idea", "No lo s&eacute; en absoluto.", "Respuesta informal, muy com&uacute;n entre amigos."),
        ("&iexcl;Venga!", "&iexcl;Vamos! / &iexcl;An&iacute;mate!", "&Aacute;nimo o invitaci&oacute;n a actuar, muy usado en Espa&ntilde;a en el habla diaria."),
        ("&iexcl;Ojal&aacute;!", "&iexcl;Espero que s&iacute;, con toda el alma!", "Expresa un deseo intenso; viene del &aacute;rabe &laquo;law &scaron;&aacute; lla&raquo;."),
        ("No pasa nada", "No hay problema, tranquilo.", "Para quitar importancia a un error o una disculpa."),
        ("&iexcl;Qu&eacute; guay!", "&iexcl;Qu&eacute; genial!", "Coloquial y muy espa&ntilde;ol; en Am&eacute;rica Latina se dice a menudo &laquo;qu&eacute; ch&eacute;vere&raquo; o &laquo;qu&eacute; padre&raquo;."),
        ("Ostras", "&iexcl;Vaya! (expresi&oacute;n de sorpresa)", "Eufemismo educado de una palabrota; se usa incluso en contextos formales."),
        ("&iexcl;Anda!", "&iexcl;Vaya! / &iexcl;No me digas!", "Sorpresa o incredulidad; tambi&eacute;n anima a alguien a hacer algo."),
        ("Estar en las nubes", "Estar distra&iacute;do, no prestar atenci&oacute;n.", "Expresi&oacute;n figurada muy com&uacute;n en toda situaci&oacute;n informal."),
    ]
    exp_rows = "".join(f"<tr><td><strong>{esc(it)}</strong></td><td>{esc(sig)}</td><td>{esc(note)}</td></tr>" for it, sig, note in expressions)

    expressions_section = f"""<section id="expressions" class="section section--surface" aria-labelledby="expr-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Suena M&aacute;s Natural</p>
                <h2 id="expr-heading">Expresiones Comunes</h2>
                <p>Frases breves y muy frecuentes que hacen que tu espa&ntilde;ol suene natural, no de manual.</p>
            </div>
            <div class="table-scroll"><table class="ref-table"><thead><tr><th>Expresi&oacute;n</th><th>Significado</th><th>Nota</th></tr></thead><tbody>{exp_rows}</tbody></table></div>
        </div>
    </section>"""

    formal_informal = f"""<section id="formal-informal" class="section section--tight" aria-labelledby="fi-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Registro</p>
                <h2 id="fi-heading">T&uacute;, Usted&hellip; y Vos</h2>
                <p>Elegir t&uacute; o usted es solo el comienzo &mdash; y en gran parte de Am&eacute;rica existe una tercera opci&oacute;n: vos.</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Informal (t&uacute;)</h3>
                    <ul class="rules-list">
                        <li>Hola, &iquest;c&oacute;mo est&aacute;s?</li>
                        <li>Perdona, &iquest;tienes un minuto?</li>
                        <li>&iquest;Puedes ayudarme?</li>
                        <li>Te quer&iacute;a preguntar una cosa.</li>
                        <li>&iexcl;Hasta pronto! / &iexcl;Nos vemos!</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Formal (usted)</h3>
                    <ul class="rules-list">
                        <li>Buenos d&iacute;as, &iquest;c&oacute;mo est&aacute; usted?</li>
                        <li>Disculpe, &iquest;tendr&iacute;a un minuto?</li>
                        <li>&iquest;Podr&iacute;a ayudarme?</li>
                        <li>Quer&iacute;a preguntarle una cosa.</li>
                        <li>Saludos cordiales / Hasta luego</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Regional (vos &mdash; Argentina, Uruguay&hellip;)</h3>
                    <ul class="rules-list">
                        <li>Hola, &iquest;c&oacute;mo est&aacute;s vos?</li>
                        <li>Che, &iquest;ten&eacute;s un minuto?</li>
                        <li>&iquest;Vos pod&eacute;s ayudarme?</li>
                        <li>Te quer&iacute;a preguntar una cosa.</li>
                        <li>&iexcl;Nos vemos, che!</li>
                    </ul>
                </div>
            </div>
            <div class="notice mt-lg"><strong>Regla general</strong><p>Usa usted con desconocidos, personas mayores, autoridades y en cualquier contexto profesional &mdash; hasta que te inviten a tutear. En Argentina, Uruguay y buena parte de Centroam&eacute;rica, vos reemplaza a t&uacute; incluso en las situaciones informales cotidianas.</p></div>
        </div>
    </section>"""

    everyday = f"""<section id="everyday" class="section section--surface" aria-labelledby="everyday-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Situaciones Reales</p>
                <h2 id="everyday-heading">Espa&ntilde;ol de Todos los D&iacute;as</h2>
                <p>Intercambios breves y pr&aacute;cticos para situaciones con las que te vas a encontrar de verdad.</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>En un bar o caf&eacute;</h3>
                    <p><em>Un caf&eacute; con leche, por favor.</em></p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">En muchos bares espa&ntilde;oles te sientas y el camarero te atiende en la mesa; en otros pa&iacute;ses hispanohablantes es m&aacute;s com&uacute;n pedir y pagar directamente en la barra.</p>
                </div>
                <div class="card">
                    <h3>En un mercado</h3>
                    <p><em>&iquest;Cu&aacute;nto cuestan estas manzanas?</em></p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">En algunos pa&iacute;ses de Am&eacute;rica Latina es habitual regatear un poco en el mercado, algo que casi nunca ocurre en Espa&ntilde;a.</p>
                </div>
                <div class="card">
                    <h3>Charla trivial</h3>
                    <p><em>Qu&eacute; calor/fr&iacute;o hace hoy, &iquest;no?</em></p>
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
                    <p>En Espa&ntilde;a se suele almorzar entre las 2 y las 3 de la tarde y cenar despu&eacute;s de las 9; en gran parte de Am&eacute;rica Latina el almuerzo es antes, entre el mediod&iacute;a y la 1, y la cena suele ser bastante m&aacute;s temprana, alrededor de las 7 u 8.</p>
                </div>
                <div class="card">
                    <h3>La cultura del mate</h3>
                    <p>En Argentina, Uruguay y Paraguay, el mate es mucho m&aacute;s que una infusi&oacute;n: compartir la bombilla y la ronda de mate es un ritual social diario, con su propio vocabulario (cebar, lavado, amargo, dulce).</p>
                </div>
                <div class="card">
                    <h3>Un idioma, muchos acentos</h3>
                    <p>El espa&ntilde;ol es lengua oficial en m&aacute;s de veinte pa&iacute;ses, desde Espa&ntilde;a hasta Argentina, pasando por M&eacute;xico, el Caribe y toda Sudam&eacute;rica &mdash; cada regi&oacute;n tiene su propio vocabulario, entonaci&oacute;n y expresiones, y ninguna variante es &laquo;m&aacute;s correcta&raquo; que otra.</p>
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
        <h3>{esc(name)}</h3>
        <p>{esc(desc)}</p>
        <div class="card__foot">
            <a class="{btn_cls}" data-dict-link href="{sample_url}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>Buscar</a>
        </div>
    </div>"""


def build_dictionary():
    header = page_header("Diccionario y Referencia", "Busca Cualquier Palabra en Espa&ntilde;ol",
                          "Escribe una palabra una sola vez y &aacute;brela directamente en cualquiera de estos diccionarios en espa&ntilde;ol, o usa las herramientas de pronunciaci&oacute;n de m&aacute;s abajo.")

    input_section = f"""<section class="section section--surface" aria-labelledby="primary-dict-heading">
        <div class="section__inner">
            <h2 id="primary-dict-heading" class="visually-hidden">Diccionarios Principales</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-lg);">
                <label for="dict-word" class="eyebrow" style="margin-bottom:0.6em;display:block;">Tu palabra</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="dict-word" class="dict-input" placeholder="Escribe una palabra, p. ej. &laquo;ojal&aacute;&raquo;" autocomplete="off" data-dict-word>
                </div>
                <p class="notice mt-lg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Cada tarjeta de abajo se actualiza mientras escribes. Pulsa Enter para saltar a uno al azar de los cuatro diccionarios principales.</p>
            </div>
            <div class="grid">
                {dict_card("RAE — Diccionario de la lengua espa&ntilde;ola", "El diccionario oficial de la Real Academia Espa&ntilde;ola: la referencia definitiva para definiciones, gram&aacute;tica y uso correcto del espa&ntilde;ol.", "https://dle.rae.es/{word}", "ojal&aacute;")}
                {dict_card("Wikcionario en espa&ntilde;ol", "Diccionario colaborativo con etimolog&iacute;a, ejemplos y variantes regionales de miles de palabras.", "https://es.wiktionary.org/wiki/{word}", "ojal&aacute;")}
                {dict_card("Fund&eacute;u BBVA", "Recomendaciones sobre el uso correcto del espa&ntilde;ol: dudas frecuentes, neologismos y cuestiones de estilo.", "https://www.fundeu.es/?s={word}", "ojal&aacute;")}
                {dict_card("Sin&oacute;nimos y Ant&oacute;nimos", "Encuentra sin&oacute;nimos y ant&oacute;nimos para enriquecer tu vocabulario y evitar repeticiones.", "https://www.wordreference.com/sinonimos/{word}", "ojal&aacute;")}
            </div>
        </div>
    </section>"""

    more_section = f"""<section class="section" aria-labelledby="more-dict-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Si Necesitas M&aacute;s</p>
                <h2 id="more-dict-heading">M&aacute;s Diccionarios y Pronunciaci&oacute;n</h2>
                <p>Para una segunda opini&oacute;n, conjugar un verbo, o para escuchar c&oacute;mo se pronuncia una palabra de verdad.</p>
            </div>
            <div class="grid">
                {dict_card("Conjugador de Verbos", "Tablas completas de conjugaci&oacute;n para cualquier verbo espa&ntilde;ol, en todos los tiempos y modos.", "https://www.conjugacion.es/del/verbo/{word}.php", "hablar", featured=False)}
                {dict_card("Forvo", "Pronunciaciones reales grabadas por hablantes nativos de espa&ntilde;ol de distintos pa&iacute;ses.", "https://forvo.com/word/{word}/#es", "ojal&aacute;", featured=False)}
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
    ("ser", "existir, tener cierta identidad o cualidad permanente", "soy", "fui", "ra&iacute;z totalmente irregular"),
    ("estar", "expresar ubicaci&oacute;n, estado o condici&oacute;n temporal", "estoy", "estuve", "ra&iacute;z irregular en el pret&eacute;rito (estuv-)"),
    ("ir", "trasladarse de un lugar a otro", "voy", "fui", "ra&iacute;z totalmente irregular"),
    ("tener", "poseer algo o sentir algo", "tengo", "tuve", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito"),
    ("hacer", "realizar o producir algo", "hago", "hice", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito"),
    ("decir", "comunicar algo con palabras", "digo", "dije", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito"),
    ("poder", "tener la capacidad de hacer algo", "puedo", "pude", "diptongaci&oacute;n o&rarr;ue + ra&iacute;z irregular en pret&eacute;rito"),
    ("querer", "desear algo o sentir cari&ntilde;o", "quiero", "quise", "diptongaci&oacute;n e&rarr;ie + ra&iacute;z irregular en pret&eacute;rito"),
    ("saber", "conocer un hecho o tener informaci&oacute;n", "s&eacute;", "supe", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito"),
    ("poner", "colocar algo en un lugar", "pongo", "puse", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito"),
    ("venir", "trasladarse hacia el lugar donde est&aacute; el hablante", "vengo", "vine", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito"),
    ("salir", "irse de un lugar", "salgo", "sal&iacute;", "1&ordf; persona irregular"),
    ("dar", "entregar algo a alguien", "doy", "di", "1&ordf; persona irregular + pret&eacute;rito sin acento"),
    ("ver", "percibir algo con los ojos", "veo", "vi", "1&ordf; persona irregular + pret&eacute;rito sin acento"),
    ("haber", "verbo auxiliar de los tiempos compuestos; tambi&eacute;n &laquo;existir&raquo; (hay)", "he", "hube", "ra&iacute;z totalmente irregular"),
    ("traer", "llevar algo hacia el hablante", "traigo", "traje", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito"),
    ("caer", "irse hacia abajo por la fuerza de la gravedad", "caigo", "ca&iacute;", "1&ordf; persona irregular"),
    ("o&iacute;r", "percibir sonidos con el o&iacute;do", "oigo", "o&iacute;", "1&ordf; persona irregular + cambio ortogr&aacute;fico (oy&oacute;)"),
    ("conducir", "guiar un veh&iacute;culo", "conduzco", "conduje", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito (-duje)"),
    ("producir", "crear o fabricar algo", "produzco", "produje", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito (-duje)"),
    ("huir", "escapar de un peligro o lugar", "huyo", "hu&iacute;", "cambio ortogr&aacute;fico i&rarr;y"),
    ("construir", "edificar o fabricar algo", "construyo", "constru&iacute;", "cambio ortogr&aacute;fico i&rarr;y"),
    ("seguir", "continuar haciendo algo o ir detr&aacute;s de alguien", "sigo", "segu&iacute;", "cambio de ra&iacute;z e&rarr;i + cambio ortogr&aacute;fico gu&rarr;g"),
    ("pedir", "solicitar algo", "pido", "ped&iacute;", "cambio de ra&iacute;z e&rarr;i"),
    ("servir", "ser &uacute;til para algo o atender a alguien", "sirvo", "serv&iacute;", "cambio de ra&iacute;z e&rarr;i"),
    ("dormir", "estar en estado de sue&ntilde;o", "duermo", "dorm&iacute;", "diptongaci&oacute;n o&rarr;ue"),
    ("morir", "dejar de vivir", "muero", "mor&iacute;", "diptongaci&oacute;n o&rarr;ue"),
    ("sentir", "experimentar una sensaci&oacute;n o emoci&oacute;n", "siento", "sent&iacute;", "diptongaci&oacute;n e&rarr;ie"),
    ("preferir", "gustar m&aacute;s una cosa que otra", "prefiero", "prefer&iacute;", "diptongaci&oacute;n e&rarr;ie"),
    ("jugar", "realizar una actividad de ocio o deporte", "juego", "jugu&eacute;", "diptongaci&oacute;n u&rarr;ue + cambio ortogr&aacute;fico g&rarr;gu"),
    ("empezar", "comenzar algo", "empiezo", "empec&eacute;", "diptongaci&oacute;n e&rarr;ie + cambio ortogr&aacute;fico z&rarr;c"),
    ("pensar", "usar la mente para razonar", "pienso", "pens&eacute;", "diptongaci&oacute;n e&rarr;ie"),
    ("volver", "regresar a un lugar", "vuelvo", "volv&iacute;", "diptongaci&oacute;n o&rarr;ue"),
    ("encontrar", "hallar algo o a alguien", "encuentro", "encontr&eacute;", "diptongaci&oacute;n o&rarr;ue"),
    ("contar", "narrar algo o decir n&uacute;meros en orden", "cuento", "cont&eacute;", "diptongaci&oacute;n o&rarr;ue"),
    ("entender", "comprender algo", "entiendo", "entend&iacute;", "diptongaci&oacute;n e&rarr;ie"),
    ("perder", "dejar de tener algo", "pierdo", "perd&iacute;", "diptongaci&oacute;n e&rarr;ie"),
    ("mostrar", "hacer ver algo a alguien", "muestro", "mostr&eacute;", "diptongaci&oacute;n o&rarr;ue"),
    ("mover", "cambiar algo de lugar", "muevo", "mov&iacute;", "diptongaci&oacute;n o&rarr;ue"),
    ("recordar", "traer algo a la memoria", "recuerdo", "record&eacute;", "diptongaci&oacute;n o&rarr;ue"),
    ("oler", "percibir un olor", "huelo", "ol&iacute;", "diptongaci&oacute;n o&rarr;hue"),
    ("caber", "poder contenerse dentro de un espacio", "quepo", "cupe", "1&ordf; persona irregular + ra&iacute;z irregular en pret&eacute;rito"),
    ("valer", "tener un precio o un m&eacute;rito", "valgo", "val&iacute;", "1&ordf; persona irregular"),
    ("andar", "caminar o moverse", "ando", "anduve", "ra&iacute;z irregular en el pret&eacute;rito"),
    ("cerrar", "hacer que algo deje de estar abierto", "cierro", "cerr&eacute;", "diptongaci&oacute;n e&rarr;ie"),
    ("comenzar", "empezar algo, dar inicio a algo", "comienzo", "comenc&eacute;", "diptongaci&oacute;n e&rarr;ie + cambio ortogr&aacute;fico z&rarr;c"),
]


def build_irregular_verbs():
    header = page_header("Referencia", "Verbos Irregulares del Espa&ntilde;ol",
                          "Los verbos irregulares m&aacute;s comunes, con su presente (yo), pret&eacute;rito (yo) y tipo de irregularidad &mdash; escribe para filtrar.")

    rows = "".join(
        f"<tr><td><strong>{esc(inf)}</strong></td><td>{esc(meaning)}</td><td>{esc(pres)}</td><td>{esc(pret)}</td><td class=\"text-muted\">{esc(tipo)}</td></tr>"
        for inf, meaning, pres, pret, tipo in IRREGULAR_VERBS
    )

    section = f"""<section class="section section--surface" aria-labelledby="verbs-heading">
        <div class="section__inner">
            <h2 id="verbs-heading" class="visually-hidden">Verbos Irregulares</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-md);">
                <label for="verb-filter" class="eyebrow" style="margin-bottom:0.6em;display:block;">Filtrar</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="verb-filter" class="dict-input" placeholder="Escribe para filtrar, p. ej. &laquo;tener&raquo; o &laquo;ser&raquo;" autocomplete="off" data-verb-filter>
                </div>
                <p class="notice mt-lg" data-verb-count><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Mostrando los {len(IRREGULAR_VERBS)} verbos.</p>
                <p class="notice mt-lg" data-verb-empty hidden>No se encontraron verbos que coincidan con &laquo;<span data-verb-empty-term></span>&raquo;.</p>
            </div>
            <div class="table-scroll">
                <table class="ref-table">
                    <caption>Verbos irregulares comunes del espa&ntilde;ol</caption>
                    <thead><tr><th>Infinitivo</th><th>Definici&oacute;n</th><th>Presente (yo)</th><th>Pret&eacute;rito (yo)</th><th>Tipo de Irregularidad</th></tr></thead>
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
                          "28 preguntas, entre tres y cuatro por nivel de Pre-A1 a C2. Responde las que puedas &mdash; la sensaci&oacute;n de d&oacute;nde empieza a costarte es la mejor gu&iacute;a de tu nivel real.")

    blocks = [
        ("Pre-A1", [
            {"id": "pt-prea1-1", "prompt": "Buenos d&iacute;as, &iquest;c&oacute;mo ___ usted?", "options": ["est&aacute;", "est&aacute;s", "es"], "answerIndex": 0, "explanation": "Con usted se usa la forma de &eacute;l/ella: est&aacute;."},
            {"id": "pt-prea1-2", "prompt": "Tengo veinte ___.", "options": ["a&ntilde;o", "a&ntilde;os", "anos"], "answerIndex": 1, "explanation": "La edad se expresa con el sustantivo en plural: a&ntilde;os."},
            {"id": "pt-prea1-3", "prompt": "Son las tres de la tarde. Se dice: &laquo;___, &iquest;c&oacute;mo est&aacute;s?&raquo;", "options": ["Buenos d&iacute;as", "Buenas tardes", "Buenas noches"], "answerIndex": 1, "explanation": "Entre el mediod&iacute;a y el anochecer se usa &laquo;buenas tardes&raquo;."},
            {"id": "pt-prea1-4", "prompt": "Yo ___ estudiante.", "options": ["soy", "eres", "es"], "answerIndex": 0, "explanation": "La primera persona del verbo ser es soy."},
        ]),
        ("A1", [
            {"id": "pt-a1-1", "prompt": "Barcelona ___ una ciudad muy bonita.", "options": ["es", "est&aacute;", "son"], "answerIndex": 0, "explanation": "Cualidad permanente &rarr; ser."},
            {"id": "pt-a1-2", "prompt": "El t&eacute; ___ fr&iacute;o ahora, no lo quiero.", "options": ["es", "est&aacute;", "eres"], "answerIndex": 1, "explanation": "Estado temporal &rarr; estar."},
            {"id": "pt-a1-3", "prompt": "___ chico es mi hermano.", "options": ["El", "La", "Los"], "answerIndex": 0, "explanation": "Chico es masculino singular &rarr; el."},
            {"id": "pt-a1-4", "prompt": "Me ___ mucho las pel&iacute;culas de terror.", "options": ["gusto", "gusta", "gustan"], "answerIndex": 2, "explanation": "Gustar concuerda con lo que gusta: &laquo;las pel&iacute;culas&raquo; (plural) &rarr; gustan."},
        ]),
        ("A2", [
            {"id": "pt-a2-1", "prompt": "Ayer ___ (yo - comer) en un restaurante muy bueno.", "options": ["com&iacute;", "como", "com&iacute;a"], "answerIndex": 0, "explanation": "Acci&oacute;n puntual y terminada &rarr; pret&eacute;rito indefinido."},
            {"id": "pt-a2-2", "prompt": "De peque&ntilde;o, ___ (yo - vivir) en un pueblo peque&ntilde;o.", "options": ["viv&iacute;", "viv&iacute;a", "he vivido"], "answerIndex": 1, "explanation": "Descripci&oacute;n de una situaci&oacute;n habitual en el pasado &rarr; imperfecto."},
            {"id": "pt-a2-3", "prompt": "Ella ___ (dormir) muy poco anoche.", "options": ["durmi&oacute;", "dormi&oacute;", "dorm&iacute;a"], "answerIndex": 0, "explanation": "Dormir cambia la ra&iacute;z o&rarr;u en la tercera persona del pret&eacute;rito: durmi&oacute;."},
            {"id": "pt-a2-4", "prompt": "&iexcl;___ (comer, t&uacute;) toda la verdura!", "options": ["come", "comes", "comas"], "answerIndex": 0, "explanation": "Imperativo afirmativo informal de comer: come."},
        ]),
        ("B1", [
            {"id": "pt-b1-1", "prompt": "Espero que ___ (t&uacute; - venir) a mi cumplea&ntilde;os.", "options": ["vienes", "vengas", "vendr&aacute;s"], "answerIndex": 1, "explanation": "Esperar que exige subjuntivo presente: vengas."},
            {"id": "pt-b1-2", "prompt": "&iquest;Me prestas tu coche? S&iacute;, ___ presto sin problema. (te + lo)", "options": ["te lo", "te la", "se lo"], "answerIndex": 0, "explanation": "Objeto indirecto (te) + directo masculino (el coche &rarr; lo) = te lo."},
            {"id": "pt-b1-3", "prompt": "El a&ntilde;o que viene ___ (yo - terminar) mis estudios.", "options": ["terminar&eacute;", "termino", "terminaba"], "answerIndex": 0, "explanation": "Plan futuro &rarr; futuro simple."},
            {"id": "pt-b1-4", "prompt": "En Argentina, en lugar de &laquo;t&uacute; tienes&raquo;, se dice: &laquo;___ ten&eacute;s&raquo;.", "options": ["vos", "t&uacute;", "usted"], "answerIndex": 0, "explanation": "El voseo rioplatense reemplaza a t&uacute; por vos, con su propia forma verbal."},
        ]),
        ("B2", [
            {"id": "pt-b2-1", "prompt": "Si ___ (yo - tener) m&aacute;s tiempo libre, aprender&iacute;a a tocar la guitarra.", "options": ["tengo", "tuviera", "tendr&iacute;a"], "answerIndex": 1, "explanation": "Condicional hipot&eacute;tico (2&ordm; tipo): si + imperfecto de subjuntivo."},
            {"id": "pt-b2-2", "prompt": "Ojal&aacute; ___ (ellos - llegar) pronto, ya es tarde.", "options": ["llegan", "lleguen", "llegaran"], "answerIndex": 1, "explanation": "Ojal&aacute; + subjuntivo presente expresa un deseo sobre algo a&uacute;n posible."},
            {"id": "pt-b2-3", "prompt": "La puerta ___ abierta cuando llegu&eacute;.", "options": ["es", "estaba", "fue"], "answerIndex": 1, "explanation": "Resultado de una acci&oacute;n anterior &rarr; estar + participio."},
            {"id": "pt-b2-4", "prompt": "El puente ___ (construir) en el siglo XIX.", "options": ["fue construido", "construy&oacute;", "ha construido"], "answerIndex": 0, "explanation": "Voz pasiva: ser + participio (concordando en g&eacute;nero y n&uacute;mero)."},
        ]),
        ("C1", [
            {"id": "pt-c1-1", "prompt": "Si lo ___ (yo - saber) antes, te habr&iacute;a avisado.", "options": ["supiera", "hubiera sabido", "sabr&iacute;a"], "answerIndex": 1, "explanation": "Condicional del 3er tipo (irreal en el pasado): si + pluscuamperfecto de subjuntivo."},
            {"id": "pt-c1-2", "prompt": "Me extra&ntilde;&oacute; que todav&iacute;a no ___ (ellos - llegar) a esa hora.", "options": ["hubieran llegado", "llegaron", "llegaran"], "answerIndex": 0, "explanation": "Pluscuamperfecto de subjuntivo: acci&oacute;n anterior a otra ya pasada."},
            {"id": "pt-c1-3", "prompt": "&iquest;Cu&aacute;l de estas frases pertenece a un registro acad&eacute;mico?", "options": ["Cabe destacar que los resultados obtenidos confirman la hip&oacute;tesis.", "Oye, mira lo que encontr&eacute;, &iexcl;es incre&iacute;ble!", "Qu&eacute; fuerte lo de ayer, &iquest;no?"], "answerIndex": 0, "explanation": "El registro acad&eacute;mico evita coloquialismos y usa construcciones impersonales como &laquo;cabe destacar&raquo;."},
            {"id": "pt-c1-4", "prompt": "En M&eacute;xico, &laquo;&iquest;qu&eacute; onda?&raquo; es una forma coloquial de preguntar&hellip;", "options": ["&iquest;c&oacute;mo est&aacute;s?", "&iquest;d&oacute;nde vives?", "&iquest;cu&aacute;nto cuesta?"], "answerIndex": 0, "explanation": "Es un saludo informal muy extendido en el espa&ntilde;ol mexicano, equivalente a &laquo;&iquest;qu&eacute; tal?&raquo;."},
        ]),
        ("C2", [
            {"id": "pt-c2-1", "prompt": "&iquest;Qu&eacute; oraci&oacute;n usa una estructura enf&aacute;tica (oraci&oacute;n hendida)?", "options": ["El problema me preocupa mucho.", "Es el problema lo que m&aacute;s me preocupa.", "Me preocupa bastante el problema."], "answerIndex": 1, "explanation": "Esta es una oraci&oacute;n hendida, que destaca &laquo;el problema&raquo; mediante &laquo;es... lo que&raquo;."},
            {"id": "pt-c2-2", "prompt": "Debo ___ una decisi&oacute;n importante.", "options": ["hacer", "tomar", "dar"], "answerIndex": 1, "explanation": "La colocaci&oacute;n fija en espa&ntilde;ol es &laquo;tomar una decisi&oacute;n&raquo;."},
            {"id": "pt-c2-3", "prompt": "&laquo;Es posible que&raquo; suele ir seguido de&hellip;", "options": ["el indicativo", "el subjuntivo", "el imperativo"], "answerIndex": 1, "explanation": "&laquo;Es posible que&raquo; presenta algo incierto, lo que exige subjuntivo."},
            {"id": "pt-c2-4", "prompt": "Trabajo mucho ___ ganar m&aacute;s dinero.", "options": ["por", "para", "de"], "answerIndex": 1, "explanation": "La finalidad de una acci&oacute;n se expresa con para."},
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
            <p class="eyebrow">C&oacute;mo Leer Tus Resultados</p>
            <h2 id="pt-guide-heading">Qu&eacute; Significa Tu Puntuaci&oacute;n</h2>
            <ul class="summary-list">
                <li>Te costaron incluso las preguntas de Pre-A1 &rarr; empieza en <a href="levels/pre-a1.html">Pre-A1</a> y construye las bases desde cero.</li>
                <li>C&oacute;modo en Pre-A1, con dificultad desde A1 &rarr; empieza en <a href="levels/a1.html">A1</a>.</li>
                <li>C&oacute;modo hasta A2, con dificultad desde B1 &rarr; empieza en <a href="levels/b1.html">B1</a>.</li>
                <li>C&oacute;modo hasta B1, con dificultad desde B2 &rarr; empieza en <a href="levels/b2.html">B2</a>.</li>
                <li>C&oacute;modo hasta B2, con dificultad desde C1 &rarr; empieza en <a href="levels/c1.html">C1</a>.</li>
                <li>Acertaste todo, incluido C2 &rarr; repasa las lecciones de <a href="levels/c2.html">C2</a> para pulir detalles, o explora la p&aacute;gina de <a href="extras.html">Extras</a>.</li>
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
                          "XP, rachas e insignias, guardado &uacute;nicamente en este dispositivo &mdash; nada se env&iacute;a nunca a ning&uacute;n servidor.")

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
            <p style="color:var(--color-text-muted);">Esto borra tu XP, tu racha y tus insignias en este dispositivo. El historial de repetici&oacute;n espaciada (Repaso de Hoy) se guarda por separado y no se ve afectado.</p>
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
    header = page_header("Repetici&oacute;n Espaciada", "Repaso de Hoy",
                          "Un repaso breve y diario de los ejercicios que has fallado antes &mdash; generado autom&aacute;ticamente a partir de tu propio historial.")

    section = f"""<section class="section section--surface" aria-labelledby="review-heading">
        <div class="section__inner">
            <h2 id="review-heading" class="visually-hidden">Repaso</h2>
            <div id="review-status-box" class="notice"><p>Cargando tu cola de repaso&hellip;</p></div>
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
    header = page_header("Pr&aacute;ctica de Examen", "Ex&aacute;menes Simulados",
                          "Secciones de pr&aacute;ctica al estilo de las certificaciones oficiales de espa&ntilde;ol &mdash; DELE y SIELE &mdash; con claves de respuestas.")

    intro = f"""<section class="section section--tight" aria-labelledby="exams-intro-heading">
        <div class="section__inner section__inner--narrow">
            <h2 id="exams-intro-heading" class="visually-hidden">Sobre Estos Ex&aacute;menes</h2>
            <p style="color:var(--color-text-muted);">El espa&ntilde;ol cuenta con dos certificaciones internacionales de referencia como lengua extranjera: el <strong>DELE</strong> (Diplomas de Espa&ntilde;ol como Lengua Extranjera, del Instituto Cervantes) y el <strong>SIELE</strong> (Servicio Internacional de Evaluaci&oacute;n de la Lengua Espa&ntilde;ola, respaldado por el propio Instituto Cervantes y varias universidades). Ambos eval&uacute;an las mismas cuatro destrezas &mdash; comprensi&oacute;n de lectura, comprensi&oacute;n auditiva, expresi&oacute;n escrita y expresi&oacute;n oral &mdash; en los niveles del MCER de A1 a C2. Las secciones siguientes son pr&aacute;ctica en ese estilo, no ex&aacute;menes oficiales reales.</p>
        </div>
    </section>"""

    b1_reading = ("<p>En los &uacute;ltimos a&ntilde;os, cada vez m&aacute;s personas en Espa&ntilde;a y Am&eacute;rica Latina eligen trabajar desde casa al menos un par de d&iacute;as a la semana. Seg&uacute;n una encuesta reciente, la mayor&iacute;a de los trabajadores se declara m&aacute;s satisfecha que antes, sobre todo gracias al tiempo que ahorran en los desplazamientos. Sin embargo, algunos encuestados se&ntilde;alan dificultades para separar la vida personal del trabajo, y se quejan de jornadas laborales m&aacute;s largas de lo habitual.</p>")
    b1_reading_ex = {"id": "sim-b1-reading", "type": "true-false", "title": "Lectura al Estilo DELE/SIELE — B1", "items": [
        {"id": "simb1r1", "statement": "La mayor&iacute;a de los trabajadores encuestados dice estar m&aacute;s satisfecha trabajando desde casa.", "answer": True, "explanation": "&laquo;La mayor&iacute;a de los trabajadores se declara m&aacute;s satisfecha.&raquo;"},
        {"id": "simb1r2", "statement": "Nadie mencion&oacute; ninguna desventaja del teletrabajo.", "answer": False, "explanation": "Algunos mencionaron dificultades para separar el trabajo de la vida personal y jornadas m&aacute;s largas."},
    ]}
    b1_grammar_ex = {"id": "sim-b1-grammar", "type": "fill-blank", "title": "Gram&aacute;tica al Estilo DELE/SIELE — B1",
                      "instructions": "Completa cada frase.",
                      "items": [
                          {"id": "simb1g1", "prompt": "De peque&ntilde;o, ___ (yo - jugar) siempre en la calle.", "answers": [["jugaba"]], "explanation": "Acci&oacute;n habitual en el pasado &rarr; imperfecto."},
                          {"id": "simb1g2", "prompt": "Ma&ntilde;ana ___ (nosotros - salir) muy temprano.", "answers": [["saldremos"]], "explanation": "Plan futuro &rarr; futuro simple."},
                          {"id": "simb1g3", "prompt": "&iquest;___ (Poder - usted) ayudarme, por favor? (formal)", "answers": [["Podr&iacute;a"]], "explanation": "Petici&oacute;n formal y cort&eacute;s &rarr; condicional."},
                      ]}

    b2_reading = ("<p>El debate sobre la inteligencia artificial en el mundo laboral sigue dividiendo a los expertos y a la opini&oacute;n p&uacute;blica. Si por un lado se subrayan las ventajas en t&eacute;rminos de eficiencia, por otro crece la preocupaci&oacute;n por la p&eacute;rdida de empleos en algunos sectores. Los economistas coinciden, sin embargo, en que la formaci&oacute;n continua ser&aacute; determinante para afrontar esta transici&oacute;n.</p>")
    b2_reading_ex = {"id": "sim-b2-reading", "type": "multiple-choice", "title": "Lectura al Estilo DELE/SIELE — B2", "items": [
        {"id": "simb2r1", "prompt": "&iquest;En qu&eacute; coinciden los economistas?", "options": ["En que la inteligencia artificial deber&iacute;a prohibirse", "En que la formaci&oacute;n continua ser&aacute; clave", "En que la p&eacute;rdida de empleos est&aacute; exagerada"], "answerIndex": 1, "explanation": "&laquo;La formaci&oacute;n continua ser&aacute; determinante.&raquo;"},
    ]}
    b2_grammar_ex = {"id": "sim-b2-grammar", "type": "fill-blank", "title": "Gram&aacute;tica al Estilo DELE/SIELE — B2",
                      "instructions": "Completa cada frase.",
                      "items": [
                          {"id": "simb2g1", "prompt": "Si ___ (yo - tener) m&aacute;s tiempo, estudiar&iacute;a m&aacute;s.", "answers": [["tuviera"]], "explanation": "Condicional hipot&eacute;tico: si + imperfecto de subjuntivo."},
                          {"id": "simb2g2", "prompt": "Dudo que ellos ___ (llegar) a tiempo.", "answers": [["lleguen"]], "explanation": "Dudar que exige subjuntivo presente."},
                      ]}

    exam_sections = []
    for level, reading, reading_ex, grammar_ex in [("B1", b1_reading, b1_reading_ex, b1_grammar_ex), ("B2", b2_reading, b2_reading_ex, b2_grammar_ex)]:
        exam_sections.append(f"""<section class="section section--surface" aria-labelledby="sim-{level}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level} &middot; Comprensi&oacute;n de Lectura</p>
                <h2 id="sim-{level}-heading">Examen Simulado {level}</h2>
                <div class="card"><div class="prose">{reading}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(reading_ex)}</div>
                <div style="margin-top:var(--space-md);">{ex_block(grammar_ex)}</div>
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
