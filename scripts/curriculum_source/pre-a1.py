# -*- coding: utf-8 -*-
"""Pre-A1 — Datos del currículo de supervivencia total. Ver curriculum/SCHEMA.md
para la forma exacta del JSON al que esto se compila (scripts/generate_curriculum.py
hace la compilación). Se escribe como Python en vez de JSON a mano para que el
HTML en línea (rules[].body, content.explanation) y las comillas dentro del
texto se puedan escribir con naturalidad."""

OVERVIEW = ("Pre-A1 es el punto de partida absoluto: el alfabeto y los sonidos del español, "
            "los saludos y las presentaciones, los números, la hora y la fecha, el vocabulario "
            "esencial para sobrevivir en una clase, las palabras más comunes de personas y "
            "objetos cotidianos, y los primeros verbos y pronombres para formar tus primeras "
            "frases. Al terminar este nivel podrás presentarte, pedir cosas simples y entender "
            "diálogos muy cortos de la vida diaria, sin necesitar ningún conocimiento previo de "
            "español.")

LESSONS = [
    {
        "id": "pre-a1-el-alfabeto-y-los-sonidos",
        "level": "Pre-A1", "unit": "1", "order": 1, "skill": "pronunciation", "strand": "alfabeto",
        "title": "El Alfabeto y los Sonidos",
        "subtitle": "Las letras del español, la ñ, la diferencia entre rr y r, y por qué las vocales siempre suenan igual.",
        "objectives": [
            "Reconocer las letras del alfabeto español, incluida la ñ.",
            "Distinguir el sonido fuerte de la rr frente al sonido suave de una sola r.",
            "Pronunciar las cinco vocales de forma clara, corta y siempre igual.",
        ],
        "content": {
            "intro": "El español se escribe casi tal como suena, así que aprender estos sonidos básicos es el primer paso para leer, escribir y hablar con confianza.",
            "explanation": "<p>El alfabeto español tiene <strong>27 letras</strong>. Es muy parecido a otros alfabetos, pero tiene una letra propia: la <strong>ñ</strong> (como en <em>español</em> o <em>niño</em>). La ñ no es una variante de la n — es una letra independiente, con su propio sonido.</p><p>Las cinco vocales (<strong>a, e, i, o, u</strong>) tienen siempre un sonido corto y claro. No cambian nunca, en ninguna palabra. Otra diferencia importante está en la letra <strong>r</strong>: al principio de una palabra, o cuando aparece doble (<strong>rr</strong>), suena fuerte y vibrante; entre vocales, una sola r suena suave.</p>",
            "rules": [
                {"heading": "a) Las cinco vocales", "body": "<ul><li><strong>a</strong> — como en <em>casa</em></li><li><strong>e</strong> — como en <em>mesa</em></li><li><strong>i</strong> — como en <em>libro</em></li><li><strong>o</strong> — como en <em>hola</em></li><li><strong>u</strong> — como en <em>uno</em></li><li>El sonido nunca cambia, ni siquiera al final de la palabra.</li></ul>"},
                {"heading": "b) La letra ñ", "body": "<ul><li>Es una letra independiente, no una variante de la n.</li><li>Aparece en palabras muy comunes: <em>año, niño, español, mañana</em>.</li><li>En un diccionario, la ñ va después de la n.</li></ul>"},
                {"heading": "c) La r simple y la rr fuerte", "body": "<ul><li>Una sola <strong>r</strong> entre vocales suena suave — <em>pero, cara, para</em>.</li><li>La <strong>rr</strong> doble siempre suena fuerte y vibrante — <em>perro, carro, tierra</em>.</li><li>La <strong>r</strong> al principio de una palabra también suena fuerte — <em>Ramón, rosa</em>.</li></ul>"},
                {"heading": "d) Otras letras especiales", "body": "<ul><li>La <strong>h</strong> nunca suena — <em>hola, hospital, hotel</em>.</li><li>La <strong>ll</strong> tiene un sonido propio, parecido a una y — <em>llamo, calle, lluvia</em>.</li></ul>"},
            ],
            "examples": [
                "Hola, me llamo Ana.",
                "La ñ está en la palabra español.",
                "Mi perro es pequeño y bonito.",
                "Pero yo prefiero el gato.",
                "El año tiene doce meses.",
                "Ramón vive en la calle Mayor.",
                "Hoy hace mucho calor.",
            ],
            "commonMistakes": [
                {"wrong": "Pronunciar la ñ como una n normal.", "right": "Pronunciar la ñ como una letra distinta, con su propio sonido.", "why": "La ñ es una letra independiente del alfabeto español, no una variante de la n."},
                {"wrong": "Pronunciar la h en la palabra hola.", "right": "Decir hola sin ningún sonido de h.", "why": "La h es siempre muda en español; nunca se pronuncia."},
                {"wrong": "Decir pero con el sonido fuerte de la rr.", "right": "Usar el sonido suave de la r en pero, y guardar el sonido fuerte para perro.", "why": "Una sola r entre vocales suena suave; cambiar el sonido puede cambiar el significado de la palabra."},
            ],
        },
        "exercises": [
            {"id": "pa1-mc", "type": "multiple-choice", "title": "¿Qué Letra o Sonido Es?",
             "items": [
                {"id": "pa1mc1", "prompt": "¿Cuál es la letra especial del alfabeto español que no existe en el alfabeto inglés?", "options": ["ñ", "w", "k"], "answerIndex": 0, "explanation": "La ñ es una letra propia del español, con su sonido característico."},
                {"id": "pa1mc2", "prompt": "¿Cómo suena la h en la palabra hola?", "options": ["No suena, es muda", "Suena fuerte, como una j", "Suena suave, como una f"], "answerIndex": 0, "explanation": "La h nunca se pronuncia en español, en ninguna palabra."},
                {"id": "pa1mc3", "prompt": "¿Qué palabra tiene el sonido fuerte y vibrante de la rr?", "options": ["pero", "perro", "cara"], "answerIndex": 1, "explanation": "Perro tiene rr doble, con un sonido fuerte y vibrante."},
                {"id": "pa1mc4", "prompt": "¿Cómo se pronuncia la vocal o en español?", "options": ["Siempre igual, con un sonido claro", "A veces como una a", "Depende de la palabra"], "answerIndex": 0, "explanation": "Las vocales del español tienen un sonido fijo; nunca cambian."},
             ]},
            {"id": "pa1-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "pa1tf1", "statement": "La ñ es simplemente una n con un signo encima, no una letra distinta.", "answer": False, "explanation": "La ñ es una letra independiente del alfabeto, con su propio sonido y su propio lugar en el diccionario."},
                {"id": "pa1tf2", "statement": "Las vocales del español siempre suenan igual, en cualquier palabra.", "answer": True, "explanation": "A diferencia de otras lenguas, las vocales españolas mantienen siempre el mismo sonido claro."},
                {"id": "pa1tf3", "statement": "La rr doble siempre suena fuerte y vibrante.", "answer": True, "explanation": "La rr, sin excepción, tiene un sonido fuerte."},
                {"id": "pa1tf4", "statement": "La letra h se pronuncia con un sonido suave en español.", "answer": False, "explanation": "La h es siempre muda; no tiene ningún sonido."},
             ]},
            {"id": "pa1-match", "type": "matching", "title": "Empareja la Letra con su Descripción",
             "items": [
                {"id": "pa1match1", "pairs": [
                    {"left": "ñ", "right": "letra independiente, con sonido propio"},
                    {"left": "h", "right": "nunca se pronuncia"},
                    {"left": "rr", "right": "siempre suena fuerte"},
                    {"left": "ll", "right": "suena parecido a una y"},
                ], "explanation": "Cada una de estas letras o combinaciones tiene un comportamiento propio en la pronunciación del español."},
             ]},
            {"id": "pa1-fill", "type": "fill-blank", "title": "Completa con la Letra Correcta",
             "instructions": "Elige la palabra bien escrita para cada espacio.",
             "items": [
                {"id": "pa1f1", "prompt": "— ___, ¿qué tal? — Muy bien, gracias.", "answers": [["hola"]], "options": ["hola", "ola", "jola"], "explanation": "Hola empieza con h muda: no se pronuncia, pero sí se escribe."},
                {"id": "pa1f2", "prompt": "Mi ___ es pequeño y bonito.", "answers": [["perro"]], "options": ["perro", "pero", "pelo"], "explanation": "Perro se escribe con rr doble, con sonido fuerte."},
                {"id": "pa1f3", "prompt": "El ___ tiene doce meses.", "answers": [["año"]], "options": ["año", "ano", "anio"], "explanation": "Año se escribe con ñ; sin la ñ, la palabra cambia completamente de significado."},
                {"id": "pa1f4", "prompt": "Vivo en la ___ Mayor.", "answers": [["calle"]], "options": ["calle", "caye", "cale"], "explanation": "Calle se escribe con ll, un sonido parecido al de la y."},
             ]},
        ],
        "summary": [
            "El alfabeto español tiene 27 letras, incluida la ñ, que es una letra independiente.",
            "Las cinco vocales suenan siempre igual, de forma clara y corta, sin excepciones.",
            "La rr (o la r al inicio de palabra) suena fuerte; una sola r entre vocales suena suave, y la h nunca se pronuncia.",
        ],
    },
    {
        "id": "pre-a1-saludos-y-presentaciones",
        "level": "Pre-A1", "unit": "1", "order": 2, "skill": "functional", "strand": "saludos",
        "title": "Saludos y Presentaciones",
        "subtitle": "Cómo saludar, despedirte y presentarte en español — y cuándo usar tú o usted.",
        "objectives": [
            "Saludar y despedirte según el momento del día.",
            "Preguntar y decir el nombre de una persona.",
            "Elegir entre tú y usted en una primera conversación.",
        ],
        "content": {
            "intro": "Toda conversación en español empieza con un saludo, y ese saludo ya dice mucho sobre el nivel de confianza entre las dos personas.",
            "explanation": "<p>En español hay saludos para cada momento del día: <strong>buenos días</strong> (por la mañana), <strong>buenas tardes</strong> (por la tarde) y <strong>buenas noches</strong> (por la noche, y también al despedirse antes de dormir). La palabra <strong>hola</strong> 👋 funciona a cualquier hora, en situaciones formales e informales.</p><p>El español también tiene dos formas de decir «tú»: <strong>tú</strong> (informal) y <strong>usted</strong> (formal). Se usa <em>tú</em> con amigos, familia y niños; se usa <em>usted</em> con personas desconocidas, personas mayores o en situaciones de trabajo, hasta que la otra persona proponga tutear.</p>",
            "rules": [
                {"heading": "a) Saludos según el momento del día", "body": "<ul><li><strong>Buenos días</strong> — por la mañana, hasta el mediodía.</li><li><strong>Buenas tardes</strong> — desde el mediodía hasta el anochecer.</li><li><strong>Buenas noches</strong> — por la noche, para saludar o para despedirse.</li><li><strong>Hola</strong> 👋 — funciona a cualquier hora del día.</li></ul>"},
                {"heading": "b) Preguntar y decir el nombre", "body": "<ul><li>Informal: <em>¿Cómo te llamas?</em> → <em>Me llamo Marta.</em></li><li>Formal: <em>¿Cómo se llama usted?</em> → <em>Me llamo Marta.</em> (la respuesta no cambia)</li><li><em>Mucho gusto</em> — se dice al conocer a alguien por primera vez.</li></ul>"},
                {"heading": "c) Tú frente a usted", "body": "<ul><li><strong>Tú</strong> — amigos, familia, niños, personas de tu edad. <em>¿Tú de dónde eres?</em></li><li><strong>Usted</strong> — desconocidos, personas mayores, contextos formales. <em>¿Usted de dónde es?</em></li><li>En caso de duda, empieza con <em>usted</em>: es la opción más segura.</li></ul>"},
                {"heading": "d) Despedidas", "body": "<ul><li><strong>Adiós</strong> — despedida general, para cualquier momento.</li><li><strong>Hasta luego</strong> — cuando vas a ver a la persona pronto.</li><li><strong>Hasta mañana</strong> — cuando la vas a ver al día siguiente.</li></ul>"},
            ],
            "examples": [
                "Buenos días, ¿cómo está usted?",
                "¡Hola! ¿Cómo estás?",
                "Me llamo Carlos. ¿Y tú, cómo te llamas?",
                "Mucho gusto en conocerla.",
                "Buenas tardes, señor García.",
                "Estoy muy bien, gracias. ¿Y usted?",
                "Adiós, ¡hasta luego!",
                "Buenas noches, que descanses.",
            ],
            "commonMistakes": [
                {"wrong": "Hola, ¿cómo está usted?", "right": "Hola, ¿cómo estás? / Buenos días, ¿cómo está usted?", "why": "Hola es informal, así que combina mejor con estás; si usas usted, es más natural empezar con un saludo formal."},
                {"wrong": "Buenas noches (al llegar por la mañana)", "right": "Buenos días (al llegar por la mañana)", "why": "Buenas noches solo se usa por la noche, nunca como saludo de la mañana."},
                {"wrong": "¿Cómo te llama?", "right": "¿Cómo te llamas? / ¿Cómo se llama usted?", "why": "Te llamas es la forma de tú; te llama mezcla tú con una forma de usted/él/ella."},
            ],
        },
        "exercises": [
            {"id": "pa2-mc", "type": "multiple-choice", "title": "Elige el Saludo Correcto",
             "items": [
                {"id": "pa2mc1", "prompt": "Son las nueve de la mañana. ¿Qué dices?", "options": ["Buenas noches", "Buenos días", "Buenas tardes"], "answerIndex": 1, "explanation": "Buenos días se usa por la mañana, hasta el mediodía."},
                {"id": "pa2mc2", "prompt": "Conoces a un profesor por primera vez. ¿Qué pronombre usas?", "options": ["tú", "usted", "vosotros"], "answerIndex": 1, "explanation": "Con una persona desconocida, en un contexto formal, se usa usted."},
                {"id": "pa2mc3", "prompt": "Te despides de un amigo que vas a ver mañana. ¿Qué dices?", "options": ["Hasta mañana", "Buenas noches", "Mucho gusto"], "answerIndex": 0, "explanation": "Hasta mañana se usa cuando vas a ver a la persona al día siguiente."},
                {"id": "pa2mc4", "prompt": "¿Qué saludo funciona a cualquier hora del día?", "options": ["Buenas tardes", "Hola", "Buenas noches"], "answerIndex": 1, "explanation": "Hola es un saludo general que funciona en cualquier momento."},
             ]},
            {"id": "pa2-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "pa2tf1", "statement": "Se usa tú con una persona desconocida en una entrevista de trabajo.", "answer": False, "explanation": "En una entrevista de trabajo, lo normal es usar usted."},
                {"id": "pa2tf2", "statement": "Mucho gusto se dice al conocer a alguien por primera vez.", "answer": True, "explanation": "Mucho gusto es la expresión típica al presentarse."},
                {"id": "pa2tf3", "statement": "La respuesta a ¿cómo te llamas? y a ¿cómo se llama usted? es diferente.", "answer": False, "explanation": "La respuesta siempre es me llamo...; cambia la pregunta, pero no la respuesta."},
                {"id": "pa2tf4", "statement": "Buenas noches solo se usa por la noche.", "answer": True, "explanation": "Buenas noches se reserva para la noche, tanto para saludar como para despedirse."},
             ]},
            {"id": "pa2-match", "type": "matching", "title": "Empareja la Situación con el Saludo",
             "items": [
                {"id": "pa2match1", "pairs": [
                    {"left": "Llegas a la oficina a las ocho de la mañana", "right": "Buenos días"},
                    {"left": "Te despides antes de dormir", "right": "Buenas noches"},
                    {"left": "Saludas a un amigo en la calle", "right": "¡Hola!"},
                    {"left": "Conoces a alguien por primera vez", "right": "Mucho gusto"},
                ], "explanation": "Cada situación tiene un saludo natural en español; elegir el correcto muestra cortesía y contexto."},
             ]},
            {"id": "pa2-fill", "type": "fill-blank", "title": "Completa el Diálogo",
             "items": [
                {"id": "pa2f1", "prompt": "— ¿Cómo ___ llamas? — Me llamo Laura.", "answers": [["te"]], "options": ["te", "se", "le"], "explanation": "Te llamas es la forma informal de tú."},
                {"id": "pa2f2", "prompt": "— Buenas tardes, ¿cómo ___ usted? — Muy bien, gracias.", "answers": [["está"]], "options": ["está", "estás", "estoy"], "explanation": "Con usted se usa la forma está, no estás."},
                {"id": "pa2f3", "prompt": "— Hola, ___ gusto. — Igualmente.", "answers": [["mucho"]], "options": ["mucho", "muy", "mucha"], "explanation": "La expresión fija es mucho gusto."},
                {"id": "pa2f4", "prompt": "— Adiós, ___ luego. — ¡Adiós!", "answers": [["hasta"]], "options": ["hasta", "desde", "para"], "explanation": "Hasta luego indica que te verás pronto con la persona."},
             ]},
        ],
        "summary": [
            "Buenos días, buenas tardes y buenas noches cambian según el momento del día; hola funciona siempre.",
            "¿Cómo te llamas? (informal) y ¿Cómo se llama usted? (formal) tienen la misma respuesta: me llamo...",
            "Usa tú con personas cercanas y usted con desconocidos o en contextos formales; en caso de duda, usted es la opción segura.",
        ],
    },
    {
        "id": "pre-a1-numeros-hora-y-fecha",
        "level": "Pre-A1", "unit": "1", "order": 3, "skill": "vocabulary", "strand": "numeros-tiempo",
        "title": "Números, Hora y Fecha",
        "subtitle": "Los números del 0 al 100, cómo preguntar y decir la hora, los días de la semana y los meses.",
        "objectives": [
            "Contar y usar los números del 0 al 100 en situaciones cotidianas.",
            "Preguntar y decir la hora en español.",
            "Nombrar los días de la semana y los meses del año.",
        ],
        "content": {
            "intro": "Los números, la hora y la fecha aparecen todos los días — en una tienda, en una cita, en una conversación — así que son vocabulario de máxima prioridad.",
            "explanation": "<p>Los números del 0 al 30 se escriben en su mayoría de una sola palabra (excepto los compuestos con <em>y</em>, como <em>veintiuno</em> hasta <em>veintinueve</em>). A partir del 31, se separan con la palabra <strong>y</strong>: <em>treinta y uno, cuarenta y dos, noventa y nueve</em>.</p><p>Para preguntar la hora se dice <strong>¿Qué hora es?</strong>, y para responder se usa el verbo <em>ser</em>: <em>Es la una</em> (solo para la una) pero <em>Son las dos, son las tres...</em> para el resto de las horas. La fecha se organiza con el día primero y el mes después: <em>el 15 de marzo</em>.</p>",
            "rules": [
                {"heading": "a) Números del 0 al 30", "body": "<ul><li>0 cero, 1 uno, 2 dos, 3 tres, 4 cuatro, 5 cinco</li><li>6 seis, 7 siete, 8 ocho, 9 nueve, 10 diez</li><li>11 once, 12 doce, 13 trece, 14 catorce, 15 quince</li><li>16 dieciséis... 19 diecinueve, 20 veinte</li><li>21 veintiuno... 29 veintinueve, 30 treinta</li></ul>"},
                {"heading": "b) Números del 31 al 100", "body": "<ul><li>A partir del 31 se usa la palabra y: <em>treinta y uno, treinta y dos...</em></li><li>40 cuarenta, 50 cincuenta, 60 sesenta, 70 setenta, 80 ochenta, 90 noventa</li><li>100 cien (pero <em>ciento uno, ciento dos...</em> a partir de 101)</li></ul>"},
                {"heading": "c) Decir la hora", "body": "<ul><li><strong>¿Qué hora es?</strong> — pregunta general para saber la hora.</li><li><em>Es la una</em> — solo para la 1:00.</li><li><em>Son las dos, son las tres, son las diez...</em> — para el resto de las horas.</li><li><em>Son las cuatro y media</em> (4:30); <em>son las cinco menos cuarto</em> (4:45).</li></ul>"},
                {"heading": "d) Días y meses", "body": "<ul><li>Días: lunes, martes, miércoles, jueves, viernes, sábado, domingo.</li><li>Meses: enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre.</li><li>Los días y los meses se escriben con minúscula en español.</li></ul>"},
            ],
            "examples": [
                "Tengo veinticinco años.",
                "Son las tres y media de la tarde.",
                "Hoy es lunes, 3 de marzo.",
                "Mi cumpleaños es el 20 de julio.",
                "Es la una en punto.",
                "Necesito noventa y nueve euros.",
                "El domingo no trabajo.",
                "Diciembre es el último mes del año.",
            ],
            "commonMistakes": [
                {"wrong": "Son la una de la tarde.", "right": "Es la una de la tarde.", "why": "Solo la una usa es (singular); todas las demás horas usan son (plural)."},
                {"wrong": "Hoy es Lunes, 3 de Marzo.", "right": "Hoy es lunes, 3 de marzo.", "why": "En español, los días de la semana y los meses se escriben siempre con minúscula inicial."},
                {"wrong": "diecisis", "right": "dieciséis", "why": "Dieciséis lleva tilde en la í; es un error común olvidarla al escribirlo."},
            ],
        },
        "exercises": [
            {"id": "pa3-mc", "type": "multiple-choice", "title": "Números, Hora y Fecha",
             "items": [
                {"id": "pa3mc1", "prompt": "¿Cómo se dice 45 en español?", "options": ["cuarenta y cinco", "cuarenta y seis", "cincuenta y cuatro"], "answerIndex": 0, "explanation": "Cuarenta y cinco combina cuarenta con y cinco."},
                {"id": "pa3mc2", "prompt": "¿Qué se dice para la 1:00?", "options": ["Son la una", "Es la una", "Son las una"], "answerIndex": 1, "explanation": "Solo para la una se usa es; el resto de las horas usa son."},
                {"id": "pa3mc3", "prompt": "¿Cuál es el primer día de la semana en el calendario hispanohablante?", "options": ["domingo", "lunes", "sábado"], "answerIndex": 1, "explanation": "En la mayoría de los países hispanohablantes, la semana empieza el lunes."},
                {"id": "pa3mc4", "prompt": "¿Cuál es el mes después de junio?", "options": ["mayo", "julio", "agosto"], "answerIndex": 1, "explanation": "El orden de los meses es ...mayo, junio, julio, agosto..."},
                {"id": "pa3mc5", "prompt": "¿Cómo se escribe 100?", "options": ["cien", "ciento", "cientos"], "answerIndex": 0, "explanation": "Cien es la forma correcta antes de un sustantivo o sola; ciento se usa a partir de 101 (ciento uno)."},
             ]},
            {"id": "pa3-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "pa3tf1", "statement": "Los días de la semana se escriben con mayúscula en español.", "answer": False, "explanation": "Se escriben con minúscula: lunes, martes, miércoles..."},
                {"id": "pa3tf2", "statement": "Son las dos se usa para las 2:00.", "answer": True, "explanation": "A partir de las dos, siempre se usa son."},
                {"id": "pa3tf3", "statement": "El año tiene doce meses en español, igual que en otras lenguas.", "answer": True, "explanation": "Sí, el calendario tiene doce meses: de enero a diciembre."},
                {"id": "pa3tf4", "statement": "Treinta y uno se escribe todo junto, sin espacios: treintayuno.", "answer": False, "explanation": "Se escribe en tres palabras separadas: treinta y uno."},
             ]},
            {"id": "pa3-match", "type": "matching", "title": "Empareja el Número con su Forma Escrita",
             "items": [
                {"id": "pa3match1", "pairs": [
                    {"left": "15", "right": "quince"},
                    {"left": "21", "right": "veintiuno"},
                    {"left": "50", "right": "cincuenta"},
                    {"left": "99", "right": "noventa y nueve"},
                    {"left": "100", "right": "cien"},
                ], "explanation": "Del 16 al 29 los números se escriben en una sola palabra; a partir del 31 se separan con y."},
             ]},
            {"id": "pa3-fill", "type": "fill-blank", "title": "Completa la Hora y la Fecha",
             "items": [
                {"id": "pa3f1", "prompt": "— ¿Qué hora es? — ___ las cinco.", "answers": [["son"]], "options": ["son", "es", "está"], "explanation": "Para las cinco (plural) se usa son."},
                {"id": "pa3f2", "prompt": "El primer mes del año es ___.", "answers": [["enero"]], "options": ["enero", "diciembre", "marzo"], "explanation": "Enero es el primer mes del calendario, seguido de febrero."},
                {"id": "pa3f3", "prompt": "El último día de la semana (en el calendario hispanohablante) es el ___.", "answers": [["domingo"]], "options": ["domingo", "sábado", "lunes"], "explanation": "La semana termina el domingo."},
                {"id": "pa3f4", "prompt": "Tengo treinta y ___ años (35).", "answers": [["cinco"]], "options": ["cinco", "seis", "cuatro"], "explanation": "Treinta y cinco es 35."},
             ]},
        ],
        "summary": [
            "Los números del 0 al 30 son en su mayoría una palabra; a partir del 31 se separan con y (treinta y uno, cuarenta y dos...).",
            "Es la una es la única hora en singular; todas las demás usan son las... (son las dos, son las tres...).",
            "Los días de la semana y los meses del año se escriben con minúscula y la semana empieza el lunes.",
        ],
    },
    {
        "id": "pre-a1-vocabulario-de-clase-y-estudio",
        "level": "Pre-A1", "unit": "1", "order": 4, "skill": "vocabulary", "strand": "clase",
        "title": "Vocabulario de Clase y Estudio",
        "subtitle": "Las palabras y frases esenciales para sobrevivir — y aprender — dentro de una clase de español.",
        "objectives": [
            "Usar frases básicas para pedir ayuda o repetición en clase.",
            "Nombrar los objetos más comunes de un estudiante.",
            "Entender instrucciones simples que da un profesor de español.",
        ],
        "content": {
            "intro": "Antes de hablar del mundo, necesitas sobrevivir dentro del aula: pedir que repitan, decir que no entiendes, y nombrar lo que tienes sobre la mesa.",
            "explanation": "<p>En una clase de español vas a escuchar y necesitar las mismas frases muchas veces: <strong>repite, por favor</strong> 🔁, <strong>no entiendo</strong>, <strong>¿cómo se dice...?</strong> Estas frases son tu herramienta más útil como principiante — te permiten seguir la clase sin frustración.</p><p>También necesitas los nombres de los objetos que usas cada día para estudiar: el <strong>cuaderno</strong> 📓, el <strong>lápiz</strong> ✏️, el <strong>libro</strong> 📖, el <strong>bolígrafo</strong>. Aprenderlos ahora te ayuda a entender instrucciones simples como <em>abre el libro</em> o <em>escribe en el cuaderno</em>.</p>",
            "rules": [
                {"heading": "a) Frases para pedir ayuda", "body": "<ul><li><strong>Repite, por favor</strong> — cuando no escuchaste bien.</li><li><strong>No entiendo</strong> — cuando no comprendes algo.</li><li><strong>¿Cómo se dice... en español?</strong> — para pedir una palabra nueva.</li><li><strong>¿Puede hablar más despacio, por favor?</strong> — cuando la persona habla muy rápido.</li></ul>"},
                {"heading": "b) Objetos del estudiante", "body": "<ul><li>el cuaderno 📓, el lápiz ✏️, el bolígrafo, la goma</li><li>el libro 📖, la mochila, la hoja de papel</li><li>la mesa, la silla, la pizarra</li></ul>"},
                {"heading": "c) Instrucciones típicas del profesor", "body": "<ul><li><strong>Abre el libro</strong> — abre tu libro.</li><li><strong>Escribe en el cuaderno</strong> — usa el cuaderno para escribir.</li><li><strong>Escucha con atención</strong> — presta atención al audio o a la voz.</li><li><strong>Trabaja con tu compañero/a</strong> — haz el ejercicio con otra persona.</li></ul>"},
            ],
            "examples": [
                "Perdón, no entiendo. ¿Puede repetir, por favor?",
                "¿Cómo se dice esta palabra otra vez, por favor?",
                "Necesito un lápiz y una hoja de papel.",
                "Abre el libro en la página diez.",
                "Escribe tu nombre en el cuaderno.",
                "¿Puede hablar más despacio, por favor?",
                "Mi mochila tiene dos cuadernos y un bolígrafo.",
                "Escucha con atención el diálogo.",
            ],
            "commonMistakes": [
                {"wrong": "Quedarse en silencio cuando no entiendes algo.", "right": "No entiendo. ¿Puede repetir, por favor?", "why": "Pedir ayuda con una frase simple es normal y esperado en una clase — es mejor que quedarse callado."},
                {"wrong": "Entiendo no (para decir que no comprendes).", "right": "No entiendo.", "why": "La negación va antes del verbo: no entiendo, no una construcción diferente."},
                {"wrong": "¿Cómo se dice en español esta palabra?", "right": "¿Cómo se dice esta palabra en español?", "why": "El orden natural pone la palabra en cuestión antes de en español."},
            ],
        },
        "exercises": [
            {"id": "pa4-mc", "type": "multiple-choice", "title": "Frases y Objetos de Clase",
             "items": [
                {"id": "pa4mc1", "prompt": "No escuchaste bien lo que dijo el profesor. ¿Qué dices?", "options": ["No entiendo", "Repite, por favor", "Mucho gusto"], "answerIndex": 1, "explanation": "Repite, por favor se usa para pedir que digan algo otra vez."},
                {"id": "pa4mc2", "prompt": "No comprendes una palabra. ¿Qué dices?", "options": ["No entiendo", "Buenos días", "Adiós"], "answerIndex": 0, "explanation": "No entiendo expresa que no comprendes algo."},
                {"id": "pa4mc3", "prompt": "¿Qué objeto usas para escribir con tinta?", "options": ["el lápiz", "el bolígrafo", "la goma"], "answerIndex": 1, "explanation": "El bolígrafo escribe con tinta; el lápiz usa grafito y se puede borrar con la goma."},
                {"id": "pa4mc4", "prompt": "El profesor habla muy rápido. ¿Qué le pides?", "options": ["¿Puede hablar más despacio, por favor?", "¿Cómo se llama?", "Mucho gusto"], "answerIndex": 0, "explanation": "Esta frase pide específicamente que hable más despacio."},
                {"id": "pa4mc5", "prompt": "¿Dónde guardas tus cuadernos y libros para ir a clase?", "options": ["en la pizarra", "en la mochila", "en la silla"], "answerIndex": 1, "explanation": "La mochila es donde llevas tus materiales de clase."},
             ]},
            {"id": "pa4-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "pa4tf1", "statement": "No entiendo es una frase útil cuando no comprendes algo en clase.", "answer": True, "explanation": "Es exactamente la frase correcta para expresar falta de comprensión."},
                {"id": "pa4tf2", "statement": "La goma sirve para escribir con tinta.", "answer": False, "explanation": "La goma sirve para borrar lo escrito con lápiz; el bolígrafo escribe con tinta."},
                {"id": "pa4tf3", "statement": "Repite, por favor se usa cuando quieres escuchar algo otra vez.", "answer": True, "explanation": "Exactamente — pides que la otra persona diga lo mismo de nuevo."},
                {"id": "pa4tf4", "statement": "La pizarra es un objeto que un estudiante lleva en la mochila.", "answer": False, "explanation": "La pizarra está fija en la clase; los estudiantes no la llevan en la mochila."},
             ]},
            {"id": "pa4-match", "type": "matching", "title": "Empareja el Objeto con su Descripción",
             "items": [
                {"id": "pa4match1", "pairs": [
                    {"left": "el cuaderno", "right": "donde escribes tus notas de clase"},
                    {"left": "el lápiz", "right": "se puede borrar con la goma"},
                    {"left": "la mochila", "right": "donde llevas tus materiales"},
                    {"left": "la pizarra", "right": "donde el profesor escribe para toda la clase"},
                ], "explanation": "Reconocer estos objetos te ayuda a seguir instrucciones simples desde el primer día de clase."},
             ]},
            {"id": "pa4-fill", "type": "fill-blank", "title": "Completa la Frase de Supervivencia",
             "items": [
                {"id": "pa4f1", "prompt": "Perdón, no ___. ¿Puede repetir?", "answers": [["entiendo"]], "options": ["entiendo", "entiende", "entiendes"], "explanation": "Entiendo es la forma de yo, la persona que habla."},
                {"id": "pa4f2", "prompt": "¿Cómo se ___ esta palabra en español?", "answers": [["dice"]], "options": ["dice", "dices", "digo"], "explanation": "Se dice es la forma impersonal usada para preguntar el nombre de algo."},
                {"id": "pa4f3", "prompt": "___ el libro en la página diez, por favor.", "answers": [["abre"]], "options": ["abre", "abres", "abro"], "explanation": "Abre es la forma de instrucción (imperativo informal) que da el profesor."},
                {"id": "pa4f4", "prompt": "Necesito un ___ para escribir con tinta.", "answers": [["bolígrafo"]], "options": ["bolígrafo", "lápiz", "goma"], "explanation": "El bolígrafo es el objeto que escribe con tinta."},
             ]},
        ],
        "summary": [
            "Repite, por favor; no entiendo; y ¿cómo se dice...? son las tres frases más útiles para sobrevivir en una clase de español.",
            "El cuaderno, el lápiz, el bolígrafo y el libro son los objetos básicos de cualquier estudiante.",
            "Reconocer instrucciones simples como abre el libro o escucha con atención te permite seguir la clase sin depender de traducciones.",
        ],
    },
    {
        "id": "pre-a1-personas-y-objetos-cotidianos",
        "level": "Pre-A1", "unit": "1", "order": 5, "skill": "vocabulary", "strand": "personas-objetos",
        "title": "Personas y Objetos Cotidianos",
        "subtitle": "Vocabulario básico para hablar de personas (hombre, mujer, niño) y de las cosas que ves cada día.",
        "objectives": [
            "Nombrar a las personas más comunes de tu entorno diario.",
            "Identificar objetos cotidianos de la casa y de la calle.",
            "Usar el o la correctamente según el género de cada palabra.",
        ],
        "content": {
            "intro": "Antes de formar frases largas, necesitas las palabras más frecuentes para hablar de las personas y los objetos que te rodean cada día.",
            "explanation": "<p>En español, todos los sustantivos tienen género: son masculinos o femeninos, y llevan un artículo — <strong>el</strong> (masculino) o <strong>la</strong> (femenino) — delante. Muchas palabras terminadas en <em>-o</em> son masculinas (<em>el niño</em>) y muchas terminadas en <em>-a</em> son femeninas (<em>la niña</em>), pero hay excepciones que aprenderás poco a poco.</p><p>Para hablar de personas usamos palabras como <strong>el hombre</strong>, <strong>la mujer</strong>, <strong>el niño</strong>, <strong>la niña</strong>. Para hablar de objetos de todos los días usamos palabras como <strong>la mesa</strong>, <strong>la silla</strong>, <strong>el teléfono</strong> 📱, <strong>la casa</strong> 🏠.</p>",
            "rules": [
                {"heading": "a) Personas", "body": "<ul><li><strong>el hombre</strong> / <strong>la mujer</strong></li><li><strong>el niño</strong> / <strong>la niña</strong></li><li><strong>el amigo</strong> / <strong>la amiga</strong></li><li><strong>la persona</strong> — siempre femenina, incluso para hablar de un hombre.</li></ul>"},
                {"heading": "b) Objetos de la casa", "body": "<ul><li><strong>la mesa</strong>, <strong>la silla</strong>, <strong>la puerta</strong>, <strong>la ventana</strong></li><li><strong>el teléfono</strong> 📱, <strong>el sofá</strong>, <strong>el libro</strong> 📖</li><li><strong>la casa</strong> 🏠 — el lugar donde vives.</li></ul>"},
                {"heading": "c) El y la: el género del artículo", "body": "<ul><li>Muchas palabras en -o son masculinas: <em>el libro, el teléfono</em>.</li><li>Muchas palabras en -a son femeninas: <em>la mesa, la casa</em>.</li><li>Hay excepciones que hay que memorizar: <em>la mano</em> es femenina aunque termina en -o.</li></ul>"},
            ],
            "examples": [
                "El hombre habla con la mujer.",
                "La niña tiene un libro nuevo.",
                "Mi teléfono está en la mesa.",
                "La casa tiene cuatro sillas.",
                "El niño abre la puerta.",
                "Mi amiga vive cerca de mi casa.",
                "La ventana de la casa es grande.",
            ],
            "commonMistakes": [
                {"wrong": "El mesa", "right": "La mesa", "why": "Mesa es una palabra femenina; su artículo correcto es la, siguiendo la regla general de las palabras terminadas en -a."},
                {"wrong": "La teléfono", "right": "El teléfono", "why": "Teléfono es una palabra masculina, aunque termina en -o; el artículo correcto es el."},
                {"wrong": "El persona (para hablar de un hombre)", "right": "La persona (siempre, incluso para hablar de un hombre)", "why": "Persona es siempre femenina en español, sin importar el género de quien describe."},
            ],
        },
        "exercises": [
            {"id": "pa5-mc", "type": "multiple-choice", "title": "Personas y Objetos",
             "items": [
                {"id": "pa5mc1", "prompt": "¿Cuál es el artículo correcto para mesa?", "options": ["el", "la"], "answerIndex": 1, "explanation": "Mesa es una palabra femenina: la mesa."},
                {"id": "pa5mc2", "prompt": "¿Cuál es el artículo correcto para teléfono?", "options": ["el", "la"], "answerIndex": 0, "explanation": "Teléfono es masculino, aunque termina en -o de forma regular: el teléfono."},
                {"id": "pa5mc3", "prompt": "¿Cómo se dice la persona adulta femenina?", "options": ["el hombre", "la mujer", "la niña"], "answerIndex": 1, "explanation": "La mujer es la persona adulta de género femenino."},
                {"id": "pa5mc4", "prompt": "¿Qué palabra usamos siempre en femenino, incluso para hablar de un hombre?", "options": ["la persona", "el hombre", "la casa"], "answerIndex": 0, "explanation": "Persona es siempre femenina en español, independientemente de a quién describa."},
                {"id": "pa5mc5", "prompt": "¿Dónde vives?", "options": ["en la casa", "en el casa", "en la mesa"], "answerIndex": 0, "explanation": "Casa es femenina: la casa; con la preposición en se dice en la casa."},
             ]},
            {"id": "pa5-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "pa5tf1", "statement": "Todas las palabras terminadas en -a son femeninas, sin excepción.", "answer": False, "explanation": "Es una regla general muy útil, pero existen excepciones que se aprenden con el uso."},
                {"id": "pa5tf2", "statement": "El niño y la niña usan artículos diferentes.", "answer": True, "explanation": "El niño es masculino y la niña es femenino, con sus propios artículos."},
                {"id": "pa5tf3", "statement": "La palabra persona siempre lleva el artículo la.", "answer": True, "explanation": "Persona es una palabra femenina fija, sin importar el género de la persona descrita."},
                {"id": "pa5tf4", "statement": "El teléfono es una palabra femenina.", "answer": False, "explanation": "Teléfono es masculino: el teléfono, aunque termina en -o."},
             ]},
            {"id": "pa5-match", "type": "matching", "title": "Empareja la Palabra con su Artículo",
             "items": [
                {"id": "pa5match1", "pairs": [
                    {"left": "mesa", "right": "la mesa"},
                    {"left": "teléfono", "right": "el teléfono"},
                    {"left": "casa", "right": "la casa"},
                    {"left": "hombre", "right": "el hombre"},
                    {"left": "niña", "right": "la niña"},
                ], "explanation": "Aprender cada palabra junto con su artículo (el o la) es la mejor forma de memorizar el género correctamente."},
             ]},
            {"id": "pa5-fill", "type": "fill-blank", "title": "Completa con El o La",
             "items": [
                {"id": "pa5f1", "prompt": "___ mujer habla con ___ hombre.", "answers": [["la"], ["el"]], "explanation": "Mujer es femenina (la) y hombre es masculino (el)."},
                {"id": "pa5f2", "prompt": "Necesito usar ___ teléfono nuevo.", "answers": [["el"]], "explanation": "Teléfono es masculino: el teléfono."},
                {"id": "pa5f3", "prompt": "___ casa tiene cuatro sillas.", "answers": [["la"]], "explanation": "Casa es femenina: la casa."},
                {"id": "pa5f4", "prompt": "___ niño abre la puerta.", "answers": [["el"]], "explanation": "Niño es masculino: el niño."},
             ]},
        ],
        "summary": [
            "En español, cada sustantivo tiene género (masculino o femenino) y lleva un artículo: el o la.",
            "Las palabras para personas más frecuentes son el hombre, la mujer, el niño y la niña; persona es siempre femenina.",
            "Muchas palabras en -o son masculinas y muchas en -a son femeninas, pero conviene aprender cada palabra junto con su artículo.",
        ],
    },
    {
        "id": "pre-a1-verbos-basicos-ser-tener-querer-gustar",
        "level": "Pre-A1", "unit": "1", "order": 6, "skill": "grammar", "strand": "verbos-basicos",
        "title": "Verbos Básicos: Ser, Tener, Querer, Gustar",
        "subtitle": "Un primer contacto con cuatro verbos esenciales, en frases muy simples con yo, tú y él/ella.",
        "objectives": [
            "Usar el verbo ser para decir quién eres y cómo eres.",
            "Usar el verbo tener para decir qué tienes o cuántos años tienes.",
            "Usar querer y gustar en frases simples para expresar deseos y preferencias.",
        ],
        "content": {
            "intro": "Con solo cuatro verbos — ser, tener, querer y gustar — ya puedes formar decenas de frases útiles sobre ti mismo y las personas que conoces.",
            "explanation": "<p>El verbo <strong>ser</strong> se usa para decir quién eres, de dónde eres o cómo eres: <em>Soy Ana. Soy de España. Soy alta.</em> El verbo <strong>tener</strong> se usa para hablar de posesión y también de la edad: <em>Tengo un perro. Tengo veinte años.</em></p><p>El verbo <strong>querer</strong> expresa un deseo: <em>Quiero un café.</em> El verbo <strong>gustar</strong> es diferente de los otros tres: no se dice «yo gusto», sino <em>me gusta</em> (a mí) o <em>te gusta</em> (a ti) — la cosa que gusta es el sujeto de la frase.</p>",
            "rules": [
                {"heading": "a) Ser (yo/tú/él-ella)", "body": "<ul><li>yo <strong>soy</strong> — <em>Soy profesor.</em></li><li>tú <strong>eres</strong> — <em>Tú eres muy amable.</em></li><li>él/ella <strong>es</strong> — <em>Ella es de Perú.</em></li></ul>"},
                {"heading": "b) Tener (yo/tú/él-ella)", "body": "<ul><li>yo <strong>tengo</strong> — <em>Tengo dos hermanos.</em></li><li>tú <strong>tienes</strong> — <em>¿Tienes tiempo?</em></li><li>él/ella <strong>tiene</strong> — <em>Él tiene treinta años.</em></li></ul>"},
                {"heading": "c) Querer (yo/tú/él-ella)", "body": "<ul><li>yo <strong>quiero</strong> — <em>Quiero agua, por favor.</em></li><li>tú <strong>quieres</strong> — <em>¿Qué quieres comer?</em></li><li>él/ella <strong>quiere</strong> — <em>Ella quiere descansar.</em></li></ul>"},
                {"heading": "d) Gustar: me gusta / te gusta / le gusta", "body": "<ul><li><strong>Me gusta</strong> el café. (a mí)</li><li><strong>Te gusta</strong> la música. (a ti)</li><li><strong>Le gusta</strong> el chocolate. (a él/a ella)</li><li>Si la cosa es plural, el verbo cambia: <em>Me gustan los libros.</em></li></ul>"},
            ],
            "examples": [
                "Soy Marta y soy de Colombia.",
                "Tengo veintiocho años.",
                "¿Tienes hermanos?",
                "Quiero un café con leche, por favor.",
                "Me gusta mucho la música.",
                "¿Te gusta el chocolate?",
                "Ella es muy simpática.",
                "Él tiene un perro pequeño.",
            ],
            "commonMistakes": [
                {"wrong": "Yo gusto el café.", "right": "Me gusta el café.", "why": "Gustar no funciona como los otros verbos: la cosa que gusta es el sujeto, y la persona necesita me/te/le."},
                {"wrong": "Yo soy veinte años.", "right": "Tengo veinte años.", "why": "La edad en español se expresa con tener, no con ser."},
                {"wrong": "Ella tiene simpática.", "right": "Ella es simpática.", "why": "Las cualidades y características se expresan con ser, no con tener."},
            ],
        },
        "exercises": [
            {"id": "pa6-mc", "type": "multiple-choice", "title": "Elige el Verbo Correcto",
             "items": [
                {"id": "pa6mc1", "prompt": "¿Cómo se dice tu edad en español?", "options": ["Soy veinte años", "Tengo veinte años", "Quiero veinte años"], "answerIndex": 1, "explanation": "La edad se expresa con tener, no con ser."},
                {"id": "pa6mc2", "prompt": "¿Cómo dices que te gusta el café?", "options": ["Yo gusto el café", "Me gusta el café", "Tengo gusto el café"], "answerIndex": 1, "explanation": "Con gustar se usa me/te/le, no el pronombre normal del sujeto."},
                {"id": "pa6mc3", "prompt": "Quieres decir de dónde eres. ¿Qué verbo usas?", "options": ["tener", "ser", "gustar"], "answerIndex": 1, "explanation": "El origen se expresa con ser: soy de..."},
                {"id": "pa6mc4", "prompt": "¿Cómo pides algo que deseas en un café?", "options": ["Soy un café, por favor", "Quiero un café, por favor", "Tengo un café, por favor"], "answerIndex": 1, "explanation": "Querer expresa un deseo directo: quiero un café."},
                {"id": "pa6mc5", "prompt": "¿Cuál es la forma de tú del verbo tener?", "options": ["tienes", "tengo", "tiene"], "answerIndex": 0, "explanation": "Tienes es la forma de tú: ¿tienes hermanos?"},
             ]},
            {"id": "pa6-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "pa6tf1", "statement": "En español, la edad se expresa con el verbo ser.", "answer": False, "explanation": "La edad se expresa con tener: tengo veinte años."},
                {"id": "pa6tf2", "statement": "Me gusta el café es correcto para decir que te gusta el café.", "answer": True, "explanation": "Es exactamente la forma correcta con el verbo gustar."},
                {"id": "pa6tf3", "statement": "Eres es la forma correcta de yo con el verbo ser.", "answer": False, "explanation": "La forma correcta de yo es soy; eres es la forma de tú."},
                {"id": "pa6tf4", "statement": "Quiero se usa para expresar un deseo.", "answer": True, "explanation": "Quiero expresa un deseo o una petición directa."},
             ]},
            {"id": "pa6-match", "type": "matching", "title": "Empareja el Pronombre con la Forma del Verbo",
             "items": [
                {"id": "pa6match1", "pairs": [
                    {"left": "yo (ser)", "right": "soy"},
                    {"left": "tú (tener)", "right": "tienes"},
                    {"left": "él/ella (querer)", "right": "quiere"},
                    {"left": "a mí (gustar)", "right": "me gusta"},
                    {"left": "yo (tener)", "right": "tengo"},
                ], "explanation": "Cada pronombre tiene su propia forma del verbo; con gustar, además, se usa me/te/le en vez del pronombre normal."},
             ]},
            {"id": "pa6-fill", "type": "fill-blank", "title": "Completa con el Verbo Correcto",
             "items": [
                {"id": "pa6f1", "prompt": "Yo ___ profesor de español.", "answers": [["soy"]], "options": ["soy", "eres", "es"], "explanation": "Soy es la forma de yo del verbo ser."},
                {"id": "pa6f2", "prompt": "¿Cuántos años ___ tú?", "answers": [["tienes"]], "options": ["tienes", "tengo", "tiene"], "explanation": "Tienes es la forma de tú del verbo tener."},
                {"id": "pa6f3", "prompt": "Ella ___ descansar un poco.", "answers": [["quiere"]], "options": ["quiere", "quiero", "quieres"], "explanation": "Quiere es la forma de él/ella del verbo querer."},
                {"id": "pa6f4", "prompt": "A mí ___ mucho la música.", "answers": [["me gusta"]], "options": ["me gusta", "te gusta", "le gusta"], "explanation": "Me gusta corresponde a a mí."},
             ]},
        ],
        "summary": [
            "Ser expresa identidad, origen y características (soy, eres, es); tener expresa posesión y edad (tengo, tienes, tiene).",
            "Querer expresa un deseo directo (quiero, quieres, quiere), útil para pedir cosas de forma simple y educada.",
            "Gustar funciona al revés que los otros verbos: se usa me gusta, te gusta, le gusta, con la cosa que gusta como sujeto.",
        ],
    },
    {
        "id": "pre-a1-pronombres-de-sujeto-y-ser-estar",
        "level": "Pre-A1", "unit": "1", "order": 7, "skill": "grammar", "strand": "pronombres",
        "title": "Pronombres de Sujeto y un Primer Acercamiento a Ser/Estar",
        "subtitle": "Yo, tú, él/ella, nosotros, ellos/ellas; y la diferencia sencilla entre soy de... (origen) y estoy en... (lugar).",
        "objectives": [
            "Reconocer y usar los pronombres de sujeto yo, tú, él/ella, nosotros y ellos/ellas.",
            "Usar soy de... para decir de dónde eres.",
            "Usar estoy en... para decir dónde estás en este momento.",
        ],
        "content": {
            "intro": "Los pronombres de sujeto identifican quién hace la acción, y dos pequeñas frases — soy de... y estoy en... — te permiten hablar de tu origen y de tu ubicación desde el primer día.",
            "explanation": "<p>Los pronombres de sujeto más usados son <strong>yo</strong>, <strong>tú</strong>, <strong>él</strong>/<strong>ella</strong>, <strong>nosotros</strong>/<strong>nosotras</strong> y <strong>ellos</strong>/<strong>ellas</strong>. En español, muchas veces no es necesario decir el pronombre, porque la forma del verbo ya indica quién habla — pero al principio es útil usarlo siempre para practicar.</p><p>El español tiene dos verbos que se traducen a veces de forma parecida: <strong>ser</strong> y <strong>estar</strong>. De forma muy simple, en este nivel: <em>ser</em> se usa para el origen (<em>Soy de México</em>) y <em>estar</em> se usa para el lugar en este momento (<em>Estoy en la escuela</em>). Más adelante aprenderás muchos más usos de cada uno.</p>",
            "rules": [
                {"heading": "a) Los pronombres de sujeto", "body": "<ul><li><strong>yo</strong> — la persona que habla.</li><li><strong>tú</strong> — la persona con quien hablas (informal).</li><li><strong>él / ella</strong> — otra persona (masculino/femenino).</li><li><strong>nosotros / nosotras</strong> — tú (quien habla) y otras personas.</li><li><strong>ellos / ellas</strong> — varias personas de las que hablas.</li></ul>"},
                {"heading": "b) Soy de... para el origen", "body": "<ul><li><em>Soy de Argentina.</em></li><li><em>¿De dónde eres tú?</em></li><li><em>Ella es de Japón.</em></li></ul>"},
                {"heading": "c) Estoy en... para el lugar", "body": "<ul><li><em>Estoy en casa.</em></li><li><em>¿Dónde estás tú ahora?</em></li><li><em>Ella está en el trabajo.</em></li></ul>"},
                {"heading": "d) Un contraste simple", "body": "<ul><li><strong>Soy de Chile</strong> — de dónde vengo (origen, con ser).</li><li><strong>Estoy en Chile</strong> — dónde me encuentro ahora (lugar, con estar).</li><li>Una persona puede ser de un país y estar en otro al mismo tiempo.</li></ul>"},
            ],
            "examples": [
                "Yo soy de Brasil.",
                "Tú estás en la universidad ahora.",
                "Ella es de Portugal, pero está en Francia.",
                "Nosotros somos de la misma ciudad.",
                "Ellos están en el parque.",
                "¿De dónde eres tú?",
                "¿Dónde estás en este momento?",
            ],
            "commonMistakes": [
                {"wrong": "Yo estoy de España.", "right": "Yo soy de España.", "why": "El origen se expresa con ser (soy de...), no con estar."},
                {"wrong": "Ella es en la escuela.", "right": "Ella está en la escuela.", "why": "El lugar donde alguien se encuentra se expresa con estar (está en...), no con ser."},
                {"wrong": "Ellos es de Perú.", "right": "Ellos son de Perú.", "why": "Con el pronombre ellos, el verbo ser toma la forma son, no es."},
            ],
        },
        "exercises": [
            {"id": "pa7-mc", "type": "multiple-choice", "title": "Pronombres, Ser y Estar",
             "items": [
                {"id": "pa7mc1", "prompt": "¿Qué pronombre usas para hablar de ti mismo?", "options": ["tú", "yo", "él"], "answerIndex": 1, "explanation": "Yo es el pronombre de la primera persona, la que habla."},
                {"id": "pa7mc2", "prompt": "¿Cómo dices de dónde eres?", "options": ["Estoy de...", "Soy de...", "Tengo de..."], "answerIndex": 1, "explanation": "El origen se expresa con soy de..."},
                {"id": "pa7mc3", "prompt": "¿Cómo dices dónde te encuentras ahora?", "options": ["Soy en...", "Estoy en...", "Quiero en..."], "answerIndex": 1, "explanation": "El lugar actual se expresa con estoy en..."},
                {"id": "pa7mc4", "prompt": "¿Qué pronombre usas para hablar de un grupo que te incluye a ti?", "options": ["ellos", "nosotros", "tú"], "answerIndex": 1, "explanation": "Nosotros incluye a la persona que habla junto con otras."},
                {"id": "pa7mc5", "prompt": "Ana y Luis están en la playa. ¿Qué pronombre los representa?", "options": ["nosotros", "ellos", "ella"], "answerIndex": 1, "explanation": "Ellos se usa para hablar de varias personas, en este caso Ana y Luis."},
             ]},
            {"id": "pa7-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "pa7tf1", "statement": "Soy de... se usa para hablar del origen de una persona.", "answer": True, "explanation": "Exactamente — soy de indica de dónde viene alguien."},
                {"id": "pa7tf2", "statement": "Estoy en... se usa para hablar del origen de una persona.", "answer": False, "explanation": "Estoy en... indica el lugar donde alguien se encuentra ahora, no su origen."},
                {"id": "pa7tf3", "statement": "Una persona puede ser de un país y estar en otro al mismo tiempo.", "answer": True, "explanation": "Sí — el origen (ser) y el lugar actual (estar) son cosas distintas."},
                {"id": "pa7tf4", "statement": "Nosotros y ellos se refieren siempre a la misma persona.", "answer": False, "explanation": "Nosotros incluye a quien habla; ellos se refiere a otras personas, sin incluir a quien habla."},
             ]},
            {"id": "pa7-match", "type": "matching", "title": "Empareja el Pronombre con la Situación",
             "items": [
                {"id": "pa7match1", "pairs": [
                    {"left": "yo", "right": "la persona que habla"},
                    {"left": "tú", "right": "la persona con quien hablas"},
                    {"left": "nosotros", "right": "tú (quien habla) y otras personas"},
                    {"left": "ellos", "right": "varias personas de las que hablas"},
                ], "explanation": "Cada pronombre de sujeto identifica claramente quién realiza la acción en la frase."},
             ]},
            {"id": "pa7-fill", "type": "fill-blank", "title": "Completa con Soy o Estoy",
             "items": [
                {"id": "pa7f1", "prompt": "___ de Colombia.", "answers": [["soy"]], "options": ["soy", "estoy", "eres"], "explanation": "El origen se expresa con soy de..."},
                {"id": "pa7f2", "prompt": "Ahora ___ en el trabajo.", "answers": [["estoy"]], "options": ["estoy", "soy", "eres"], "explanation": "El lugar actual se expresa con estoy en..."},
                {"id": "pa7f3", "prompt": "¿De dónde ___ tú?", "answers": [["eres"]], "options": ["eres", "estás", "soy"], "explanation": "Eres es la forma de tú del verbo ser, usada para preguntar el origen."},
                {"id": "pa7f4", "prompt": "¿Dónde ___ tú ahora?", "answers": [["estás"]], "options": ["estás", "eres", "soy"], "explanation": "Estás es la forma de tú del verbo estar, usada para preguntar el lugar."},
             ]},
        ],
        "summary": [
            "Los pronombres de sujeto (yo, tú, él/ella, nosotros, ellos/ellas) identifican quién realiza la acción.",
            "Soy de... expresa el origen de una persona; estoy en... expresa dónde se encuentra en este momento.",
            "Una persona puede ser de un lugar y estar en otro distinto al mismo tiempo — origen y ubicación son cosas diferentes.",
        ],
    },
    {
        "id": "pre-a1-lectura-y-escucha-de-supervivencia",
        "level": "Pre-A1", "unit": "1", "order": 8, "skill": "reading", "strand": "supervivencia",
        "title": "Lectura y Escucha de Supervivencia",
        "subtitle": "Lee y escucha diálogos cortos de situaciones básicas: presentarte y pedir algo en una tienda.",
        "objectives": [
            "Leer un diálogo corto de presentación y entender la información principal.",
            "Leer un diálogo corto en una tienda y entender qué pide cada persona.",
            "Reconocer palabras y frases de supervivencia dentro de un texto simple.",
        ],
        "content": {
            "intro": "Con el vocabulario y las frases de las lecciones anteriores, ya puedes leer y entender diálogos cortos de la vida real — el objetivo final de todo principiante.",
            "explanation": "<p>Leer diálogos reales, aunque sean muy simples, es diferente de aprender palabras sueltas: tienes que reconocer el vocabulario que ya conoces dentro de una conversación completa, con preguntas, respuestas y algo de contexto.</p><p>Esta lección junta todo lo aprendido — saludos, nombres, números, objetos — en dos situaciones muy comunes para un principiante: <strong>presentarse</strong> ante otra persona y <strong>pedir algo en una tienda</strong>.</p>",
            "rules": [
                {"heading": "a) Estrategia de lectura", "body": "<ul><li>No necesitas entender cada palabra — busca las palabras que ya conoces.</li><li>Usa el contexto (quién habla, dónde están) para adivinar palabras nuevas.</li><li>Lee el diálogo dos veces: la primera para tener una idea general, la segunda para los detalles.</li></ul>"},
                {"heading": "b) Diálogo 1 — Presentarse", "body": "<p><strong>Sara:</strong> Hola, ¿cómo te llamas?<br><strong>Diego:</strong> Me llamo Diego. ¿Y tú?<br><strong>Sara:</strong> Me llamo Sara. Mucho gusto.<br><strong>Diego:</strong> Mucho gusto, Sara. ¿De dónde eres?<br><strong>Sara:</strong> Soy de Colombia. ¿Y tú?<br><strong>Diego:</strong> Yo soy de México.</p>"},
                {"heading": "c) Diálogo 2 — En una tienda", "body": "<p><strong>Vendedora:</strong> Buenos días, ¿qué necesita?<br><strong>Cliente:</strong> Buenos días. Quiero un cuaderno y un lápiz, por favor.<br><strong>Vendedora:</strong> Aquí tiene. ¿Algo más?<br><strong>Cliente:</strong> No, gracias. ¿Cuánto es?<br><strong>Vendedora:</strong> Son cinco euros.<br><strong>Cliente:</strong> Aquí tiene. Gracias, adiós.</p>"},
            ],
            "examples": [
                "Hola, ¿cómo te llamas?",
                "Me llamo Diego. Mucho gusto.",
                "¿De dónde eres tú?",
                "Buenos días, ¿qué necesita?",
                "Quiero un cuaderno y un lápiz, por favor.",
                "¿Cuánto es? — Son cinco euros.",
            ],
            "commonMistakes": [
                {"wrong": "Traducir cada palabra del diálogo antes de entenderlo.", "right": "Buscar primero las palabras y frases que ya conoces.", "why": "Buscar el sentido general con el vocabulario conocido es más rápido y más útil que traducir palabra por palabra."},
                {"wrong": "Responder ¿Cuánto es? con Son cinco euros, por favor.", "right": "¿Cuánto es? — Son cinco euros.", "why": "La respuesta al precio no necesita por favor; por favor se usa al pedir algo, no al dar información."},
                {"wrong": "No entender nada y abandonar la lectura.", "right": "Leer el diálogo dos veces: primero para la idea general, después para los detalles.", "why": "Una segunda lectura, con la idea general ya clara, ayuda a identificar más detalles y palabras nuevas."},
            ],
        },
        "exercises": [
            {"id": "pa8-tf", "type": "true-false", "title": "Comprensión: ¿Verdadero o Falso?",
             "items": [
                {"id": "pa8tf1", "statement": "En el Diálogo 1, Sara es de Colombia.", "answer": True, "explanation": "Sara dice: Soy de Colombia."},
                {"id": "pa8tf2", "statement": "En el Diálogo 1, Diego es de Colombia.", "answer": False, "explanation": "Diego dice que es de México, no de Colombia."},
                {"id": "pa8tf3", "statement": "En el Diálogo 2, el cliente quiere un cuaderno y un lápiz.", "answer": True, "explanation": "El cliente dice: Quiero un cuaderno y un lápiz, por favor."},
                {"id": "pa8tf4", "statement": "En el Diálogo 2, el precio total es cinco euros.", "answer": True, "explanation": "La vendedora dice: Son cinco euros."},
                {"id": "pa8tf5", "statement": "En el Diálogo 2, el cliente pide también un libro.", "answer": False, "explanation": "El cliente solo pide un cuaderno y un lápiz; cuando le preguntan ¿algo más?, dice que no."},
             ]},
            {"id": "pa8-mc", "type": "multiple-choice", "title": "Preguntas sobre los Diálogos",
             "items": [
                {"id": "pa8mc1", "prompt": "¿Quién habla primero en el Diálogo 1?", "options": ["Diego", "Sara", "La vendedora"], "answerIndex": 1, "explanation": "Sara es quien saluda primero: Hola, ¿cómo te llamas?"},
                {"id": "pa8mc2", "prompt": "¿De dónde es Diego?", "options": ["Colombia", "España", "México"], "answerIndex": 2, "explanation": "Diego dice: Yo soy de México."},
                {"id": "pa8mc3", "prompt": "¿Qué pide el cliente en la tienda?", "options": ["Un cuaderno y un lápiz", "Un libro y una goma", "Un teléfono"], "answerIndex": 0, "explanation": "El cliente dice: Quiero un cuaderno y un lápiz, por favor."},
                {"id": "pa8mc4", "prompt": "¿Cuánto cuesta la compra del cliente?", "options": ["Cinco euros", "Diez euros", "Dos euros"], "answerIndex": 0, "explanation": "La vendedora responde: Son cinco euros."},
             ]},
            {"id": "pa8-order", "type": "ordering", "title": "Ordena las Frases del Diálogo",
             "instructions": "Coloca las líneas o palabras en el orden correcto.",
             "items": [
                {"id": "pa8order1", "prompt": "Ordena las líneas del Diálogo 1 en la secuencia correcta.", "words": ["Hola, ¿cómo te llamas?", "Me llamo Diego. ¿Y tú?", "Me llamo Sara. Mucho gusto.", "Mucho gusto, Sara. ¿De dónde eres?", "Soy de Colombia. ¿Y tú?", "Yo soy de México."], "explanation": "El diálogo sigue un orden lógico: primero el saludo y los nombres, después la pregunta sobre el origen y las respuestas."},
                {"id": "pa8order2", "prompt": "Ordena las líneas del Diálogo 2 en la secuencia correcta.", "words": ["Buenos días, ¿qué necesita?", "Buenos días. Quiero un cuaderno y un lápiz, por favor.", "Aquí tiene. ¿Algo más?", "No, gracias. ¿Cuánto es?", "Son cinco euros.", "Aquí tiene. Gracias, adiós."], "explanation": "La conversación en la tienda sigue el orden: saludo, petición, entrega, pregunta por el precio, pago y despedida."},
                {"id": "pa8order3", "prompt": "Ordena las palabras para formar una frase correcta.", "words": ["Quiero", "un", "cuaderno", "y", "un", "lápiz"], "explanation": "El orden correcto es quiero seguido del primer objeto, y, y el segundo objeto — quiero va siempre al principio para pedir algo."},
             ]},
        ],
        "summary": [
            "Leer un diálogo simple es más fácil si buscas primero las palabras que ya conoces, en vez de traducir todo.",
            "El Diálogo 1 (presentarse) combina saludos, nombres y origen; el Diálogo 2 (en una tienda) combina saludos, objetos y números.",
            "Con el vocabulario de las lecciones anteriores ya puedes seguir conversaciones cortas de la vida real en español.",
        ],
    },
]

# =======================================================================
# EXTRA_EXERCISES — bloques adicionales de práctica (lectura y
# ordenar frases) fusionados en cada lección por id, para ampliar la
# colección de ejercicios sin tocar el contenido pedagógico ya escrito
# arriba. Ver el bucle de fusión al final de este archivo.
# =======================================================================
EXTRA_EXERCISES = {
    "pre-a1-el-alfabeto-y-los-sonidos": [
        {"id": "pa1x-reading", "type": "reading-comprehension", "title": "Lectura: Un Mensaje de Ana",
         "passage": "<p>¡Hola! Me llamo Ana. Mi nombre tiene una ñ: A-N-A no, espera, ¡no tiene ñ! Pero mi apellido sí: Muñoz. La ñ es una letra especial del español. Mi perro se llama Ñoño y también tiene ñ. Vivo en una calle con doble r: Carretera Nueva.</p>",
         "items": [
            {"id": "pa1xr1", "prompt": "¿Qué letra especial tiene el apellido de Ana?", "options": ["la ñ", "la h", "la doble r"], "answerIndex": 0, "explanation": "El texto dice: «Mi apellido sí (tiene ñ): Muñoz»."},
            {"id": "pa1xr2", "prompt": "¿Cómo se llama el perro de Ana?", "options": ["Ana", "Ñoño", "Muñoz"], "answerIndex": 1, "explanation": "El texto dice: «Mi perro se llama Ñoño»."},
            {"id": "pa1xr3", "prompt": "¿Qué combinación de letras aparece en el nombre de la calle?", "options": ["ñ", "h muda", "doble r"], "answerIndex": 2, "explanation": "«Carretera» tiene doble r, mencionada explícitamente en el texto."},
            {"id": "pa1xr4", "prompt": "¿El nombre \"Ana\" tiene la letra ñ?", "options": ["Sí", "No"], "answerIndex": 1, "explanation": "El texto aclara que \"Ana\" no tiene ñ, aunque parezca similar a otras palabras con ñ."},
         ]},
        {"id": "pa1x-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "pa1xo1", "prompt": "Ordena las palabras.", "words": ["La", "ñ", "es", "una", "letra", "especial", "del", "español"], "explanation": "Sujeto (La ñ), verbo (es), y el resto describe qué es."},
            {"id": "pa1xo2", "prompt": "Ordena las palabras.", "words": ["El", "perro", "se", "llama", "Ñoño"], "explanation": "Estructura típica para nombrar a una mascota: sujeto + se llama + nombre."},
         ]},
    ],
    "pre-a1-saludos-y-presentaciones": [
        {"id": "pa2x-reading", "type": "reading-comprehension", "title": "Lectura: En la Fiesta",
         "passage": "<p>—¡Buenas tardes! Me llamo Carlos. ¿Cómo te llamas?<br>—Buenas tardes, Carlos. Me llamo Elena. Mucho gusto.<br>—Mucho gusto, Elena. ¿De dónde eres?<br>—Soy de Perú. ¿Y tú?<br>—Yo soy de España. ¡Bienvenida a la fiesta!</p>",
         "items": [
            {"id": "pa2xr1", "prompt": "¿Cómo se llama la persona que llega de Perú?", "options": ["Carlos", "Elena", "Ninguno de los dos"], "answerIndex": 1, "explanation": "Elena dice: «Soy de Perú»."},
            {"id": "pa2xr2", "prompt": "¿De dónde es Carlos?", "options": ["De Perú", "De España", "No lo dice"], "answerIndex": 1, "explanation": "Carlos dice: «Yo soy de España»."},
            {"id": "pa2xr3", "prompt": "¿A qué hora del día ocurre este saludo?", "options": ["Por la mañana", "Por la tarde", "Por la noche"], "answerIndex": 1, "explanation": "El diálogo empieza con «Buenas tardes»."},
            {"id": "pa2xr4", "prompt": "¿El diálogo termina con una bienvenida?", "options": ["Sí", "No"], "answerIndex": 0, "explanation": "La última línea es «¡Bienvenida a la fiesta!»."},
         ]},
        {"id": "pa2x-order", "type": "ordering", "title": "Ordena el Diálogo",
         "items": [
            {"id": "pa2xo1", "prompt": "Ordena las palabras.", "words": ["¿Cómo", "te", "llamas", "tú"], "explanation": "La pregunta empieza con la palabra interrogativa ¿Cómo?."},
            {"id": "pa2xo2", "prompt": "Ordena las palabras.", "words": ["Mucho", "gusto", "en", "conocerte"], "explanation": "Expresión fija de cortesía al conocer a alguien."},
         ]},
    ],
    "pre-a1-numeros-hora-y-fecha": [
        {"id": "pa3x-reading", "type": "reading-comprehension", "title": "Lectura: El Horario de Marta",
         "passage": "<p>Marta se levanta a las siete de la mañana. Desayuna a las siete y media. Sus clases empiezan a las nueve y terminan a la una de la tarde. Hoy es martes, tres de marzo. El cumpleaños de Marta es el veinte de mayo.</p>",
         "items": [
            {"id": "pa3xr1", "prompt": "¿A qué hora se levanta Marta?", "options": ["A las siete", "A las siete y media", "A las nueve"], "answerIndex": 0, "explanation": "El texto dice: «Marta se levanta a las siete de la mañana»."},
            {"id": "pa3xr2", "prompt": "¿A qué hora terminan las clases de Marta?", "options": ["A la una de la tarde", "A las nueve", "A las siete y media"], "answerIndex": 0, "explanation": "El texto dice: «terminan a la una de la tarde»."},
            {"id": "pa3xr3", "prompt": "¿Qué día es hoy en el texto?", "options": ["Lunes", "Martes", "Miércoles"], "answerIndex": 1, "explanation": "El texto dice: «Hoy es martes, tres de marzo»."},
            {"id": "pa3xr4", "prompt": "¿En qué mes es el cumpleaños de Marta?", "options": ["Marzo", "Abril", "Mayo"], "answerIndex": 2, "explanation": "El texto dice: «El cumpleaños de Marta es el veinte de mayo»."},
         ]},
        {"id": "pa3x-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "pa3xo1", "prompt": "Ordena las palabras.", "words": ["Son", "las", "nueve", "de", "la", "mañana"], "explanation": "Para dar la hora en plural se usa son las + número."},
            {"id": "pa3xo2", "prompt": "Ordena las palabras.", "words": ["Hoy", "es", "el", "tres", "de", "marzo"], "explanation": "Para la fecha: hoy es el + número + de + mes."},
         ]},
    ],
    "pre-a1-vocabulario-de-clase-y-estudio": [
        {"id": "pa4x-reading", "type": "reading-comprehension", "title": "Lectura: La Mochila de Pablo",
         "passage": "<p>Pablo lleva su mochila a clase todos los días. Dentro tiene dos cuadernos, tres lápices, un libro y una goma. Su profesora escribe en la pizarra y los estudiantes escuchan con atención. Después de la clase, Pablo guarda todo en la mochila otra vez.</p>",
         "items": [
            {"id": "pa4xr1", "prompt": "¿Cuántos cuadernos tiene Pablo en la mochila?", "options": ["Uno", "Dos", "Tres"], "answerIndex": 1, "explanation": "El texto dice: «Dentro tiene dos cuadernos»."},
            {"id": "pa4xr2", "prompt": "¿Dónde escribe la profesora?", "options": ["En un cuaderno", "En la pizarra", "En un libro"], "answerIndex": 1, "explanation": "El texto dice: «Su profesora escribe en la pizarra»."},
            {"id": "pa4xr3", "prompt": "¿Qué hacen los estudiantes durante la clase?", "options": ["Duermen", "Escuchan con atención", "Comen"], "answerIndex": 1, "explanation": "El texto dice: «los estudiantes escuchan con atención»."},
            {"id": "pa4xr4", "prompt": "¿Pablo lleva la mochila solo algunos días?", "options": ["Sí, solo los lunes", "No, todos los días", "No lo dice"], "answerIndex": 1, "explanation": "El texto dice que Pablo lleva su mochila «todos los días»."},
         ]},
        {"id": "pa4x-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "pa4xo1", "prompt": "Ordena las palabras.", "words": ["Necesito", "un", "lápiz", "y", "una", "goma"], "explanation": "Necesito + objeto + y + otro objeto, con los artículos correctos según el género."},
            {"id": "pa4xo2", "prompt": "Ordena las palabras.", "words": ["La", "profesora", "escribe", "en", "la", "pizarra"], "explanation": "Sujeto + verbo + complemento de lugar."},
         ]},
    ],
    "pre-a1-personas-y-objetos-cotidianos": [
        {"id": "pa5x-reading", "type": "reading-comprehension", "title": "Lectura: La Familia de Luis",
         "passage": "<p>Esta es la familia de Luis. Su madre se llama Rosa y es alta. Su padre se llama Tomás y es simpático. Luis tiene un hermano pequeño que se llama Iván. En la sala de su casa hay una mesa, dos sillas y un televisor nuevo.</p>",
         "items": [
            {"id": "pa5xr1", "prompt": "¿Cómo se llama la madre de Luis?", "options": ["Rosa", "Tomás", "Iván"], "answerIndex": 0, "explanation": "El texto dice: «Su madre se llama Rosa»."},
            {"id": "pa5xr2", "prompt": "¿Cómo es el padre de Luis, según el texto?", "options": ["Alto", "Simpático", "Pequeño"], "answerIndex": 1, "explanation": "El texto dice: «Su padre se llama Tomás y es simpático»."},
            {"id": "pa5xr3", "prompt": "¿Qué hay en la sala de la casa?", "options": ["Una cama y un armario", "Una mesa, dos sillas y un televisor", "Un perro y un gato"], "answerIndex": 1, "explanation": "El texto describe la sala con esos tres objetos."},
            {"id": "pa5xr4", "prompt": "¿Iván es el hermano mayor de Luis?", "options": ["Sí", "No, es el hermano pequeño"], "answerIndex": 1, "explanation": "El texto dice: «un hermano pequeño que se llama Iván»."},
         ]},
        {"id": "pa5x-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "pa5xo1", "prompt": "Ordena las palabras.", "words": ["Mi", "padre", "es", "muy", "simpático"], "explanation": "Posesivo + sustantivo + verbo ser + adverbio + adjetivo."},
            {"id": "pa5xo2", "prompt": "Ordena las palabras.", "words": ["Hay", "una", "mesa", "en", "la", "sala"], "explanation": "Hay (existencia) + objeto + complemento de lugar."},
         ]},
    ],
    "pre-a1-verbos-basicos-ser-tener-querer-gustar": [
        {"id": "pa6x-reading", "type": "reading-comprehension", "title": "Lectura: Sofía se Presenta",
         "passage": "<p>Me llamo Sofía y soy estudiante. Tengo veinte años y tengo dos hermanas. Quiero aprender español muy bien. Me gusta la música y también me gusta el café por las mañanas. No me gusta levantarme temprano los domingos.</p>",
         "items": [
            {"id": "pa6xr1", "prompt": "¿Cuántos años tiene Sofía?", "options": ["Dieciocho", "Veinte", "Veinticinco"], "answerIndex": 1, "explanation": "El texto dice: «Tengo veinte años»."},
            {"id": "pa6xr2", "prompt": "¿Qué quiere aprender Sofía?", "options": ["Música", "Inglés", "Español"], "answerIndex": 2, "explanation": "El texto dice: «Quiero aprender español muy bien»."},
            {"id": "pa6xr3", "prompt": "¿A Sofía le gusta levantarse temprano los domingos?", "options": ["Sí, mucho", "No, no le gusta"], "answerIndex": 1, "explanation": "El texto dice: «No me gusta levantarme temprano los domingos»."},
            {"id": "pa6xr4", "prompt": "¿Cuántas hermanas tiene Sofía?", "options": ["Una", "Dos", "Tres"], "answerIndex": 1, "explanation": "El texto dice: «tengo dos hermanas»."},
         ]},
        {"id": "pa6x-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "pa6xo1", "prompt": "Ordena las palabras.", "words": ["Me", "gusta", "mucho", "el", "café"], "explanation": "Pronombre + gustar (singular) + adverbio + sustantivo con artículo."},
            {"id": "pa6xo2", "prompt": "Ordena las palabras.", "words": ["Quiero", "aprender", "español", "muy", "bien"], "explanation": "Quiero + infinitivo + complemento + intensificador."},
         ]},
    ],
    "pre-a1-pronombres-de-sujeto-y-ser-estar": [
        {"id": "pa7x-reading", "type": "reading-comprehension", "title": "Lectura: Nosotros Somos Estudiantes",
         "passage": "<p>Nosotros somos estudiantes de español. Yo soy de Brasil y ella es de Francia. Él está cansado hoy porque trabaja mucho. Ellos están en la biblioteca ahora, estudiando para el examen de la próxima semana.</p>",
         "items": [
            {"id": "pa7xr1", "prompt": "¿De dónde es la persona que habla (yo)?", "options": ["De Francia", "De Brasil", "No lo dice"], "answerIndex": 1, "explanation": "El texto dice: «Yo soy de Brasil»."},
            {"id": "pa7xr2", "prompt": "¿Por qué él está cansado?", "options": ["Porque estudia mucho", "Porque trabaja mucho", "Porque no duerme"], "answerIndex": 1, "explanation": "El texto dice: «Él está cansado hoy porque trabaja mucho»."},
            {"id": "pa7xr3", "prompt": "¿Dónde están ellos ahora?", "options": ["En casa", "En la biblioteca", "En el trabajo"], "answerIndex": 1, "explanation": "El texto dice: «Ellos están en la biblioteca ahora»."},
            {"id": "pa7xr4", "prompt": "¿Para qué estudian en la biblioteca?", "options": ["Para un examen", "Para una fiesta", "Para un viaje"], "answerIndex": 0, "explanation": "El texto dice que estudian «para el examen de la próxima semana»."},
         ]},
        {"id": "pa7x-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "pa7xo1", "prompt": "Ordena las palabras.", "words": ["Nosotros", "somos", "estudiantes", "de", "español"], "explanation": "Pronombre plural + ser (nosotros) + sustantivo + complemento."},
            {"id": "pa7xo2", "prompt": "Ordena las palabras.", "words": ["Ellos", "están", "en", "la", "biblioteca"], "explanation": "Pronombre + estar (ellos) + complemento de lugar."},
         ]},
    ],
    "pre-a1-lectura-y-escucha-de-supervivencia": [
        {"id": "pa8x-reading", "type": "reading-comprehension", "title": "Lectura: Pedir Ayuda en la Calle",
         "passage": "<p>—Disculpe, ¿dónde está la estación de tren?<br>—Está muy cerca, a dos calles de aquí, a la derecha.<br>—Muchas gracias. Una pregunta más: ¿hay un banco cerca también?<br>—Sí, hay uno enfrente de la estación.<br>—Perfecto, muchísimas gracias por su ayuda.</p>",
         "items": [
            {"id": "pa8xr1", "prompt": "¿Qué busca la persona que pregunta?", "options": ["Un banco", "La estación de tren", "Un restaurante"], "answerIndex": 1, "explanation": "La primera pregunta es: «¿dónde está la estación de tren?»."},
            {"id": "pa8xr2", "prompt": "¿En qué dirección está la estación?", "options": ["A la izquierda", "A la derecha", "Todo recto"], "answerIndex": 1, "explanation": "La respuesta dice: «a dos calles de aquí, a la derecha»."},
            {"id": "pa8xr3", "prompt": "¿Dónde está el banco?", "options": ["Enfrente de la estación", "Dentro de la estación", "Lejos de la estación"], "answerIndex": 0, "explanation": "La respuesta dice: «hay uno enfrente de la estación»."},
            {"id": "pa8xr4", "prompt": "¿La persona da las gracias más de una vez?", "options": ["Sí", "No"], "answerIndex": 0, "explanation": "Dice «Muchas gracias» y después «muchísimas gracias»."},
         ]},
        {"id": "pa8x-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "pa8xo1", "prompt": "Ordena las palabras.", "words": ["Disculpe", "¿dónde", "está", "la", "estación"], "explanation": "Fórmula de cortesía + pregunta de ubicación."},
            {"id": "pa8xo2", "prompt": "Ordena las palabras.", "words": ["Está", "a", "dos", "calles", "de", "aquí"], "explanation": "Estar (ubicación) + distancia + referencia."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
