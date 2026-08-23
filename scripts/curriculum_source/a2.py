# -*- coding: utf-8 -*-
"""A2 — datos del currículo de nivel elemental. Ver curriculum/SCHEMA.md
para la forma exacta del JSON que esto compila (scripts/generate_curriculum.py
hace la compilación). Escrito como Python en vez de JSON a mano para que el
texto en español con comillas, tildes y ñ se lea con naturalidad.

Curso monolingüe: los ejemplos son strings simples en español, sin
traducción al inglés en ningún campo."""

OVERVIEW = (
    "El nivel A2 te da las herramientas para hablar del pasado, del futuro y "
    "de comparaciones, además de sustituir sustantivos por pronombres para "
    "sonar más natural. Aprenderás los dos pasados básicos del español — el "
    "pretérito indefinido y el pretérito imperfecto — y, sobre todo, cuándo "
    "usar cada uno; también el futuro simple, los comparativos y "
    "superlativos, los verbos con cambio de raíz, los pronombres de objeto "
    "directo e indirecto, y el imperativo afirmativo para dar órdenes e "
    "instrucciones. Al terminar este nivel podrás contar lo que hiciste "
    "ayer, describir cómo era algo en el pasado, hacer planes y dar "
    "instrucciones sencillas."
)

LESSONS = [
    {
        "id": "a2-preterito-perfecto-compuesto",
        "level": "A2", "unit": "1", "order": 1, "skill": "grammar", "strand": "preterito-perfecto",
        "title": "Pretérito Perfecto Compuesto",
        "subtitle": "Haber + participio: acciones pasadas conectadas con el presente.",
        "objectives": [
            "Conjugar haber en presente como verbo auxiliar",
            "Formar el participio de verbos regulares e irregulares frecuentes",
            "Usar el pretérito perfecto compuesto para acciones recientes o con conexión al presente",
        ],
        "content": {
            "intro": "El pretérito perfecto compuesto une un hecho pasado con el momento presente: es el tiempo que usas cuando lo que pasó todavía importa ahora, o pasó muy recientemente.",
            "explanation": "<p>Se forma con el presente de <strong>haber</strong> (he, has, ha, hemos, habéis, han) más el <strong>participio</strong> del verbo principal. Los participios regulares terminan en <strong>-ado</strong> (verbos en -ar) o <strong>-ido</strong> (verbos en -er/-ir), pero varios verbos muy frecuentes tienen un participio irregular que hay que memorizar aparte.</p><p>Se usa sobre todo para hablar de acciones ocurridas en un periodo de tiempo que todavía no ha terminado (<em>hoy, esta semana, este año</em>), para experiencias de vida sin momento concreto, y para hechos recientes cuyo resultado se nota ahora. En España es el tiempo más habitual para el pasado reciente; en gran parte de América Latina se prefiere el pretérito indefinido incluso para hechos de hoy mismo.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Haber + participio</caption><thead><tr><th>Sujeto</th><th>haber</th><th>hablar</th><th>comer</th><th>vivir</th></tr></thead><tbody><tr><td>yo</td><td>he</td><td>hablado</td><td>comido</td><td>vivido</td></tr><tr><td>tú</td><td>has</td><td>hablado</td><td>comido</td><td>vivido</td></tr><tr><td>él/ella/usted</td><td>ha</td><td>hablado</td><td>comido</td><td>vivido</td></tr><tr><td>nosotros/as</td><td>hemos</td><td>hablado</td><td>comido</td><td>vivido</td></tr><tr><td>vosotros/as</td><td>habéis</td><td>hablado</td><td>comido</td><td>vivido</td></tr><tr><td>ellos/as/ustedes</td><td>han</td><td>hablado</td><td>comido</td><td>vivido</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Participios irregulares frecuentes", "body": "<ul><li><em>hacer &rarr; hecho, decir &rarr; dicho, escribir &rarr; escrito, ver &rarr; visto</em></li><li><em>poner &rarr; puesto, volver &rarr; vuelto, abrir &rarr; abierto, romper &rarr; roto</em></li><li><em>morir &rarr; muerto, resolver &rarr; resuelto</em></li></ul>"},
                {"heading": "b) Cuándo se usa", "body": "<ul><li>Periodo de tiempo no terminado: <em>Hoy he trabajado mucho.</em></li><li>Experiencia sin momento concreto: <em>He viajado a Perú dos veces.</em></li><li>Resultado presente de un hecho reciente: <em>Se ha roto el vaso.</em></li></ul>"},
                {"heading": "c) Nunca se separa haber del participio", "body": "<p>A diferencia de otros idiomas, en español no se puede meter ninguna palabra entre el auxiliar y el participio: <em>He siempre querido viajar</em> es incorrecto; la posición correcta es <em>Siempre he querido viajar.</em></p>"},
            ],
            "examples": [
                "Esta semana he estudiado mucho para el examen.",
                "¿Has visto la nueva película del director mexicano?",
                "Todavía no hemos terminado el proyecto.",
                "Mis padres han vivido en tres países distintos.",
                "¿Alguna vez has comido comida picante de verdad?",
                "Se ha roto la impresora otra vez esta mañana.",
                "Nunca he estado en Argentina, pero quiero ir pronto.",
                "Ellos ya han hecho toda la tarea del fin de semana.",
            ],
            "commonMistakes": [
                {"wrong": "He hablado con él ayer.", "right": "Hablé con él ayer.", "why": "Con un marcador de tiempo terminado como ayer, se prefiere el pretérito indefinido, no el perfecto compuesto."},
                {"wrong": "Ha escribido una carta.", "right": "Ha escrito una carta.", "why": "Escribir tiene un participio irregular: escrito, no escribido."},
                {"wrong": "He siempre querido aprender español.", "right": "Siempre he querido aprender español.", "why": "Ninguna palabra puede separar el auxiliar haber del participio; el adverbio va antes de haber o después del participio."},
            ],
        },
        "exercises": [
            {"id": "a2pp-fill", "type": "fill-blank", "title": "Completa con el Pretérito Perfecto Compuesto",
             "items": [
                {"id": "a2pp1", "prompt": "Yo ___ (comer) ya.", "answers": [["he comido"]], "options": ["he comido", "has comido", "ha comido"], "explanation": "Yo + haber (he) + participio de comer (comido)."},
                {"id": "a2pp2", "prompt": "¿___ (tú - ver) esta serie?", "answers": [["Has visto"]], "options": ["Has visto", "Ha visto", "He visto"], "explanation": "Tú + haber (has) + participio irregular de ver (visto)."},
                {"id": "a2pp3", "prompt": "Nosotros no ___ (hacer) la compra todavía.", "answers": [["hemos hecho"]], "options": ["hemos hecho", "habemos hecho", "han hecho"], "explanation": "Nosotros + haber (hemos) + participio irregular de hacer (hecho)."},
             ]},
            {"id": "a2pp-mc", "type": "multiple-choice", "title": "Elige el Participio Correcto",
             "items": [
                {"id": "a2pp4", "prompt": "El participio de \"escribir\" es...", "options": ["escribido", "escrito", "escribiendo"], "answerIndex": 1, "explanation": "Escribir tiene participio irregular: escrito."},
                {"id": "a2pp5", "prompt": "El participio de \"poner\" es...", "options": ["ponido", "puesto", "poniendo"], "answerIndex": 1, "explanation": "Poner tiene participio irregular: puesto."},
             ]},
            {"id": "a2pp-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2pp6", "incorrect": "Ellos han rompido la ventana.", "answer": ["Ellos han roto la ventana."], "explanation": "Romper tiene participio irregular: roto, no rompido."},
                {"id": "a2pp7", "incorrect": "He nunca visitado España.", "answer": ["Nunca he visitado España."], "explanation": "El adverbio nunca no puede separar haber del participio; debe ir antes de haber."},
             ]},
        ],
        "summary": [
            "El pretérito perfecto compuesto se forma con haber en presente más el participio del verbo principal.",
            "Varios verbos frecuentes tienen participio irregular: hecho, dicho, escrito, visto, puesto, vuelto, abierto, roto, muerto, resuelto.",
            "Se usa para periodos de tiempo no terminados, experiencias sin momento concreto y hechos recientes con resultado presente; nada puede separar haber del participio.",
        ],
    },
    {
        "id": "a2-preterito-indefinido-regulares",
        "level": "A2", "unit": "1", "order": 2, "skill": "grammar", "strand": "preterito-indefinido",
        "title": "Pretérito Indefinido — Verbos Regulares",
        "subtitle": "El tiempo para contar hechos pasados terminados y completos.",
        "objectives": [
            "Conjugar verbos regulares en -ar, -er e -ir en pretérito indefinido",
            "Reconocer los marcadores de tiempo típicos de este tiempo verbal",
            "Usar el pretérito indefinido para narrar una serie de hechos pasados",
        ],
        "content": {
            "intro": "El pretérito indefinido es el tiempo de la narración: cuenta hechos que ocurrieron y terminaron en un momento concreto del pasado, uno detrás de otro.",
            "explanation": "<p>Se forma añadiendo terminaciones propias a la raíz del verbo, distintas de las del presente. Los verbos en <strong>-er</strong> e <strong>-ir</strong> comparten exactamente las mismas terminaciones en este tiempo, a diferencia del presente, donde se diferencian un poco más.</p><p>Se usa con marcadores de tiempo cerrados y terminados: <em>ayer, anoche, la semana pasada, en 2020, hace tres años</em>. Es el tiempo típico de una narración: cuenta lo que pasó, paso a paso, como una serie de fotos fijas.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Pretérito indefinido — hablar, comer, vivir</caption><thead><tr><th>Sujeto</th><th>hablar</th><th>comer</th><th>vivir</th></tr></thead><tbody><tr><td>yo</td><td>hablé</td><td>comí</td><td>viví</td></tr><tr><td>tú</td><td>hablaste</td><td>comiste</td><td>viviste</td></tr><tr><td>él/ella/usted</td><td>habló</td><td>comió</td><td>vivió</td></tr><tr><td>nosotros/as</td><td>hablamos</td><td>comimos</td><td>vivimos</td></tr><tr><td>vosotros/as</td><td>hablasteis</td><td>comisteis</td><td>vivisteis</td></tr><tr><td>ellos/as/ustedes</td><td>hablaron</td><td>comieron</td><td>vivieron</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Terminaciones -ar", "body": "<p>-é, -aste, -ó, -amos, -asteis, -aron</p>"},
                {"heading": "b) Terminaciones -er/-ir (idénticas)", "body": "<p>-í, -iste, -ió, -imos, -isteis, -ieron</p>"},
                {"heading": "c) Nosotros coincide con el presente en -ar e -ir", "body": "<p>Hablamos y vivimos se escriben igual en presente y en pretérito indefinido; solo el contexto de la frase indica el tiempo.</p>"},
                {"heading": "d) Marcadores de tiempo típicos", "body": "<ul><li><em>ayer, anoche, anteayer</em></li><li><em>la semana/el mes/el año pasado</em></li><li><em>en + año (en 2019), hace + tiempo (hace dos días)</em></li></ul>"},
            ],
            "examples": [
                "Ayer hablé con mi hermano por teléfono.",
                "Anoche comimos en un restaurante nuevo del centro.",
                "El año pasado viví seis meses en Chile.",
                "¿Estudiaste para el examen de la semana pasada?",
                "Mis amigos viajaron a la costa el mes pasado.",
                "Ella nació en 1998 en Bogotá.",
                "Terminamos el proyecto hace dos días.",
                "Ustedes compraron una casa nueva el año pasado.",
            ],
            "commonMistakes": [
                {"wrong": "Yo hablé con él ayer y como pizza.", "right": "Yo hablé con él ayer y comí pizza.", "why": "Al narrar una serie de hechos pasados, todos los verbos deben mantenerse en pretérito indefinido, no cambiar a presente."},
                {"wrong": "Nosotros hablastemos con el profesor.", "right": "Nosotros hablamos con el profesor.", "why": "La forma de nosotros es hablamos, no existe la terminación -astemos."},
                {"wrong": "Ellos viviaron en Madrid.", "right": "Ellos vivieron en Madrid.", "why": "Los verbos en -ir usan la terminación -ieron en la tercera persona plural, no -iaron."},
            ],
        },
        "exercises": [
            {"id": "a2pir-fill", "type": "fill-blank", "title": "Conjuga en Pretérito Indefinido",
             "items": [
                {"id": "a2pir1", "prompt": "Ayer yo ___ (trabajar) hasta muy tarde.", "answers": [["trabajé"]], "options": ["trabajé", "trabajo", "trabajaba"], "explanation": "Yo + verbo en -ar en indefinido = terminación -é."},
                {"id": "a2pir2", "prompt": "Anoche nosotros ___ (comer) en casa de mis abuelos.", "answers": [["comimos"]], "options": ["comimos", "comemos", "comieron"], "explanation": "Nosotros + verbo en -er en indefinido = terminación -imos."},
                {"id": "a2pir3", "prompt": "El año pasado ellos ___ (vivir) en Uruguay.", "answers": [["vivieron"]], "options": ["vivieron", "vivían", "viven"], "explanation": "Ellos + verbo en -ir en indefinido = terminación -ieron."},
             ]},
            {"id": "a2pir-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "a2pir4", "prompt": "¿Cuál es la forma de \"tú\" del verbo \"estudiar\" en indefinido?", "options": ["estudiaste", "estudiabas", "estudias"], "answerIndex": 0, "explanation": "Tú + verbo en -ar en indefinido = terminación -aste."},
                {"id": "a2pir5", "prompt": "¿Qué marcador de tiempo acompaña naturalmente al pretérito indefinido?", "options": ["siempre", "la semana pasada", "todos los días"], "answerIndex": 1, "explanation": "La semana pasada señala un periodo cerrado y terminado, típico del pretérito indefinido."},
             ]},
            {"id": "a2pir-ordering", "type": "ordering", "title": "Ordena la Oración",
             "items": [
                {"id": "a2pir6", "prompt": "Ordena para narrar un hecho del pasado.", "words": ["El", "mes", "pasado", "viajamos", "a", "la", "playa", "con", "toda", "la", "familia"], "explanation": "El mes pasado marca un momento cerrado del pasado, y viajamos es la forma de nosotros en pretérito indefinido."},
             ]},
        ],
        "summary": [
            "El pretérito indefinido usa terminaciones propias: -é/-aste/-ó/-amos/-asteis/-aron para -ar, e -í/-iste/-ió/-imos/-isteis/-ieron para -er/-ir.",
            "Se usa con marcadores de tiempo cerrados como ayer, la semana pasada o en + año.",
            "Es el tiempo de la narración: cuenta hechos pasados, uno detrás de otro, como una serie de momentos completos.",
        ],
    },
    {
        "id": "a2-preterito-indefinido-irregulares",
        "level": "A2", "unit": "1", "order": 3, "skill": "grammar", "strand": "preterito-indefinido",
        "title": "Pretérito Indefinido — Verbos Irregulares",
        "subtitle": "Ser, ir, tener, hacer, estar, poder y otros verbos con raíz irregular en el pasado.",
        "objectives": [
            "Conjugar ser/ir, tener, hacer y estar en pretérito indefinido",
            "Reconocer el grupo de verbos con raíz irregular fuerte (tuve, hice, estuve...)",
            "Distinguir ser de ir en pretérito indefinido a partir del contexto",
        ],
        "content": {
            "intro": "Los verbos más usados del español suelen ser también los más irregulares en el pasado — vale la pena memorizarlos aparte, porque aparecen en casi cualquier conversación sobre el pasado.",
            "explanation": "<p><strong>Ser</strong> e <strong>ir</strong> comparten exactamente las mismas formas en pretérito indefinido (<em>fui, fuiste, fue, fuimos, fuisteis, fueron</em>); solo el contexto de la frase indica cuál de los dos verbos es. Un gran grupo de verbos frecuentes (<em>tener, estar, poder, poner, saber, querer, venir, hacer, decir</em>) comparte un patrón distinto: cambian la raíz y usan terminaciones sin tilde (<em>tuve, no tové</em>).</p><p>Estos verbos irregulares no siguen ningún patrón regular de -ar/-er/-ir, así que se memorizan como bloque, pero una vez aprendidos aparecen constantemente en cualquier historia sobre el pasado.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Pretérito indefinido — ser/ir, tener, hacer, estar</caption><thead><tr><th>Sujeto</th><th>ser / ir</th><th>tener</th><th>hacer</th><th>estar</th></tr></thead><tbody><tr><td>yo</td><td>fui</td><td>tuve</td><td>hice</td><td>estuve</td></tr><tr><td>tú</td><td>fuiste</td><td>tuviste</td><td>hiciste</td><td>estuviste</td></tr><tr><td>él/ella/usted</td><td>fue</td><td>tuvo</td><td>hizo</td><td>estuvo</td></tr><tr><td>nosotros/as</td><td>fuimos</td><td>tuvimos</td><td>hicimos</td><td>estuvimos</td></tr><tr><td>vosotros/as</td><td>fuisteis</td><td>tuvisteis</td><td>hicisteis</td><td>estuvisteis</td></tr><tr><td>ellos/as/ustedes</td><td>fueron</td><td>tuvieron</td><td>hicieron</td><td>estuvieron</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Ser e ir: formas idénticas", "body": "<ul><li><em>Fui profesor durante diez años.</em> (ser)</li><li><em>Fui al mercado esta mañana.</em> (ir)</li><li>Solo el contexto — si hay un lugar/destino o una identidad — distingue los dos verbos.</li></ul>"},
                {"heading": "b) El grupo con raíz irregular fuerte", "body": "<ul><li><em>tener &rarr; tuv-, estar &rarr; estuv-, poder &rarr; pud-, poner &rarr; pus-, saber &rarr; sup-, querer &rarr; quis-, venir &rarr; vin-</em></li><li>Todos usan las mismas terminaciones: <strong>-e, -iste, -o, -imos, -isteis, -ieron</strong> (sin tilde, a diferencia de los verbos regulares).</li></ul>"},
                {"heading": "c) Hacer y decir: raíz con \"j\"", "body": "<ul><li><em>hacer &rarr; hic-/hiz- (hice, hizo)</em></li><li><em>decir &rarr; dij-</em> — y la tercera persona plural pierde la i: <em>dijeron</em>, no dijieron</li></ul>"},
            ],
            "examples": [
                "Fui a la playa el fin de semana pasado.",
                "Ella fue mi profesora de matemáticas hace cinco años.",
                "Tuvimos una reunión muy larga ayer por la tarde.",
                "¿Dónde estuviste todo el día de ayer?",
                "Hicieron la tarea juntos antes de la cena.",
                "No pude terminar el informe a tiempo.",
                "Ellos dijeron la verdad al final.",
                "Vine a verte tan pronto como pude.",
            ],
            "commonMistakes": [
                {"wrong": "Yo tuvé una reunión ayer.", "right": "Yo tuve una reunión ayer.", "why": "Los verbos irregulares fuertes usan la terminación -e sin tilde, no -é."},
                {"wrong": "Ellos dijieron que no.", "right": "Ellos dijieron... dijeron que no.", "why": "Decir pierde la i de la terminación -ieron en la tercera persona plural: dijeron, no dijieron."},
                {"wrong": "Ellos hacieron la comida.", "right": "Ellos hicieron la comida.", "why": "Hacer cambia la raíz a hic-/hiz-, no se conjuga sobre la raíz regular hac-."},
            ],
        },
        "exercises": [
            {"id": "a2pii-fill", "type": "fill-blank", "title": "Completa con el Verbo Irregular",
             "items": [
                {"id": "a2pii1", "prompt": "Ayer yo ___ (tener) mucho trabajo.", "answers": [["tuve"]], "options": ["tuve", "tení", "tuvé"], "explanation": "Tener tiene raíz irregular tuv- y terminación -e sin tilde."},
                {"id": "a2pii2", "prompt": "Nosotros ___ (estar) en la fiesta hasta muy tarde.", "answers": [["estuvimos"]], "options": ["estuvimos", "estamos", "estabamos"], "explanation": "Estar tiene raíz irregular estuv- en el pretérito indefinido."},
                {"id": "a2pii3", "prompt": "Ella ___ (hacer) toda la tarea sola.", "answers": [["hizo"]], "options": ["hizo", "hació", "hace"], "explanation": "Hacer cambia a hiz- en la tercera persona del singular, con terminación -o."},
             ]},
            {"id": "a2pii-mc", "type": "multiple-choice", "title": "¿Ser o Ir?",
             "items": [
                {"id": "a2pii4", "prompt": "\"Fui médico durante quince años\" usa la forma fui de...", "options": ["ser", "ir", "ambos son posibles aquí"], "answerIndex": 0, "explanation": "Aquí describe una identidad/profesión pasada, así que es una forma de ser."},
                {"id": "a2pii5", "prompt": "\"Fuimos al cine anoche\" usa la forma fuimos de...", "options": ["ser", "ir", "ninguno de los dos"], "answerIndex": 1, "explanation": "Aquí describe un movimiento hacia un destino, así que es una forma de ir."},
             ]},
            {"id": "a2pii-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2pii6", "incorrect": "Ellos vinieron... ellos venieron tarde a la fiesta.", "answer": ["Ellos vinieron tarde a la fiesta."], "explanation": "Venir tiene raíz irregular vin-, no la forma regular venieron."},
                {"id": "a2pii7", "incorrect": "Yo pudí terminar el trabajo.", "answer": ["Yo pude terminar el trabajo."], "explanation": "Poder usa terminación -e sin tilde en primera persona: pude, no pudí."},
             ]},
        ],
        "summary": [
            "Ser e ir comparten exactamente las mismas formas en pretérito indefinido: fui, fuiste, fue, fuimos, fuisteis, fueron.",
            "Un grupo grande de verbos (tener, estar, poder, poner, saber, querer, venir) cambia la raíz y usa las terminaciones -e, -iste, -o, -imos, -isteis, -ieron, sin tilde.",
            "Hacer y decir cambian la raíz con j; decir además pierde la i en dijeron.",
        ],
    },
    {
        "id": "a2-preterito-imperfecto",
        "level": "A2", "unit": "1", "order": 4, "skill": "grammar", "strand": "imperfecto",
        "title": "Pretérito Imperfecto",
        "subtitle": "El tiempo para describir el pasado: cómo era, qué pasaba, qué se hacía habitualmente.",
        "objectives": [
            "Conjugar verbos regulares e irregulares (ser, ir, ver) en pretérito imperfecto",
            "Usar el imperfecto para describir el pasado y hablar de hábitos pasados",
            "Distinguir el imperfecto de un tiempo que narra hechos concretos",
        ],
        "content": {
            "intro": "El pretérito imperfecto no cuenta lo que pasó como un hecho puntual, sino cómo era el fondo de la escena: la descripción, el hábito, lo que se repetía o lo que ya estaba en marcha.",
            "explanation": "<p>El imperfecto es uno de los tiempos más regulares del español: solo tres verbos son irregulares (<strong>ser, ir, ver</strong>); todos los demás siguen el mismo patrón según su terminación en -ar o en -er/-ir.</p><p>Se usa para describir personas, lugares y situaciones en el pasado (<em>La casa era grande y tenía un jardín</em>), para hábitos y rutinas pasadas (<em>De niño jugaba en la calle todos los días</em>), y para dar el contexto o el fondo de una historia sobre el que luego ocurre un hecho puntual, normalmente en pretérito indefinido.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Pretérito imperfecto — hablar, comer, vivir, ser, ir, ver</caption><thead><tr><th>Sujeto</th><th>hablar</th><th>comer</th><th>vivir</th><th>ser</th><th>ir</th><th>ver</th></tr></thead><tbody><tr><td>yo</td><td>hablaba</td><td>comía</td><td>vivía</td><td>era</td><td>iba</td><td>veía</td></tr><tr><td>tú</td><td>hablabas</td><td>comías</td><td>vivías</td><td>eras</td><td>ibas</td><td>veías</td></tr><tr><td>él/ella/usted</td><td>hablaba</td><td>comía</td><td>vivía</td><td>era</td><td>iba</td><td>veía</td></tr><tr><td>nosotros/as</td><td>hablábamos</td><td>comíamos</td><td>vivíamos</td><td>éramos</td><td>íbamos</td><td>veíamos</td></tr><tr><td>vosotros/as</td><td>hablabais</td><td>comíais</td><td>vivíais</td><td>erais</td><td>ibais</td><td>veíais</td></tr><tr><td>ellos/as/ustedes</td><td>hablaban</td><td>comían</td><td>vivían</td><td>eran</td><td>iban</td><td>veían</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Verbos en -ar", "body": "<p>Terminaciones: -aba, -abas, -aba, -ábamos, -abais, -aban (yo y él/ella/usted son idénticos)</p>"},
                {"heading": "b) Verbos en -er/-ir", "body": "<p>Terminaciones: -ía, -ías, -ía, -íamos, -íais, -ían (yo y él/ella/usted también son idénticos)</p>"},
                {"heading": "c) Los tres únicos irregulares", "body": "<ul><li><em>ser &rarr; era, eras, era, éramos, erais, eran</em></li><li><em>ir &rarr; iba, ibas, iba, íbamos, ibais, iban</em></li><li><em>ver &rarr; veía, veías, veía, veíamos, veíais, veían</em></li></ul>"},
                {"heading": "d) Usos principales", "body": "<ul><li>Descripción del pasado: <em>El pueblo era pequeño y tranquilo.</em></li><li>Hábitos y rutinas pasadas: <em>Todos los veranos íbamos a la playa.</em></li><li>Fondo de una historia: <em>Llovía mucho cuando salimos de casa.</em></li></ul>"},
            ],
            "examples": [
                "Cuando era niño, vivía en un pueblo muy pequeño.",
                "Mis abuelos siempre hablaban de sus viajes por Europa.",
                "Todos los días caminábamos juntos hasta la escuela.",
                "La casa tenía un jardín enorme y muchos árboles.",
                "Ella era muy tímida cuando era joven.",
                "Nosotros veíamos esa serie todos los sábados por la noche.",
                "Hacía mucho frío esa mañana de invierno.",
                "Ustedes siempre llegaban temprano a las reuniones.",
            ],
            "commonMistakes": [
                {"wrong": "Cuando fui niño, vivía en un pueblo.", "right": "Cuando era niño, vivía en un pueblo.", "why": "Describir una etapa o estado prolongado del pasado (ser niño) usa el imperfecto, no el indefinido."},
                {"wrong": "Nosotros ibamos a la playa cada verano.", "right": "Nosotros íbamos a la playa cada verano.", "why": "La forma de nosotros de ir en imperfecto lleva tilde en la í: íbamos."},
                {"wrong": "Yo veiía la televisión de niño.", "right": "Yo veía la televisión de niño.", "why": "Ver en imperfecto es veía, con una sola i, no veiía."},
            ],
        },
        "exercises": [
            {"id": "a2pim-fill", "type": "fill-blank", "title": "Completa con el Pretérito Imperfecto",
             "items": [
                {"id": "a2pim1", "prompt": "De niña, yo ___ (jugar) en el parque todos los días.", "answers": [["jugaba"]], "options": ["jugaba", "jugué", "juego"], "explanation": "Hábito repetido en el pasado: imperfecto de un verbo en -ar."},
                {"id": "a2pim2", "prompt": "Mis abuelos ___ (ser) muy trabajadores.", "answers": [["eran"]], "options": ["eran", "fueron", "son"], "explanation": "Descripción de una característica en el pasado: imperfecto irregular de ser."},
                {"id": "a2pim3", "prompt": "Nosotros ___ (ir) a la playa cada verano.", "answers": [["íbamos"]], "options": ["íbamos", "fuimos", "vamos"], "explanation": "Hábito repetido en el pasado: imperfecto irregular de ir."},
             ]},
            {"id": "a2pim-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "a2pim4", "statement": "El imperfecto tiene solo tres verbos irregulares: ser, ir y ver.", "answer": True, "explanation": "Es uno de los tiempos más regulares del español; todos los demás verbos siguen el patrón regular."},
                {"id": "a2pim5", "statement": "El imperfecto se usa principalmente para narrar hechos puntuales y terminados.", "answer": False, "explanation": "Ese es el uso del pretérito indefinido; el imperfecto describe, da contexto o habla de hábitos."},
             ]},
            {"id": "a2pim-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2pim6", "incorrect": "Cuando yo fui joven, viví en Madrid.", "answer": ["Cuando yo era joven, vivía en Madrid."], "explanation": "Ambas ideas describen un estado prolongado del pasado, así que se usa el imperfecto."},
             ]},
        ],
        "summary": [
            "El imperfecto de -ar termina en -aba/-abas/-aba/-ábamos/-abais/-aban; el de -er/-ir en -ía/-ías/-ía/-íamos/-íais/-ían.",
            "Solo tres verbos son irregulares en imperfecto: ser (era...), ir (iba...) y ver (veía...).",
            "Se usa para describir el pasado, hablar de hábitos repetidos y dar el fondo o contexto de una historia.",
        ],
    },
    {
        "id": "a2-indefinido-vs-imperfecto",
        "level": "A2", "unit": "1", "order": 5, "skill": "grammar", "strand": "pasado",
        "title": "Indefinido vs. Imperfecto",
        "subtitle": "Cómo elegir entre los dos pasados básicos del español según la función de cada frase.",
        "objectives": [
            "Explicar la diferencia funcional entre el pretérito indefinido y el imperfecto",
            "Combinar los dos tiempos en una misma historia con naturalidad",
            "Reconocer los marcadores de tiempo que suelen acompañar a cada uno",
        ],
        "content": {
            "intro": "Este es uno de los puntos más importantes de todo el curso: los dos pasados del español no compiten entre sí, cumplen funciones distintas y muchas veces aparecen juntos en la misma frase.",
            "explanation": "<p>Piensa en una historia como una película: el <strong>imperfecto</strong> es el decorado, la escena de fondo — cómo era el lugar, qué tiempo hacía, qué estaba pasando. El <strong>indefinido</strong> es la acción que interrumpe esa escena — el hecho puntual que avanza la historia.</p><p>Una misma frase puede combinar ambos: <em>Yo dormía (imperfecto: la escena de fondo) cuando sonó el teléfono (indefinido: el hecho puntual que interrumpe)</em>. Elegir el tiempo equivocado cambia por completo el significado de la frase, así que esta distinción merece práctica constante.</p>",
            "rules": [
                {"heading": "a) Usa el indefinido cuando...", "body": "<ul><li>Cuentas una serie de hechos completos: <em>Me levanté, desayuné y salí.</em></li><li>Hay un marcador de tiempo cerrado: <em>ayer, el año pasado, en 2015</em></li><li>El hecho tiene un principio y un final claros dentro de la historia</li></ul>"},
                {"heading": "b) Usa el imperfecto cuando...", "body": "<ul><li>Describes personas, lugares o el clima: <em>Hacía sol y el cielo estaba despejado.</em></li><li>Hablas de hábitos o rutinas: <em>Todos los días desayunaba café con leche.</em></li><li>Describes una acción en curso que es interrumpida por otra: <em>Cocinaba cuando llegaron mis amigos.</em></li></ul>"},
                {"heading": "c) Los dos juntos en la misma historia", "body": "<p><em>Eran las diez de la noche (imperfecto: escena) y llovía mucho (imperfecto: escena) cuando alguien llamó a la puerta (indefinido: hecho puntual). Me levanté (indefinido) y abrí (indefinido) con cuidado.</em></p>"},
            ],
            "examples": [
                "Cuando llegué a casa, mis padres veían la televisión.",
                "Hacía mucho calor el día que nos conocimos.",
                "Estudiaba tranquilamente cuando se cortó la luz.",
                "El accidente ocurrió mientras cruzaba la calle.",
                "De pequeño, jugaba al fútbol todos los fines de semana, pero ayer no jugué.",
                "Ella dormía profundamente cuando sonó la alarma.",
                "Vivíamos en Sevilla cuando nació mi hermano menor.",
                "Mientras cenábamos, alguien tocó el timbre dos veces.",
            ],
            "commonMistakes": [
                {"wrong": "Cuando yo era niño, viajé a Francia cinco veces.", "right": "Cuando era niño, viajé a Francia cinco veces.", "why": "\"Cuando yo era niño\" describe una etapa (imperfecto); \"viajé cinco veces\" cuenta un hecho puntual y contable, así que va en indefinido — la combinación es correcta tal como está, pero conviene notar que ambos verbos cumplen funciones distintas dentro de la misma frase."},
                {"wrong": "Mientras cociné, sonó el teléfono.", "right": "Mientras cocinaba, sonó el teléfono.", "why": "La acción en curso interrumpida (cocinar) va en imperfecto; el hecho puntual que interrumpe (sonó) va en indefinido."},
                {"wrong": "Ayer hacía mucho sol, así que fuimos a la playa.", "right": "Ayer hacía mucho sol, así que fuimos a la playa. (correcta, pero cuidado con...)", "why": "Aquí hacía describe el clima como escena de fondo y fuimos es el hecho puntual: la combinación es correcta, precisamente el patrón que hay que dominar."},
            ],
        },
        "exercises": [
            {"id": "a2iv-fill", "type": "fill-blank", "title": "Elige el Tiempo Correcto",
             "items": [
                {"id": "a2iv1", "prompt": "___ (Yo - caminar) por el parque cuando ___ (empezar) a llover.", "answers": [["Caminaba"], ["empezó"]], "options": ["Caminaba", "empezó"], "explanation": "Acción en curso (caminaba, imperfecto) interrumpida por un hecho puntual (empezó, indefinido)."},
                {"id": "a2iv2", "prompt": "De joven, ella ___ (vivir) en Roma, pero el año pasado ___ (mudarse) a Barcelona.", "answers": [["vivía"], ["se mudó"]], "options": ["vivía", "se mudó"], "explanation": "Etapa prolongada del pasado (vivía, imperfecto) frente a un hecho puntual con marcador de tiempo cerrado (se mudó, indefinido)."},
             ]},
            {"id": "a2iv-mc", "type": "multiple-choice", "title": "Elige el Tiempo Correcto",
             "items": [
                {"id": "a2iv3", "prompt": "\"___ las tres de la tarde cuando llegamos al hotel.\"", "options": ["Eran", "Fueron", "Son"], "answerIndex": 0, "explanation": "Dar la hora en el pasado, como escena de fondo, siempre usa el imperfecto: eran las tres."},
                {"id": "a2iv4", "prompt": "\"Todos los domingos, mi abuela ___ un pastel.\"", "options": ["hizo", "hacía", "hace"], "answerIndex": 1, "explanation": "Un hábito repetido en el pasado (todos los domingos) se expresa con el imperfecto."},
             ]},
            {"id": "a2iv-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2iv5", "incorrect": "Yo leía un libro cuando tú llamabas por teléfono.", "answer": ["Yo leía un libro cuando tú llamaste por teléfono."], "explanation": "La acción que interrumpe (llamar) debe ir en indefinido, no en imperfecto, para marcar el hecho puntual."},
             ]},
        ],
        "summary": [
            "El imperfecto describe el fondo de la escena — cómo era, qué pasaba, qué se hacía habitualmente.",
            "El indefinido cuenta hechos puntuales y completos que avanzan la historia.",
            "Es normal combinar los dos tiempos en la misma frase: imperfecto para la acción en curso, indefinido para la que la interrumpe.",
        ],
    },
    {
        "id": "a2-futuro-simple-e-ir-a-infinitivo",
        "level": "A2", "unit": "1", "order": 6, "skill": "grammar", "strand": "futuro",
        "title": "Futuro Simple e Ir + a + Infinitivo",
        "subtitle": "Dos formas de hablar del futuro: la conjugación propia y la construcción con ir.",
        "objectives": [
            "Conjugar el futuro simple de verbos regulares e irregulares frecuentes",
            "Formar la construcción ir + a + infinitivo",
            "Distinguir cuándo se prefiere cada una de las dos formas",
        ],
        "content": {
            "intro": "El español tiene dos maneras muy vivas de hablar del futuro: una conjugación propia para cada verbo, y una construcción con el verbo ir que suena más natural en la conversación cotidiana.",
            "explanation": "<p>El <strong>futuro simple</strong> se forma añadiendo las mismas terminaciones al infinitivo completo del verbo (sin quitar -ar/-er/-ir), iguales para las tres conjugaciones. Algunos verbos frecuentes tienen una raíz irregular para el futuro, aunque las terminaciones siguen siendo las mismas.</p><p>La construcción <strong>ir + a + infinitivo</strong> (<em>voy a estudiar</em>) es mucho más frecuente en el habla cotidiana para planes cercanos o decisiones ya tomadas, mientras que el futuro simple suena algo más formal y se usa también para predicciones, promesas y suposiciones sobre el presente.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Futuro simple — hablar, comer, vivir</caption><thead><tr><th>Sujeto</th><th>hablar</th><th>comer</th><th>vivir</th></tr></thead><tbody><tr><td>yo</td><td>hablaré</td><td>comeré</td><td>viviré</td></tr><tr><td>tú</td><td>hablarás</td><td>comerás</td><td>vivirás</td></tr><tr><td>él/ella/usted</td><td>hablará</td><td>comerá</td><td>vivirá</td></tr><tr><td>nosotros/as</td><td>hablaremos</td><td>comeremos</td><td>viviremos</td></tr><tr><td>vosotros/as</td><td>hablaréis</td><td>comeréis</td><td>viviréis</td></tr><tr><td>ellos/as/ustedes</td><td>hablarán</td><td>comerán</td><td>vivirán</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Terminaciones del futuro simple (iguales para -ar/-er/-ir)", "body": "<p>-é, -ás, -á, -emos, -éis, -án — se añaden al infinitivo completo.</p>"},
                {"heading": "b) Raíces irregulares frecuentes", "body": "<ul><li><em>tener &rarr; tendr-, poner &rarr; pondr-, salir &rarr; saldr-, venir &rarr; vendr-</em></li><li><em>poder &rarr; podr-, saber &rarr; sabr-, querer &rarr; querr-</em></li><li><em>decir &rarr; dir-, hacer &rarr; har-</em></li></ul>"},
                {"heading": "c) Ir + a + infinitivo", "body": "<p>Presente de ir (voy, vas, va, vamos, vais, van) + a + infinitivo: <em>Voy a llamar a mi hermana esta tarde.</em> Se usa para planes ya decididos, sobre todo en el habla informal.</p>"},
                {"heading": "d) El futuro simple para suposiciones sobre el presente", "body": "<p><em>¿Qué hora será?</em> (no lo sé con certeza, pero calculo); <em>Tendrá unos treinta años.</em> (supongo su edad).</p>"},
            ],
            "examples": [
                "Mañana hablaré con el director de la escuela.",
                "El próximo año viviremos en otra ciudad.",
                "Ellos vendrán a la fiesta de cumpleaños seguro.",
                "Voy a estudiar toda la tarde para el examen.",
                "¿Vas a llamar a tus padres esta noche?",
                "Dentro de dos semanas tendremos las vacaciones.",
                "No sé qué haré este fin de semana todavía.",
                "¿Qué hora será? Debe de ser casi medianoche.",
            ],
            "commonMistakes": [
                {"wrong": "Yo teneré una reunión mañana.", "right": "Yo tendré una reunión mañana.", "why": "Tener tiene raíz irregular en futuro: tendr-, no la raíz regular tener-."},
                {"wrong": "Voy a hablo con mi jefe.", "right": "Voy a hablar con mi jefe.", "why": "Después de ir + a siempre va un infinitivo completo, nunca una forma conjugada."},
                {"wrong": "Nosotros hablaremos... hablaremos con él ayer.", "right": "Nosotros hablamos con él ayer.", "why": "El futuro nunca se usa para hechos ya ocurridos; ayer necesita un tiempo de pasado como el indefinido."},
            ],
        },
        "exercises": [
            {"id": "a2fs-fill", "type": "fill-blank", "title": "Completa con el Futuro Simple",
             "items": [
                {"id": "a2fs1", "prompt": "El próximo mes yo ___ (viajar) a Colombia.", "answers": [["viajaré"]], "options": ["viajaré", "viajo", "viajaba"], "explanation": "Futuro simple regular de un verbo en -ar."},
                {"id": "a2fs2", "prompt": "Nosotros ___ (tener) que estudiar mucho este semestre.", "answers": [["tendremos"]], "options": ["tendremos", "teneremos", "tenemos"], "explanation": "Tener usa la raíz irregular tendr- en futuro."},
                {"id": "a2fs3", "prompt": "Ellos ___ (poder) venir a la reunión de mañana.", "answers": [["podrán"]], "options": ["podrán", "poderán", "pueden"], "explanation": "Poder usa la raíz irregular podr- en futuro."},
             ]},
            {"id": "a2fs-mc", "type": "multiple-choice", "title": "Ir + a + Infinitivo",
             "items": [
                {"id": "a2fs4", "prompt": "¿Cuál es la forma correcta para expresar un plan cercano?", "options": ["Voy a estudiar esta tarde.", "Voy a estudio esta tarde.", "Voy estudiar esta tarde."], "answerIndex": 0, "explanation": "Ir + a siempre va seguido de un infinitivo completo."},
                {"id": "a2fs5", "prompt": "¿Qué construcción suena más natural en una conversación informal sobre un plan ya decidido?", "options": ["El futuro simple", "Ir + a + infinitivo", "El presente de subjuntivo"], "answerIndex": 1, "explanation": "Ir + a + infinitivo es más frecuente en el habla cotidiana para planes ya decididos."},
             ]},
            {"id": "a2fs-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2fs6", "incorrect": "Ellos diranán la verdad mañana.", "answer": ["Ellos dirán la verdad mañana."], "explanation": "Decir usa la raíz irregular dir- en futuro, con las terminaciones normales: dirán."},
             ]},
        ],
        "summary": [
            "El futuro simple añade -é/-ás/-á/-emos/-éis/-án al infinitivo completo; varios verbos frecuentes cambian la raíz (tendr-, podr-, dir-, har-...).",
            "Ir + a + infinitivo es la forma más natural en el habla cotidiana para planes cercanos ya decididos.",
            "El futuro simple también sirve para predicciones, promesas y suposiciones sobre el presente (¿Qué hora será?).",
        ],
    },
    {
        "id": "a2-comparativos-y-superlativos",
        "level": "A2", "unit": "1", "order": 7, "skill": "grammar", "strand": "comparativos",
        "title": "Comparativos y Superlativos",
        "subtitle": "Más...que, menos...que, tan...como, y el superlativo con el/la/los/las más.",
        "objectives": [
            "Formar comparativos de superioridad, inferioridad e igualdad",
            "Usar las formas irregulares mejor, peor, mayor y menor",
            "Formar el superlativo relativo y el superlativo absoluto con -ísimo",
        ],
        "content": {
            "intro": "Comparar dos cosas o destacar una por encima de todas las demás son operaciones muy frecuentes en cualquier idioma, y el español tiene estructuras fijas y sencillas para hacerlo.",
            "explanation": "<p>El comparativo de superioridad usa <strong>más...que</strong>, el de inferioridad <strong>menos...que</strong>, y el de igualdad <strong>tan...como</strong> (con adjetivos y adverbios) o <strong>tanto/a/os/as...como</strong> (con sustantivos). Cuatro adjetivos tienen una forma comparativa irregular que sustituye a más bueno/más malo/más grande/más pequeño.</p><p>El superlativo relativo destaca algo dentro de un grupo (<em>el más alto de la clase</em>), mientras que el superlativo absoluto con el sufijo <strong>-ísimo</strong> expresa un grado muy alto sin comparar con nada (<em>facilísimo</em>, en vez de decir muy fácil).</p>",
            "rules": [
                {"heading": "a) Comparativo de superioridad e inferioridad", "body": "<ul><li><strong>más + adjetivo/adverbio/sustantivo + que</strong>: <em>Ana es más alta que Luis.</em></li><li><strong>menos + adjetivo/adverbio/sustantivo + que</strong>: <em>Este libro es menos interesante que el otro.</em></li></ul>"},
                {"heading": "b) Comparativo de igualdad", "body": "<ul><li><strong>tan + adjetivo/adverbio + como</strong>: <em>Ella es tan simpática como su hermana.</em></li><li><strong>tanto/tanta/tantos/tantas + sustantivo + como</strong>: <em>Tengo tantos libros como tú.</em></li></ul>"},
                {"heading": "c) Comparativos irregulares", "body": "<ul><li><em>bueno &rarr; mejor</em> (no más bueno), <em>malo &rarr; peor</em> (no más malo)</li><li><em>grande &rarr; mayor</em> (edad) o más grande (tamaño), <em>pequeño &rarr; menor</em> (edad) o más pequeño (tamaño)</li></ul>"},
                {"heading": "d) Superlativos", "body": "<ul><li>Relativo: <strong>el/la/los/las (+ sustantivo) + más/menos + adjetivo + de</strong>: <em>Es la ciudad más grande del país.</em></li><li>Absoluto con -ísimo: <em>fácil &rarr; facilísimo, rápido &rarr; rapidísimo, feliz &rarr; felicísimo</em></li></ul>"},
            ],
            "examples": [
                "Mi hermano es más alto que yo, pero yo soy más rápido.",
                "Este ejercicio es menos difícil que el anterior.",
                "Ella habla tan bien inglés como francés.",
                "Tengo tantos amigos aquí como en mi ciudad natal.",
                "Este restaurante es mejor que el de la esquina.",
                "Mi hermano mayor tiene treinta años.",
                "Es la montaña más alta de toda la región.",
                "La película estuvo buenísima, mucho mejor de lo que esperaba.",
            ],
            "commonMistakes": [
                {"wrong": "Ella es más buena que su hermana.", "right": "Ella es mejor que su hermana.", "why": "Bueno tiene una forma comparativa irregular, mejor, que sustituye a más bueno."},
                {"wrong": "Tengo tanto libros como tú.", "right": "Tengo tantos libros como tú.", "why": "Tanto debe concordar en género y número con el sustantivo que acompaña: tantos libros, no tanto libros."},
                {"wrong": "Es el más alto estudiante de la clase.", "right": "Es el estudiante más alto de la clase.", "why": "En el superlativo relativo, el sustantivo va entre el artículo y más/menos, no antes del artículo."},
            ],
        },
        "exercises": [
            {"id": "a2cs-fill", "type": "fill-blank", "title": "Completa la Comparación",
             "items": [
                {"id": "a2cs1", "prompt": "Mi coche es ___ rápido ___ el tuyo. (superioridad)", "answers": [["más"], ["que"]], "options": ["más", "que"], "explanation": "Comparativo de superioridad: más + adjetivo + que."},
                {"id": "a2cs2", "prompt": "Esta ciudad es ___ tranquila ___ la capital. (igualdad)", "answers": [["tan"], ["como"]], "options": ["tan", "como"], "explanation": "Comparativo de igualdad con adjetivo: tan + adjetivo + como."},
             ]},
            {"id": "a2cs-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "a2cs3", "prompt": "¿Cuál es la forma comparativa irregular de \"malo\"?", "options": ["más malo", "peor", "menos malo"], "answerIndex": 1, "explanation": "Malo tiene la forma comparativa irregular peor."},
                {"id": "a2cs4", "prompt": "\"Este examen fue ___.\" (muy difícil, superlativo absoluto)", "options": ["más difícil", "dificilísimo", "el más difícil"], "answerIndex": 1, "explanation": "El superlativo absoluto con -ísimo expresa un grado muy alto sin comparar con nada."},
             ]},
            {"id": "a2cs-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2cs5", "incorrect": "Mi hermana es más pequeña de edad que yo.", "answer": ["Mi hermana es menor que yo."], "explanation": "Para la edad, se usa la forma irregular menor en vez de más pequeña."},
                {"id": "a2cs6", "incorrect": "Tengo tanta problemas como tú.", "answer": ["Tengo tantos problemas como tú."], "explanation": "Problema es masculino, así que la concordancia correcta es tantos, no tanta."},
             ]},
        ],
        "summary": [
            "Más...que, menos...que y tan...como/tanto...como cubren la superioridad, la inferioridad y la igualdad.",
            "Bueno, malo, grande y pequeño tienen formas comparativas irregulares: mejor, peor, mayor y menor.",
            "El superlativo relativo usa el/la/los/las + más/menos + adjetivo + de; el absoluto usa el sufijo -ísimo.",
        ],
    },
    {
        "id": "a2-verbos-con-cambio-de-raiz",
        "level": "A2", "unit": "1", "order": 8, "skill": "grammar", "strand": "verbos",
        "title": "Verbos con Cambio de Raíz",
        "subtitle": "E&rarr;ie, o&rarr;ue, e&rarr;i: la vocal de la raíz cambia cuando lleva la fuerza de la palabra.",
        "objectives": [
            "Reconocer los tres patrones de cambio de raíz (e>ie, o>ue, e>i) en presente",
            "Conjugar verbos frecuentes de cada patrón en presente de indicativo",
            "Explicar por qué nosotros y vosotros no cambian la raíz",
        ],
        "content": {
            "intro": "Muchos verbos muy comunes cambian una vocal de su raíz cuando esa sílaba lleva la fuerza de la palabra — no son irregulares al azar, siguen un patrón predecible una vez que lo conoces.",
            "explanation": "<p>Estos verbos cambian la última vocal de la raíz solo quando esa sílaba recibe la fuerza de pronunciación, es decir, en todas las personas <strong>excepto nosotros y vosotros</strong> (donde la fuerza cae en la terminación, no en la raíz). Hay tres patrones principales: <strong>e&rarr;ie</strong> (querer &rarr; quiero), <strong>o&rarr;ue</strong> (poder &rarr; puedo) y <strong>e&rarr;i</strong>, este último solo en verbos terminados en -ir (pedir &rarr; pido).</p><p>Fuera de ese cambio de vocal, estos verbos usan las terminaciones normales de su conjugación (-ar, -er, -ir), así que una vez identificado el patrón, el resto de la conjugación es totalmente regular.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Cambio de raíz — querer (e&rarr;ie), poder (o&rarr;ue), pedir (e&rarr;i)</caption><thead><tr><th>Sujeto</th><th>querer</th><th>poder</th><th>pedir</th></tr></thead><tbody><tr><td>yo</td><td>quiero</td><td>puedo</td><td>pido</td></tr><tr><td>tú</td><td>quieres</td><td>puedes</td><td>pides</td></tr><tr><td>él/ella/usted</td><td>quiere</td><td>puede</td><td>pide</td></tr><tr><td>nosotros/as</td><td>queremos</td><td>podemos</td><td>pedimos</td></tr><tr><td>vosotros/as</td><td>queréis</td><td>podéis</td><td>pedís</td></tr><tr><td>ellos/as/ustedes</td><td>quieren</td><td>pueden</td><td>piden</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) E&rarr;IE", "body": "<p><em>querer, pensar, cerrar, empezar, entender, preferir, sentir</em> — <em>Pienso que tienes razón. Cierro la puerta con cuidado.</em></p>"},
                {"heading": "b) O&rarr;UE", "body": "<p><em>poder, dormir, volver, contar, encontrar, jugar (u&rarr;ue)</em> — <em>Duermo ocho horas cada noche. Juego al tenis los sábados.</em></p>"},
                {"heading": "c) E&rarr;I (solo verbos en -ir)", "body": "<p><em>pedir, servir, repetir, seguir, vestir</em> — <em>Pido un café todas las mañanas. Sigo estudiando después de clase.</em></p>"},
                {"heading": "d) Nosotros y vosotros no cambian", "body": "<p>En estas dos personas, la fuerza cae en la terminación, no en la raíz, así que la vocal se mantiene sin cambio: <em>queremos, podemos, pedimos</em> (no quieremos, puedemos, pidemos).</p>"},
            ],
            "examples": [
                "Prefiero el té al café por las mañanas.",
                "Ella nunca entiende bien las instrucciones al principio.",
                "Nosotros preferimos quedarnos en casa este fin de semana.",
                "¿Cuántas horas duermes normalmente cada noche?",
                "Encuentro este ejercicio bastante difícil.",
                "Ellos juegan al fútbol todos los domingos.",
                "Yo siempre pido lo mismo en ese restaurante.",
                "Vosotros seguís las mismas reglas que nosotros.",
            ],
            "commonMistakes": [
                {"wrong": "Nosotros queremos... nosotros quieremos ir al cine.", "right": "Nosotros queremos ir al cine.", "why": "Nosotros no cambia la raíz porque la fuerza cae en la terminación: queremos, no quieremos."},
                {"wrong": "Yo pedo un café, por favor.", "right": "Yo pido un café, por favor.", "why": "Pedir cambia e por i en la raíz cuando lleva la fuerza: pido, no pedo."},
                {"wrong": "Ella dorme ocho horas.", "right": "Ella duerme ocho horas.", "why": "Dormir cambia o por ue cuando la raíz lleva la fuerza: duerme, no dorme."},
            ],
        },
        "exercises": [
            {"id": "a2cr-fill", "type": "fill-blank", "title": "Conjuga el Verbo con Cambio de Raíz",
             "items": [
                {"id": "a2cr1", "prompt": "Yo ___ (querer) aprender español muy bien.", "answers": [["quiero"]], "options": ["quiero", "quero", "queremos"], "explanation": "Querer cambia e por ie: quiero."},
                {"id": "a2cr2", "prompt": "¿Tú ___ (poder) ayudarme con esto?", "answers": [["puedes"]], "options": ["puedes", "podes", "podéis"], "explanation": "Poder cambia o por ue: puedes."},
                {"id": "a2cr3", "prompt": "Nosotros ___ (pedir) siempre el mismo plato.", "answers": [["pedimos"]], "options": ["pedimos", "pidemos", "piden"], "explanation": "Nosotros no cambia la raíz: pedimos, no pidemos."},
             ]},
            {"id": "a2cr-mc", "type": "multiple-choice", "title": "Identifica el Patrón",
             "items": [
                {"id": "a2cr4", "prompt": "\"Duermo\" pertenece al patrón...", "options": ["e&rarr;ie", "o&rarr;ue", "e&rarr;i"], "answerIndex": 1, "explanation": "Dormir cambia la o de la raíz por ue: duermo."},
                {"id": "a2cr5", "prompt": "\"Sirve\" pertenece al patrón...", "options": ["e&rarr;ie", "o&rarr;ue", "e&rarr;i"], "answerIndex": 2, "explanation": "Servir cambia la e de la raíz por i, patrón exclusivo de verbos en -ir."},
             ]},
            {"id": "a2cr-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2cr6", "incorrect": "Vosotros quieréis mucho a vuestra familia.", "answer": ["Vosotros queréis mucho a vuestra familia."], "explanation": "Vosotros no cambia la raíz: queréis, no quieréis."},
             ]},
        ],
        "summary": [
            "Los verbos con cambio de raíz cambian una vocal (e>ie, o>ue, e>i) solo en las formas donde la raíz lleva la fuerza de la palabra.",
            "Nosotros y vosotros nunca cambian la raíz, porque en esas formas la fuerza cae en la terminación.",
            "E>i es un patrón exclusivo de verbos terminados en -ir, como pedir, servir y repetir.",
        ],
    },
    {
        "id": "a2-pronombres-de-objeto-directo",
        "level": "A2", "unit": "1", "order": 9, "skill": "grammar", "strand": "pronombres",
        "title": "Pronombres de Objeto Directo",
        "subtitle": "Lo, la, los, las: sustituyen a la cosa o persona directamente afectada por la acción.",
        "objectives": [
            "Identificar el objeto directo de una frase",
            "Sustituir el objeto directo por el pronombre correspondiente (lo, la, los, las)",
            "Colocar correctamente el pronombre antes del verbo conjugado o pegado al infinitivo/gerundio",
        ],
        "content": {
            "intro": "Repetir el mismo sustantivo una y otra vez suena artificial en cualquier idioma — el pronombre de objeto directo permite sustituirlo una vez que ya quedó claro de qué se habla.",
            "explanation": "<p>El objeto directo es la persona o cosa que recibe directamente la acción del verbo: en <em>Compré el libro</em>, <strong>el libro</strong> es el objeto directo. Los pronombres <strong>lo, la, los, las</strong> concuerdan en género y número con el sustantivo que sustituyen, no con quien habla.</p><p>La posición depende de la forma verbal: con un verbo conjugado, el pronombre va <strong>antes</strong> (<em>Lo compré</em>); con un infinitivo o un gerundio, puede ir antes del verbo conjugado o pegado al final del infinitivo/gerundio (<em>Lo voy a comprar</em> / <em>Voy a comprarlo</em>); con un imperativo afirmativo, siempre va pegado al final (<em>Cómpralo</em>).</p>",
            "rules": [
                {"heading": "a) Las cuatro formas", "body": "<ul><li><strong>lo</strong> — masculino singular: <em>¿El libro? Lo tengo aquí.</em></li><li><strong>la</strong> — femenino singular: <em>¿La tarea? La terminé anoche.</em></li><li><strong>los</strong> — masculino plural: <em>¿Los boletos? Los compré ayer.</em></li><li><strong>las</strong> — femenino plural: <em>¿Las llaves? Las dejé en la mesa.</em></li></ul>"},
                {"heading": "b) Posición con verbo conjugado", "body": "<p>El pronombre va inmediatamente antes del verbo: <em>Lo veo todos los días.</em></p>"},
                {"heading": "c) Posición con infinitivo o gerundio", "body": "<p>Dos posiciones posibles, ambas correctas: <em>Lo quiero ver</em> / <em>Quiero verlo</em>; <em>Lo estoy viendo</em> / <em>Estoy viéndolo</em> (nota la tilde añadida al pegar el pronombre al gerundio).</p>"},
                {"heading": "d) Posición con imperativo afirmativo", "body": "<p>Siempre pegado al final del verbo: <em>Cómpralo. Hazlo ahora. Ábrela con cuidado.</em></p>"},
            ],
            "examples": [
                "¿Tienes las llaves? Sí, las tengo en el bolsillo.",
                "Compré el pan esta mañana y ya lo comí todo.",
                "¿Has visto mi teléfono? No, no lo he visto.",
                "Vamos a preparar la cena juntos, la vamos a preparar ahora.",
                "Estoy leyendo un libro muy interesante, lo estoy disfrutando mucho.",
                "Necesito los documentos; ¿puedes traérmelos, por favor?",
                "La profesora explica la lección y todos la entendemos bien.",
                "Termina la tarea antes de salir, termínala ya.",
            ],
            "commonMistakes": [
                {"wrong": "Veo lo todos los días.", "right": "Lo veo todos los días.", "why": "Con un verbo conjugado, el pronombre de objeto directo va antes del verbo, no después."},
                {"wrong": "¿Las llaves? Los tengo aquí.", "right": "¿Las llaves? Las tengo aquí.", "why": "El pronombre debe concordar en género con llaves (femenino), así que es las, no los."},
                {"wrong": "Cómpra lo mañana.", "right": "Cómpralo mañana.", "why": "Con el imperativo afirmativo, el pronombre se escribe pegado al verbo, sin espacio, formando una sola palabra."},
            ],
        },
        "exercises": [
            {"id": "a2od-fill", "type": "fill-blank", "title": "Sustituye por el Pronombre Correcto",
             "items": [
                {"id": "a2od1", "prompt": "¿Tienes el pasaporte? Sí, ___ tengo en el bolso.", "answers": [["lo"]], "options": ["lo", "la", "los"], "explanation": "Pasaporte es masculino singular: lo."},
                {"id": "a2od2", "prompt": "¿Compraste las entradas? Sí, ___ compré ayer.", "answers": [["las"]], "options": ["lo", "la", "las"], "explanation": "Entradas es femenino plural: las."},
                {"id": "a2od3", "prompt": "Necesito el informe; voy a terminar___ esta noche.", "answers": [["lo"]], "options": ["lo", "la", "le"], "explanation": "Informe es masculino singular; con el infinitivo, el pronombre puede ir pegado al final: terminarlo."},
             ]},
            {"id": "a2od-mc", "type": "multiple-choice", "title": "Elige la Posición Correcta",
             "items": [
                {"id": "a2od4", "prompt": "¿Cuál es la forma correcta con el imperativo?", "options": ["Lo hazlo ahora.", "Hazlo ahora.", "Haz lo ahora."], "answerIndex": 1, "explanation": "Con el imperativo afirmativo, el pronombre siempre va pegado al final del verbo."},
                {"id": "a2od5", "prompt": "¿Cuál de estas dos frases es también correcta junto a \"Lo voy a comprar\"?", "options": ["Voy a comprarlo.", "Voy a lo comprar.", "Voy comprarlo a."], "answerIndex": 0, "explanation": "Con infinitivo, el pronombre puede ir antes del verbo conjugado o pegado al infinitivo: ambas son correctas."},
             ]},
            {"id": "a2od-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2od6", "incorrect": "Necesito ayuda con la tarea, ¿puedes ayudar me con lo?", "answer": ["Necesito ayuda con la tarea, ¿puedes ayudarme con ella?"], "explanation": "Tarea es femenina, así que el pronombre correcto es la/ella, no lo; además me se pega directamente al infinitivo."},
             ]},
        ],
        "summary": [
            "Lo, la, los, las sustituyen al objeto directo y concuerdan en género y número con el sustantivo que reemplazan.",
            "Con un verbo conjugado, el pronombre va antes; con infinitivo o gerundio hay dos posiciones posibles; con el imperativo afirmativo, siempre va pegado al final.",
            "El pronombre nunca concuerda con quien habla, sino con la cosa o persona sustituida.",
        ],
    },
    {
        "id": "a2-pronombres-de-objeto-indirecto",
        "level": "A2", "unit": "1", "order": 10, "skill": "grammar", "strand": "pronombres",
        "title": "Pronombres de Objeto Indirecto",
        "subtitle": "Me, te, le, nos, os, les: a quién o para quién se dirige la acción.",
        "objectives": [
            "Identificar el objeto indirecto de una frase",
            "Usar los pronombres me, te, le, nos, os, les correctamente",
            "Reconocer verbos frecuentes que casi siempre llevan objeto indirecto (dar, decir, gustar, escribir)",
        ],
        "content": {
            "intro": "El objeto indirecto indica a quién o para quién se hace algo — la persona que recibe el beneficio, el daño o la información de la acción, aunque no sea lo que se da o se dice directamente.",
            "explanation": "<p>En <em>Le doy el libro a mi hermano</em>, <strong>el libro</strong> es el objeto directo (lo que se da) y <strong>a mi hermano</strong> es el objeto indirecto (a quién se le da). Los pronombres <strong>me, te, le, nos, os, les</strong> sustituyen a ese destinatario, y a diferencia de los pronombres de objeto directo, no cambian según el género — solo según la persona.</p><p>Una particularidad muy frecuente del español es repetir el pronombre incluso cuando el destinatario ya aparece nombrado con <em>a</em>: <em>Le doy el libro a mi hermano</em> es la forma natural, no una redundancia que deba evitarse. Verbos como <strong>gustar, encantar, parecer, doler</strong> funcionan siempre con objeto indirecto, no con sujeto en primera persona.</p>",
            "rules": [
                {"heading": "a) Las seis formas", "body": "<ul><li><strong>me</strong> — a mí</li><li><strong>te</strong> — a ti</li><li><strong>le</strong> — a él/ella/usted</li><li><strong>nos</strong> — a nosotros/as</li><li><strong>os</strong> — a vosotros/as</li><li><strong>les</strong> — a ellos/ellas/ustedes</li></ul>"},
                {"heading": "b) Duplicación con \"a + persona\"", "body": "<p>Es normal, casi obligatorio, mantener el pronombre aunque ya se mencione a quién: <em>Le escribí una carta a mi abuela.</em> No es un error de redundancia, es la estructura habitual del español.</p>"},
                {"heading": "c) Verbos que siempre llevan objeto indirecto", "body": "<ul><li><em>Me gusta el chocolate.</em> (no \"yo gusto\")</li><li><em>Le duele la cabeza.</em></li><li><em>Nos parece una buena idea.</em></li><li><em>Les encanta viajar.</em></li></ul>"},
                {"heading": "d) Posición", "body": "<p>Las mismas reglas que el objeto directo: antes del verbo conjugado, o pegado al infinitivo/gerundio/imperativo afirmativo — <em>Le voy a escribir</em> / <em>Voy a escribirle</em>; <em>Escríbele pronto.</em></p>"},
            ],
            "examples": [
                "Le mandé un mensaje a mi jefe esta mañana.",
                "¿Me puedes explicar esta parte de la lección?",
                "Les dimos las gracias por su ayuda.",
                "Nos parece una idea excelente para el proyecto.",
                "Te escribo pronto con más detalles del viaje.",
                "A ella le encanta la música clásica.",
                "¿Os gusta el plan que preparamos para el sábado?",
                "Le duele mucho la espalda desde ayer.",
            ],
            "commonMistakes": [
                {"wrong": "Yo gusto el chocolate.", "right": "Me gusta el chocolate.", "why": "Gustar funciona al revés que en otros idiomas: la persona es el objeto indirecto (me), y el sujeto gramatical es lo que gusta (el chocolate)."},
                {"wrong": "Escribí una carta a mi abuela.", "right": "Le escribí una carta a mi abuela.", "why": "El español mantiene el pronombre le aunque ya se mencione a quién con \"a mi abuela\"; es la estructura natural, no una redundancia."},
                {"wrong": "Les gusta a ellos el fútbol.", "right": "A ellos les gusta el fútbol. / Les gusta el fútbol.", "why": "El pronombre les es obligatorio; \"a ellos\" es opcional y solo se añade para dar énfasis o claridad, sin sustituir al pronombre."},
            ],
        },
        "exercises": [
            {"id": "a2oi-fill", "type": "fill-blank", "title": "Completa con el Pronombre de Objeto Indirecto",
             "items": [
                {"id": "a2oi1", "prompt": "A mí ___ gusta mucho leer novelas.", "answers": [["me"]], "options": ["me", "le", "te"], "explanation": "A mí corresponde el pronombre me."},
                {"id": "a2oi2", "prompt": "A ellos ___ encanta viajar por Sudamérica.", "answers": [["les"]], "options": ["les", "le", "nos"], "explanation": "A ellos corresponde el pronombre les."},
                {"id": "a2oi3", "prompt": "___ escribí un correo a mi profesora ayer.", "answers": [["Le"]], "options": ["Le", "La", "Lo"], "explanation": "Profesora es el destinatario (a quién), así que se usa el pronombre de objeto indirecto le, no la de objeto directo."},
             ]},
            {"id": "a2oi-mc", "type": "multiple-choice", "title": "Elige el Pronombre Correcto",
             "items": [
                {"id": "a2oi4", "prompt": "\"___ duele la cabeza a mi hermana.\"", "options": ["La", "Le", "Lo"], "answerIndex": 1, "explanation": "Doler funciona como gustar: la persona afectada es el objeto indirecto, le."},
                {"id": "a2oi5", "prompt": "¿Cuál es la forma correcta para \"a nosotros\"?", "options": ["nos", "os", "les"], "answerIndex": 0, "explanation": "A nosotros corresponde el pronombre nos."},
             ]},
            {"id": "a2oi-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2oi6", "incorrect": "Yo gusto mucho el café por las mañanas.", "answer": ["Me gusta mucho el café por las mañanas."], "explanation": "Gustar requiere el pronombre de objeto indirecto me; el sujeto gramatical es el café, no yo."},
             ]},
        ],
        "summary": [
            "Los pronombres de objeto indirecto (me, te, le, nos, os, les) indican a quién o para quién se dirige la acción.",
            "El español suele mantener el pronombre aunque el destinatario ya se mencione con a + persona.",
            "Verbos como gustar, encantar, parecer y doler siempre usan objeto indirecto: la persona nunca es el sujeto gramatical.",
        ],
    },
    {
        "id": "a2-imperativo-afirmativo",
        "level": "A2", "unit": "1", "order": 11, "skill": "grammar", "strand": "imperativo",
        "title": "Imperativo Afirmativo (Tú/Usted)",
        "subtitle": "Cómo dar órdenes, instrucciones y consejos de forma directa y afirmativa.",
        "objectives": [
            "Formar el imperativo afirmativo regular de tú y usted",
            "Reconocer los imperativos irregulares más frecuentes de tú",
            "Añadir pronombres de objeto correctamente al imperativo afirmativo",
        ],
        "content": {
            "intro": "El imperativo afirmativo sirve para pedir, mandar, aconsejar o instruir directamente a alguien — su forma cambia según se hable de tú (informal) o de usted (formal).",
            "explanation": "<p>Para <strong>tú</strong>, el imperativo afirmativo regular coincide con la forma de <em>él/ella</em> del presente de indicativo: <em>habla, come, escribe</em>. Sin embargo, ocho verbos muy frecuentes tienen una forma irregular corta que hay que memorizar aparte.</p><p>Para <strong>usted</strong>, el imperativo afirmativo usa la misma forma que el presente de subjuntivo (se estudiará en detalle más adelante), que en la práctica significa: para verbos en -ar, cambia la -a final por -e; para verbos en -er/-ir, cambia la -e/-o final por -a.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Imperativo afirmativo — tú y usted</caption><thead><tr><th>Verbo</th><th>tú</th><th>usted</th></tr></thead><tbody><tr><td>hablar</td><td>habla</td><td>hable</td></tr><tr><td>comer</td><td>come</td><td>coma</td></tr><tr><td>escribir</td><td>escribe</td><td>escriba</td></tr><tr><td>decir</td><td>di</td><td>diga</td></tr><tr><td>hacer</td><td>haz</td><td>haga</td></tr><tr><td>poner</td><td>pon</td><td>ponga</td></tr><tr><td>ir</td><td>ve</td><td>vaya</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Tú regular", "body": "<p>Coincide con la forma de él/ella del presente: <em>Habla más despacio, por favor. Come toda la verdura. Escribe tu nombre aquí.</em></p>"},
                {"heading": "b) Los ocho irregulares de tú", "body": "<p><em>decir&rarr;di, hacer&rarr;haz, ir&rarr;ve, poner&rarr;pon, salir&rarr;sal, ser&rarr;sé, tener&rarr;ten, venir&rarr;ven</em></p>"},
                {"heading": "c) Usted", "body": "<p>Verbos en -ar cambian a -e; verbos en -er/-ir cambian a -a: <em>Hable más despacio, por favor. Coma toda la verdura. Escriba su nombre aquí.</em></p>"},
                {"heading": "d) Pronombres pegados al final", "body": "<p>Con el imperativo afirmativo, los pronombres de objeto directo, indirecto y reflexivos siempre van pegados al final del verbo, formando una sola palabra: <em>Levántate. Cómelo. Escríbeme pronto.</em></p>"},
            ],
            "examples": [
                "Abre la ventana, por favor, hace mucho calor aquí.",
                "Ten paciencia, todo va a salir bien.",
                "Señor García, siéntese aquí, por favor.",
                "Ven aquí un momento, necesito tu ayuda.",
                "Haga el favor de esperar unos minutos.",
                "Escríbeme cuando llegues a casa esta noche.",
                "Pon la mesa antes de que lleguen los invitados.",
                "Levántese temprano mañana, tenemos mucho que hacer.",
            ],
            "commonMistakes": [
                {"wrong": "Hace la tarea ahora mismo.", "right": "Haz la tarea ahora mismo.", "why": "El imperativo de tú de hacer es la forma irregular haz, no hace (que es la forma de él/ella del presente)."},
                {"wrong": "Sientese aquí, por favor.", "right": "Siéntese aquí, por favor.", "why": "Al pegar el pronombre reflexivo al imperativo, se añade una tilde para mantener la fuerza original de la palabra: siéntese."},
                {"wrong": "Escribeme cuando llegues.", "right": "Escríbeme cuando llegues.", "why": "Al pegar el pronombre me al imperativo escribe, se necesita tilde para mantener la fuerza en la í: escríbeme."},
            ],
        },
        "exercises": [
            {"id": "a2ia-fill", "type": "fill-blank", "title": "Completa con el Imperativo Afirmativo",
             "items": [
                {"id": "a2ia1", "prompt": "___ (Tú - hacer) la cama antes de salir.", "answers": [["Haz"]], "options": ["Haz", "Hace", "Haces"], "explanation": "Hacer tiene imperativo de tú irregular: haz."},
                {"id": "a2ia2", "prompt": "Señora Pérez, ___ (usted - comer) despacio, por favor.", "answers": [["coma"]], "options": ["coma", "come", "comé"], "explanation": "Usted + verbo en -er = terminación -a: coma."},
                {"id": "a2ia3", "prompt": "___ (Tú - ir) a la tienda y compra pan.", "answers": [["Ve"]], "options": ["Ve", "Va", "Vas"], "explanation": "Ir tiene imperativo de tú irregular: ve."},
             ]},
            {"id": "a2ia-mc", "type": "multiple-choice", "title": "Elige el Imperativo Correcto",
             "items": [
                {"id": "a2ia4", "prompt": "¿Cómo le dices a un amigo que se siente aquí?", "options": ["Siéntate aquí.", "Siéntese aquí.", "Sentarse aquí."], "answerIndex": 0, "explanation": "Con tú se usa la forma informal siéntate, con el reflexivo pegado al final."},
                {"id": "a2ia5", "prompt": "¿Cuál es la forma de usted del imperativo de \"escribir\"?", "options": ["escribe", "escriba", "escribí"], "answerIndex": 1, "explanation": "Usted + verbo en -ir = terminación -a: escriba."},
             ]},
            {"id": "a2ia-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2ia6", "incorrect": "Pone la mesa, por favor.", "answer": ["Pon la mesa, por favor."], "explanation": "Poner tiene imperativo de tú irregular: pon, no pone."},
             ]},
        ],
        "summary": [
            "El imperativo afirmativo de tú regular coincide con la forma de él/ella del presente; ocho verbos frecuentes tienen forma irregular corta (di, haz, ve, pon, sal, sé, ten, ven).",
            "El imperativo de usted cambia la vocal final: -ar pasa a -e, -er/-ir pasan a -a.",
            "Los pronombres siempre se pegan al final del imperativo afirmativo, y a menudo se añade una tilde para conservar la fuerza original de la palabra.",
        ],
    },
    {
        "id": "a2-adverbios-de-frecuencia-y-conectores",
        "level": "A2", "unit": "1", "order": 12, "skill": "vocabulary", "strand": "conectores",
        "title": "Adverbios de Frecuencia y Conectores Básicos",
        "subtitle": "Siempre, a veces, nunca; y, pero, porque, entonces: para hablar de rutinas y encadenar ideas.",
        "objectives": [
            "Usar adverbios de frecuencia para describir hábitos y rutinas",
            "Ordenar adverbios de frecuencia de mayor a menor frecuencia",
            "Encadenar ideas simples con conectores básicos (y, pero, porque, entonces, además)",
        ],
        "content": {
            "intro": "Los adverbios de frecuencia dicen con qué regularidad ocurre algo, y los conectores básicos permiten unir frases sueltas en un discurso que fluye de manera natural.",
            "explanation": "<p>Los adverbios de frecuencia se colocan normalmente antes del verbo principal (<em>siempre desayuno</em>) o al final de la frase (<em>desayuno siempre</em>), salvo <strong>nunca</strong>, que puede ir antes del verbo sin necesitar ninguna otra negación (<em>Nunca como carne</em>), o después del verbo, en cuyo caso sí se necesita <strong>no</strong> antes del verbo (<em>No como carne nunca</em>).</p><p>Los conectores básicos organizan la relación lógica entre dos ideas: <strong>y</strong> suma, <strong>pero</strong> contrasta, <strong>porque</strong> explica una causa, <strong>entonces</strong>/<strong>por eso</strong> indica una consecuencia, y <strong>además</strong> añade información nueva a favor de la misma idea.</p>",
            "rules": [
                {"heading": "a) Escala de frecuencia (de más a menos)", "body": "<p><em>siempre &gt; casi siempre &gt; normalmente/generalmente &gt; a veces &gt; casi nunca &gt; nunca</em></p>"},
                {"heading": "b) Posición de los adverbios de frecuencia", "body": "<ul><li>Antes del verbo: <em>Siempre llego temprano.</em></li><li>Al final de la frase: <em>Llego temprano siempre.</em></li><li>Nunca antes del verbo no necesita no: <em>Nunca llego tarde.</em> Después del verbo sí lo necesita: <em>No llego tarde nunca.</em></li></ul>"},
                {"heading": "c) Conectores de suma y contraste", "body": "<ul><li><strong>y</strong>: <em>Estudio español y trabajo por las tardes.</em></li><li><strong>pero</strong>: <em>Me gusta el café, pero prefiero el té por la noche.</em></li></ul>"},
                {"heading": "d) Conectores de causa y consecuencia", "body": "<ul><li><strong>porque</strong> (causa): <em>Llego tarde porque hay mucho tráfico.</em></li><li><strong>entonces / por eso</strong> (consecuencia): <em>Hay mucho tráfico, entonces llego tarde.</em></li><li><strong>además</strong> (información adicional): <em>El piso es grande y, además, está muy bien situado.</em></li></ul>"},
            ],
            "examples": [
                "Siempre desayuno antes de salir de casa.",
                "A veces voy al gimnasio después del trabajo.",
                "Casi nunca como comida rápida entre semana.",
                "Estudio mucho, pero todavía cometo muchos errores.",
                "No hablo francés, porque nunca lo estudié en la escuela.",
                "Llovió toda la noche, entonces cancelamos el partido.",
                "El hotel es cómodo y, además, está muy bien situado.",
                "Nunca llego tarde a mis clases de español.",
            ],
            "commonMistakes": [
                {"wrong": "No siempre como carne.", "right": "Nunca como carne. / No como carne nunca.", "why": "\"No siempre\" significa \"a veces sí, a veces no\", un significado distinto del que se buscaba (nunca), que expresa frecuencia cero."},
                {"wrong": "Estudio mucho pero yo aprendo rápido.", "right": "Estudio mucho, pero aprendo rápido.", "why": "En español, después de pero, no suele repetirse el pronombre de sujeto si ya está claro por el contexto."},
                {"wrong": "Llego tarde entonces hay mucho tráfico.", "right": "Llego tarde porque hay mucho tráfico.", "why": "Porque introduce la causa; entonces introduce la consecuencia — el orden lógico aquí es al revés."},
            ],
        },
        "exercises": [
            {"id": "a2af-mc", "type": "multiple-choice", "title": "Elige el Conector Correcto",
             "items": [
                {"id": "a2af1", "prompt": "\"Estudio mucho, ___ todavía cometo errores.\"", "options": ["y", "pero", "porque"], "answerIndex": 1, "explanation": "Pero introduce un contraste entre las dos ideas."},
                {"id": "a2af2", "prompt": "\"Llegué tarde ___ había mucho tráfico.\"", "options": ["porque", "entonces", "pero"], "answerIndex": 0, "explanation": "Porque introduce la causa del hecho anterior."},
                {"id": "a2af3", "prompt": "¿Cuál de estos adverbios indica mayor frecuencia?", "options": ["a veces", "casi nunca", "casi siempre"], "answerIndex": 2, "explanation": "Casi siempre está mucho más cerca del extremo de máxima frecuencia que las otras dos opciones."},
             ]},
            {"id": "a2af-fill", "type": "fill-blank", "title": "Completa con el Adverbio o Conector",
             "items": [
                {"id": "a2af4", "prompt": "Yo ___ (frecuencia máxima) desayuno café con pan.", "answers": [["siempre"]], "options": ["siempre", "nunca", "a veces"], "explanation": "Siempre expresa la frecuencia máxima."},
                {"id": "a2af5", "prompt": "No tengo tiempo hoy, ___ no puedo ir contigo.", "answers": [["entonces"], ["por eso"]], "options": ["entonces", "por eso", "porque"], "explanation": "Entonces/por eso introducen la consecuencia lógica de la falta de tiempo."},
             ]},
            {"id": "a2af-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "a2af6", "incorrect": "Como verduras porque, además, hago ejercicio todos los días.", "answer": ["Como verduras y, además, hago ejercicio todos los días."], "explanation": "Además añade información adicional a favor de la misma idea, no introduce una causa; el conector correcto para sumar las dos ideas es y."},
             ]},
        ],
        "summary": [
            "La escala de frecuencia va de siempre a nunca; nunca antes del verbo no necesita no, después del verbo sí lo necesita.",
            "Y suma, pero contrasta, porque explica una causa, entonces/por eso indica una consecuencia y además añade información nueva.",
            "El orden lógico entre causa y consecuencia importa: no se puede intercambiar porque por entonces sin cambiar el sentido.",
        ],
    },
]
