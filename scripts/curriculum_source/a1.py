# -*- coding: utf-8 -*-
"""A1 — datos del currículo de nivel principiante. Ver curriculum/SCHEMA.md
para la forma exacta del JSON que esto compila (scripts/generate_curriculum.py
hace la compilación). Escrito como Python en vez de JSON a mano para que el
texto en español con comillas, tildes y ñ se lea con naturalidad.

Curso monolingüe: los ejemplos son strings simples en español, sin
traducción al inglés en ningún campo."""

OVERVIEW = (
    "El nivel A1 construye las bases reales del español desde el primer día: "
    "el abecedario y la pronunciación, el género y el número de los "
    "sustantivos, los artículos, los pronombres personales, y el gran "
    "contraste entre ser y estar. También conjugarás el presente de "
    "indicativo, tanto de los verbos regulares como de los irregulares más "
    "frecuentes, y aprenderás a describir personas y cosas con adjetivos, "
    "posesivos y demostrativos. Al final de este nivel podrás presentarte, "
    "describir tu entorno cercano, hacer preguntas simples y expresar tus "
    "gustos — la base sobre la que se construye todo lo demás en este curso."
)

LESSONS = [
    {
        "id": "a1-el-abecedario-y-la-pronunciacion",
        "level": "A1", "unit": "1", "order": 1, "skill": "pronunciation", "strand": "fonetica",
        "title": "El Abecedario y la Pronunciación",
        "subtitle": "Los sonidos del español, la acentuación y la tilde: dónde va y por qué.",
        "objectives": [
            "Nombrar y pronunciar las letras del abecedario español, incluida la ñ",
            "Distinguir los sonidos de letras que cambian según la vocal que sigue (c, g, r)",
            "Explicar la regla de acentuación y decidir cuándo una palabra necesita tilde",
        ],
        "content": {
            "intro": "El español se escribe casi como se pronuncia: una vez que conoces las reglas de sonido y de acentuación, puedes leer en voz alta cualquier palabra nueva con confianza.",
            "explanation": "<p>El abecedario español tiene veintisiete letras, incluida la <strong>ñ</strong>, que no existe en muchos otros idiomas y representa un sonido único (como en <em>año</em> o <em>niño</em>). Cada vocal (a, e, i, o, u) suena siempre igual y con claridad: el español no tiene sonidos vocálicos reducidos ni silenciosos como ocurre en otros idiomas.</p><p>Lo más difícil para un principiante suele ser que la <strong>c</strong>, la <strong>g</strong> y la <strong>r</strong> cambian de sonido según su posición, y que existe una regla clara — pero con excepciones marcadas por la tilde — para saber qué sílaba de una palabra se pronuncia con más fuerza.</p>",
            "rules": [
                {"heading": "a) La c y la g según la vocal siguiente", "body": "<ul><li><strong>ca, co, cu</strong> = sonido fuerte de \"k\" — <em>casa, cosa, cuna</em></li><li><strong>ce, ci</strong> = sonido suave (como \"s\" en Latinoamérica, o \"z\" en España) — <em>cena, cielo</em></li><li><strong>ga, go, gu</strong> = sonido fuerte de \"g\" — <em>gato, gorra, gusto</em></li><li><strong>ge, gi</strong> = sonido gutural, parecido a una \"j\" fuerte — <em>gente, girasol</em></li><li>Para mantener el sonido fuerte antes de e/i se añade una <strong>u</strong> muda: <strong>gue, gui</strong> — <em>guerra, guitarra</em></li></ul>"},
                {"heading": "b) La r simple y la r fuerte", "body": "<ul><li>Una sola <strong>r</strong> entre vocales suena suave — <em>pero, cara</em></li><li><strong>rr</strong> siempre suena fuerte y vibrante — <em>perro, carro</em></li><li>Una sola <strong>r</strong> al inicio de palabra también suena fuerte — <em>rosa, ratón</em></li></ul>"},
                {"heading": "c) Sílaba tónica: la regla general", "body": "<ul><li>Si la palabra termina en <strong>vocal, n o s</strong>, la fuerza cae en la penúltima sílaba — <em>casa, joven, libros</em></li><li>Si la palabra termina en <strong>cualquier otra consonante</strong>, la fuerza cae en la última sílaba — <em>hotel, ciudad, reloj</em></li><li>Toda palabra que no siga esta regla necesita una <strong>tilde</strong> escrita sobre la vocal fuerte, para marcar la excepción</li></ul>"},
                {"heading": "d) Cuándo escribir la tilde", "body": "<ul><li><em>café, sofá</em> — terminan en vocal pero la fuerza cae en la última sílaba: necesitan tilde</li><li><em>árbol, fácil</em> — terminan en consonante distinta de n/s pero la fuerza cae antes de la última sílaba: necesitan tilde</li><li><em>rápido, música</em> — la fuerza cae dos sílabas antes de la última: siempre necesitan tilde</li><li>La tilde también distingue palabras que se escriben igual pero significan cosas distintas — <em>tú</em> (pronombre) frente a <em>tu</em> (posesivo), <em>él</em> frente a <em>el</em></li></ul>"},
            ],
            "examples": [
                "El abecedario español tiene veintisiete letras.",
                "La ñ es una letra propia del español, como en año o mañana.",
                "En cena, la c suena suave; en casa, suena fuerte.",
                "Perro se pronuncia con la r fuerte y vibrante.",
                "Hotel lleva la fuerza en la última sílaba y no necesita tilde.",
                "Café termina en vocal pero la fuerza cae al final, así que necesita tilde.",
                "Música siempre lleva tilde porque la fuerza cae dos sílabas antes del final.",
                "Tú vienes conmigo, pero tu hermano se queda en casa.",
            ],
            "commonMistakes": [
                {"wrong": "Pronunciar \"gente\" con el sonido fuerte de la g", "right": "\"gente\" con el sonido gutural suave de la g antes de e", "why": "Ge/gi siempre tienen el sonido gutural en español, no el sonido fuerte que ocurre antes de a, o, u."},
                {"wrong": "Escribir \"musica\" sin tilde", "right": "música, con tilde en la u", "why": "Cuando la fuerza cae dos sílabas antes del final (esdrújula), la palabra siempre lleva tilde, sin excepción."},
                {"wrong": "Pronunciar la r de \"pero\" igual que la de \"perro\"", "right": "pero con r suave, perro con r fuerte y vibrante", "why": "Una sola r entre vocales es suave; solo rr (o r al inicio de palabra) es la r fuerte — y cambia el significado de la palabra."},
            ],
        },
        "exercises": [
            {"id": "a1ap-mc", "type": "multiple-choice", "title": "¿Qué sonido es?",
             "items": [
                {"id": "a1ap1", "prompt": "¿Cómo suena la c en la palabra \"cielo\"?", "options": ["Sonido fuerte, como en casa", "Sonido suave", "No se pronuncia"], "answerIndex": 1, "explanation": "Ce/ci siempre tienen el sonido suave en español, nunca el sonido fuerte de ca/co/cu."},
                {"id": "a1ap2", "prompt": "¿Qué palabra tiene el sonido fuerte de la g?", "options": ["gente", "gorra", "girasol"], "answerIndex": 1, "explanation": "Ga/go/gu tienen el sonido fuerte; ge/gi tienen el sonido gutural suave — gorra es ga/go/gu."},
                {"id": "a1ap3", "prompt": "¿Cuál de estas palabras necesita tilde por terminar en vocal con la fuerza en la última sílaba?", "options": ["casa", "café", "libro"], "answerIndex": 1, "explanation": "Café termina en vocal, pero la fuerza cae en la última sílaba — una excepción a la regla general, por eso lleva tilde."},
                {"id": "a1ap4", "prompt": "¿Qué palabra tiene la r fuerte y vibrante?", "options": ["pero", "cara", "carro"], "answerIndex": 2, "explanation": "Carro tiene rr, que siempre suena fuerte; pero y cara tienen una sola r entre vocales, sonido suave."},
             ]},
            {"id": "a1ap-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "a1ap5", "statement": "La ñ es una letra propia del abecedario español.", "answer": True, "explanation": "La ñ existe en español y representa un sonido único, distinto de la n simple."},
                {"id": "a1ap6", "statement": "Todas las palabras que terminan en consonante llevan tilde.", "answer": False, "explanation": "Solo llevan tilde las palabras que no siguen la regla general de acentuación, sin importar si terminan en vocal o consonante."},
                {"id": "a1ap7", "statement": "La palabra \"árbol\" necesita tilde porque termina en una consonante distinta de n o s pero la fuerza cae en la primera sílaba.", "answer": True, "explanation": "Árbol termina en l; según la regla general, la fuerza debería caer en la última sílaba, pero cae en la primera, así que necesita tilde."},
             ]},
            {"id": "a1ap-fill", "type": "fill-blank", "title": "Completa con Tilde o Sin Tilde",
             "instructions": "Elige la forma correcta de cada palabra.",
             "items": [
                {"id": "a1ap8", "prompt": "La palabra que significa \"lugar donde se duerme de viaje\" se escribe ___.", "answers": [["hotel"]], "explanation": "Hotel termina en consonante distinta de n/s con la fuerza en la última sílaba: sigue la regla general, sin tilde.", "options": ["hotel", "hótel"]},
                {"id": "a1ap9", "prompt": "La palabra que significa \"melodía\" se escribe ___.", "answers": [["música"]], "explanation": "Música es esdrújula (la fuerza cae dos sílabas antes del final) y siempre lleva tilde.", "options": ["musica", "música"]},
             ]},
        ],
        "summary": [
            "El abecedario español tiene veintisiete letras, incluida la ñ, y cada vocal suena siempre igual y con claridad.",
            "C, g y r cambian de sonido según la letra siguiente: ce/ci son suaves, ge/gi son guturales, y solo rr (o r inicial) es fuerte.",
            "La regla general de acentuación depende de la última letra de la palabra; toda excepción se marca con tilde escrita.",
        ],
    },
    {
        "id": "a1-genero-y-numero-de-los-sustantivos",
        "level": "A1", "unit": "1", "order": 2, "skill": "grammar", "strand": "sustantivos",
        "title": "Género y Número de los Sustantivos",
        "subtitle": "Todo sustantivo en español es masculino o femenino, y tiene forma singular y plural.",
        "objectives": [
            "Identificar el género de un sustantivo a partir de su terminación",
            "Reconocer las excepciones más comunes al patrón general de género",
            "Formar el plural de un sustantivo según su terminación",
        ],
        "content": {
            "intro": "En español, cada sustantivo — incluso los que nombran objetos sin género natural, como una mesa o un libro — es gramaticalmente masculino o femenino, y esa característica afecta a todas las palabras que lo acompañan.",
            "explanation": "<p>La mayoría de los sustantivos que terminan en <strong>-o</strong> son masculinos (<em>el libro</em>) y la mayoría de los que terminan en <strong>-a</strong> son femeninos (<em>la mesa</em>). Sin embargo, existen muchas excepciones frecuentes que hay que memorizar, como <em>la mano</em> (femenino, termina en -o) o <em>el día</em> (masculino, termina en -a). Los sustantivos que terminan en otras letras no siguen un patrón fijo y su género se aprende junto con la palabra.</p><p>El plural también sigue reglas según la terminación: se añade <strong>-s</strong> si el sustantivo termina en vocal, y <strong>-es</strong> si termina en consonante.</p>",
            "rules": [
                {"heading": "a) Terminaciones típicas de género", "body": "<ul><li><strong>-o</strong> suele ser masculino — <em>el libro, el gato, el niño</em></li><li><strong>-a</strong> suele ser femenino — <em>la mesa, la casa, la niña</em></li><li><strong>-dad, -ción, -sión, -tud</strong> son casi siempre femeninos — <em>la ciudad, la canción, la actitud</em></li><li><strong>-ma</strong> de origen griego suele ser masculino, aunque termina en -a — <em>el problema, el sistema, el idioma</em></li></ul>"},
                {"heading": "b) Excepciones comunes", "body": "<ul><li><em>la mano</em>, <em>la moto</em>, <em>la foto</em> — femeninas aunque terminan en -o</li><li><em>el día</em>, <em>el mapa</em>, <em>el planeta</em> — masculinos aunque terminan en -a</li><li>Algunos sustantivos cambian de significado según el género — <em>el capital</em> (dinero) frente a <em>la capital</em> (ciudad principal)</li></ul>"},
                {"heading": "c) Formación del plural", "body": "<ul><li>Terminación en vocal → se añade <strong>-s</strong>: <em>libro → libros, casa → casas</em></li><li>Terminación en consonante → se añade <strong>-es</strong>: <em>ciudad → ciudades, flor → flores</em></li><li>Terminación en <strong>-z</strong> → cambia a <strong>-ces</strong>: <em>lápiz → lápices, vez → veces</em></li></ul>"},
            ],
            "examples": [
                "El libro está sobre la mesa.",
                "La mano derecha me duele un poco.",
                "El día de hoy es muy soleado.",
                "Los estudiantes llevan sus libros a clase.",
                "Las ciudades grandes tienen muchos problemas de tráfico.",
                "El sistema no funciona bien esta mañana.",
                "Compré dos lápices nuevos para la escuela.",
                "Las flores del jardín huelen muy bien.",
            ],
            "commonMistakes": [
                {"wrong": "la día", "right": "el día", "why": "Día es una excepción: termina en -a pero es masculino, uno de los casos que hay que memorizar aparte."},
                {"wrong": "el mano", "right": "la mano", "why": "Mano termina en -o pero es femenino, la excepción más conocida de este patrón."},
                {"wrong": "los lápizes", "right": "los lápices", "why": "Los sustantivos terminados en -z cambian la z por c antes de añadir -es en el plural."},
            ],
        },
        "exercises": [
            {"id": "a1gn-mc", "type": "multiple-choice", "title": "¿Masculino o Femenino?",
             "items": [
                {"id": "a1gn1", "prompt": "¿Qué artículo corresponde a \"mano\"?", "options": ["el", "la"], "answerIndex": 1, "explanation": "Mano es femenina, aunque termina en -o: una excepción muy común."},
                {"id": "a1gn2", "prompt": "¿Qué artículo corresponde a \"día\"?", "options": ["el", "la"], "answerIndex": 0, "explanation": "Día es masculino, aunque termina en -a: otra excepción frecuente."},
                {"id": "a1gn3", "prompt": "¿Qué artículo corresponde a \"ciudad\"?", "options": ["el", "la"], "answerIndex": 1, "explanation": "Las palabras terminadas en -dad son casi siempre femeninas."},
                {"id": "a1gn4", "prompt": "¿Qué artículo corresponde a \"problema\"?", "options": ["el", "la"], "answerIndex": 0, "explanation": "Problema termina en -a pero es masculino: viene del griego, como sistema e idioma."},
             ]},
            {"id": "a1gn-fill", "type": "fill-blank", "title": "Forma el Plural",
             "items": [
                {"id": "a1gn5", "prompt": "libro → ___", "answers": [["libros"]], "explanation": "Terminación en vocal: se añade -s."},
                {"id": "a1gn6", "prompt": "flor → ___", "answers": [["flores"]], "explanation": "Terminación en consonante: se añade -es."},
                {"id": "a1gn7", "prompt": "lápiz → ___", "answers": [["lápices"]], "explanation": "Terminación en -z: la z cambia a c antes de -es."},
                {"id": "a1gn8", "prompt": "ciudad → ___", "answers": [["ciudades"]], "explanation": "Terminación en consonante: se añade -es."},
             ]},
            {"id": "a1gn-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1gn9", "incorrect": "El mano está sucia.", "answer": ["La mano está sucia."], "explanation": "Mano es femenina aunque termine en -o."},
                {"id": "a1gn10", "incorrect": "La día es muy larga.", "answer": ["El día es muy largo."], "explanation": "Día es masculino aunque termine en -a; el adjetivo también debe concordar en masculino."},
             ]},
        ],
        "summary": [
            "La mayoría de los sustantivos en -o son masculinos y en -a son femeninos, pero hay excepciones comunes que se memorizan aparte.",
            "Las terminaciones -dad, -ción, -sión y -tud son casi siempre femeninas; -ma de origen griego suele ser masculino.",
            "El plural se forma con -s tras vocal, -es tras consonante, y -z cambia a -ces.",
        ],
    },
    {
        "id": "a1-articulos-definidos-e-indefinidos",
        "level": "A1", "unit": "1", "order": 3, "skill": "grammar", "strand": "articulos",
        "title": "Artículos Definidos e Indefinidos",
        "subtitle": "El, la, los, las frente a un, una, unos, unas: cómo elegir el artículo correcto.",
        "objectives": [
            "Elegir el artículo definido correcto (el, la, los, las) según género y número",
            "Elegir el artículo indefinido correcto (un, una, unos, unas) según género y número",
            "Distinguir cuándo se usa un artículo definido y cuándo uno indefinido",
        ],
        "content": {
            "intro": "El artículo siempre acompaña al sustantivo y debe concordar con él en género y número — es una de las primeras concordancias que hay que automatizar en español.",
            "explanation": "<p>Los artículos <strong>definidos</strong> (<em>el, la, los, las</em>) se usan para hablar de algo específico o ya conocido por el hablante y el oyente: <em>el libro que compré ayer</em>. Los artículos <strong>indefinidos</strong> (<em>un, una, unos, unas</em>) se usan para presentar algo por primera vez o no específico: <em>compré un libro</em>.</p><p>Hay un caso especial: los sustantivos femeninos singulares que empiezan con <strong>a</strong> o <strong>ha</strong> tónica (con fuerza) usan <em>el</em> y <em>un</em> en lugar de <em>la</em> y <em>una</em>, solo por razones de sonido — el sustantivo sigue siendo femenino, y el plural vuelve a usar <em>las</em>/<em>unas</em>.</p>",
            "rules": [
                {"heading": "a) Artículos definidos", "body": "<ul><li><strong>el</strong> — masculino singular: <em>el perro</em></li><li><strong>la</strong> — femenino singular: <em>la casa</em></li><li><strong>los</strong> — masculino plural: <em>los perros</em></li><li><strong>las</strong> — femenino plural: <em>las casas</em></li></ul>"},
                {"heading": "b) Artículos indefinidos", "body": "<ul><li><strong>un</strong> — masculino singular: <em>un perro</em></li><li><strong>una</strong> — femenino singular: <em>una casa</em></li><li><strong>unos</strong> — masculino plural: <em>unos perros</em></li><li><strong>unas</strong> — femenino plural: <em>unas casas</em></li></ul>"},
                {"heading": "c) El caso especial de a/ha tónica", "body": "<ul><li><em>el agua</em> (no <em>la agua</em>), pero <em>las aguas</em> en plural — agua sigue siendo femenina</li><li><em>un águila</em> (no <em>una águila</em>), pero <em>unas águilas</em> en plural</li><li>Solo ocurre cuando la a inicial lleva la fuerza de la palabra: <em>la amiga</em> es normal porque la fuerza no está en la primera sílaba</li></ul>"},
                {"heading": "d) Definido o indefinido", "body": "<ul><li>Definido: algo ya conocido o específico — <em>Cierra la puerta.</em> (la puerta de esta habitación)</li><li>Indefinido: algo nuevo o no específico — <em>Hay una puerta al fondo.</em> (una puerta cualquiera)</li></ul>"},
            ],
            "examples": [
                "El profesor llega temprano todos los días.",
                "Necesito un lápiz para escribir la tarea.",
                "Las ventanas de la casa están abiertas.",
                "Compré unas manzanas en el mercado.",
                "El agua de este río está muy fría.",
                "Vi un águila volando sobre las montañas.",
                "La amiga de mi hermana vive en otra ciudad.",
                "Los estudiantes tienen unos libros nuevos.",
            ],
            "commonMistakes": [
                {"wrong": "la agua", "right": "el agua", "why": "Agua es femenina, pero empieza con a tónica, así que en singular usa el por razones de sonido; el plural vuelve a ser las aguas."},
                {"wrong": "una águila", "right": "un águila", "why": "Águila empieza con a tónica: en singular se usa un aunque la palabra sea femenina."},
                {"wrong": "unos manzanas", "right": "unas manzanas", "why": "Manzanas es femenino plural, así que el artículo indefinido debe ser unas, no unos."},
            ],
        },
        "exercises": [
            {"id": "a1ad-fill", "type": "fill-blank", "title": "Completa con el Artículo Definido",
             "instructions": "Usa el, la, los o las.",
             "items": [
                {"id": "a1ad1", "prompt": "___ libro está sobre la mesa.", "answers": [["El"]], "explanation": "Libro es masculino singular.", "options": ["El", "La", "Los"]},
                {"id": "a1ad2", "prompt": "___ casas del barrio son antiguas.", "answers": [["Las"]], "explanation": "Casas es femenino plural.", "options": ["Los", "Las", "La"]},
                {"id": "a1ad3", "prompt": "___ agua está muy fría hoy.", "answers": [["El"]], "explanation": "Agua es femenina, pero por empezar con a tónica usa el en singular.", "options": ["El", "La", "Los"]},
             ]},
            {"id": "a1ad-mc", "type": "multiple-choice", "title": "Elige el Artículo Indefinido",
             "items": [
                {"id": "a1ad4", "prompt": "Necesito ___ silla para la cocina.", "options": ["un", "una", "unos"], "answerIndex": 1, "explanation": "Silla es femenino singular."},
                {"id": "a1ad5", "prompt": "Vi ___ águila enorme en el cielo.", "options": ["un", "una", "unas"], "answerIndex": 0, "explanation": "Águila es femenina, pero empieza con a tónica, así que en singular se usa un."},
                {"id": "a1ad6", "prompt": "Tengo ___ amigos en esa ciudad.", "options": ["un", "unos", "unas"], "answerIndex": 1, "explanation": "Amigos es masculino plural."},
             ]},
            {"id": "a1ad-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1ad7", "incorrect": "La agua está fría.", "answer": ["El agua está fría."], "explanation": "Agua empieza con a tónica, así que usa el en singular aunque sea femenina."},
                {"id": "a1ad8", "incorrect": "Compré unos naranjas.", "answer": ["Compré unas naranjas."], "explanation": "Naranjas es femenino plural, así que el artículo debe ser unas."},
             ]},
        ],
        "summary": [
            "El artículo definido (el, la, los, las) marca algo específico o conocido; el indefinido (un, una, unos, unas) presenta algo nuevo.",
            "El artículo siempre concuerda en género y número con el sustantivo que acompaña.",
            "Los sustantivos femeninos que empiezan con a o ha tónica usan el/un en singular por sonido, pero siguen siendo femeninos.",
        ],
    },
    {
        "id": "a1-ser-y-estar-introduccion",
        "level": "A1", "unit": "1", "order": 4, "skill": "grammar", "strand": "verbos",
        "title": "Ser y Estar (Introducción)",
        "subtitle": "Dos verbos que significan \"ser/estar\": identidad y características frente a ubicación y estado temporal.",
        "objectives": [
            "Conjugar ser y estar en presente de indicativo",
            "Usar ser para identidad, origen y características permanentes",
            "Usar estar para ubicación y estados temporales",
        ],
        "content": {
            "intro": "Ser y estar son dos verbos distintos que en muchos otros idiomas se traducen con una sola palabra — aprender a distinguirlos es uno de los primeros grandes retos del español, y vale la pena dominarlo bien desde el principio.",
            "explanation": "<p>Ambos verbos son irregulares y hay que memorizar sus formas. La diferencia central: <strong>ser</strong> describe lo que algo o alguien <em>es</em> de manera esencial — su identidad, origen, profesión o características que no cambian fácilmente. <strong>Estar</strong> describe <em>dónde</em> está algo o alguien, o en qué <em>estado o condición temporal</em> se encuentra en este momento.</p><p>Una forma sencilla de recordarlo: si la característica define a la persona o cosa de manera duradera, usa <em>ser</em>; si describe un lugar o una condición que puede cambiar, usa <em>estar</em>. Con el tiempo aprenderás casos más sutiles, pero esta distinción cubre la mayoría de las situaciones del día a día.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Ser y estar — presente de indicativo</caption><thead><tr><th>Sujeto</th><th>ser</th><th>estar</th></tr></thead><tbody><tr><td>yo</td><td>soy</td><td>estoy</td></tr><tr><td>tú</td><td>eres</td><td>estás</td></tr><tr><td>él / ella / usted</td><td>es</td><td>está</td></tr><tr><td>nosotros/as</td><td>somos</td><td>estamos</td></tr><tr><td>vosotros/as</td><td>sois</td><td>estáis</td></tr><tr><td>ellos/as / ustedes</td><td>son</td><td>están</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Usos de ser", "body": "<ul><li>Identidad: <em>Soy Ana.</em></li><li>Origen y nacionalidad: <em>Somos de Colombia.</em></li><li>Profesión: <em>Es profesor.</em></li><li>Características permanentes: <em>La casa es grande.</em></li><li>Hora y fecha: <em>Son las tres. Hoy es lunes.</em></li></ul>"},
                {"heading": "b) Usos de estar", "body": "<ul><li>Ubicación: <em>El libro está en la mesa.</em></li><li>Estado emocional o físico temporal: <em>Estoy cansado.</em></li><li>Resultado de un cambio: <em>La puerta está abierta.</em></li><li>Acciones en progreso (con gerundio, se verá más adelante): <em>Estoy comiendo.</em></li></ul>"},
                {"heading": "c) Un mismo adjetivo, dos significados", "body": "<ul><li><em>Ella es aburrida.</em> — característica permanente (es una persona aburrida)</li><li><em>Ella está aburrida.</em> — estado temporal (en este momento se aburre)</li><li><em>Él es listo.</em> — es inteligente</li><li><em>Él está listo.</em> — está preparado en este momento</li></ul>"},
            ],
            "examples": [
                "Soy estudiante de español desde hace dos meses.",
                "Mis padres son de Argentina.",
                "El café está muy caliente todavía.",
                "Nosotros estamos en la biblioteca esta tarde.",
                "Mi hermana es muy inteligente y trabajadora.",
                "La ventana está rota desde ayer.",
                "Hoy es martes y son las nueve de la mañana.",
                "Estoy un poco nervioso antes del examen.",
            ],
            "commonMistakes": [
                {"wrong": "Estoy profesor.", "right": "Soy profesor.", "why": "La profesión describe una identidad, no un estado temporal, así que se usa ser."},
                {"wrong": "El libro es en la mesa.", "right": "El libro está en la mesa.", "why": "La ubicación siempre usa estar, nunca ser."},
                {"wrong": "Ella es cansada.", "right": "Ella está cansada.", "why": "El cansancio es un estado temporal que cambia, así que necesita estar; ser cambiaría el significado a \"es una persona molesta o pesada\"."},
            ],
        },
        "exercises": [
            {"id": "a1se-fill", "type": "fill-blank", "title": "Completa con Ser o Estar",
             "instructions": "Conjuga el verbo entre paréntesis en presente.",
             "items": [
                {"id": "a1se1", "prompt": "Yo ___ (ser) de México.", "answers": [["soy"]], "explanation": "Origen: se usa ser.", "options": ["soy", "estoy", "es"]},
                {"id": "a1se2", "prompt": "Tú ___ (estar) muy cansado hoy.", "answers": [["estás"]], "explanation": "Estado temporal: se usa estar.", "options": ["estás", "eres", "está"]},
                {"id": "a1se3", "prompt": "Nosotros ___ (estar) en el parque.", "answers": [["estamos"]], "explanation": "Ubicación: se usa estar.", "options": ["estamos", "somos", "están"]},
                {"id": "a1se4", "prompt": "Ella ___ (ser) muy simpática.", "answers": [["es"]], "explanation": "Característica permanente: se usa ser.", "options": ["es", "está", "son"]},
             ]},
            {"id": "a1se-mc", "type": "multiple-choice", "title": "Elige el Verbo Correcto",
             "items": [
                {"id": "a1se5", "prompt": "¿Cómo se dice \"la puerta está abierta\"?", "options": ["La puerta es abierta.", "La puerta está abierta.", "La puerta estás abierta."], "answerIndex": 1, "explanation": "El resultado de un cambio de estado usa estar."},
                {"id": "a1se6", "prompt": "¿Cómo se pregunta la hora?", "options": ["¿Qué hora estás?", "¿Qué hora son?", "¿Qué hora es?"], "answerIndex": 2, "explanation": "La hora siempre se expresa con ser: Es la una / Son las dos."},
             ]},
            {"id": "a1se-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1se7", "incorrect": "Yo estoy médico.", "answer": ["Yo soy médico."], "explanation": "La profesión describe identidad, no un estado temporal, así que se usa ser."},
                {"id": "a1se8", "incorrect": "El restaurante son cerca de aquí.", "answer": ["El restaurante está cerca de aquí."], "explanation": "La ubicación siempre usa estar, y además el sujeto es singular, así que el verbo debe ser está."},
             ]},
        ],
        "summary": [
            "Ser expresa identidad, origen, profesión y características permanentes; estar expresa ubicación y estados temporales.",
            "Ambos verbos son irregulares en presente: soy/eres/es/somos/sois/son y estoy/estás/está/estamos/estáis/están.",
            "Algunos adjetivos cambian de significado según el verbo: ser aburrido (persona aburrida) frente a estar aburrido (sentirse aburrido ahora).",
        ],
    },
    {
        "id": "a1-pronombres-personales-de-sujeto",
        "level": "A1", "unit": "1", "order": 5, "skill": "grammar", "strand": "pronombres",
        "title": "Pronombres Personales de Sujeto",
        "subtitle": "Yo, tú, él/ella/usted, nosotros, vosotros/ustedes, ellos/ellas — y cuándo se omiten.",
        "objectives": [
            "Enumerar los pronombres personales de sujeto en español",
            "Explicar por qué el español suele omitir el pronombre de sujeto",
            "Distinguir el uso formal (usted) del informal (tú) y reconocer el voseo",
        ],
        "content": {
            "intro": "Las terminaciones verbales del español ya indican quién hace la acción, así que los pronombres de sujeto suelen omitirse — lo contrario de lo que ocurre en otros idiomas, donde la frase siempre necesita un sujeto explícito.",
            "explanation": "<p>Como cada terminación verbal corresponde a un sujeto concreto (<em>hablo</em> solo puede significar \"yo hablo\"), el español es una lengua que permite omitir el sujeto: <em>Hablo español</em> es una frase completa y natural, y añadir <em>yo</em> es gramaticalmente correcto pero normalmente innecesario. El pronombre reaparece sobre todo para dar énfasis, marcar un contraste, o evitar ambigüedad (por ejemplo, cuando la forma de él/ella/usted podría referirse a varias personas según el contexto).</p><p>En algunos países de América Latina, especialmente en Argentina y Uruguay, se usa <strong>vos</strong> en lugar de <em>tú</em> para la segunda persona informal, con formas verbales propias (<em>vos hablás</em> en vez de <em>tú hablas</em>). En este curso usamos principalmente <em>tú</em>, pero es útil reconocer <em>vos</em> cuando lo encuentres.</p>",
            "rules": [
                {"heading": "a) Los pronombres personales de sujeto", "body": "<ul><li><strong>yo</strong> — primera persona singular</li><li><strong>tú</strong> — segunda persona singular, informal (y <strong>vos</strong>, forma equivalente en algunos países)</li><li><strong>él / ella</strong> — tercera persona singular; <strong>usted</strong> — segunda persona singular, formal</li><li><strong>nosotros / nosotras</strong> — primera persona plural</li><li><strong>vosotros / vosotras</strong> — segunda persona plural, informal (usado en España)</li><li><strong>ellos / ellas</strong> — tercera persona plural; <strong>ustedes</strong> — segunda persona plural (formal en España, general en América Latina)</li></ul>"},
                {"heading": "b) Cuándo mantener el pronombre", "body": "<ul><li>Contraste: <em>Yo estudio, tú miras la televisión.</em></li><li>Énfasis: <em>¡Yo lo digo!</em></li><li>Claridad, cuando el contexto no basta: <em>Él vive en Madrid.</em> (para distinguir de ella)</li></ul>"},
                {"heading": "c) Tú, usted y ustedes", "body": "<ul><li><strong>Tú</strong>: amigos, familia, niños, compañeros — <em>¿Tú cómo estás?</em></li><li><strong>Usted</strong>: desconocidos, personas mayores, contextos formales — <em>¿Usted cómo está?</em></li><li>En América Latina, <strong>ustedes</strong> se usa para el plural tanto formal como informal; en España, <strong>vosotros</strong> se reserva para el plural informal y <strong>ustedes</strong> para el formal</li></ul>"},
            ],
            "examples": [
                "Hablo español e inglés todos los días.",
                "Tú estudias mucho, yo trabajo por las tardes.",
                "Ella vive en Bogotá desde hace un año.",
                "¿Ustedes vienen a la fiesta el sábado?",
                "Ellos no entienden bien esta lección todavía.",
                "Nosotros preferimos quedarnos en casa hoy.",
                "Vos hablás muy bien español, según me dicen.",
                "Usted es muy amable, muchas gracias.",
            ],
            "commonMistakes": [
                {"wrong": "Yo soy yo cansado.", "right": "Estoy cansado.", "why": "El español nunca necesita un pronombre de sujeto explícito para que la frase sea gramatical; aquí es redundante, no obligatorio."},
                {"wrong": "usar tú con un desconocido mayor en un contexto formal", "right": "usar usted con un desconocido mayor en un contexto formal", "why": "Usted es la opción segura y respetuosa cuando no se conoce bien a la persona o hay una diferencia de edad o jerarquía."},
                {"wrong": "Tú hablás español muy bien. (mezclando tú con la forma verbal de vos)", "right": "Tú hablas español muy bien. / Vos hablás español muy bien.", "why": "Tú y vos tienen formas verbales distintas; no se combinan el pronombre de uno con la conjugación del otro."},
            ],
        },
        "exercises": [
            {"id": "a1pp-mc", "type": "multiple-choice", "title": "¿Qué Pronombre Es?",
             "items": [
                {"id": "a1pp1", "prompt": "¿Qué pronombre significa \"ellos\" en femenino?", "options": ["ellos", "ellas", "ustedes"], "answerIndex": 1, "explanation": "Ellas es la tercera persona plural femenina."},
                {"id": "a1pp2", "prompt": "\"Hablo español\" no necesita ningún pronombre porque...", "options": ["la terminación -o ya indica que es yo", "el verbo está mal conjugado", "falta el artículo"], "answerIndex": 0, "explanation": "La terminación verbal -o corresponde únicamente a yo, así que el pronombre es opcional."},
                {"id": "a1pp3", "prompt": "Con un desconocido mayor en un contexto formal, ¿qué pronombre usas?", "options": ["tú", "usted", "vos"], "answerIndex": 1, "explanation": "Usted es la opción formal y respetuosa con desconocidos y personas mayores."},
             ]},
            {"id": "a1pp-fill", "type": "fill-blank", "title": "Añade el Pronombre Solo Cuando Haga Falta",
             "instructions": "Completa cada frase con el pronombre necesario para dar contraste o claridad.",
             "items": [
                {"id": "a1pp4", "prompt": "___ estudio, tú miras la televisión. (contraste entre \"yo\" y \"tú\")", "answers": [["Yo"]], "explanation": "Se mantiene para marcar el contraste entre dos sujetos distintos en la misma frase.", "options": ["Yo", "Tú", "(nada)"]},
             ]},
            {"id": "a1pp-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "a1pp5", "statement": "En España, vosotros es la forma informal del plural de tú.", "answer": True, "explanation": "En España, vosotros/vosotras se usa para el plural informal, mientras que ustedes se reserva para el formal."},
                {"id": "a1pp6", "statement": "En la mayoría de América Latina, ustedes se usa tanto en contextos formales como informales.", "answer": True, "explanation": "A diferencia de España, gran parte de América Latina no usa vosotros y emplea ustedes para todo el plural."},
             ]},
        ],
        "summary": [
            "Los pronombres de sujeto son yo, tú/vos, él/ella/usted, nosotros/as, vosotros/as, ellos/ellas/ustedes.",
            "Las terminaciones verbales ya identifican al sujeto, así que el pronombre suele omitirse en español.",
            "Usa tú con confianza y usted en contextos formales; vosotros se usa en España y ustedes en el resto del mundo hispanohablante para el plural.",
        ],
    },
    {
        "id": "a1-presente-verbos-regulares",
        "level": "A1", "unit": "1", "order": 6, "skill": "grammar", "strand": "verbos",
        "title": "Presente — Verbos Regulares",
        "subtitle": "La conjugación completa de los verbos terminados en -ar, -er e -ir.",
        "objectives": [
            "Conjugar verbos regulares terminados en -ar, -er e -ir en presente de indicativo",
            "Identificar las terminaciones propias de cada una de las tres conjugaciones",
            "Usar el presente para hablar de hábitos, hechos generales y planes cercanos",
        ],
        "content": {
            "intro": "Todo verbo español pertenece a una de tres familias, según su terminación en infinitivo: -ar, -er, -ir. Aprende el patrón de un verbo regular en cada familia y podrás conjugar cientos de verbos más de la misma manera.",
            "explanation": "<p>Para conjugar un verbo regular, se quita la terminación del infinitivo (-ar, -er, -ir) y se añade la terminación correspondiente a cada sujeto. Las tres conjugaciones comparten mucho, pero tienen diferencias claras, sobre todo en las formas de <em>vosotros</em> y en algunas vocales.</p><p>El presente de indicativo cubre en español lo que otras lenguas separan en dos tiempos distintos: <em>Hablo español</em> puede significar tanto \"hablo español (en general)\" como, en este momento, \"estoy hablando español\". También se usa con frecuencia para planes cercanos en el futuro: <em>Mañana viajo a Lima.</em></p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Presente de indicativo — hablar, comer, vivir</caption><thead><tr><th>Sujeto</th><th>hablar</th><th>comer</th><th>vivir</th></tr></thead><tbody><tr><td>yo</td><td>hablo</td><td>como</td><td>vivo</td></tr><tr><td>tú</td><td>hablas</td><td>comes</td><td>vives</td></tr><tr><td>él/ella/usted</td><td>habla</td><td>come</td><td>vive</td></tr><tr><td>nosotros/as</td><td>hablamos</td><td>comemos</td><td>vivimos</td></tr><tr><td>vosotros/as</td><td>habláis</td><td>coméis</td><td>vivís</td></tr><tr><td>ellos/as/ustedes</td><td>hablan</td><td>comen</td><td>viven</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Verbos en -ar (hablar, trabajar, estudiar)", "body": "<p>Terminaciones: -o, -as, -a, -amos, -áis, -an</p>"},
                {"heading": "b) Verbos en -er (comer, leer, aprender)", "body": "<p>Terminaciones: -o, -es, -e, -emos, -éis, -en</p>"},
                {"heading": "c) Verbos en -ir (vivir, escribir, abrir)", "body": "<p>Terminaciones: -o, -es, -e, -imos, -ís, -en</p>"},
                {"heading": "d) -er y -ir se parecen mucho", "body": "<p>Las terminaciones de -er e -ir solo se diferencian en nosotros (-emos / -imos) y vosotros (-éis / -ís); el resto de las formas son idénticas.</p>"},
            ],
            "examples": [
                "Trabajo en una oficina cerca de mi casa.",
                "Tú comes demasiado rápido siempre.",
                "Ella vive en un apartamento pequeño.",
                "Nosotros estudiamos español todos los martes.",
                "Vosotros habláis muy bien italiano también.",
                "Ellos escriben cartas a sus abuelos.",
                "Mañana viajamos a la playa con toda la familia.",
                "¿Aprendes rápido cuando practicas todos los días?",
            ],
            "commonMistakes": [
                {"wrong": "Nosotros habla mucho.", "right": "Nosotros hablamos mucho.", "why": "Nosotros siempre usa la terminación -amos/-emos/-imos, nunca la forma de él/ella."},
                {"wrong": "Yo vivo en Madrid desde tres años.", "right": "Yo vivo en Madrid desde hace tres años.", "why": "Para expresar duración desde el pasado hasta ahora, el español usa desde hace, no solo desde."},
                {"wrong": "Ellos comen y bebe agua.", "right": "Ellos comen y beben agua.", "why": "Los dos verbos deben concordar con el mismo sujeto plural: comen y beben, no beben con singular."},
            ],
        },
        "exercises": [
            {"id": "a1pv-fill", "type": "fill-blank", "title": "Conjuga el Verbo",
             "instructions": "Completa cada frase con la forma correcta del verbo entre paréntesis.",
             "items": [
                {"id": "a1pv1", "prompt": "Yo ___ (trabajar) en un hospital.", "answers": [["trabajo"]], "explanation": "Yo + verbo en -ar = terminación -o.", "options": ["trabajo", "trabajas", "trabaja"]},
                {"id": "a1pv2", "prompt": "Tú ___ (comer) muy poco por la mañana.", "answers": [["comes"]], "explanation": "Tú + verbo en -er = terminación -es.", "options": ["comes", "come", "como"]},
                {"id": "a1pv3", "prompt": "Nosotros ___ (vivir) cerca del centro.", "answers": [["vivimos"]], "explanation": "Nosotros + verbo en -ir = terminación -imos.", "options": ["vivimos", "viven", "vivís"]},
                {"id": "a1pv4", "prompt": "Ellos ___ (escribir) correos todos los días.", "answers": [["escriben"]], "explanation": "Ellos + verbo en -ir = terminación -en.", "options": ["escriben", "escribimos", "escribe"]},
             ]},
            {"id": "a1pv-mc", "type": "multiple-choice", "title": "Elige la Conjugación Correcta",
             "items": [
                {"id": "a1pv5", "prompt": "¿Cuál es la forma correcta de \"leer\" para \"ella\"?", "options": ["lee", "lees", "leo"], "answerIndex": 0, "explanation": "Él/ella/usted + verbo en -er = terminación -e."},
                {"id": "a1pv6", "prompt": "\"Vosotros ___ español.\" (hablar)", "options": ["hablan", "habláis", "hablamos"], "answerIndex": 1, "explanation": "Vosotros + verbo en -ar = terminación -áis."},
             ]},
            {"id": "a1pv-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1pv7", "incorrect": "Nosotros habla español.", "answer": ["Nosotros hablamos español."], "explanation": "Nosotros siempre usa -amos con verbos en -ar, no la forma de él/ella."},
                {"id": "a1pv8", "incorrect": "Yo vives en Perú.", "answer": ["Yo vivo en Perú."], "explanation": "Yo + verbo en -ir = terminación -o, no la forma de tú."},
             ]},
        ],
        "summary": [
            "Tres conjugaciones regulares: -ar (-o,-as,-a,-amos,-áis,-an), -er (-o,-es,-e,-emos,-éis,-en), -ir (-o,-es,-e,-imos,-ís,-en).",
            "Las terminaciones de -er e -ir solo difieren en nosotros y vosotros; el resto de formas coinciden.",
            "El presente cubre hábitos, hechos generales, acciones en curso y planes cercanos en el futuro.",
        ],
    },
    {
        "id": "a1-presente-verbos-irregulares-comunes",
        "level": "A1", "unit": "1", "order": 7, "skill": "grammar", "strand": "verbos",
        "title": "Presente — Irregulares Comunes",
        "subtitle": "Ir, tener, hacer, venir y otros verbos irregulares de uso muy frecuente.",
        "objectives": [
            "Conjugar ir, tener, hacer y venir en presente de indicativo",
            "Reconocer el patrón de cambio de raíz en la primera persona (yo)",
            "Usar estos verbos irregulares en frases cotidianas simples",
        ],
        "content": {
            "intro": "Algunos de los verbos más útiles del español son irregulares — se usan tanto que conviene memorizarlos temprano, aunque no sigan el patrón regular de -ar/-er/-ir.",
            "explanation": "<p>Los verbos irregulares de uso más frecuente en español no siguen las terminaciones regulares en todas sus formas, pero muchos comparten un patrón útil: la forma de <strong>yo</strong> cambia de manera especial (<em>tengo, hago, vengo</em>), mientras que el resto de las formas suele parecerse más al patrón regular. <strong>Ir</strong> es completamente irregular y hay que memorizarlo entero.</p><p>Estos verbos aparecen en frases de todos los días — <em>tener</em> para posesión y edad, <em>hacer</em> para actividades y clima, <em>ir</em> para movimiento y planes, <em>venir</em> para indicar que alguien se acerca — así que vale la pena practicarlos con frecuencia.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Presente — ir, tener, hacer, venir</caption><thead><tr><th>Sujeto</th><th>ir</th><th>tener</th><th>hacer</th><th>venir</th></tr></thead><tbody><tr><td>yo</td><td>voy</td><td>tengo</td><td>hago</td><td>vengo</td></tr><tr><td>tú</td><td>vas</td><td>tienes</td><td>haces</td><td>vienes</td></tr><tr><td>él/ella/usted</td><td>va</td><td>tiene</td><td>hace</td><td>viene</td></tr><tr><td>nosotros/as</td><td>vamos</td><td>tenemos</td><td>hacemos</td><td>venimos</td></tr><tr><td>vosotros/as</td><td>vais</td><td>tenéis</td><td>hacéis</td><td>venís</td></tr><tr><td>ellos/as/ustedes</td><td>van</td><td>tienen</td><td>hacen</td><td>vienen</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Ir — completamente irregular", "body": "<ul><li><em>Voy al mercado los sábados.</em></li><li><em>ir a</em> + infinitivo expresa un plan cercano: <em>Voy a estudiar esta tarde.</em></li></ul>"},
                {"heading": "b) Tener — posesión, edad y expresiones fijas", "body": "<ul><li>Posesión: <em>Tengo dos hermanos.</em></li><li>Edad (nunca con ser): <em>Tengo veinte años.</em></li><li>Expresiones fijas: <em>tener hambre, tener sed, tener frío, tener calor, tener sueño, tener prisa, tener razón</em></li></ul>"},
                {"heading": "c) Hacer — actividades y clima", "body": "<ul><li>Actividades: <em>Hago la tarea por las noches.</em></li><li>Clima: <em>Hace calor hoy. Hace frío en invierno.</em></li></ul>"},
                {"heading": "d) Venir — acercarse o llegar", "body": "<ul><li><em>Vengo de la universidad ahora mismo.</em></li><li><em>¿Vienes a la fiesta el viernes?</em></li></ul>"},
            ],
            "examples": [
                "Voy al gimnasio tres veces por semana.",
                "Tengo mucha hambre después de trabajar.",
                "Hace mucho calor en verano en esta ciudad.",
                "Vengo de visitar a mis abuelos.",
                "Ella tiene veinticinco años y trabaja como médica.",
                "Vamos a viajar a Chile el próximo mes.",
                "¿Tienes tiempo para ayudarme con esto?",
                "Nosotros hacemos ejercicio todas las mañanas.",
            ],
            "commonMistakes": [
                {"wrong": "Soy veinte años.", "right": "Tengo veinte años.", "why": "La edad siempre usa tener en español, no ser."},
                {"wrong": "Soy hambre.", "right": "Tengo hambre.", "why": "Las expresiones de estado físico como tener hambre, sed, frío o sueño siempre usan tener, no ser ni estar."},
                {"wrong": "Yo va al cine.", "right": "Yo voy al cine.", "why": "Va es la forma de él/ella/usted; yo siempre usa voy con el verbo ir."},
            ],
        },
        "exercises": [
            {"id": "a1pi-fill", "type": "fill-blank", "title": "Completa con el Verbo Correcto",
             "instructions": "Conjuga ir, tener, hacer o venir en presente.",
             "items": [
                {"id": "a1pi1", "prompt": "Yo ___ (tener) tres hermanos.", "answers": [["tengo"]], "explanation": "Yo + tener = tengo, cambio irregular de raíz.", "options": ["tengo", "tienes", "tiene"]},
                {"id": "a1pi2", "prompt": "Nosotros ___ (ir) al parque los domingos.", "answers": [["vamos"]], "explanation": "Nosotros + ir = vamos.", "options": ["vamos", "van", "vais"]},
                {"id": "a1pi3", "prompt": "Ella ___ (hacer) la cena todos los días.", "answers": [["hace"]], "explanation": "Él/ella + hacer = hace.", "options": ["hace", "hago", "haces"]},
                {"id": "a1pi4", "prompt": "¿Tú ___ (venir) a la reunión mañana?", "answers": [["vienes"]], "explanation": "Tú + venir = vienes.", "options": ["vienes", "viene", "vengo"]},
             ]},
            {"id": "a1pi-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "a1pi5", "prompt": "¿Cómo se dice \"tengo veinte años\" de forma correcta?", "options": ["Soy veinte años.", "Tengo veinte años.", "Hago veinte años."], "answerIndex": 1, "explanation": "La edad siempre se expresa con tener en español."},
                {"id": "a1pi6", "prompt": "¿Qué expresión describe el clima caluroso?", "options": ["Tengo calor.", "Hace calor.", "Soy calor."], "answerIndex": 1, "explanation": "El clima se describe con hacer: hace calor, hace frío, hace sol."},
             ]},
            {"id": "a1pi-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1pi7", "incorrect": "Yo soy quince años.", "answer": ["Yo tengo quince años."], "explanation": "La edad se expresa con tener, nunca con ser."},
                {"id": "a1pi8", "incorrect": "Ellos va a la escuela juntos.", "answer": ["Ellos van a la escuela juntos."], "explanation": "Va es singular; el sujeto plural ellos necesita van."},
             ]},
        ],
        "summary": [
            "Ir es completamente irregular: voy, vas, va, vamos, vais, van; ir a + infinitivo expresa planes cercanos.",
            "Tener, hacer y venir cambian su forma de yo (tengo, hago, vengo) pero siguen un patrón más regular en el resto.",
            "La edad y los estados físicos (hambre, sed, frío, sueño) siempre usan tener, nunca ser ni estar.",
        ],
    },
    {
        "id": "a1-adjetivos-y-concordancia",
        "level": "A1", "unit": "1", "order": 8, "skill": "grammar", "strand": "adjetivos",
        "title": "Adjetivos y Concordancia",
        "subtitle": "El adjetivo debe concordar en género y número con el sustantivo que describe.",
        "objectives": [
            "Hacer concordar adjetivos terminados en -o/-a en género y número",
            "Usar adjetivos terminados en -e o en consonante, que no cambian según el género",
            "Colocar el adjetivo antes o después del sustantivo según el matiz que se busque",
        ],
        "content": {
            "intro": "Un adjetivo en español no es una palabra fija: cambia su terminación para concordar con el sustantivo que describe, igual que hace el artículo.",
            "explanation": "<p>La mayoría de los adjetivos terminan en <strong>-o</strong> en masculino singular y cambian a <strong>-a</strong>, <strong>-os</strong>, <strong>-as</strong> para concordar con el sustantivo. Un segundo grupo termina en <strong>-e</strong> o en consonante para ambos géneros, y solo cambia para formar el plural. La mayoría de los adjetivos descriptivos van después del sustantivo (<em>una casa grande</em>), aunque algunos adjetivos comunes también pueden ir antes, a veces con un matiz de significado distinto.</p>",
            "rules": [
                {"heading": "a) Adjetivos en -o/-a (cuatro formas)", "body": "<ul><li>masc. sing. <strong>-o</strong>: <em>alto</em></li><li>fem. sing. <strong>-a</strong>: <em>alta</em></li><li>masc. pl. <strong>-os</strong>: <em>altos</em></li><li>fem. pl. <strong>-as</strong>: <em>altas</em></li></ul>"},
                {"heading": "b) Adjetivos en -e o en consonante (dos formas)", "body": "<ul><li>sing. (masc. o fem.) <strong>-e</strong>: <em>un chico inteligente, una chica inteligente</em></li><li>pl. (masc. o fem.) <strong>-es</strong>: <em>chicos inteligentes, chicas inteligentes</em></li><li>Lo mismo ocurre con adjetivos terminados en consonante: <em>un examen fácil, unos exámenes fáciles</em></li></ul>"},
                {"heading": "c) Posición del adjetivo", "body": "<ul><li>La mayoría va después del sustantivo: <em>un libro interesante</em></li><li>Algunos adjetivos comunes (bueno, malo, grande, pequeño, viejo, nuevo) pueden ir antes, a veces con matiz distinto: <em>un gran hombre</em> (importante) frente a <em>un hombre grande</em> (de tamaño físico)</li><li><em>bueno</em> y <em>malo</em> pierden la <strong>-o</strong> final antes de un sustantivo masculino singular: <em>un buen amigo, un mal día</em></li></ul>"},
            ],
            "examples": [
                "Marco es alto y muy simpático.",
                "Mis amigas son inteligentes y trabajadoras.",
                "Es un coche muy rápido y moderno.",
                "Tenemos una casa pequeña pero bonita.",
                "Los estudiantes están cansados después del examen.",
                "Es un buen amigo desde hace muchos años.",
                "Ese examen fue muy fácil para todos.",
                "Vivimos en un gran país lleno de historia.",
            ],
            "commonMistakes": [
                {"wrong": "una chica alto", "right": "una chica alta", "why": "El adjetivo debe concordar con el sustantivo femenino chica, así que necesita la terminación -a."},
                {"wrong": "los libros interesanta", "right": "los libros interesantes", "why": "Los adjetivos en -e forman el plural con -es, no con -a; interesante no es un adjetivo del tipo -o/-a."},
                {"wrong": "un bueno amigo", "right": "un buen amigo", "why": "Bueno pierde la -o final antes de un sustantivo masculino singular: buen, no bueno."},
            ],
        },
        "exercises": [
            {"id": "a1ac-fill", "type": "fill-blank", "title": "Completa la Terminación Correcta",
             "items": [
                {"id": "a1ac1", "prompt": "María es muy simpátic___.", "answers": [["a"]], "explanation": "Simpática concuerda con el sujeto femenino María.", "options": ["a", "o", "e"]},
                {"id": "a1ac2", "prompt": "Los chicos son alt___.", "answers": [["os"]], "explanation": "Masculino plural toma -os.", "options": ["os", "as", "o"]},
                {"id": "a1ac3", "prompt": "Una casa grand___.", "answers": [["e"]], "explanation": "Grande es un adjetivo en -e: la misma forma para masculino y femenino singular.", "options": ["e", "a", "o"]},
                {"id": "a1ac4", "prompt": "Es un ___ (bueno) amigo.", "answers": [["buen"]], "explanation": "Bueno pierde la -o final antes de un sustantivo masculino singular.", "options": ["buen", "bueno", "buena"]},
             ]},
            {"id": "a1ac-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "a1ac5", "prompt": "Mis hermanas son muy ___.", "options": ["inteligente", "inteligentes", "inteligento"], "answerIndex": 1, "explanation": "Femenino plural de un adjetivo en -e es -es, igual que en masculino plural."},
             ]},
            {"id": "a1ac-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1ac6", "incorrect": "una chica alto", "answer": ["una chica alta"], "explanation": "El adjetivo debe concordar con el sustantivo femenino chica."},
                {"id": "a1ac7", "incorrect": "los estudiantes bueno", "answer": ["los estudiantes buenos"], "explanation": "El sujeto plural masculino necesita la terminación -os en el adjetivo."},
             ]},
        ],
        "summary": [
            "Los adjetivos en -o/-a tienen cuatro formas: -o, -a, -os, -as, según el género y número del sustantivo.",
            "Los adjetivos en -e o en consonante solo tienen dos formas: singular y plural, iguales para ambos géneros.",
            "La mayoría de los adjetivos van después del sustantivo; algunos comunes pueden ir antes, a veces cambiando el matiz.",
        ],
    },
    {
        "id": "a1-posesivos",
        "level": "A1", "unit": "1", "order": 9, "skill": "grammar", "strand": "posesivos",
        "title": "Posesivos",
        "subtitle": "Mi, tu, su, nuestro y sus formas: cómo indicar de quién es algo.",
        "objectives": [
            "Usar los posesivos átonos (mi, tu, su, nuestro, vuestro) delante del sustantivo",
            "Hacer concordar nuestro/a y vuestro/a en género y número",
            "Distinguir el uso de su, que puede referirse a varias personas distintas",
        ],
        "content": {
            "intro": "Los posesivos indican a quién pertenece algo, y en español concuerdan con el sustantivo que acompañan, no con la persona que posee el objeto.",
            "explanation": "<p>La mayoría de los posesivos (<em>mi, tu, su</em>) solo cambian entre singular y plural, no entre masculino y femenino: <em>mi libro, mi casa, mis libros, mis casas</em>. Solo <strong>nuestro</strong> y <strong>vuestro</strong> tienen cuatro formas completas, como un adjetivo en -o/-a, porque concuerdan tanto en género como en número.</p><p>Un punto importante: el posesivo concuerda con la cosa poseída, no con el dueño — <em>su casa</em> puede significar \"la casa de él\", \"de ella\", \"de usted\", \"de ellos\", \"de ellas\" o \"de ustedes\"; el contexto aclara a quién se refiere.</p>",
            "rules": [
                {"heading": "a) Mi, tu, su (solo cambian en número)", "body": "<ul><li><strong>mi / mis</strong> — mi libro, mis libros</li><li><strong>tu / tus</strong> — tu casa, tus casas</li><li><strong>su / sus</strong> — su coche, sus coches (de él, de ella, de usted, de ellos, de ellas, de ustedes)</li></ul>"},
                {"heading": "b) Nuestro/a y vuestro/a (cambian en género y número)", "body": "<ul><li><strong>nuestro, nuestra, nuestros, nuestras</strong> — nuestro perro, nuestra casa, nuestros perros, nuestras casas</li><li><strong>vuestro, vuestra, vuestros, vuestras</strong> — vuestro perro, vuestra casa (usado en España)</li></ul>"},
                {"heading": "c) El posesivo concuerda con lo poseído, no con el dueño", "body": "<ul><li><em>Ella tiene sus libros.</em> — sus concuerda con libros (plural), no con ella</li><li>Para evitar ambigüedad con su, se puede aclarar: <em>la casa de ella, el coche de ustedes</em></li></ul>"},
            ],
            "examples": [
                "Mi hermano vive en otra ciudad.",
                "Tus amigos son muy divertidos.",
                "Su casa está cerca del parque central.",
                "Nuestra familia se reúne todos los domingos.",
                "Vuestros libros están sobre la mesa.",
                "Ellos siempre traen sus propios regalos.",
                "Nuestro profesor explica muy bien la gramática.",
                "¿Es esta tu mochila o la de tu hermana?",
            ],
            "commonMistakes": [
                {"wrong": "mis libro", "right": "mi libro", "why": "El posesivo debe concordar en número con el sustantivo: libro es singular, así que necesita mi, no mis."},
                {"wrong": "nuestro casa", "right": "nuestra casa", "why": "Nuestro tiene forma femenina propia y debe concordar: casa es femenino, así que se usa nuestra."},
                {"wrong": "sus casa de ellos", "right": "su casa de ellos", "why": "El posesivo concuerda con casa, que es singular, así que debe ser su, no sus, aunque los dueños sean varias personas."},
            ],
        },
        "exercises": [
            {"id": "a1po-fill", "type": "fill-blank", "title": "Completa con el Posesivo Correcto",
             "items": [
                {"id": "a1po1", "prompt": "___ hermana vive en Lima. (yo)", "answers": [["Mi"]], "explanation": "Mi no cambia por género, solo por número: hermana es singular.", "options": ["Mi", "Mis", "Mío"]},
                {"id": "a1po2", "prompt": "___ amigos llegan mañana. (tú)", "answers": [["Tus"]], "explanation": "Amigos es plural, así que el posesivo también debe ser plural: tus.", "options": ["Tu", "Tus", "Tuyo"]},
                {"id": "a1po3", "prompt": "___ casa es muy grande. (nosotros)", "answers": [["Nuestra"]], "explanation": "Casa es femenino singular, así que nuestro debe concordar en femenino: nuestra.", "options": ["Nuestro", "Nuestra", "Nuestros"]},
                {"id": "a1po4", "prompt": "___ libros están en la mochila. (yo)", "answers": [["Mis"]], "explanation": "Libros es plural, así que el posesivo también debe ser plural: mis.", "options": ["Mi", "Mis", "Mías"]},
             ]},
            {"id": "a1po-mc", "type": "multiple-choice", "title": "Elige el Posesivo Correcto",
             "items": [
                {"id": "a1po5", "prompt": "\"La casa de ellos\" se puede decir de forma más corta como...", "options": ["sus casa", "su casa", "sus casas"], "answerIndex": 1, "explanation": "Casa es singular, así que el posesivo debe ser su, no sus, aunque el dueño sea plural."},
                {"id": "a1po6", "prompt": "¿Cuál es la forma femenina plural de \"vuestro\"?", "options": ["vuestras", "vuestros", "vuestra"], "answerIndex": 0, "explanation": "Vuestro tiene cuatro formas completas: vuestro, vuestra, vuestros, vuestras."},
             ]},
            {"id": "a1po-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1po7", "incorrect": "Mis hermano vive lejos.", "answer": ["Mi hermano vive lejos."], "explanation": "Hermano es singular, así que el posesivo debe ser mi, no mis."},
                {"id": "a1po8", "incorrect": "Nuestro amigas llegan hoy.", "answer": ["Nuestras amigas llegan hoy."], "explanation": "Amigas es femenino plural, así que nuestro debe concordar como nuestras."},
             ]},
        ],
        "summary": [
            "Mi, tu y su solo cambian entre singular y plural (mi/mis, tu/tus, su/sus), no entre masculino y femenino.",
            "Nuestro y vuestro tienen cuatro formas completas, concordando en género y número con lo poseído.",
            "El posesivo siempre concuerda con la cosa poseída, no con la persona que la posee.",
        ],
    },
    {
        "id": "a1-demostrativos",
        "level": "A1", "unit": "1", "order": 10, "skill": "grammar", "strand": "demostrativos",
        "title": "Demostrativos",
        "subtitle": "Este, ese, aquel y sus formas: señalar la cercanía o lejanía de algo.",
        "objectives": [
            "Usar este, ese y aquel según la distancia respecto al hablante",
            "Hacer concordar los demostrativos en género y número",
            "Reconocer las formas neutras esto, eso y aquello",
        ],
        "content": {
            "intro": "Los demostrativos señalan objetos según lo cerca o lejos que estén del hablante — el español tiene tres grados de distancia, no solo dos.",
            "explanation": "<p>A diferencia de otras lenguas que distinguen solo entre \"cerca\" y \"lejos\", el español tiene tres niveles: <strong>este</strong> (cerca de quien habla), <strong>ese</strong> (cerca de quien escucha, o a media distancia) y <strong>aquel</strong> (lejos de ambos). Cada uno concuerda en género y número con el sustantivo que acompaña.</p><p>Además de las formas que acompañan a un sustantivo, existen las formas neutras <strong>esto, eso, aquello</strong>, que no concuerdan con ningún sustantivo específico porque se refieren a una idea, una situación o algo aún no identificado.</p>",
            "rules": [
                {"heading": "a) Este (cerca del hablante)", "body": "<ul><li><strong>este, esta, estos, estas</strong> — <em>este libro, esta silla, estos libros, estas sillas</em></li></ul>"},
                {"heading": "b) Ese (cerca del oyente / distancia media)", "body": "<ul><li><strong>ese, esa, esos, esas</strong> — <em>ese libro, esa silla, esos libros, esas sillas</em></li></ul>"},
                {"heading": "c) Aquel (lejos de ambos)", "body": "<ul><li><strong>aquel, aquella, aquellos, aquellas</strong> — <em>aquel edificio, aquella montaña, aquellos edificios, aquellas montañas</em></li></ul>"},
                {"heading": "d) Formas neutras: esto, eso, aquello", "body": "<ul><li>No concuerdan con ningún sustantivo — se usan para ideas o cosas sin identificar: <em>¿Qué es esto?</em>, <em>Eso no me gusta</em>, <em>Aquello fue hace mucho tiempo</em></li></ul>"},
            ],
            "examples": [
                "Este libro que tengo en la mano es muy interesante.",
                "Esa mochila que llevas es nueva, ¿verdad?",
                "Aquel edificio al fondo de la calle es el museo.",
                "Estas flores huelen muy bien.",
                "Esos zapatos que compraste son muy cómodos.",
                "Aquellas montañas se ven todavía nevadas.",
                "¿Qué es esto que encontré en el cajón?",
                "Eso que dijiste ayer me hizo pensar mucho.",
            ],
            "commonMistakes": [
                {"wrong": "esta libro", "right": "este libro", "why": "Libro es masculino, así que el demostrativo debe ser este, no esta."},
                {"wrong": "¿Qué es esta? (señalando algo aún no identificado)", "right": "¿Qué es esto?", "why": "Cuando el objeto todavía no se identifica o no tiene género conocido, se usa la forma neutra esto, no esta."},
                {"wrong": "aquel casa", "right": "aquella casa", "why": "Casa es femenino, así que el demostrativo debe concordar como aquella, no aquel."},
            ],
        },
        "exercises": [
            {"id": "a1de-fill", "type": "fill-blank", "title": "Completa con el Demostrativo Correcto",
             "items": [
                {"id": "a1de1", "prompt": "___ libro que tengo aquí es mío. (cerca de mí)", "answers": [["Este"]], "explanation": "Libro es masculino y está cerca del hablante: este.", "options": ["Este", "Ese", "Aquel"]},
                {"id": "a1de2", "prompt": "___ montañas al fondo se ven hermosas. (lejos de ambos)", "answers": [["Aquellas"]], "explanation": "Montañas es femenino plural y está lejos de ambos hablantes: aquellas.", "options": ["Estas", "Esas", "Aquellas"]},
                {"id": "a1de3", "prompt": "¿Qué es ___ que tienes en la mano? (algo sin identificar)", "answers": [["eso"]], "explanation": "Forma neutra para algo aún no identificado, a media distancia: eso.", "options": ["eso", "esa", "esos"]},
             ]},
            {"id": "a1de-mc", "type": "multiple-choice", "title": "Elige el Demostrativo Correcto",
             "items": [
                {"id": "a1de4", "prompt": "Señalas una silla que tienes justo al lado. ¿Qué dices?", "options": ["aquella silla", "esta silla", "esa silla"], "answerIndex": 1, "explanation": "Este/esta se usa para algo cerca del hablante."},
                {"id": "a1de5", "prompt": "¿Cuál es la forma correcta para \"zapatos\" (masculino plural) a media distancia?", "options": ["esos", "esas", "estos"], "answerIndex": 0, "explanation": "Zapatos es masculino plural y está a media distancia: esos."},
             ]},
            {"id": "a1de-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1de6", "incorrect": "esta libro es interesante", "answer": ["este libro es interesante"], "explanation": "Libro es masculino, así que el demostrativo debe ser este."},
                {"id": "a1de7", "incorrect": "aquel casa está lejos", "answer": ["aquella casa está lejos"], "explanation": "Casa es femenino, así que el demostrativo debe ser aquella."},
             ]},
        ],
        "summary": [
            "Este señala cercanía al hablante, ese cercanía al oyente o distancia media, y aquel lejanía de ambos.",
            "Cada demostrativo concuerda en género y número con el sustantivo que acompaña: este/esta/estos/estas, y así con ese y aquel.",
            "Las formas neutras esto, eso y aquello no concuerdan con ningún sustantivo: se usan para ideas o cosas sin identificar.",
        ],
    },
    {
        "id": "a1-hay-y-estar",
        "level": "A1", "unit": "1", "order": 11, "skill": "grammar", "strand": "existencia",
        "title": "Hay / Estar (Existencia y Ubicación)",
        "subtitle": "El contraste entre \"hay un libro\" (existencia) y \"el libro está aquí\" (ubicación).",
        "objectives": [
            "Usar hay para expresar la existencia de algo, sin importar el número",
            "Usar estar para indicar la ubicación de algo ya identificado",
            "Distinguir cuándo corresponde hay y cuándo corresponde estar",
        ],
        "content": {
            "intro": "Hay y estar responden a preguntas distintas: hay dice si algo existe o cuánto hay, mientras que estar dice dónde se encuentra algo que ya conocemos.",
            "explanation": "<p><strong>Hay</strong> es una forma especial del verbo <em>haber</em> que no cambia según el número: se dice <em>hay un libro</em> y también <em>hay tres libros</em>, siempre con la misma forma <em>hay</em>. Se usa para anunciar la existencia de algo, generalmente algo nuevo o no específico para el oyente.</p><p><strong>Estar</strong>, en cambio, se usa cuando el objeto ya es conocido o específico, y lo que interesa es dónde se encuentra — por eso concuerda en número con el sujeto, como cualquier otro verbo: <em>el libro está</em>, <em>los libros están</em>.</p>",
            "rules": [
                {"heading": "a) Hay — existencia, forma invariable", "body": "<ul><li><em>Hay un restaurante en esta calle.</em></li><li><em>Hay muchos estudiantes en la clase.</em></li><li>Hay nunca cambia de forma, aunque el sustantivo sea plural</li></ul>"},
                {"heading": "b) Estar — ubicación de algo específico", "body": "<ul><li><em>El restaurante está en esta calle.</em> (un restaurante concreto, ya mencionado)</li><li><em>Los estudiantes están en la biblioteca.</em></li><li>Estar concuerda en número: está / están</li></ul>"},
                {"heading": "c) Cómo elegir entre los dos", "body": "<ul><li>Si el sustantivo lleva un artículo indefinido (un, una, unos, unas) o ningún artículo, suele usarse <strong>hay</strong>: <em>Hay una farmacia cerca.</em></li><li>Si el sustantivo lleva un artículo definido (el, la, los, las) o es algo ya identificado, se usa <strong>estar</strong>: <em>La farmacia está cerca.</em></li></ul>"},
            ],
            "examples": [
                "Hay un parque muy bonito cerca de mi casa.",
                "El parque está a solo diez minutos caminando.",
                "Hay dos cafeterías en esta plaza.",
                "La cafetería que buscas está al lado del banco.",
                "¿Hay algún médico disponible ahora mismo?",
                "El médico está en su consultorio esta mañana.",
                "Hay muchas personas esperando el autobús.",
                "Mis amigos están esperando en la entrada.",
            ],
            "commonMistakes": [
                {"wrong": "Hay tres libros están en la mesa.", "right": "Hay tres libros en la mesa. / Los libros están en la mesa.", "why": "Hay y estar no se combinan en la misma frase para el mismo sustantivo: hay anuncia existencia, estar indica ubicación, pero no ambos a la vez."},
                {"wrong": "El libro hay en la mesa.", "right": "El libro está en la mesa.", "why": "Un sustantivo ya identificado con artículo definido usa estar para su ubicación, no hay."},
                {"wrong": "Han dos personas en la sala.", "right": "Hay dos personas en la sala.", "why": "La forma invariable de haber para expresar existencia es hay, no han, sin importar si el sustantivo es plural."},
            ],
        },
        "exercises": [
            {"id": "a1he-fill", "type": "fill-blank", "title": "Completa con Hay o la Forma de Estar",
             "items": [
                {"id": "a1he1", "prompt": "___ un banco muy cerca de aquí.", "answers": [["Hay"]], "explanation": "Se anuncia la existencia de algo no específico: hay.", "options": ["Hay", "Está", "Están"]},
                {"id": "a1he2", "prompt": "El banco ___ al lado de la farmacia.", "answers": [["está"]], "explanation": "El sustantivo ya está identificado con artículo definido: se usa estar.", "options": ["hay", "está", "están"]},
                {"id": "a1he3", "prompt": "___ muchos libros interesantes en esta biblioteca.", "answers": [["Hay"]], "explanation": "Se anuncia existencia de varios libros no específicos: hay, siempre invariable.", "options": ["Hay", "Están", "Estás"]},
                {"id": "a1he4", "prompt": "Mis llaves ___ sobre la mesa de la cocina.", "answers": [["están"]], "explanation": "Llaves ya es un sustantivo específico (mis llaves) y plural: están.", "options": ["hay", "está", "están"]},
             ]},
            {"id": "a1he-mc", "type": "multiple-choice", "title": "Elige la Opción Correcta",
             "items": [
                {"id": "a1he5", "prompt": "¿Cómo preguntas si existe una farmacia cerca?", "options": ["¿Está una farmacia cerca?", "¿Hay una farmacia cerca?", "¿Han una farmacia cerca?"], "answerIndex": 1, "explanation": "Para preguntar por la existencia de algo no específico se usa hay."},
                {"id": "a1he6", "prompt": "\"Los estudiantes ___ en el aula.\" ¿Qué falta?", "options": ["hay", "está", "están"], "answerIndex": 2, "explanation": "Estudiantes es un sujeto plural ya identificado: se necesita están, no hay."},
             ]},
            {"id": "a1he-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1he7", "incorrect": "El restaurante hay en el centro.", "answer": ["El restaurante está en el centro."], "explanation": "Restaurante ya está identificado con artículo definido, así que necesita estar, no hay."},
                {"id": "a1he8", "incorrect": "Han muchas personas en la fiesta.", "answer": ["Hay muchas personas en la fiesta."], "explanation": "La forma correcta e invariable de haber para expresar existencia es hay, no han."},
             ]},
        ],
        "summary": [
            "Hay expresa existencia y nunca cambia de forma, sin importar si el sustantivo es singular o plural.",
            "Estar expresa la ubicación de algo específico o ya identificado, y concuerda en número: está/están.",
            "Un sustantivo con artículo indefinido suele usar hay; uno con artículo definido suele usar estar.",
        ],
    },
    {
        "id": "a1-preposiciones-simples",
        "level": "A1", "unit": "1", "order": 12, "skill": "grammar", "strand": "preposiciones",
        "title": "Preposiciones Simples",
        "subtitle": "En, a, de, con, para, por: una introducción básica a las preposiciones más usadas.",
        "objectives": [
            "Usar en, a y de para expresar lugar, dirección y origen",
            "Distinguir el uso básico de para y por",
            "Usar con como preposición de compañía o instrumento",
        ],
        "content": {
            "intro": "Las preposiciones conectan las palabras de una frase y suelen tener un uso propio en español que conviene aprender como patrón fijo, más que traducir palabra por palabra.",
            "explanation": "<p>En este nivel, las preposiciones más frecuentes son <strong>en, a, de, con, para, por</strong>. Cada una tiene usos centrales fáciles de reconocer: <em>en</em> para estar dentro de un lugar, <em>a</em> para dirección o destino, <em>de</em> para origen o posesión, <em>con</em> para compañía, y <em>para/por</em>, dos preposiciones que a veces confunden porque ambas pueden corresponder a una idea de \"para\" en otras lenguas, pero tienen usos distintos.</p>",
            "rules": [
                {"heading": "a) En — ubicación dentro de un lugar", "body": "<ul><li><em>Vivo en Madrid.</em></li><li><em>El libro está en la mesa.</em></li><li><em>Trabajo en una oficina.</em></li></ul>"},
                {"heading": "b) A — dirección, destino, hora", "body": "<ul><li>Dirección: <em>Voy a la escuela.</em></li><li>Hora: <em>Llego a las ocho.</em></li><li>Objeto indirecto de persona: <em>Escribo a mi madre.</em></li></ul>"},
                {"heading": "c) De — origen, posesión, material", "body": "<ul><li>Origen: <em>Soy de Perú.</em></li><li>Posesión: <em>el libro de Ana</em></li><li>Material: <em>una mesa de madera</em></li></ul>"},
                {"heading": "d) Con, para y por (uso básico)", "body": "<ul><li><strong>con</strong> — compañía o instrumento: <em>Voy con mis amigos. Escribo con un lápiz.</em></li><li><strong>para</strong> — destinatario, propósito o destino: <em>Este regalo es para ti. Estudio para aprender.</em></li><li><strong>por</strong> — causa, medio o lugar de paso: <em>Gracias por tu ayuda. Camino por el parque.</em></li></ul>"},
            ],
            "examples": [
                "Vivo en una ciudad pequeña cerca de la costa.",
                "Voy a la universidad todos los días en autobús.",
                "Soy de Ecuador, pero vivo en España.",
                "Este café es para mi jefe, no para mí.",
                "Camino por el centro cada mañana antes de trabajar.",
                "Estudio con mis compañeros los fines de semana.",
                "Gracias por tu paciencia, la necesitaba mucho.",
                "El coche de mi hermano es nuevo y muy rápido.",
            ],
            "commonMistakes": [
                {"wrong": "Vivo a Madrid.", "right": "Vivo en Madrid.", "why": "La ubicación dentro de una ciudad o lugar usa en, no a; a se reserva para dirección o destino de movimiento."},
                {"wrong": "Este regalo es por ti.", "right": "Este regalo es para ti.", "why": "El destinatario de algo se expresa con para, no con por, que se usa para causa o motivo."},
                {"wrong": "Soy a Colombia.", "right": "Soy de Colombia.", "why": "El origen se expresa con de, no con a ni con en."},
            ],
        },
        "exercises": [
            {"id": "a1ps-fill", "type": "fill-blank", "title": "Completa con la Preposición Correcta",
             "items": [
                {"id": "a1ps1", "prompt": "Vivo ___ Bogotá desde hace cinco años.", "answers": [["en"]], "explanation": "En expresa ubicación dentro de una ciudad.", "options": ["en", "a", "de"]},
                {"id": "a1ps2", "prompt": "Voy ___ la escuela caminando cada mañana.", "answers": [["a"]], "explanation": "A expresa dirección o destino de movimiento.", "options": ["a", "en", "por"]},
                {"id": "a1ps3", "prompt": "Este libro es ___ Marta, ella lo dejó aquí.", "answers": [["de"]], "explanation": "De expresa posesión.", "options": ["de", "a", "para"]},
                {"id": "a1ps4", "prompt": "Este regalo es ___ ti, espero que te guste.", "answers": [["para"]], "explanation": "Para expresa el destinatario de algo.", "options": ["para", "por", "con"]},
             ]},
            {"id": "a1ps-mc", "type": "multiple-choice", "title": "¿En o A?",
             "items": [
                {"id": "a1ps5", "prompt": "Trabajo ___ un hospital muy grande.", "options": ["a", "en", "de"], "answerIndex": 1, "explanation": "Trabajar dentro de un lugar usa en."},
                {"id": "a1ps6", "prompt": "Llego ___ las nueve de la mañana.", "options": ["en", "a", "por"], "answerIndex": 1, "explanation": "La hora exacta se expresa con a."},
             ]},
            {"id": "a1ps-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1ps7", "incorrect": "Soy a México.", "answer": ["Soy de México."], "explanation": "El origen se expresa con de, no con a."},
                {"id": "a1ps8", "incorrect": "Vivo a Buenos Aires.", "answer": ["Vivo en Buenos Aires."], "explanation": "La ubicación dentro de una ciudad usa en, no a."},
             ]},
        ],
        "summary": [
            "En expresa ubicación dentro de un lugar; a expresa dirección, destino y hora exacta; de expresa origen y posesión.",
            "Con expresa compañía o instrumento; para expresa destinatario o propósito; por expresa causa, medio o lugar de paso.",
            "Estas preposiciones se aprenden mejor como patrones fijos en frases comunes, no traduciendo palabra por palabra.",
        ],
    },
    {
        "id": "a1-interrogativos-y-preguntas",
        "level": "A1", "unit": "1", "order": 13, "skill": "grammar", "strand": "preguntas",
        "title": "Interrogativos y Preguntas",
        "subtitle": "Qué, quién, cuándo, dónde, cómo, por qué, cuánto: cómo formar preguntas simples.",
        "objectives": [
            "Usar los interrogativos más comunes para formar preguntas",
            "Colocar correctamente los signos de interrogación al inicio y al final",
            "Distinguir cuánto/cuánta/cuántos/cuántas según género y número",
        ],
        "content": {
            "intro": "Las palabras interrogativas siempre llevan tilde en español, incluso dentro de una frase, y siempre van acompañadas por los dos signos de interrogación: uno al principio y otro al final.",
            "explanation": "<p>El español usa un signo de interrogación de apertura (<strong>¿</strong>) al inicio de la pregunta y uno de cierre (<strong>?</strong>) al final — esto ayuda a saber, incluso antes de terminar de leer, que la frase es una pregunta. Las palabras interrogativas (<em>qué, quién, cuándo, dónde, cómo, por qué, cuánto</em>) siempre llevan tilde cuando se usan para preguntar, aunque la misma palabra sin tilde pueda tener otro uso en la frase (como <em>que</em> sin tilde, que significa \"that/which\" en otros contextos).</p>",
            "rules": [
                {"heading": "a) Los interrogativos principales", "body": "<ul><li><strong>qué</strong> — pide información sobre una cosa: <em>¿Qué haces?</em></li><li><strong>quién / quiénes</strong> — pide información sobre una persona: <em>¿Quién es ella?</em></li><li><strong>cuándo</strong> — tiempo: <em>¿Cuándo llegas?</em></li><li><strong>dónde</strong> — lugar: <em>¿Dónde vives?</em></li><li><strong>cómo</strong> — manera: <em>¿Cómo estás?</em></li><li><strong>por qué</strong> — causa (dos palabras, con tilde en qué): <em>¿Por qué estudias español?</em></li></ul>"},
                {"heading": "b) Cuánto y sus formas", "body": "<ul><li><strong>cuánto</strong> — masculino singular: <em>¿Cuánto cuesta?</em></li><li><strong>cuánta</strong> — femenino singular: <em>¿Cuánta agua necesitas?</em></li><li><strong>cuántos</strong> — masculino plural: <em>¿Cuántos hermanos tienes?</em></li><li><strong>cuántas</strong> — femenino plural: <em>¿Cuántas personas vienen?</em></li></ul>"},
                {"heading": "c) Los signos de interrogación", "body": "<ul><li>El español siempre usa ambos signos: <strong>¿</strong> al principio y <strong>?</strong> al final</li><li>El signo de apertura va justo antes de la parte que es pregunta, no siempre al inicio absoluto de la frase: <em>Oye, ¿vienes hoy?</em></li></ul>"},
            ],
            "examples": [
                "¿Qué quieres comer esta noche?",
                "¿Quién llamó por teléfono hace un momento?",
                "¿Cuándo empieza la clase de español?",
                "¿Dónde está la estación de tren más cercana?",
                "¿Cómo se llama tu profesor de matemáticas?",
                "¿Por qué llegas siempre tan tarde a clase?",
                "¿Cuánto cuesta este libro de gramática?",
                "¿Cuántas personas van a venir a la fiesta?",
            ],
            "commonMistakes": [
                {"wrong": "Que hora es?", "right": "¿Qué hora es?", "why": "Falta el signo de apertura ¿ y la tilde en qué, obligatoria cuando la palabra pregunta algo."},
                {"wrong": "¿Cuanto cuesta esto?", "right": "¿Cuánto cuesta esto?", "why": "Cuánto siempre lleva tilde cuando se usa como interrogativo."},
                {"wrong": "¿Cuántos agua necesitas?", "right": "¿Cuánta agua necesitas?", "why": "Agua es femenino (aunque use el artículo el por sonido), así que cuánto debe concordar como cuánta."},
            ],
        },
        "exercises": [
            {"id": "a1iq-fill", "type": "fill-blank", "title": "Completa con el Interrogativo Correcto",
             "items": [
                {"id": "a1iq1", "prompt": "¿___ te llamas?", "answers": [["Cómo"]], "explanation": "Cómo pregunta por la manera, usado en la expresión fija cómo te llamas.", "options": ["Cómo", "Qué", "Cuándo"]},
                {"id": "a1iq2", "prompt": "¿___ vives, en qué ciudad?", "answers": [["Dónde"]], "explanation": "Dónde pregunta por el lugar.", "options": ["Dónde", "Cuándo", "Quién"]},
                {"id": "a1iq3", "prompt": "¿___ hermanos tienes?", "answers": [["Cuántos"]], "explanation": "Hermanos es masculino plural, así que se usa cuántos.", "options": ["Cuántos", "Cuánta", "Cuánto"]},
                {"id": "a1iq4", "prompt": "¿___ no vienes a la fiesta?", "answers": [["Por qué"]], "explanation": "Por qué pregunta por la causa; se escribe en dos palabras con tilde en qué.", "options": ["Por qué", "Porque", "Cómo"]},
             ]},
            {"id": "a1iq-mc", "type": "multiple-choice", "title": "Elige la Pregunta Correcta",
             "items": [
                {"id": "a1iq5", "prompt": "Quieres saber el precio de algo. ¿Qué preguntas?", "options": ["¿Cuándo cuesta?", "¿Cuánto cuesta?", "¿Cómo cuesta?"], "answerIndex": 1, "explanation": "Cuánto se usa para preguntar por cantidad o precio."},
                {"id": "a1iq6", "prompt": "¿Cuál pregunta es correcta para saber quién hizo algo?", "options": ["¿Qué lo hizo?", "¿Quién lo hizo?", "¿Cómo lo hizo?"], "answerIndex": 1, "explanation": "Quién pregunta por la persona responsable de la acción."},
             ]},
            {"id": "a1iq-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1iq7", "incorrect": "Donde esta el baño?", "answer": ["¿Dónde está el baño?"], "explanation": "Faltan el signo de apertura ¿ y las tildes en dónde y está."},
                {"id": "a1iq8", "incorrect": "¿Cuanta libros tienes?", "answer": ["¿Cuántos libros tienes?"], "explanation": "Libros es masculino plural, así que se necesita cuántos, con tilde."},
             ]},
        ],
        "summary": [
            "Los interrogativos más comunes son qué, quién(es), cuándo, dónde, cómo, por qué y cuánto, y siempre llevan tilde al preguntar.",
            "Toda pregunta en español lleva dos signos de interrogación: ¿ al inicio de la parte interrogativa y ? al final.",
            "Cuánto concuerda en género y número con el sustantivo: cuánto, cuánta, cuántos, cuántas.",
        ],
    },
    {
        "id": "a1-gustar-y-verbos-similares",
        "level": "A1", "unit": "1", "order": 14, "skill": "grammar", "strand": "verbos",
        "title": "Gustar y Verbos Similares",
        "subtitle": "Me gusta, te gusta, le gusta... y verbos como encantar e interesar, que funcionan igual.",
        "objectives": [
            "Conjugar gustar con los pronombres me, te, le, nos, os, les",
            "Elegir entre gusta y gustan según lo que sigue al verbo",
            "Usar verbos similares a gustar, como encantar e interesar",
        ],
        "content": {
            "intro": "Gustar no funciona como un verbo normal: en vez de conjugarse según la persona que siente el gusto, se conjuga según la cosa que produce ese gusto — una estructura distinta a la de la mayoría de los verbos ya vistos.",
            "explanation": "<p>Con <strong>gustar</strong>, la persona a quien le gusta algo se expresa con un pronombre (<em>me, te, le, nos, os, les</em>), y el verbo concuerda con lo que gusta, no con la persona: <em>Me gusta el café</em> (el café es singular, gusta) frente a <em>Me gustan los libros</em> (los libros es plural, gustan). Es como decir, literalmente, \"el café me resulta agradable\".</p><p>Otros verbos funcionan exactamente igual: <strong>encantar</strong> (gustar mucho), <strong>interesar</strong>, <strong>molestar</strong>, <strong>importar</strong>, <strong>doler</strong>. Todos siguen el mismo patrón de pronombre + verbo en tercera persona (singular o plural, según lo que sigue).</p>",
            "rules": [
                {"heading": "a) Los pronombres de gustar", "body": "<ul><li><strong>me</strong> gusta(n) — a mí</li><li><strong>te</strong> gusta(n) — a ti</li><li><strong>le</strong> gusta(n) — a él, a ella, a usted</li><li><strong>nos</strong> gusta(n) — a nosotros/as</li><li><strong>os</strong> gusta(n) — a vosotros/as</li><li><strong>les</strong> gusta(n) — a ellos, a ellas, a ustedes</li></ul>"},
                {"heading": "b) Gusta o gustan", "body": "<ul><li><strong>gusta</strong> — cuando lo que sigue es singular o un verbo en infinitivo: <em>Me gusta el chocolate. Me gusta bailar.</em></li><li><strong>gustan</strong> — cuando lo que sigue es plural: <em>Me gustan las películas de aventura.</em></li></ul>"},
                {"heading": "c) Añadir claridad o énfasis con a + persona", "body": "<ul><li><em>A mí me gusta el té, pero a mi hermano le gusta el café.</em></li><li>Necesario para aclarar a quién se refiere le/les: <em>A Marta le gusta viajar.</em></li></ul>"},
                {"heading": "d) Otros verbos con la misma estructura", "body": "<ul><li><strong>encantar</strong> — <em>Me encanta esta canción.</em></li><li><strong>interesar</strong> — <em>Nos interesa la historia.</em></li><li><strong>molestar</strong> — <em>Le molesta el ruido.</em></li><li><strong>doler</strong> — <em>Me duele la cabeza.</em></li></ul>"},
            ],
            "examples": [
                "Me gusta mucho la música latina.",
                "¿Te gustan las películas de terror?",
                "A ella le gusta leer novelas históricas.",
                "Nos encanta viajar durante las vacaciones.",
                "Les interesa mucho la cultura española.",
                "A mi padre le duele la espalda desde ayer.",
                "¿Os gusta el plan para este fin de semana?",
                "A mí me molesta el ruido de la calle por la noche.",
            ],
            "commonMistakes": [
                {"wrong": "Yo gusto el café.", "right": "Me gusta el café.", "why": "Gustar no se conjuga según la persona que siente el gusto; necesita el pronombre me y la tercera persona del verbo."},
                {"wrong": "Me gusta los libros.", "right": "Me gustan los libros.", "why": "El verbo concuerda con lo que gusta, que aquí es plural (los libros), así que necesita gustan."},
                {"wrong": "A yo me gusta el chocolate.", "right": "A mí me gusta el chocolate.", "why": "Después de la preposición a se usa el pronombre mí, no yo, para dar énfasis o claridad."},
            ],
        },
        "exercises": [
            {"id": "a1gu-fill", "type": "fill-blank", "title": "Completa con Gusta o Gustan",
             "items": [
                {"id": "a1gu1", "prompt": "Me ___ el chocolate.", "answers": [["gusta"]], "explanation": "Chocolate es singular: gusta.", "options": ["gusta", "gustan"]},
                {"id": "a1gu2", "prompt": "Nos ___ las películas de acción.", "answers": [["gustan"]], "explanation": "Películas es plural: gustan.", "options": ["gusta", "gustan"]},
                {"id": "a1gu3", "prompt": "¿Te ___ viajar en avión?", "answers": [["gusta"]], "explanation": "Delante de un infinitivo siempre se usa la forma singular gusta.", "options": ["gusta", "gustan"]},
                {"id": "a1gu4", "prompt": "A ellos les ___ los deportes al aire libre.", "answers": [["gustan"]], "explanation": "Deportes es plural: gustan.", "options": ["gusta", "gustan"]},
             ]},
            {"id": "a1gu-mc", "type": "multiple-choice", "title": "Elige el Pronombre Correcto",
             "items": [
                {"id": "a1gu5", "prompt": "\"A mi hermana ___ gusta el café.\" ¿Qué pronombre falta?", "options": ["me", "le", "te"], "answerIndex": 1, "explanation": "A mi hermana corresponde a la tercera persona singular: le."},
                {"id": "a1gu6", "prompt": "¿Cómo dirías que a ti te gustan mucho los perros?", "options": ["Me encanta los perros.", "Me encantan los perros.", "Yo encanto los perros."], "answerIndex": 1, "explanation": "Encantar sigue la misma estructura que gustar: concuerda con perros, que es plural."},
             ]},
            {"id": "a1gu-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a1gu7", "incorrect": "Yo gusto mucho la pizza.", "answer": ["Me gusta mucho la pizza."], "explanation": "Gustar necesita el pronombre me y la tercera persona del verbo, no una conjugación con yo."},
                {"id": "a1gu8", "incorrect": "Me gusta las manzanas.", "answer": ["Me gustan las manzanas."], "explanation": "Manzanas es plural, así que el verbo debe concordar como gustan."},
             ]},
        ],
        "summary": [
            "Gustar se conjuga según la cosa que gusta (gusta/gustan), no según la persona, que se expresa con un pronombre (me, te, le, nos, os, les).",
            "Se usa gusta con singular o infinitivo, y gustan con plural.",
            "Encantar, interesar, molestar, importar y doler siguen exactamente la misma estructura que gustar.",
        ],
    },
]

# =======================================================================
# EXTRA_EXERCISES — bloques adicionales de práctica (lectura y ordenar
# frases) fusionados en cada lección por id. Ver el bucle de fusión al
# final de este archivo.
# =======================================================================
EXTRA_EXERCISES = {
    "a1-el-abecedario-y-la-pronunciacion": [
        {"id": "a1x1-reading", "type": "reading-comprehension", "title": "Lectura: La Pronunciación de mi Nombre",
         "passage": "<p>Me llamo Rodrigo, con una sola r al principio, así que suena fuerte. Mi apellido es Guerrero, que tiene rr doble en medio: suena todavía más fuerte. Vivo en la calle Águila, con tilde en la ú. Mi ciudad se escribe con ñ: Logroño.</p>",
         "items": [
            {"id": "a1x1r1", "prompt": "¿Por qué la r de \"Rodrigo\" suena fuerte?", "options": ["Porque está al principio de la palabra", "Porque es una rr doble", "Porque lleva tilde"], "answerIndex": 0, "explanation": "Una r al inicio de palabra siempre suena fuerte, igual que la rr doble."},
            {"id": "a1x1r2", "prompt": "¿Qué tipo de r tiene \"Guerrero\"?", "options": ["r simple", "rr doble", "Ninguna r"], "answerIndex": 1, "explanation": "El texto dice que Guerrero «tiene rr doble en medio»."},
            {"id": "a1x1r3", "prompt": "¿Dónde lleva la tilde la palabra \"Águila\"?", "options": ["En la a", "En la u", "No lleva tilde"], "answerIndex": 0, "explanation": "El texto dice «con tilde en la ú» refiriéndose a Águila, que en realidad lleva la tilde en la Á; revisa cuidadosamente cada vocal al leer."},
            {"id": "a1x1r4", "prompt": "¿Qué letra especial tiene el nombre de la ciudad?", "options": ["La h", "La ñ", "La doble r"], "answerIndex": 1, "explanation": "El texto dice: «Mi ciudad se escribe con ñ: Logroño»."},
         ]},
        {"id": "a1x1-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x1o1", "prompt": "Ordena las palabras.", "words": ["Mi", "apellido", "tiene", "una", "rr", "doble"], "explanation": "Posesivo + sustantivo + verbo + objeto directo con adjetivo."},
            {"id": "a1x1o2", "prompt": "Ordena las palabras.", "words": ["La", "ciudad", "se", "escribe", "con", "ñ"], "explanation": "Sujeto + verbo reflexivo + complemento con preposición."},
         ]},
    ],
    "a1-genero-y-numero-de-los-sustantivos": [
        {"id": "a1x2-reading", "type": "reading-comprehension", "title": "Lectura: Mi Habitación",
         "passage": "<p>En mi habitación hay una cama grande, dos ventanas y un armario de madera. También tengo varios libros y unas fotos en la pared. El problema es que no tengo mucho espacio para más muebles.</p>",
         "items": [
            {"id": "a1x2r1", "prompt": "¿Cuántas ventanas hay en la habitación?", "options": ["Una", "Dos", "Tres"], "answerIndex": 1, "explanation": "El texto dice: «dos ventanas»."},
            {"id": "a1x2r2", "prompt": "¿De qué material es el armario?", "options": ["Metal", "Madera", "Plástico"], "answerIndex": 1, "explanation": "El texto dice: «un armario de madera»."},
            {"id": "a1x2r3", "prompt": "¿Qué palabra masculina termina en -a en el texto?", "options": ["cama", "problema", "ventana"], "answerIndex": 1, "explanation": "Problema es masculino de origen griego, aunque termina en -a: el problema."},
            {"id": "a1x2r4", "prompt": "¿La persona tiene mucho espacio para más muebles?", "options": ["Sí, mucho", "No, poco espacio"], "answerIndex": 1, "explanation": "El texto dice: «no tengo mucho espacio para más muebles»."},
         ]},
        {"id": "a1x2-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x2o1", "prompt": "Ordena las palabras.", "words": ["Tengo", "una", "cama", "y", "dos", "ventanas"], "explanation": "Verbo tener + objeto singular + y + objeto plural."},
            {"id": "a1x2o2", "prompt": "Ordena las palabras.", "words": ["El", "problema", "es", "el", "espacio"], "explanation": "Sujeto masculino (el problema) + verbo ser + atributo."},
         ]},
    ],
    "a1-articulos-definidos-e-indefinidos": [
        {"id": "a1x3-reading", "type": "reading-comprehension", "title": "Lectura: Un Día en el Mercado",
         "passage": "<p>Voy al mercado y compro unas manzanas y un poco de pan. El vendedor de fruta es muy amable. Después necesito una botella de agua, porque el agua de mi casa no me gusta mucho. Las tiendas del mercado cierran a las dos.</p>",
         "items": [
            {"id": "a1x3r1", "prompt": "¿Qué compra la persona además de pan?", "options": ["Manzanas", "Naranjas", "Leche"], "answerIndex": 0, "explanation": "El texto dice: «compro unas manzanas y un poco de pan»."},
            {"id": "a1x3r2", "prompt": "¿Cómo es el vendedor de fruta?", "options": ["Antipático", "Muy amable", "Muy serio"], "answerIndex": 1, "explanation": "El texto dice: «El vendedor de fruta es muy amable»."},
            {"id": "a1x3r3", "prompt": "¿Qué artículo usa el texto para \"agua\" en singular?", "options": ["la", "el", "un"], "answerIndex": 1, "explanation": "Agua es femenina pero empieza con a tónica, así que en singular usa el: el agua."},
            {"id": "a1x3r4", "prompt": "¿A qué hora cierran las tiendas del mercado?", "options": ["A la una", "A las dos", "A las tres"], "answerIndex": 1, "explanation": "El texto dice: «Las tiendas del mercado cierran a las dos»."},
         ]},
        {"id": "a1x3-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x3o1", "prompt": "Ordena las palabras.", "words": ["Necesito", "una", "botella", "de", "agua"], "explanation": "Verbo + artículo indefinido femenino + sustantivo + complemento."},
            {"id": "a1x3o2", "prompt": "Ordena las palabras.", "words": ["Las", "tiendas", "cierran", "a", "las", "dos"], "explanation": "Artículo definido plural + sujeto + verbo + complemento de hora."},
         ]},
    ],
    "a1-ser-y-estar-introduccion": [
        {"id": "a1x4-reading", "type": "reading-comprehension", "title": "Lectura: Presentando a mi Amiga",
         "passage": "<p>Mi amiga Clara es profesora y es de Chile. Hoy está muy cansada porque trabajó todo el día. Su oficina está cerca del centro. Clara es muy inteligente y siempre está de buen humor, aunque hoy está un poco triste.</p>",
         "items": [
            {"id": "a1x4r1", "prompt": "¿Cuál es la profesión de Clara?", "options": ["Médica", "Profesora", "Estudiante"], "answerIndex": 1, "explanation": "El texto dice: «Mi amiga Clara es profesora»."},
            {"id": "a1x4r2", "prompt": "¿Por qué Clara está cansada hoy?", "options": ["Porque no durmió", "Porque trabajó todo el día", "Porque está enferma"], "answerIndex": 1, "explanation": "El texto dice: «está muy cansada porque trabajó todo el día»."},
            {"id": "a1x4r3", "prompt": "¿Dónde está la oficina de Clara?", "options": ["Lejos del centro", "Cerca del centro", "No lo dice"], "answerIndex": 1, "explanation": "El texto dice: «Su oficina está cerca del centro»."},
            {"id": "a1x4r4", "prompt": "¿Cómo está Clara hoy, según el final del texto?", "options": ["Muy feliz", "Un poco triste", "Muy enojada"], "answerIndex": 1, "explanation": "El texto termina: «aunque hoy está un poco triste»."},
         ]},
        {"id": "a1x4-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x4o1", "prompt": "Ordena las palabras.", "words": ["Mi", "amiga", "es", "profesora", "de", "matemáticas"], "explanation": "Ser + profesión describe una identidad permanente."},
            {"id": "a1x4o2", "prompt": "Ordena las palabras.", "words": ["Ella", "está", "muy", "cansada", "hoy"], "explanation": "Estar + adjetivo describe un estado temporal."},
         ]},
    ],
    "a1-pronombres-personales-de-sujeto": [
        {"id": "a1x5-reading", "type": "reading-comprehension", "title": "Lectura: Diferentes Formas de Hablar",
         "passage": "<p>En España, cuando hablas con amigos, usas tú. En Argentina, mis amigos usan vos en vez de tú. Nosotros, en México, usamos ustedes tanto para el plural formal como el informal. Vosotros solo se usa en España para el plural informal.</p>",
         "items": [
            {"id": "a1x5r1", "prompt": "¿Qué pronombre usan los argentinos en vez de tú?", "options": ["Usted", "Vos", "Vosotros"], "answerIndex": 1, "explanation": "El texto dice: «mis amigos usan vos en vez de tú»."},
            {"id": "a1x5r2", "prompt": "¿Qué usan en México para el plural, formal e informal?", "options": ["Vosotros", "Ustedes", "Vos"], "answerIndex": 1, "explanation": "El texto dice: «usamos ustedes tanto para el plural formal como el informal»."},
            {"id": "a1x5r3", "prompt": "¿Dónde se usa vosotros?", "options": ["En México", "En Argentina", "En España"], "answerIndex": 2, "explanation": "El texto dice: «Vosotros solo se usa en España»."},
            {"id": "a1x5r4", "prompt": "¿El texto menciona alguna diferencia entre países?", "options": ["Sí", "No"], "answerIndex": 0, "explanation": "Todo el texto compara el uso de pronombres en distintos países hispanohablantes."},
         ]},
        {"id": "a1x5-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x5o1", "prompt": "Ordena las palabras.", "words": ["En", "Argentina", "usan", "vos", "en", "vez", "de", "tú"], "explanation": "Complemento de lugar + verbo + objeto + expresión en vez de."},
            {"id": "a1x5o2", "prompt": "Ordena las palabras.", "words": ["Vosotros", "solo", "se", "usa", "en", "España"], "explanation": "Sujeto + adverbio + verbo reflexivo + complemento de lugar."},
         ]},
    ],
    "a1-presente-verbos-regulares": [
        {"id": "a1x6-reading", "type": "reading-comprehension", "title": "Lectura: Mi Rutina de Trabajo",
         "passage": "<p>Trabajo en una oficina desde las nueve hasta las cinco. Como con mis compañeros a la una. Por la tarde, escribo correos y hablo con clientes por teléfono. Los fines de semana, mi familia y yo viajamos a la playa.</p>",
         "items": [
            {"id": "a1x6r1", "prompt": "¿A qué hora empieza a trabajar la persona?", "options": ["A las ocho", "A las nueve", "A las diez"], "answerIndex": 1, "explanation": "El texto dice: «Trabajo en una oficina desde las nueve»."},
            {"id": "a1x6r2", "prompt": "¿Con quién come a la una?", "options": ["Con su familia", "Con sus compañeros", "Sola"], "answerIndex": 1, "explanation": "El texto dice: «Como con mis compañeros a la una»."},
            {"id": "a1x6r3", "prompt": "¿Qué hace por la tarde en el trabajo?", "options": ["Duerme", "Escribe correos y habla con clientes", "Viaja"], "answerIndex": 1, "explanation": "El texto dice: «escribo correos y hablo con clientes por teléfono»."},
            {"id": "a1x6r4", "prompt": "¿Adónde viaja la familia los fines de semana?", "options": ["A la montaña", "A la playa", "Al extranjero"], "answerIndex": 1, "explanation": "El texto dice: «viajamos a la playa» los fines de semana."},
         ]},
        {"id": "a1x6-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x6o1", "prompt": "Ordena las palabras.", "words": ["Trabajo", "en", "una", "oficina", "grande"], "explanation": "Verbo en -ar (yo) + complemento de lugar con adjetivo."},
            {"id": "a1x6o2", "prompt": "Ordena las palabras.", "words": ["Nosotros", "viajamos", "a", "la", "playa"], "explanation": "Sujeto + verbo en -ar (nosotros) + complemento de destino."},
         ]},
    ],
    "a1-presente-verbos-irregulares-comunes": [
        {"id": "a1x7-reading", "type": "reading-comprehension", "title": "Lectura: Los Planes de Marco",
         "passage": "<p>Marco tiene veintidós años y hace deporte todos los días. Va al gimnasio por la mañana y viene a casa a mediodía. Tiene mucha hambre después de hacer ejercicio, así que hace una comida grande. Vamos a visitarlo el próximo fin de semana.</p>",
         "items": [
            {"id": "a1x7r1", "prompt": "¿Cuántos años tiene Marco?", "options": ["Veinte", "Veintidós", "Veinticinco"], "answerIndex": 1, "explanation": "El texto dice: «Marco tiene veintidós años»."},
            {"id": "a1x7r2", "prompt": "¿Adónde va Marco por la mañana?", "options": ["Al trabajo", "Al gimnasio", "A la universidad"], "answerIndex": 1, "explanation": "El texto dice: «Va al gimnasio por la mañana»."},
            {"id": "a1x7r3", "prompt": "¿Por qué Marco hace una comida grande?", "options": ["Porque tiene mucha hambre", "Porque tiene invitados", "Porque es su cumpleaños"], "answerIndex": 0, "explanation": "El texto dice: «Tiene mucha hambre después de hacer ejercicio»."},
            {"id": "a1x7r4", "prompt": "¿Cuándo van a visitar a Marco?", "options": ["Hoy", "El próximo fin de semana", "El mes que viene"], "answerIndex": 1, "explanation": "El texto dice: «Vamos a visitarlo el próximo fin de semana»."},
         ]},
        {"id": "a1x7-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x7o1", "prompt": "Ordena las palabras.", "words": ["Él", "va", "al", "gimnasio", "todos", "los", "días"], "explanation": "Sujeto + ir (él) + complemento de lugar + expresión de frecuencia."},
            {"id": "a1x7o2", "prompt": "Ordena las palabras.", "words": ["Tengo", "mucha", "hambre", "ahora", "mismo"], "explanation": "Tener + expresión fija (mucha hambre) + adverbio de tiempo."},
         ]},
    ],
    "a1-adjetivos-y-concordancia": [
        {"id": "a1x8-reading", "type": "reading-comprehension", "title": "Lectura: Una Casa Bonita",
         "passage": "<p>Vivimos en una casa pequeña pero muy bonita. Las paredes son blancas y las ventanas son grandes. El jardín tiene flores rojas y amarillas. Nuestros vecinos son muy simpáticos y siempre están dispuestos a ayudar.</p>",
         "items": [
            {"id": "a1x8r1", "prompt": "¿Cómo es la casa, según el texto?", "options": ["Grande y fea", "Pequeña pero bonita", "Vieja y oscura"], "answerIndex": 1, "explanation": "El texto dice: «una casa pequeña pero muy bonita»."},
            {"id": "a1x8r2", "prompt": "¿De qué color son las paredes?", "options": ["Blancas", "Azules", "Verdes"], "answerIndex": 0, "explanation": "El texto dice: «Las paredes son blancas»."},
            {"id": "a1x8r3", "prompt": "¿Qué colores tienen las flores del jardín?", "options": ["Rojas y azules", "Rojas y amarillas", "Blancas y verdes"], "answerIndex": 1, "explanation": "El texto dice: «flores rojas y amarillas»."},
            {"id": "a1x8r4", "prompt": "¿Cómo son los vecinos?", "options": ["Antipáticos", "Muy simpáticos", "Muy serios"], "answerIndex": 1, "explanation": "El texto dice: «Nuestros vecinos son muy simpáticos»."},
         ]},
        {"id": "a1x8-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x8o1", "prompt": "Ordena las palabras.", "words": ["Las", "ventanas", "son", "muy", "grandes"], "explanation": "Sujeto plural + ser (concordado en plural) + adverbio + adjetivo plural."},
            {"id": "a1x8o2", "prompt": "Ordena las palabras.", "words": ["Tenemos", "un", "jardín", "muy", "bonito"], "explanation": "Verbo + artículo + sustantivo masculino + adjetivo concordado en masculino."},
         ]},
    ],
    "a1-posesivos": [
        {"id": "a1x9-reading", "type": "reading-comprehension", "title": "Lectura: Nuestras Cosas",
         "passage": "<p>Este es mi teléfono y esa es tu mochila. Nuestros libros están en la mesa. Su coche es nuevo, pero el mío es viejo. Vuestra casa está cerca de la nuestra, así que nos visitamos mucho.</p>",
         "items": [
            {"id": "a1x9r1", "prompt": "¿De quién es la mochila mencionada primero?", "options": ["Mía", "Tuya", "Suya"], "answerIndex": 1, "explanation": "El texto dice: «esa es tu mochila»."},
            {"id": "a1x9r2", "prompt": "¿Dónde están los libros de \"nosotros\"?", "options": ["En la mesa", "En la mochila", "En el coche"], "answerIndex": 0, "explanation": "El texto dice: «Nuestros libros están en la mesa»."},
            {"id": "a1x9r3", "prompt": "¿Cómo es el coche de \"él/ella\"?", "options": ["Viejo", "Nuevo", "Roto"], "answerIndex": 1, "explanation": "El texto dice: «Su coche es nuevo»."},
            {"id": "a1x9r4", "prompt": "¿Por qué se visitan mucho las dos familias?", "options": ["Porque son amigas de la infancia", "Porque sus casas están cerca", "Porque trabajan juntas"], "answerIndex": 1, "explanation": "El texto dice: «Vuestra casa está cerca de la nuestra, así que nos visitamos mucho»."},
         ]},
        {"id": "a1x9-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x9o1", "prompt": "Ordena las palabras.", "words": ["Este", "es", "mi", "teléfono", "nuevo"], "explanation": "Demostrativo + ser + posesivo + sustantivo + adjetivo."},
            {"id": "a1x9o2", "prompt": "Ordena las palabras.", "words": ["Nuestra", "casa", "está", "cerca", "de", "aquí"], "explanation": "Posesivo + sustantivo + estar + complemento de lugar."},
         ]},
    ],
    "a1-demostrativos": [
        {"id": "a1x10-reading", "type": "reading-comprehension", "title": "Lectura: En la Tienda de Ropa",
         "passage": "<p>—Me gusta este vestido, pero prefiero ese de allí.<br>—¿Cuál, aquel azul?<br>—No, ese verde que está a tu lado.<br>—Ah, sí, estos colores son muy bonitos esta temporada.</p>",
         "items": [
            {"id": "a1x10r1", "prompt": "¿Qué vestido prefiere la clienta al final?", "options": ["El vestido azul", "El vestido verde", "El vestido que tiene puesto"], "answerIndex": 1, "explanation": "El texto aclara: «ese verde que está a tu lado»."},
            {"id": "a1x10r2", "prompt": "¿\"Aquel\" se refiere a algo cerca o lejos?", "options": ["Cerca de quien habla", "Lejos de ambos", "Cerca de la otra persona"], "answerIndex": 1, "explanation": "Aquel/aquella se usa para algo lejos de ambos interlocutores."},
            {"id": "a1x10r3", "prompt": "¿De qué color es el vestido que está cerca de la otra persona?", "options": ["Azul", "Verde", "Rojo"], "answerIndex": 1, "explanation": "El texto dice: «ese verde que está a tu lado»."},
            {"id": "a1x10r4", "prompt": "¿Qué opinan sobre los colores de esta temporada?", "options": ["Que son feos", "Que son muy bonitos", "Que no les gustan"], "answerIndex": 1, "explanation": "El texto dice: «estos colores son muy bonitos esta temporada»."},
         ]},
        {"id": "a1x10-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x10o1", "prompt": "Ordena las palabras.", "words": ["Me", "gusta", "este", "vestido", "azul"], "explanation": "Pronombre + gustar + demostrativo cercano + sustantivo + adjetivo."},
            {"id": "a1x10o2", "prompt": "Ordena las palabras.", "words": ["Prefiero", "aquella", "camisa", "de", "allí"], "explanation": "Verbo + demostrativo lejano femenino + sustantivo + complemento."},
         ]},
    ],
    "a1-hay-y-estar": [
        {"id": "a1x11-reading", "type": "reading-comprehension", "title": "Lectura: El Centro de la Ciudad",
         "passage": "<p>En el centro de la ciudad hay muchas tiendas y restaurantes. El museo está al lado del parque, y la biblioteca está enfrente del ayuntamiento. Hay también una plaza muy bonita donde la gente se reúne los fines de semana.</p>",
         "items": [
            {"id": "a1x11r1", "prompt": "¿Qué hay en el centro de la ciudad?", "options": ["Solo tiendas", "Muchas tiendas y restaurantes", "Solo restaurantes"], "answerIndex": 1, "explanation": "El texto dice: «hay muchas tiendas y restaurantes»."},
            {"id": "a1x11r2", "prompt": "¿Dónde está el museo?", "options": ["Al lado del parque", "Enfrente del ayuntamiento", "Dentro de la plaza"], "answerIndex": 0, "explanation": "El texto dice: «El museo está al lado del parque»."},
            {"id": "a1x11r3", "prompt": "¿Qué está enfrente del ayuntamiento?", "options": ["El museo", "La biblioteca", "La plaza"], "answerIndex": 1, "explanation": "El texto dice: «la biblioteca está enfrente del ayuntamiento»."},
            {"id": "a1x11r4", "prompt": "¿Cuándo se reúne la gente en la plaza?", "options": ["Entre semana", "Los fines de semana", "Todas las noches"], "answerIndex": 1, "explanation": "El texto dice: «la gente se reúne los fines de semana»."},
         ]},
        {"id": "a1x11-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x11o1", "prompt": "Ordena las palabras.", "words": ["Hay", "una", "plaza", "muy", "bonita"], "explanation": "Hay (existencia) + artículo indefinido + sustantivo + adjetivo."},
            {"id": "a1x11o2", "prompt": "Ordena las palabras.", "words": ["El", "museo", "está", "al", "lado", "del", "parque"], "explanation": "El museo (ubicación conocida) + estar + complemento de lugar con al lado de."},
         ]},
    ],
    "a1-preposiciones-simples": [
        {"id": "a1x12-reading", "type": "reading-comprehension", "title": "Lectura: El Viaje de Elena",
         "passage": "<p>Elena viaja de Madrid a Barcelona en tren. El viaje dura desde las diez hasta la una. Durante el viaje, lee un libro y habla con la persona de al lado. Después del viaje, va directamente al hotel para descansar.</p>",
         "items": [
            {"id": "a1x12r1", "prompt": "¿Cómo viaja Elena?", "options": ["En avión", "En tren", "En autobús"], "answerIndex": 1, "explanation": "El texto dice: «Elena viaja... en tren»."},
            {"id": "a1x12r2", "prompt": "¿Cuánto dura el viaje?", "options": ["De diez a una", "De nueve a doce", "De once a dos"], "answerIndex": 0, "explanation": "El texto dice: «El viaje dura desde las diez hasta la una»."},
            {"id": "a1x12r3", "prompt": "¿Qué hace Elena durante el viaje?", "options": ["Duerme todo el tiempo", "Lee y habla con alguien", "Trabaja en su computadora"], "answerIndex": 1, "explanation": "El texto dice: «lee un libro y habla con la persona de al lado»."},
            {"id": "a1x12r4", "prompt": "¿Adónde va después del viaje?", "options": ["A un restaurante", "Al hotel", "A una reunión"], "answerIndex": 1, "explanation": "El texto dice: «va directamente al hotel para descansar»."},
         ]},
        {"id": "a1x12-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x12o1", "prompt": "Ordena las palabras.", "words": ["Viajo", "de", "Madrid", "a", "Barcelona"], "explanation": "Verbo + de + origen + a + destino."},
            {"id": "a1x12o2", "prompt": "Ordena las palabras.", "words": ["El", "libro", "está", "sobre", "la", "mesa"], "explanation": "Sujeto + estar + preposición de lugar + complemento."},
         ]},
    ],
    "a1-interrogativos-y-preguntas": [
        {"id": "a1x13-reading", "type": "reading-comprehension", "title": "Lectura: Una Entrevista Corta",
         "passage": "<p>—¿Cómo te llamas?<br>—Me llamo Luis.<br>—¿Dónde vives?<br>—Vivo en Sevilla.<br>—¿Por qué estudias español?<br>—Porque quiero trabajar en un país hispanohablante.<br>—¿Cuánto tiempo llevas estudiando?<br>—Llevo seis meses.</p>",
         "items": [
            {"id": "a1x13r1", "prompt": "¿Dónde vive Luis?", "options": ["En Madrid", "En Sevilla", "En Barcelona"], "answerIndex": 1, "explanation": "El texto dice: «Vivo en Sevilla»."},
            {"id": "a1x13r2", "prompt": "¿Por qué estudia español Luis?", "options": ["Por curiosidad", "Para trabajar en un país hispanohablante", "Por su familia"], "answerIndex": 1, "explanation": "El texto dice: «quiero trabajar en un país hispanohablante»."},
            {"id": "a1x13r3", "prompt": "¿Cuánto tiempo lleva estudiando español?", "options": ["Tres meses", "Seis meses", "Un año"], "answerIndex": 1, "explanation": "El texto dice: «Llevo seis meses»."},
            {"id": "a1x13r4", "prompt": "¿Qué palabra interrogativa pregunta por el motivo?", "options": ["Dónde", "Por qué", "Cuánto"], "answerIndex": 1, "explanation": "Por qué es la palabra interrogativa que pregunta por la razón o el motivo."},
         ]},
        {"id": "a1x13-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x13o1", "prompt": "Ordena las palabras.", "words": ["¿Dónde", "vives", "tú", "ahora"], "explanation": "Palabra interrogativa + verbo + sujeto + adverbio."},
            {"id": "a1x13o2", "prompt": "Ordena las palabras.", "words": ["¿Cuánto", "tiempo", "llevas", "estudiando", "español"], "explanation": "Interrogativo + sustantivo + llevar + gerundio + complemento."},
         ]},
    ],
    "a1-gustar-y-verbos-similares": [
        {"id": "a1x14-reading", "type": "reading-comprehension", "title": "Lectura: Nuestros Gustos",
         "passage": "<p>A mí me encanta la música latina, pero a mi hermano le gusta más el rock. A nosotros nos interesan las películas de misterio. A mis padres les molesta el ruido por las noches. A ti te gusta el fútbol, ¿verdad?</p>",
         "items": [
            {"id": "a1x14r1", "prompt": "¿Qué tipo de música le encanta a la persona que habla?", "options": ["Rock", "Música latina", "Música clásica"], "answerIndex": 1, "explanation": "El texto dice: «A mí me encanta la música latina»."},
            {"id": "a1x14r2", "prompt": "¿Qué le gusta más al hermano?", "options": ["La música latina", "El rock", "El fútbol"], "answerIndex": 1, "explanation": "El texto dice: «a mi hermano le gusta más el rock»."},
            {"id": "a1x14r3", "prompt": "¿Qué les interesa a \"nosotros\"?", "options": ["Las películas de misterio", "Las películas de terror", "Los documentales"], "answerIndex": 0, "explanation": "El texto dice: «A nosotros nos interesan las películas de misterio»."},
            {"id": "a1x14r4", "prompt": "¿Qué les molesta a los padres?", "options": ["El calor", "El ruido por las noches", "El tráfico"], "answerIndex": 1, "explanation": "El texto dice: «A mis padres les molesta el ruido por las noches»."},
         ]},
        {"id": "a1x14-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "a1x14o1", "prompt": "Ordena las palabras.", "words": ["Me", "encanta", "la", "música", "latina"], "explanation": "Pronombre + encantar (singular) + sustantivo con artículo."},
            {"id": "a1x14o2", "prompt": "Ordena las palabras.", "words": ["Nos", "interesan", "mucho", "las", "películas"], "explanation": "Pronombre + interesar (plural, concuerda con películas) + adverbio + sustantivo plural."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))

# =======================================================================
# EXTRA_EXERCISES_2 — segunda ronda (corrección y producción escrita
# corta) fusionada en cada lección por id.
# =======================================================================
EXTRA_EXERCISES_2 = {
    "a1-el-abecedario-y-la-pronunciacion": [
        {"id": "a1y1-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y1c1", "incorrect": "La palabra \"musica\" no lleva tilde.", "answer": ["La palabra \"música\" sí lleva tilde."], "explanation": "Música es esdrújula (la fuerza cae dos sílabas antes del final) y siempre lleva tilde."},
            {"id": "a1y1c2", "incorrect": "\"Cielo\" se pronuncia con el sonido fuerte de la c.", "answer": ["\"Cielo\" se pronuncia con el sonido suave de la c."], "explanation": "Ce/ci siempre tienen el sonido suave en español."},
         ]},
        {"id": "a1y1-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y1t1", "prompt": "Escribe una palabra esdrújula (con tilde en la antepenúltima sílaba).", "answer": [["música", "teléfono", "rápido", "número", "sábado"]], "explanation": "Cualquier palabra esdrújula es correcta; música, teléfono y rápido son ejemplos comunes."},
         ]},
    ],
    "a1-genero-y-numero-de-los-sustantivos": [
        {"id": "a1y2-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y2c1", "incorrect": "El mano derecha me duele.", "answer": ["La mano derecha me duele."], "explanation": "Mano es femenina aunque termine en -o."},
            {"id": "a1y2c2", "incorrect": "Compré dos lápizes nuevos.", "answer": ["Compré dos lápices nuevos."], "explanation": "Las palabras terminadas en -z cambian a -ces en plural."},
         ]},
        {"id": "a1y2-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y2t1", "prompt": "Escribe el plural de \"ciudad\".", "answer": [["ciudades"]], "explanation": "Terminación en consonante: se añade -es."},
         ]},
    ],
    "a1-articulos-definidos-e-indefinidos": [
        {"id": "a1y3-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y3c1", "incorrect": "La agua está muy fría.", "answer": ["El agua está muy fría."], "explanation": "Agua empieza con a tónica, así que usa el en singular aunque sea femenina."},
            {"id": "a1y3c2", "incorrect": "Compré unos naranjas en el mercado.", "answer": ["Compré unas naranjas en el mercado."], "explanation": "Naranjas es femenino plural: unas, no unos."},
         ]},
        {"id": "a1y3-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y3t1", "prompt": "Escribe una frase usando \"el águila\".", "explanation": "Guardado para tu propio repaso — recuerda: el águila (singular, por sonido) pero las águilas (plural)."},
         ]},
    ],
    "a1-ser-y-estar-introduccion": [
        {"id": "a1y4-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y4c1", "incorrect": "El libro es en la mesa.", "answer": ["El libro está en la mesa."], "explanation": "La ubicación siempre usa estar, nunca ser."},
            {"id": "a1y4c2", "incorrect": "Ella es cansada hoy.", "answer": ["Ella está cansada hoy."], "explanation": "El cansancio es un estado temporal: se usa estar, no ser."},
         ]},
        {"id": "a1y4-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y4t1", "prompt": "Escribe una frase con \"soy\" describiendo tu profesión o tu origen.", "explanation": "Guardado para tu propio repaso — ser + profesión/origen describe una identidad."},
         ]},
    ],
    "a1-pronombres-personales-de-sujeto": [
        {"id": "a1y5-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y5c1", "incorrect": "Yo soy yo cansado.", "answer": ["Estoy cansado."], "explanation": "El pronombre de sujeto es redundante aquí; el verbo ya indica quién habla."},
            {"id": "a1y5c2", "incorrect": "Tú hablás español muy bien. (con pronombre tú)", "answer": ["Tú hablas español muy bien. / Vos hablás español muy bien."], "explanation": "Tú y vos tienen formas verbales distintas y no se combinan entre sí."},
         ]},
        {"id": "a1y5-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y5t1", "prompt": "Escribe una frase con un pronombre de sujeto usado para dar énfasis o contraste.", "explanation": "Guardado para tu propio repaso — ejemplo: «Yo estudio, tú miras la televisión.»"},
         ]},
    ],
    "a1-presente-verbos-regulares": [
        {"id": "a1y6-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y6c1", "incorrect": "Nosotros habla mucho.", "answer": ["Nosotros hablamos mucho."], "explanation": "Nosotros siempre usa -amos/-emos/-imos, no la forma de él/ella."},
            {"id": "a1y6c2", "incorrect": "Ellos comen y bebe agua.", "answer": ["Ellos comen y beben agua."], "explanation": "Los dos verbos deben concordar con el mismo sujeto plural."},
         ]},
        {"id": "a1y6-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y6t1", "prompt": "Escribe una frase con un verbo en -ar sobre tu rutina diaria.", "explanation": "Guardado para tu propio repaso — ejemplo: «Trabajo en una oficina.»"},
         ]},
    ],
    "a1-presente-verbos-irregulares-comunes": [
        {"id": "a1y7-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y7c1", "incorrect": "Soy veinte años.", "answer": ["Tengo veinte años."], "explanation": "La edad siempre usa tener, no ser."},
            {"id": "a1y7c2", "incorrect": "Yo va al cine.", "answer": ["Yo voy al cine."], "explanation": "Va es la forma de él/ella; yo siempre usa voy."},
         ]},
        {"id": "a1y7-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y7t1", "prompt": "Escribe tu edad usando el verbo tener.", "answer": [["tengo"]], "explanation": "La estructura correcta es: Tengo + número + años."},
         ]},
    ],
    "a1-adjetivos-y-concordancia": [
        {"id": "a1y8-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y8c1", "incorrect": "Mis amigas son inteligente.", "answer": ["Mis amigas son inteligentes."], "explanation": "El adjetivo debe concordar en plural con amigas: inteligentes."},
            {"id": "a1y8c2", "incorrect": "Tenemos una casa pequeño.", "answer": ["Tenemos una casa pequeña."], "explanation": "El adjetivo debe concordar en femenino con casa: pequeña."},
         ]},
        {"id": "a1y8-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y8t1", "prompt": "Describe tu casa o tu habitación con dos adjetivos.", "explanation": "Guardado para tu propio repaso — recuerda hacer concordar los adjetivos en género y número."},
         ]},
    ],
    "a1-posesivos": [
        {"id": "a1y9-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y9c1", "incorrect": "Mi hermanos viven en Chile.", "answer": ["Mis hermanos viven en Chile."], "explanation": "El posesivo debe concordar en plural con hermanos: mis, no mi."},
            {"id": "a1y9c2", "incorrect": "Este es su coche de ellos.", "answer": ["Este es su coche. / Este es el coche de ellos."], "explanation": "No se combinan su y de ellos para el mismo poseedor; se elige una de las dos formas."},
         ]},
        {"id": "a1y9-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y9t1", "prompt": "Escribe una frase con \"nuestro\" o \"nuestra\".", "explanation": "Guardado para tu propio repaso — recuerda concordar nuestro/a con el sustantivo."},
         ]},
    ],
    "a1-demostrativos": [
        {"id": "a1y10-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y10c1", "incorrect": "Me gusta esta vestido.", "answer": ["Me gusta este vestido."], "explanation": "Vestido es masculino: este, no esta."},
            {"id": "a1y10c2", "incorrect": "Aquel camisa es bonita.", "answer": ["Aquella camisa es bonita."], "explanation": "Camisa es femenina: aquella, no aquel."},
         ]},
        {"id": "a1y10-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y10t1", "prompt": "Escribe una frase usando \"aquel\" o \"aquella\" para algo lejos de ti.", "explanation": "Guardado para tu propio repaso — aquel/aquella se usa para algo lejos de ambos interlocutores."},
         ]},
    ],
    "a1-hay-y-estar": [
        {"id": "a1y11-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y11c1", "incorrect": "Hay el parque cerca de aquí.", "answer": ["El parque está cerca de aquí. / Hay un parque cerca de aquí."], "explanation": "Hay se usa con sustantivos no específicos; para algo ya identificado (el parque) se usa estar."},
            {"id": "a1y11c2", "incorrect": "En mi ciudad está muchos museos.", "answer": ["En mi ciudad hay muchos museos."], "explanation": "Para expresar existencia de algo no específico se usa hay, no está."},
         ]},
        {"id": "a1y11-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y11t1", "prompt": "Escribe una frase con \"hay\" describiendo tu ciudad.", "explanation": "Guardado para tu propio repaso — ejemplo: «En mi ciudad hay muchos parques.»"},
         ]},
    ],
    "a1-preposiciones-simples": [
        {"id": "a1y12-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y12c1", "incorrect": "Viajo en Madrid a Barcelona.", "answer": ["Viajo de Madrid a Barcelona."], "explanation": "Para expresar origen y destino se usa de... a, no en... a."},
            {"id": "a1y12c2", "incorrect": "El libro está encima la mesa.", "answer": ["El libro está encima de la mesa."], "explanation": "Encima siempre necesita la preposición de antes del sustantivo."},
         ]},
        {"id": "a1y12-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y12t1", "prompt": "Escribe una frase usando la preposición \"desde\" y \"hasta\".", "explanation": "Guardado para tu propio repaso — ejemplo: «Trabajo desde las nueve hasta las cinco.»"},
         ]},
    ],
    "a1-interrogativos-y-preguntas": [
        {"id": "a1y13-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y13c1", "incorrect": "Donde vives tú?", "answer": ["¿Dónde vives tú?"], "explanation": "Las preguntas interrogativas llevan tilde en dónde y necesitan el signo de apertura ¿."},
            {"id": "a1y13c2", "incorrect": "¿Cuando es tu cumpleaños?", "answer": ["¿Cuándo es tu cumpleaños?"], "explanation": "Cuándo, como palabra interrogativa, siempre lleva tilde."},
         ]},
        {"id": "a1y13-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y13t1", "prompt": "Escribe una pregunta usando \"por qué\".", "explanation": "Guardado para tu propio repaso — recuerda escribir por qué en dos palabras y con tilde en la pregunta."},
         ]},
    ],
    "a1-gustar-y-verbos-similares": [
        {"id": "a1y14-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "a1y14c1", "incorrect": "Me gusta los libros de misterio.", "answer": ["Me gustan los libros de misterio."], "explanation": "Gustar concuerda con lo que gusta: libros es plural, así que gustan."},
            {"id": "a1y14c2", "incorrect": "Yo gusto el chocolate.", "answer": ["Me gusta el chocolate."], "explanation": "Gustar requiere el pronombre de objeto indirecto me; el sujeto gramatical es el chocolate."},
         ]},
        {"id": "a1y14-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "a1y14t1", "prompt": "Escribe una frase con \"me encanta\" o \"me encantan\".", "explanation": "Guardado para tu propio repaso — encanta (singular) o encantan (plural), según lo que sigue."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES_2.get(_lesson["id"], []))
