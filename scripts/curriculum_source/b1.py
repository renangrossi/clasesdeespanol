# -*- coding: utf-8 -*-
"""B1 — datos del currículo de nivel intermedio. Ver curriculum/SCHEMA.md
para la forma exacta del JSON que esto compila (scripts/generate_curriculum.py
hace la compilación). Escrito como Python en vez de JSON a mano para que el
texto en español con comillas, tildes y ñ se lea con naturalidad.

Curso monolingüe: los ejemplos son strings simples en español, sin
traducción al inglés en ningún campo."""

OVERVIEW = (
    "El nivel B1 profundiza en los matices del pasado (perfecto frente a "
    "indefinido, y el pluscuamperfecto para lo anterior a lo anterior), "
    "añade el futuro compuesto y el condicional, y da el gran salto al modo "
    "subjuntivo — el modo del deseo, la duda y la emoción, que dominará gran "
    "parte de los niveles siguientes. También verás el imperativo negativo, "
    "los pronombres combinados, la diferencia entre por y para, las "
    "oraciones relativas, el voseo argentino y los principales conectores "
    "del discurso. Al terminar este nivel podrás usar el español de forma "
    "independiente para el trabajo, los estudios y los viajes, y empezarás "
    "a sonar mucho más natural y menos \"traducido\"."
)

LESSONS = [
    {
        "id": "b1-perfecto-vs-indefinido-matices",
        "level": "B1", "unit": "1", "order": 1, "skill": "grammar", "strand": "pasado",
        "title": "Perfecto vs. Indefinido: los Matices",
        "subtitle": "Por qué España y América Latina no siempre coinciden al elegir entre estos dos tiempos.",
        "objectives": [
            "Repasar y afinar la diferencia funcional entre el pretérito perfecto compuesto y el indefinido",
            "Reconocer la variación regional en el uso de ambos tiempos",
            "Elegir el tiempo adecuado según el marcador temporal y la variedad de español",
        ],
        "content": {
            "intro": "En A2 aprendiste la regla general de estos dos tiempos; en B1 toca afinarla, porque el uso real varía según la región del mundo hispanohablante en la que te encuentres.",
            "explanation": "<p>La regla de base sigue siendo válida: el <strong>perfecto compuesto</strong> conecta un hecho con un periodo de tiempo no terminado o con el presente, y el <strong>indefinido</strong> narra hechos cerrados en el pasado. Pero en España, sobre todo en el centro y el norte, el perfecto compuesto se extiende también a hechos de hoy con un final claro (<em>Esta mañana he desayunado tarde</em>), mientras que gran parte de América Latina prefiere el indefinido incluso para hechos de hoy mismo (<em>Esta mañana desayuné tarde</em>).</p><p>No hay una versión \"incorrecta\": son dos normas regionales distintas, y ambas se enseñan y se entienden en todo el mundo hispanohablante. Lo importante es ser consistente y reconocer ambos usos al leer o escuchar.</p>",
            "rules": [
                {"heading": "a) La base que no cambia en ningún país", "body": "<ul><li>Marcador de tiempo cerrado y terminado (<em>ayer, en 2020, el mes pasado</em>) → siempre indefinido.</li><li>Experiencia de vida sin momento concreto (<em>alguna vez, nunca, ya</em>) → siempre perfecto compuesto.</li></ul>"},
                {"heading": "b) La zona de variación regional", "body": "<ul><li>España (centro/norte): <em>Hoy he comido en un restaurante nuevo.</em> (hecho de hoy, aunque ya terminó)</li><li>Gran parte de América Latina: <em>Hoy comí en un restaurante nuevo.</em> (mismo hecho, con indefinido)</li></ul>"},
                {"heading": "c) Cómo decidir en la práctica", "body": "<p>Si no sabes qué variedad prefiere tu interlocutor, la regla de base (marcador cerrado → indefinido; experiencia sin momento → perfecto) siempre funciona y se entiende en cualquier país.</p>"},
            ],
            "examples": [
                "¿Has estado alguna vez en Argentina? (experiencia, cualquier país)",
                "El año pasado viajé a Perú por primera vez. (marcador cerrado, cualquier país)",
                "Esta mañana he tomado un café con mi vecina. (España, hoy)",
                "Esta mañana tomé un café con mi vecina. (América Latina, hoy)",
                "Todavía no he terminado el informe. (periodo no cerrado, cualquier país)",
                "Nunca he comido insectos, la verdad. (experiencia, cualquier país)",
                "En 2019 nos mudamos a esta ciudad. (marcador cerrado, cualquier país)",
                "¿Ya comiste? / ¿Ya has comido? (ambas formas, según la región)",
            ],
            "commonMistakes": [
                {"wrong": "Pensar que una de las dos normas regionales es incorrecta", "right": "Reconocer que ambas son correctas dentro de su propia variedad", "why": "La diferencia entre España y América Latina en este punto es de norma regional, no de corrección gramatical."},
                {"wrong": "He viajado a Chile en 2015.", "right": "Viajé a Chile en 2015.", "why": "Un marcador de tiempo cerrado como \"en 2015\" siempre pide indefinido, sin importar la variedad regional."},
                {"wrong": "Fui a España muchas veces en mi vida (sin marcador temporal).", "right": "He ido a España muchas veces en mi vida.", "why": "Una experiencia de vida sin momento concreto (\"en mi vida\") se expresa con el perfecto compuesto en cualquier variedad."},
            ],
        },
        "exercises": [
            {"id": "b1pi-mc", "type": "multiple-choice", "title": "Elige el Tiempo Correcto",
             "items": [
                {"id": "b1pi1", "prompt": "\"___ a Colombia el año pasado.\" (marcador cerrado)", "options": ["He viajado", "Viajé", "Viajaba"], "answerIndex": 1, "explanation": "El año pasado es un marcador de tiempo cerrado: siempre pide indefinido."},
                {"id": "b1pi2", "prompt": "\"¿___ alguna vez sushi?\" (experiencia sin momento concreto)", "options": ["comiste", "has comido", "comías"], "answerIndex": 1, "explanation": "Alguna vez señala una experiencia de vida, que se expresa con el perfecto compuesto."},
             ]},
            {"id": "b1pi-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "b1pi3", "statement": "En gran parte de América Latina es habitual usar el indefinido incluso para hechos de hoy mismo.", "answer": True, "explanation": "Es una diferencia regional real, no un error: el indefinido se extiende más al presente en esas variedades."},
                {"id": "b1pi4", "statement": "Un marcador como \"ayer\" puede usarse con el perfecto compuesto en cualquier variedad del español.", "answer": False, "explanation": "Ayer marca un momento cerrado y terminado, así que exige el indefinido en todas las variedades."},
             ]},
            {"id": "b1pi-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1pi5", "incorrect": "He nacido en 1995 en Madrid.", "answer": ["Nací en 1995 en Madrid."], "explanation": "Un año concreto como marcador de tiempo cerrado siempre pide el indefinido, no el perfecto compuesto."},
             ]},
        ],
        "summary": [
            "La regla de base se mantiene: marcador cerrado → indefinido; experiencia sin momento concreto → perfecto compuesto.",
            "España tiende a extender el perfecto compuesto a hechos de hoy; gran parte de América Latina prefiere el indefinido incluso para hoy.",
            "Ninguna de las dos normas es incorrecta: son variedades regionales igualmente válidas.",
        ],
    },
    {
        "id": "b1-pluscuamperfecto",
        "level": "B1", "unit": "1", "order": 2, "skill": "grammar", "strand": "pasado",
        "title": "El Pluscuamperfecto",
        "subtitle": "Había + participio: lo que ya había pasado antes de otro momento del pasado.",
        "objectives": [
            "Conjugar el imperfecto de haber como auxiliar del pluscuamperfecto",
            "Usar el pluscuamperfecto para expresar anterioridad dentro del pasado",
            "Combinar el pluscuamperfecto con el indefinido o el imperfecto en una misma narración",
        ],
        "content": {
            "intro": "Cuando cuentas una historia en pasado y necesitas retroceder a un momento todavía anterior, el español usa el pluscuamperfecto — el pasado del pasado.",
            "explanation": "<p>Se forma con el <strong>imperfecto de haber</strong> (había, habías, había, habíamos, habíais, habían) más el <strong>participio</strong> del verbo principal, con los mismos participios irregulares ya vistos en el pretérito perfecto compuesto. Expresa un hecho que ya había ocurrido antes de otro punto de referencia en el pasado.</p><p>Por ejemplo: <em>Cuando llegué a la estación, el tren ya había salido</em> — primero salió el tren (pluscuamperfecto), y después llegué yo (indefinido); el pluscuamperfecto marca claramente cuál de los dos hechos pasó primero.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Pluscuamperfecto — había + participio</caption><thead><tr><th>Sujeto</th><th>haber</th><th>+ participio</th></tr></thead><tbody><tr><td>yo</td><td>había</td><td>hablado / comido / vivido</td></tr><tr><td>tú</td><td>habías</td><td>hablado / comido / vivido</td></tr><tr><td>él/ella/usted</td><td>había</td><td>hablado / comido / vivido</td></tr><tr><td>nosotros/as</td><td>habíamos</td><td>hablado / comido / vivido</td></tr><tr><td>vosotros/as</td><td>habíais</td><td>hablado / comido / vivido</td></tr><tr><td>ellos/as/ustedes</td><td>habían</td><td>hablado / comido / vivido</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Estructura", "body": "<p>Imperfecto de haber + participio: <em>había hablado, habías comido, había vivido.</em></p>"},
                {"heading": "b) Uso: anterioridad dentro del pasado", "body": "<p>Marca qué hecho pasó primero cuando hay dos momentos distintos en el pasado: <em>Ya habíamos cenado cuando llamaste.</em></p>"},
                {"heading": "c) Con nunca antes / ya", "body": "<p>Es muy frecuente con expresiones como <em>nunca antes, ya, todavía no</em>: <em>Nunca antes había visto una tormenta así.</em></p>"},
            ],
            "examples": [
                "Cuando llegamos al cine, la película ya había empezado.",
                "Ella nunca había viajado en avión antes de ese verano.",
                "Ya habíamos terminado de cenar cuando sonó el teléfono.",
                "No sabía que ya habías hablado con el director.",
                "Antes de mudarnos aquí, habíamos vivido diez años en el campo.",
                "Cuando por fin llegó el médico, el paciente ya se había recuperado un poco.",
                "Todavía no habían decidido el destino de las vacaciones.",
                "Me di cuenta de que había olvidado las llaves en casa.",
            ],
            "commonMistakes": [
                {"wrong": "Cuando llegué, la película ya empezó.", "right": "Cuando llegué, la película ya había empezado.", "why": "Para marcar que un hecho ocurrió antes que otro hecho pasado, se necesita el pluscuamperfecto, no el indefinido."},
                {"wrong": "Ella nunca ha viajado antes de ese año.", "right": "Ella nunca había viajado antes de ese año.", "why": "El punto de referencia es un momento del pasado (ese año), así que se necesita el pluscuamperfecto, no el perfecto compuesto."},
                {"wrong": "Habíamos escribido la carta antes de salir.", "right": "Habíamos escrito la carta antes de salir.", "why": "Escribir mantiene su participio irregular escrito también en el pluscuamperfecto."},
            ],
        },
        "exercises": [
            {"id": "b1pl-fill", "type": "fill-blank", "title": "Completa con el Pluscuamperfecto",
             "items": [
                {"id": "b1pl1", "prompt": "Cuando llegamos, ellos ya ___ (salir).", "answers": [["habían salido"]], "options": ["habían salido", "salieron", "salían"], "explanation": "Un hecho anterior a otro hecho pasado (llegamos) se expresa con pluscuamperfecto."},
                {"id": "b1pl2", "prompt": "Yo nunca ___ (ver) una playa tan bonita antes de ese viaje.", "answers": [["había visto"]], "options": ["había visto", "he visto", "vi"], "explanation": "El punto de referencia (ese viaje) es pasado, así que se necesita el pluscuamperfecto."},
             ]},
            {"id": "b1pl-mc", "type": "multiple-choice", "title": "¿Qué Hecho Ocurrió Primero?",
             "items": [
                {"id": "b1pl3", "prompt": "\"Cuando desperté, ya había amanecido.\" ¿Qué ocurrió primero?", "options": ["Despertar", "Amanecer", "Los dos al mismo tiempo"], "answerIndex": 1, "explanation": "El pluscuamperfecto (había amanecido) marca el hecho anterior al otro hecho pasado (desperté)."},
             ]},
            {"id": "b1pl-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1pl4", "incorrect": "Antes de ese día, nunca comí paella.", "answer": ["Antes de ese día, nunca había comido paella."], "explanation": "El punto de referencia es un momento pasado (ese día), así que corresponde el pluscuamperfecto."},
             ]},
        ],
        "summary": [
            "El pluscuamperfecto se forma con el imperfecto de haber más el participio del verbo principal.",
            "Expresa un hecho que ya había ocurrido antes de otro punto de referencia en el pasado.",
            "Aparece con frecuencia junto a expresiones como nunca antes, ya o todavía no.",
        ],
    },
    {
        "id": "b1-futuro-compuesto-y-condicional-simple",
        "level": "B1", "unit": "1", "order": 3, "skill": "grammar", "strand": "futuro",
        "title": "Futuro Compuesto y Condicional Simple",
        "subtitle": "Habré + participio para el futuro anterior; el condicional simple para hipótesis y deseos.",
        "objectives": [
            "Formar y usar el futuro compuesto para acciones terminadas antes de un momento futuro",
            "Conjugar el condicional simple de verbos regulares e irregulares",
            "Usar el condicional simple para hipótesis, deseos y suposiciones sobre el pasado",
        ],
        "content": {
            "intro": "El futuro compuesto mira hacia adelante y hacia atrás a la vez —qué habrá pasado ya para cierto momento futuro—, mientras que el condicional simple es el \"futuro del pasado\" y también el tiempo de la cortesía y de las hipótesis.",
            "explanation": "<p>El <strong>futuro compuesto</strong> se forma con el futuro simple de haber (habré, habrás, habrá...) más el participio: <em>Para las diez ya habré terminado el informe.</em> También expresa una suposición sobre algo ya ocurrido: <em>Ya habrán llegado, supongo.</em></p><p>El <strong>condicional simple</strong> se forma añadiendo las terminaciones -ía, -ías, -ía, -íamos, -íais, -ían al infinitivo completo (las mismas raíces irregulares del futuro simple: tendr-, podr-, dir-...). Expresa lo que haría alguien bajo ciertas condiciones, deseos suavizados, y suposiciones sobre el pasado.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Condicional simple — hablar, tener, decir</caption><thead><tr><th>Sujeto</th><th>hablar</th><th>tener</th><th>decir</th></tr></thead><tbody><tr><td>yo</td><td>hablaría</td><td>tendría</td><td>diría</td></tr><tr><td>tú</td><td>hablarías</td><td>tendrías</td><td>dirías</td></tr><tr><td>él/ella/usted</td><td>hablaría</td><td>tendría</td><td>diría</td></tr><tr><td>nosotros/as</td><td>hablaríamos</td><td>tendríamos</td><td>diríamos</td></tr><tr><td>vosotros/as</td><td>hablaríais</td><td>tendríais</td><td>diríais</td></tr><tr><td>ellos/as/ustedes</td><td>hablarían</td><td>tendrían</td><td>dirían</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Futuro compuesto: habré + participio", "body": "<p>Para acciones que ya estarán terminadas en un momento futuro: <em>Cuando llegues, ya habré salido del trabajo.</em></p>"},
                {"heading": "b) Condicional simple: mismas raíces irregulares del futuro", "body": "<p>Las mismas raíces del futuro (tendr-, podr-, sabr-, querr-, dir-, har-, pondr-, saldr-, vendr-) se usan también en condicional, con las terminaciones -ía/-ías/-ía/-íamos/-íais/-ían.</p>"},
                {"heading": "c) Usos del condicional", "body": "<ul><li>Cortesía: <em>¿Podrías ayudarme?</em></li><li>Consejo suave: <em>Yo que tú, hablaría con ella.</em></li><li>Deseo: <em>Me encantaría viajar a Japón.</em></li><li>Suposición sobre el pasado: <em>Serían las diez cuando llamó.</em></li></ul>"},
            ],
            "examples": [
                "Para el próximo año, ya habré terminado la carrera.",
                "Cuando vuelvas a casa, ya habremos cenado seguramente.",
                "¿Podrías cerrar la ventana, por favor?",
                "Me gustaría mucho visitar Machu Picchu algún día.",
                "Yo en tu lugar, no diría nada todavía.",
                "Serían las once de la noche cuando por fin llegaron.",
                "¿Te importaría prestarme tu diccionario un momento?",
                "Ellos dijeron que vendrían, pero todavía no habrán llegado.",
            ],
            "commonMistakes": [
                {"wrong": "¿Puedrías ayudarme?", "right": "¿Podrías ayudarme?", "why": "Poder usa la raíz irregular podr- también en condicional, no la forma regular puedr-."},
                {"wrong": "Me gustaría... me gustaba viajar mucho.", "right": "Me gustaría viajar mucho.", "why": "Un deseo hipotético se expresa con condicional (gustaría), no con imperfecto (gustaba), que describe un hábito o estado real del pasado."},
                {"wrong": "Para mañana, ya habré terminaré el proyecto.", "right": "Para mañana, ya habré terminado el proyecto.", "why": "El futuro compuesto necesita el participio (terminado), no otra forma conjugada del verbo."},
            ],
        },
        "exercises": [
            {"id": "b1fc-fill", "type": "fill-blank", "title": "Completa con Futuro Compuesto o Condicional",
             "items": [
                {"id": "b1fc1", "prompt": "Para las ocho, ya ___ (yo - terminar) de trabajar.", "answers": [["habré terminado"]], "options": ["habré terminado", "terminaría", "terminaré"], "explanation": "Futuro compuesto: habré + participio, para una acción ya terminada en un momento futuro."},
                {"id": "b1fc2", "prompt": "¿___ (tú - poder) prestarme un bolígrafo?", "answers": [["Podrías"]], "options": ["Podrías", "Puedrías", "Podrás"], "explanation": "Condicional simple con raíz irregular podr-, usado para una petición cortés."},
             ]},
            {"id": "b1fc-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "b1fc3", "prompt": "\"___ las tres cuando sonó la alarma.\" (suposición sobre el pasado)", "options": ["Serían", "Serán", "Fueron"], "answerIndex": 0, "explanation": "El condicional simple expresa una suposición sobre un hecho pasado."},
                {"id": "b1fc4", "prompt": "¿Cuál es la forma correcta de \"decir\" en condicional para \"yo\"?", "options": ["deciría", "diría", "diciría"], "answerIndex": 1, "explanation": "Decir usa la raíz irregular dir- en condicional: diría."},
             ]},
            {"id": "b1fc-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1fc5", "incorrect": "Yo querría ayudarte, pero no puedo ahora.", "answer": ["Yo querría ayudarte, pero no puedo ahora. (correcto)"], "explanation": "Esta frase ya es correcta: querría es el condicional simple de querer, con raíz irregular querr-."},
             ]},
        ],
        "summary": [
            "El futuro compuesto (habré + participio) expresa lo que ya estará terminado en un momento futuro, o una suposición sobre el pasado reciente.",
            "El condicional simple usa las mismas raíces irregulares que el futuro, con las terminaciones -ía/-ías/-ía/-íamos/-íais/-ían.",
            "El condicional expresa cortesía, consejo suave, deseo y suposiciones sobre el pasado.",
        ],
    },
    {
        "id": "b1-condicional-cortesia-e-hipotesis",
        "level": "B1", "unit": "1", "order": 4, "skill": "functional", "strand": "condicional",
        "title": "El Condicional para Cortesía e Hipótesis",
        "subtitle": "Cómo suavizar peticiones, dar consejos y hablar de situaciones imaginarias.",
        "objectives": [
            "Usar el condicional para hacer peticiones y preguntas más corteses",
            "Dar consejos con la estructura \"yo que tú\" / \"yo en tu lugar\"",
            "Formar hipótesis simples con si + presente y si + imperfecto de subjuntivo (introducción)",
        ],
        "content": {
            "intro": "El condicional no solo describe lo que pasaría bajo ciertas condiciones: en la conversación cotidiana, es sobre todo la forma más natural de pedir algo con educación o de dar un consejo sin sonar autoritario.",
            "explanation": "<p>Frente a un imperativo directo (<em>Ciérrala</em>), el condicional suaviza la petición: <em>¿Podrías cerrarla?</em> Es la forma habitual para pedir favores, hacer sugerencias en una tienda o un restaurante, o dar una opinión sin imponerla.</p><p>La estructura <strong>yo que tú</strong> / <strong>yo en tu lugar</strong> + condicional es la manera más natural de dar un consejo en español hablado: <em>Yo que tú, hablaría con ella cuanto antes.</em> Además, verás una primera hipótesis con <strong>si + imperfecto de subjuntivo + condicional</strong> (<em>Si tuviera tiempo, viajaría más</em>) — el subjuntivo se estudiará a fondo más adelante, pero conviene reconocer ya esta estructura tan frecuente.</p>",
            "rules": [
                {"heading": "a) Peticiones corteses", "body": "<ul><li><em>¿Podrías ayudarme con esto?</em></li><li><em>¿Te importaría abrir la puerta?</em></li><li><em>Me gustaría reservar una mesa para dos.</em></li></ul>"},
                {"heading": "b) Consejos con \"yo que tú\"", "body": "<ul><li><em>Yo que tú, no diría nada.</em></li><li><em>Yo en tu lugar, hablaría con el jefe.</em></li><li><em>Deberías descansar más, en tu lugar yo lo haría.</em></li></ul>"},
                {"heading": "c) Hipótesis con si + imperfecto de subjuntivo + condicional", "body": "<p><em>Si tuviera más dinero, viajaría por todo el mundo.</em> (una condición poco probable o imaginaria en el presente, con su consecuencia en condicional)</p>"},
            ],
            "examples": [
                "¿Podría traerme la cuenta, por favor?",
                "¿Te importaría bajar un poco el volumen de la música?",
                "Yo que tú, aceptaría esa oferta de trabajo.",
                "En tu lugar, yo hablaría directamente con ella.",
                "Si tuviera más tiempo libre, aprendería a tocar la guitarra.",
                "Si viviera en la playa, nadaría todos los días.",
                "Me encantaría probar esa comida algún día.",
                "¿Sería posible cambiar la reserva para otra fecha?",
            ],
            "commonMistakes": [
                {"wrong": "¿Puedes traerme la cuenta?", "right": "¿Podrías traerme la cuenta?", "why": "Aunque puedes no es incorrecto, podrías suena más cortés y es la forma preferida en situaciones formales como un restaurante."},
                {"wrong": "Si tengo más dinero, viajaría más.", "right": "Si tuviera más dinero, viajaría más.", "why": "Una condición hipotética o poco probable en el presente necesita el imperfecto de subjuntivo (tuviera), no el presente de indicativo (tengo)."},
                {"wrong": "Yo que tú hablo con ella.", "right": "Yo que tú, hablaría con ella.", "why": "El consejo con yo que tú se expresa en condicional, no en presente de indicativo."},
            ],
        },
        "exercises": [
            {"id": "b1cc-mc", "type": "multiple-choice", "title": "Elige la Forma Más Cortés",
             "items": [
                {"id": "b1cc1", "prompt": "¿Cuál de estas peticiones suena más cortés en un restaurante?", "options": ["Tráigame agua.", "¿Podría traerme agua?", "Traes agua."], "answerIndex": 1, "explanation": "El condicional suaviza la petición y suena mucho más cortés que un imperativo directo."},
                {"id": "b1cc2", "prompt": "\"Yo que tú, ___ esa oferta.\"", "options": ["acepto", "aceptaría", "aceptaba"], "answerIndex": 1, "explanation": "El consejo con yo que tú siempre se expresa en condicional."},
             ]},
            {"id": "b1cc-fill", "type": "fill-blank", "title": "Completa la Hipótesis",
             "items": [
                {"id": "b1cc3", "prompt": "Si ___ (yo - tener) más tiempo, ___ (aprender) a cocinar mejor.", "answers": [["tuviera"], ["aprendería"]], "options": ["tuviera", "aprendería"], "explanation": "Si + imperfecto de subjuntivo (tuviera) + condicional (aprendería) forma una hipótesis sobre el presente."},
             ]},
            {"id": "b1cc-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1cc4", "incorrect": "¿Te importa si abro la ventana? (versión menos cortés que se pide corregir hacia el condicional)", "answer": ["¿Te importaría si abro la ventana?"], "explanation": "El condicional (importaría) suaviza aún más la pregunta que el presente (importa), aunque ambas formas son posibles."},
             ]},
        ],
        "summary": [
            "El condicional es la forma más natural de hacer peticiones y preguntas corteses en español.",
            "Yo que tú / yo en tu lugar + condicional es la estructura habitual para dar un consejo.",
            "Si + imperfecto de subjuntivo + condicional forma una hipótesis sobre una condición poco probable en el presente.",
        ],
    },
    {
        "id": "b1-imperativo-negativo-y-pronombres",
        "level": "B1", "unit": "1", "order": 5, "skill": "grammar", "strand": "imperativo",
        "title": "Imperativo Negativo y Pronombres con el Imperativo",
        "subtitle": "No hables, no comas, no lo hagas: cómo cambia la forma y la posición del pronombre.",
        "objectives": [
            "Formar el imperativo negativo de tú y usted",
            "Explicar por qué el imperativo negativo usa las formas del subjuntivo",
            "Colocar correctamente los pronombres antes del imperativo negativo",
        ],
        "content": {
            "intro": "El imperativo negativo no es simplemente el afirmativo con no delante: usa una forma verbal distinta, y también cambia dónde se coloca el pronombre.",
            "explanation": "<p>El imperativo negativo, tanto para <strong>tú</strong> como para <strong>usted</strong>, usa las mismas formas que el presente de subjuntivo (que se estudiará a fondo en la próxima lección): para tú, verbos en -ar cambian a -es y verbos en -er/-ir cambian a -as; para usted, se mantienen las mismas formas que en el imperativo afirmativo.</p><p>A diferencia del imperativo afirmativo, donde el pronombre va pegado al final, en el <strong>negativo</strong> el pronombre siempre va <strong>antes</strong> del verbo, entre <em>no</em> y el verbo: <em>No lo hagas. No me lo digas. No se preocupe.</em></p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Imperativo negativo — tú y usted</caption><thead><tr><th>Verbo</th><th>tú (negativo)</th><th>usted (negativo)</th></tr></thead><tbody><tr><td>hablar</td><td>no hables</td><td>no hable</td></tr><tr><td>comer</td><td>no comas</td><td>no coma</td></tr><tr><td>escribir</td><td>no escribas</td><td>no escriba</td></tr><tr><td>hacer</td><td>no hagas</td><td>no haga</td></tr><tr><td>ir</td><td>no vayas</td><td>no vaya</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Tú negativo: -ar → -es, -er/-ir → -as", "body": "<p><em>No hables tan alto. No comas tan rápido. No escribas con lápiz.</em></p>"},
                {"heading": "b) Usted negativo: misma forma que el afirmativo", "body": "<p><em>No hable tan alto. No coma tan rápido. No escriba con lápiz.</em> (la forma verbal en sí no cambia entre afirmativo y negativo para usted, solo se añade no)</p>"},
                {"heading": "c) Irregulares frecuentes en negativo (tú)", "body": "<p><em>ir → no vayas, ser → no seas, estar → no estés, dar → no des, saber → no sepas</em> — nota que estos son distintos de los irregulares del afirmativo (ve, sé, está...).</p>"},
                {"heading": "d) Los pronombres van antes, no pegados", "body": "<p>Compara: <em>Hazlo</em> (afirmativo, pegado) frente a <em>No lo hagas</em> (negativo, separado y antes del verbo).</p>"},
            ],
            "examples": [
                "No hables tan rápido, por favor, no te entiendo bien.",
                "No comas entre horas si quieres cenar con ganas.",
                "No le digas nada todavía, prefiero contárselo yo mismo.",
                "No se preocupe, todo va a salir bien.",
                "No vayas sola por esa calle de noche.",
                "No lo dejes para el último momento, empieza ya.",
                "No os quedéis hasta muy tarde, mañana hay que madrugar.",
                "No seas tan duro contigo mismo, todos cometemos errores.",
            ],
            "commonMistakes": [
                {"wrong": "No hablas tan alto.", "right": "No hables tan alto.", "why": "El imperativo negativo de tú usa la forma del subjuntivo (hables), no el presente de indicativo (hablas)."},
                {"wrong": "No hazlo ahora.", "right": "No lo hagas ahora.", "why": "En el imperativo negativo, el pronombre va antes del verbo, no pegado al final como en el afirmativo."},
                {"wrong": "No ves solo por la noche.", "right": "No vayas sola por la noche.", "why": "El imperativo negativo de ir para tú es no vayas, una forma completamente distinta del afirmativo ve."},
            ],
        },
        "exercises": [
            {"id": "b1in-fill", "type": "fill-blank", "title": "Completa con el Imperativo Negativo",
             "items": [
                {"id": "b1in1", "prompt": "___ (Tú - no hablar) tan alto en la biblioteca.", "answers": [["No hables"]], "options": ["No hables", "No hablas", "No habla"], "explanation": "Tú + no + verbo en -ar en negativo = terminación -es: no hables."},
                {"id": "b1in2", "prompt": "___ (Usted - no preocuparse) por el resultado.", "answers": [["No se preocupe"]], "options": ["No se preocupe", "No se preocupa", "No preocúpese"], "explanation": "El pronombre reflexivo se va antes del verbo en el imperativo negativo."},
             ]},
            {"id": "b1in-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1in3", "incorrect": "No cómelo todo de una vez.", "answer": ["No lo comas todo de una vez."], "explanation": "En el imperativo negativo, el pronombre va antes del verbo, y el verbo usa la forma del subjuntivo: comas, no cómelo."},
                {"id": "b1in4", "incorrect": "No vas tan rápido con el coche.", "answer": ["No vayas tan rápido con el coche."], "explanation": "El imperativo negativo de ir para tú es no vayas, no la forma de presente vas."},
             ]},
            {"id": "b1in-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "b1in5", "prompt": "¿Cuál es la forma correcta de decirle a un amigo que no se lo diga a nadie?", "options": ["No se lo digas a nadie.", "No dígaselo a nadie.", "No lo digas a nadie se."], "answerIndex": 0, "explanation": "Los dos pronombres (se, lo) van juntos antes del verbo en el imperativo negativo."},
             ]},
        ],
        "summary": [
            "El imperativo negativo usa las formas del presente de subjuntivo, tanto para tú como para usted.",
            "Varios verbos tienen formas irregulares distintas en negativo (no vayas, no seas, no estés, no des, no sepas).",
            "A diferencia del afirmativo, en el imperativo negativo el pronombre siempre va antes del verbo, nunca pegado al final.",
        ],
    },
    {
        "id": "b1-subjuntivo-presente-formacion",
        "level": "B1", "unit": "1", "order": 6, "skill": "grammar", "strand": "subjuntivo",
        "title": "El Presente de Subjuntivo — Formación",
        "subtitle": "Cómo se forma el modo verbal del deseo, la duda y la emoción en español.",
        "objectives": [
            "Formar el presente de subjuntivo de verbos regulares en -ar, -er e -ir",
            "Reconocer los verbos con cambio de raíz e irregularidades propias del subjuntivo",
            "Explicar la regla general de formación a partir de la forma de yo del presente de indicativo",
        ],
        "content": {
            "intro": "Hasta ahora has usado el modo indicativo, que presenta los hechos como reales y objetivos. El subjuntivo es un modo distinto — no un tiempo más — que presenta la acción como deseada, dudosa, temida o valorada emocionalmente, nunca como un hecho seguro.",
            "explanation": "<p>La regla de formación más útil: se toma la forma de <strong>yo</strong> del presente de indicativo, se le quita la <strong>-o</strong> final, y se añaden las terminaciones \"cruzadas\" — los verbos en -ar toman terminaciones con <strong>e</strong>, y los verbos en -er/-ir toman terminaciones con <strong>a</strong>. Esto significa que cualquier irregularidad de la forma de yo del indicativo (tengo → tenga, hago → haga, conozco → conozca) se conserva automáticamente en todo el subjuntivo.</p><p>Solo un puñado de verbos muy frecuentes no siguen esta regla porque su forma de yo en indicativo no termina en -o: <strong>ser, estar, ir, saber, haber, dar</strong> tienen formas de subjuntivo propias que hay que memorizar aparte.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Presente de subjuntivo — hablar, comer, vivir, tener</caption><thead><tr><th>Sujeto</th><th>hablar</th><th>comer</th><th>vivir</th><th>tener</th></tr></thead><tbody><tr><td>yo</td><td>hable</td><td>coma</td><td>viva</td><td>tenga</td></tr><tr><td>tú</td><td>hables</td><td>comas</td><td>vivas</td><td>tengas</td></tr><tr><td>él/ella/usted</td><td>hable</td><td>coma</td><td>viva</td><td>tenga</td></tr><tr><td>nosotros/as</td><td>hablemos</td><td>comamos</td><td>vivamos</td><td>tengamos</td></tr><tr><td>vosotros/as</td><td>habléis</td><td>comáis</td><td>viváis</td><td>tengáis</td></tr><tr><td>ellos/as/ustedes</td><td>hablen</td><td>coman</td><td>vivan</td><td>tengan</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) La regla de la \"terminación cruzada\"", "body": "<p>-ar → -e, -es, -e, -emos, -éis, -en; -er/-ir → -a, -as, -a, -amos, -áis, -an.</p>"},
                {"heading": "b) La irregularidad de yo se hereda automáticamente", "body": "<p>tener (tengo) → tenga; hacer (hago) → haga; conocer (conozco) → conozca; salir (salgo) → salga; decir (digo) → diga.</p>"},
                {"heading": "c) Los seis verbos totalmente irregulares", "body": "<p><em>ser → sea, estar → esté, ir → vaya, saber → sepa, haber → haya, dar → dé</em> (con todas sus personas correspondientes).</p>"},
                {"heading": "d) Verbos con cambio de raíz en -ar/-er mantienen el cambio", "body": "<p><em>pensar (pienso) → piense; poder (puedo) → pueda</em> — igual que en indicativo, nosotros y vosotros no cambian: pensemos, podamos.</p>"},
            ],
            "examples": [
                "Espero que hables con ella antes de decidir nada.",
                "Quiero que comas algo antes de salir de casa.",
                "Es importante que tengamos paciencia con este proceso.",
                "Ojalá que ella esté bien después del viaje.",
                "No creo que sea tan difícil como parece.",
                "Dudo que ellos sepan la respuesta correcta.",
                "Es necesario que vayas al médico esta semana.",
                "Espero que tengáis un buen viaje mañana.",
            ],
            "commonMistakes": [
                {"wrong": "Espero que tienes razón.", "right": "Espero que tengas razón.", "why": "Después de esperar que, se necesita el subjuntivo (tengas), no el indicativo (tienes)."},
                {"wrong": "Quiero que él es feliz.", "right": "Quiero que él sea feliz.", "why": "Ser es uno de los seis verbos totalmente irregulares en subjuntivo: sea, no es (que es indicativo)."},
                {"wrong": "Ojalá que nosotros pensemos... ojalá que pensamos bien la decisión.", "right": "Ojalá que pensemos bien la decisión.", "why": "Ojalá siempre exige subjuntivo (pensemos), nunca indicativo (pensamos)."},
            ],
        },
        "exercises": [
            {"id": "b1sf-fill", "type": "fill-blank", "title": "Forma el Presente de Subjuntivo",
             "items": [
                {"id": "b1sf1", "prompt": "hablar → que yo ___", "answers": [["hable"]], "options": ["hable", "hablo", "hablé"], "explanation": "Verbo en -ar: terminación cruzada con e."},
                {"id": "b1sf2", "prompt": "tener (yo tengo) → que tú ___", "answers": [["tengas"]], "options": ["tengas", "tienes", "tenes"], "explanation": "La irregularidad de la forma de yo (tengo) se hereda en todo el subjuntivo: tengas."},
                {"id": "b1sf3", "prompt": "ser → que ellos ___", "answers": [["sean"]], "options": ["sean", "seen", "son"], "explanation": "Ser es uno de los seis verbos totalmente irregulares: sea, seas, sea, seamos, seáis, sean."},
             ]},
            {"id": "b1sf-mc", "type": "multiple-choice", "title": "Identifica la Forma Correcta",
             "items": [
                {"id": "b1sf4", "prompt": "¿Cuál es la forma de subjuntivo de \"ir\" para \"nosotros\"?", "options": ["vayamos", "vamos", "iamos"], "answerIndex": 0, "explanation": "Ir es totalmente irregular en subjuntivo: vaya, vayas, vaya, vayamos, vayáis, vayan."},
             ]},
            {"id": "b1sf-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "b1sf5", "statement": "La irregularidad de la forma de yo del presente de indicativo se conserva en todo el subjuntivo.", "answer": True, "explanation": "Por eso tengo da tenga, hago da haga, conozco da conozca, etc."},
                {"id": "b1sf6", "statement": "Ser, estar, ir, saber, haber y dar siguen la regla general del subjuntivo.", "answer": False, "explanation": "Estos seis verbos son totalmente irregulares en subjuntivo y no siguen la regla de la forma de yo."},
             ]},
        ],
        "summary": [
            "El presente de subjuntivo se forma quitando la -o de la forma de yo del indicativo y añadiendo terminaciones cruzadas (e para -ar, a para -er/-ir).",
            "Cualquier irregularidad de la forma de yo del indicativo se hereda automáticamente en todo el subjuntivo.",
            "Ser, estar, ir, saber, haber y dar son totalmente irregulares y deben memorizarse aparte.",
        ],
    },
    {
        "id": "b1-subjuntivo-deseo-duda-emocion",
        "level": "B1", "unit": "1", "order": 7, "skill": "grammar", "strand": "subjuntivo",
        "title": "El Presente de Subjuntivo — Deseo, Duda y Emoción",
        "subtitle": "Cuándo el verbo principal exige subjuntivo en la frase que sigue.",
        "objectives": [
            "Identificar los verbos y expresiones que activan el subjuntivo en la subordinada",
            "Distinguir el uso de creer/pensar en afirmativo (indicativo) y en negativo (subjuntivo)",
            "Construir frases completas con deseo, duda y emoción usando el subjuntivo correctamente",
        ],
        "content": {
            "intro": "Ya sabes formar el subjuntivo; ahora toca aprender cuándo aparece — y la clave está casi siempre en el verbo de la primera parte de la frase, no en el segundo verbo en sí.",
            "explanation": "<p>El subjuntivo aparece en una oración subordinada (normalmente introducida por <strong>que</strong>) cuando el verbo principal expresa <strong>deseo</strong> (querer, esperar, desear), <strong>duda o negación de la realidad</strong> (dudar, no creer, no pensar), o <strong>emoción/valoración</strong> (alegrarse de, es una pena que, es importante que). La estructura exige que el sujeto de las dos partes sea distinto; si es el mismo, se usa un infinitivo en lugar de que + subjuntivo.</p><p>Un caso especialmente importante: <strong>creer</strong> y <strong>pensar</strong> en afirmativo expresan una certeza asumida y piden indicativo (<em>Creo que tiene razón</em>), pero al negarlos, la certeza desaparece y piden subjuntivo (<em>No creo que tenga razón</em>).</p>",
            "rules": [
                {"heading": "a) Verbos de deseo", "body": "<p><em>querer, esperar, desear, preferir, necesitar</em> + que + subjuntivo: <em>Quiero que vengas a la fiesta.</em></p>"},
                {"heading": "b) Verbos y expresiones de duda o negación", "body": "<p><em>dudar, no creer, no pensar, no estar seguro de, es posible que, puede que</em> + que + subjuntivo: <em>Dudo que llegue a tiempo.</em></p>"},
                {"heading": "c) Verbos y expresiones de emoción/valoración", "body": "<p><em>alegrarse de, sentir, es una pena que, es importante que, me sorprende que, ojalá</em> + que + subjuntivo: <em>Me alegro de que estés aquí.</em></p>"},
                {"heading": "d) Mismo sujeto → infinitivo, no que + subjuntivo", "body": "<p><em>Quiero ir al cine</em> (un solo sujeto: yo) frente a <em>Quiero que vayas al cine</em> (dos sujetos distintos: yo/tú).</p>"},
            ],
            "examples": [
                "Espero que tengas un buen fin de semana.",
                "Dudo que ese restaurante esté abierto los lunes.",
                "Me alegro de que hayas encontrado trabajo, aunque eso ya es otro tiempo verbal que verás pronto.",
                "Es importante que todos lleguen puntuales a la reunión.",
                "No creo que sea buena idea salir con esta lluvia.",
                "Ojalá que el examen no sea tan difícil.",
                "Prefiero que me llames por la tarde, no por la mañana.",
                "Es una pena que no puedas venir al viaje con nosotros.",
            ],
            "commonMistakes": [
                {"wrong": "Espero que tú vienes mañana.", "right": "Espero que tú vengas mañana.", "why": "Esperar que expresa deseo y siempre exige subjuntivo en la subordinada."},
                {"wrong": "Creo que él tenga razón.", "right": "Creo que él tiene razón.", "why": "Creer en afirmativo expresa una certeza asumida y pide indicativo, no subjuntivo."},
                {"wrong": "Quiero que yo vaya al cine.", "right": "Quiero ir al cine.", "why": "Cuando el sujeto de las dos partes es el mismo, se usa un infinitivo, no que + subjuntivo."},
            ],
        },
        "exercises": [
            {"id": "b1sd-fill", "type": "fill-blank", "title": "Completa con Indicativo o Subjuntivo",
             "items": [
                {"id": "b1sd1", "prompt": "Espero que tú ___ (poder) venir a mi cumpleaños.", "answers": [["puedas"]], "options": ["puedas", "puedes", "podrás"], "explanation": "Esperar que expresa deseo: siempre exige subjuntivo."},
                {"id": "b1sd2", "prompt": "Creo que ella ___ (tener) razón en esto.", "answers": [["tiene"]], "options": ["tiene", "tenga", "tendría"], "explanation": "Creer en afirmativo expresa certeza: pide indicativo."},
                {"id": "b1sd3", "prompt": "No creo que ellos ___ (saber) la verdad completa.", "answers": [["sepan"]], "options": ["sepan", "saben", "sabrán"], "explanation": "No creer niega la certeza y exige subjuntivo."},
             ]},
            {"id": "b1sd-mc", "type": "multiple-choice", "title": "¿Infinitivo o Subjuntivo?",
             "items": [
                {"id": "b1sd4", "prompt": "¿Cuál es la forma correcta cuando el sujeto es el mismo en ambas partes?", "options": ["Quiero que estudie más.", "Quiero estudiar más.", "Quiero que estudio más."], "answerIndex": 1, "explanation": "Con un solo sujeto (yo), se usa el infinitivo, no que + subjuntivo."},
             ]},
            {"id": "b1sd-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1sd5", "incorrect": "Me alegro de que estás aquí con nosotros.", "answer": ["Me alegro de que estés aquí con nosotros."], "explanation": "Alegrarse de expresa emoción y exige subjuntivo en la subordinada."},
             ]},
        ],
        "summary": [
            "Los verbos de deseo, duda/negación y emoción activan el subjuntivo en la subordinada introducida por que.",
            "Creer y pensar piden indicativo en afirmativo, pero subjuntivo al negarlos, porque la certeza desaparece.",
            "Con un solo sujeto en toda la frase, se usa un infinitivo en lugar de que + subjuntivo.",
        ],
    },
    {
        "id": "b1-voz-pasiva-y-pasiva-refleja",
        "level": "B1", "unit": "1", "order": 8, "skill": "grammar", "strand": "voz-pasiva",
        "title": "Voz Pasiva con Ser y Pasiva Refleja con Se",
        "subtitle": "Dos formas de expresar una acción sin poner el foco en quién la realiza.",
        "objectives": [
            "Formar la voz pasiva con ser + participio",
            "Formar la pasiva refleja con se",
            "Elegir entre las dos formas según el registro y la presencia o no de un agente explícito",
        ],
        "content": {
            "intro": "A veces lo importante no es quién hace algo, sino qué se hace o a quién le pasa — el español tiene dos estructuras distintas para poner el foco en la acción o en quien la recibe, en vez de en quien la realiza.",
            "explanation": "<p>La <strong>voz pasiva con ser</strong> (<em>ser + participio</em>) es poco frecuente en el habla cotidiana, pero aparece en noticias y textos formales: <em>El edificio fue construido en 1920.</em> El participio concuerda en género y número con el sujeto, y puede incluir el agente con <strong>por</strong>: <em>La novela fue escrita por un autor colombiano.</em></p><p>La <strong>pasiva refleja con se</strong> es mucho más natural y frecuente en español hablado y escrito, sobre todo cuando no importa o no se conoce quién realiza la acción: <em>Se venden pisos en esta zona. Aquí se habla español.</em> El verbo concuerda en número con lo que se vende/habla/hace, y nunca lleva un agente explícito con por.</p>",
            "rules": [
                {"heading": "a) Voz pasiva con ser", "body": "<p>ser (en el tiempo que corresponda) + participio (concordado) + por + agente (opcional): <em>La ciudad fue fundada por colonizadores españoles en el siglo XVI.</em></p>"},
                {"heading": "b) Pasiva refleja con se", "body": "<p>se + verbo en tercera persona (singular o plural según el sustantivo): <em>Se vende esta casa. Se venden estos pisos.</em> Es la forma preferida en carteles, instrucciones y el habla cotidiana.</p>"},
                {"heading": "c) Se impersonal (sin sujeto claro)", "body": "<p>Cuando no hay un sustantivo claro que reciba la acción, el verbo va siempre en singular: <em>Se trabaja mucho en esta empresa. Se vive bien en esta ciudad.</em></p>"},
                {"heading": "d) Cuándo usar cada una", "body": "<p>Ser + participio: textos formales, históricos o periodísticos, sobre todo con un agente conocido. Pasiva refleja: habla cotidiana, carteles, instrucciones, cuando el agente no importa.</p>"},
            ],
            "examples": [
                "El puente fue diseñado por un ingeniero muy famoso.",
                "Se buscan camareros con experiencia para este restaurante.",
                "Esta canción fue grabada en los años ochenta.",
                "En España se cena bastante más tarde que en otros países.",
                "El museo fue inaugurado el año pasado por el alcalde.",
                "Se habla inglés y español en esta oficina de turismo.",
                "Las entradas fueron vendidas en menos de una hora.",
                "Se prohíbe fumar dentro del edificio.",
            ],
            "commonMistakes": [
                {"wrong": "El libro fue escribido por un autor famoso.", "right": "El libro fue escrito por un autor famoso.", "why": "El participio de escribir es escrito, irregular, también en la voz pasiva con ser."},
                {"wrong": "Se vende pisos en esta zona.", "right": "Se venden pisos en esta zona.", "why": "En la pasiva refleja, el verbo concuerda en número con el sustantivo: pisos es plural, así que el verbo debe ser venden."},
                {"wrong": "Se habla español por los turistas aquí.", "right": "Aquí se habla español. / El español es hablado por muchos turistas aquí.", "why": "La pasiva refleja con se nunca lleva un agente explícito con por; si se necesita mencionar al agente, se usa la voz pasiva con ser."},
            ],
        },
        "exercises": [
            {"id": "b1vp-fill", "type": "fill-blank", "title": "Completa con Pasiva Refleja",
             "items": [
                {"id": "b1vp1", "prompt": "___ (vender) casas nuevas en este barrio. (plural)", "answers": [["Se venden"]], "options": ["Se venden", "Se vende", "Son vendidas"], "explanation": "El sustantivo casas es plural, así que el verbo debe concordar: se venden."},
                {"id": "b1vp2", "prompt": "En este país ___ (comer) mucho pescado. (impersonal, singular)", "answers": [["se come"]], "options": ["se come", "se comen", "son comidos"], "explanation": "Se impersonal, sin sustantivo específico que reciba la acción, siempre va en singular."},
             ]},
            {"id": "b1vp-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "b1vp3", "prompt": "¿Cuál de estas frases es la voz pasiva con ser, correctamente formada?", "options": ["La carta fue escrita por Ana.", "La carta se escribió por Ana.", "La carta era escribida por Ana."], "answerIndex": 0, "explanation": "Ser + participio (escrita, concordado con carta) + por + agente es la voz pasiva correcta."},
             ]},
            {"id": "b1vp-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1vp4", "incorrect": "Se alquila apartamentos en el centro de la ciudad.", "answer": ["Se alquilan apartamentos en el centro de la ciudad."], "explanation": "Apartamentos es plural, así que el verbo de la pasiva refleja debe concordar en plural: se alquilan."},
            ]},
        ],
        "summary": [
            "La voz pasiva con ser (ser + participio, + por + agente opcional) es más frecuente en textos formales y periodísticos.",
            "La pasiva refleja con se es más natural en el habla cotidiana y nunca lleva un agente explícito con por.",
            "En la pasiva refleja, el verbo concuerda en número con el sustantivo; si no hay uno claro (se impersonal), va siempre en singular.",
        ],
    },
    {
        "id": "b1-estilo-indirecto-presente",
        "level": "B1", "unit": "1", "order": 9, "skill": "grammar", "strand": "estilo-indirecto",
        "title": "Estilo Indirecto (Presente)",
        "subtitle": "Cómo contar lo que otra persona dijo, sin citar sus palabras exactas.",
        "objectives": [
            "Transformar un estilo directo simple en estilo indirecto con decir que",
            "Ajustar los pronombres y posesivos al cambiar de estilo directo a indirecto",
            "Reconocer los cambios de tiempo verbal más comunes al reportar desde el presente",
        ],
        "content": {
            "intro": "Cuando cuentas lo que alguien dijo sin repetir sus palabras exactas entre comillas, necesitas reorganizar la frase — cambiar los pronombres, y a veces también el tiempo verbal.",
            "explanation": "<p>El estilo indirecto se introduce con un verbo de habla (<strong>decir, comentar, contar, explicar</strong>) seguido de <strong>que</strong>. Cuando el verbo introductor está en presente (<em>Dice que...</em>), los tiempos verbales normalmente no cambian, solo los pronombres y posesivos se ajustan al nuevo punto de vista.</p><p>Por ejemplo, si Marta dice \"Estoy cansada\", en estilo indirecto se convierte en <em>Marta dice que está cansada</em> — el pronombre implícito cambia de primera a tercera persona. Las preguntas también cambian de forma: se introducen con <strong>si</strong> (preguntas de sí/no) o se mantiene la palabra interrogativa (qué, dónde, cuándo), y se elimina el signo de interrogación.</p>",
            "rules": [
                {"heading": "a) Afirmaciones: decir que + frase reorganizada", "body": "<p>\"Estoy cansada\" → <em>Dice que está cansada.</em> \"Vivo en Madrid\" → <em>Dice que vive en Madrid.</em></p>"},
                {"heading": "b) Preguntas de sí/no: preguntar si", "body": "<p>\"¿Vienes a la fiesta?\" → <em>Me pregunta si voy a la fiesta.</em></p>"},
                {"heading": "c) Preguntas con palabra interrogativa: se mantiene la palabra", "body": "<p>\"¿Dónde vives?\" → <em>Me pregunta dónde vivo.</em> \"¿Qué hora es?\" → <em>Pregunta qué hora es.</em></p>"},
                {"heading": "d) Ajuste de pronombres y posesivos", "body": "<p>\"Mi hermano me llamó\" (dicho por Juan) → <em>Juan dice que su hermano lo llamó.</em></p>"},
            ],
            "examples": [
                "Ella dice que está muy contenta con su nuevo trabajo.",
                "Mi madre comenta que hace mucho tiempo que no nos visita.",
                "Él explica que necesita más tiempo para terminar el proyecto.",
                "Me preguntan si quiero ir con ellos al cine.",
                "Le pregunto dónde compró esos zapatos tan bonitos.",
                "Cuentan que el nuevo restaurante es excelente.",
                "Dice que su hermana vive cerca de la universidad.",
                "Nos pregunta cuándo empezamos las clases este año.",
            ],
            "commonMistakes": [
                {"wrong": "Ella dice que \"está cansada\".", "right": "Ella dice que está cansada.", "why": "En estilo indirecto no se usan comillas; la frase se integra directamente en la oración con que."},
                {"wrong": "Me pregunta que si voy a la fiesta.", "right": "Me pregunta si voy a la fiesta.", "why": "Con preguntas de sí/no, se usa solo si, sin añadir además la palabra que antes."},
                {"wrong": "Me pregunta que dónde vivo.", "right": "Me pregunta dónde vivo.", "why": "Con una palabra interrogativa (dónde, qué, cuándo), no se añade que; la palabra interrogativa ya cumple esa función."},
            ],
        },
        "exercises": [
            {"id": "b1ei-fill", "type": "fill-blank", "title": "Transforma a Estilo Indirecto",
             "items": [
                {"id": "b1ei1", "prompt": "Ana dice: \"Estoy muy ocupada.\" → Ana dice que ___ muy ocupada.", "answers": [["está"]], "options": ["está", "estoy", "esté"], "explanation": "El pronombre implícito cambia de yo a ella, así que el verbo pasa a tercera persona: está."},
                {"id": "b1ei2", "prompt": "Pregunta: \"¿Vienes mañana?\" → Me pregunta ___ voy mañana.", "answers": [["si"]], "options": ["si", "que si", "qué"], "explanation": "Las preguntas de sí/no se introducen con si, sin añadir que antes."},
             ]},
            {"id": "b1ei-mc", "type": "multiple-choice", "title": "Elige la Transformación Correcta",
             "items": [
                {"id": "b1ei3", "prompt": "\"¿Dónde trabajas?\" en estilo indirecto es...", "options": ["Me pregunta que dónde trabajo.", "Me pregunta dónde trabajo.", "Me pregunta si dónde trabajo."], "answerIndex": 1, "explanation": "Con una palabra interrogativa como dónde, no se añade que ni si."},
             ]},
            {"id": "b1ei-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1ei4", "incorrect": "Él dice que \"tiene mucho trabajo esta semana\".", "answer": ["Él dice que tiene mucho trabajo esta semana."], "explanation": "El estilo indirecto no usa comillas: la frase citada se integra sin ellas en la oración con que."},
             ]},
        ],
        "summary": [
            "El estilo indirecto se introduce con un verbo de habla + que, sin comillas, reorganizando pronombres y posesivos.",
            "Las preguntas de sí/no se introducen con si; las preguntas con palabra interrogativa mantienen esa palabra, sin añadir que.",
            "Cuando el verbo introductor está en presente, los tiempos verbales normalmente no cambian.",
        ],
    },
    {
        "id": "b1-pronombres-combinados",
        "level": "B1", "unit": "1", "order": 10, "skill": "grammar", "strand": "pronombres",
        "title": "Pronombres Combinados",
        "subtitle": "Se lo, me lo, te la: cuando el objeto directo y el indirecto aparecen juntos.",
        "objectives": [
            "Combinar correctamente un pronombre de objeto indirecto y uno directo en la misma frase",
            "Aplicar la regla \"le/les se convierte en se\" ante lo, la, los, las",
            "Colocar los pronombres combinados en la posición correcta según la forma verbal",
        ],
        "content": {
            "intro": "Cuando una frase tiene tanto un objeto directo como uno indirecto y ambos se sustituyen por pronombres, el español los combina en un orden fijo — y con una transformación que sorprende a muchos estudiantes.",
            "explanation": "<p>El orden fijo es siempre <strong>objeto indirecto + objeto directo</strong>: <em>Te lo digo</em> (te = indirecto, lo = directo). Pero cuando el pronombre de objeto indirecto sería <strong>le</strong> o <strong>les</strong> y va seguido de <strong>lo, la, los</strong> o <strong>las</strong>, <em>le/les se convierte en se</em> para evitar el choque de sonidos \"le lo\": <em>Se lo dije</em> (no \"le lo dije\"), donde <em>se</em> sustituye a le/les y <em>lo</em> es el objeto directo.</p><p>Este <em>se</em> combinado no tiene relación con el se reflexivo ni con la pasiva refleja — es simplemente la forma que toma le/les antes de un pronombre de objeto directo que empieza por l-.</p>",
            "rules": [
                {"heading": "a) Orden fijo: indirecto + directo", "body": "<p><em>Me lo dan. Te la explico. Nos los envían.</em></p>"},
                {"heading": "b) Le/les → se ante lo/la/los/las", "body": "<p><em>Le doy el libro a Juan</em> → <em>Se lo doy.</em> (no \"le lo doy\") <em>Les cuento la noticia a mis padres</em> → <em>Se la cuento.</em></p>"},
                {"heading": "c) Posición: igual que un solo pronombre", "body": "<p>Antes del verbo conjugado, o pegados juntos al final del infinitivo/gerundio/imperativo afirmativo: <em>Se lo voy a decir</em> / <em>Voy a decírselo</em> (con tilde añadida); <em>Dímelo.</em></p>"},
            ],
            "examples": [
                "¿Me lo puedes explicar otra vez, por favor?",
                "Se lo conté todo a mi mejor amiga ayer.",
                "Te la presto con mucho gusto, no hay problema.",
                "Nos los enviaron por correo la semana pasada.",
                "Ya se lo dijimos varias veces, pero no nos hace caso.",
                "¿Podrías dármelo cuando termines de usarlo?",
                "Se las regalé a mis sobrinas por su cumpleaños.",
                "Explícaselo con calma, todavía no lo entiende bien.",
            ],
            "commonMistakes": [
                {"wrong": "Le lo di ayer por la tarde.", "right": "Se lo di ayer por la tarde.", "why": "Le se convierte en se antes de lo, para evitar el choque de sonidos entre los dos pronombres."},
                {"wrong": "Lo te digo mañana.", "right": "Te lo digo mañana.", "why": "El orden fijo es siempre objeto indirecto primero, objeto directo después: te lo, no lo te."},
                {"wrong": "Voy a decirlo se mañana.", "right": "Voy a decírselo mañana. / Se lo voy a decir mañana.", "why": "Los dos pronombres combinados se pegan juntos al infinitivo (con tilde añadida) o van juntos antes del verbo conjugado, nunca separados."},
            ],
        },
        "exercises": [
            {"id": "b1pc-fill", "type": "fill-blank", "title": "Combina los Pronombres",
             "items": [
                {"id": "b1pc1", "prompt": "Le presté el coche a mi hermano. → ___ presté.", "answers": [["Se lo"]], "options": ["Se lo", "Le lo", "Lo le"], "explanation": "Le se convierte en se antes de lo: se lo presté."},
                {"id": "b1pc2", "prompt": "Te doy la información ahora mismo. → ___ doy ahora mismo.", "answers": [["Te la"]], "options": ["Te la", "La te", "Se la"], "explanation": "Orden fijo: indirecto (te) + directo (la), sin necesidad de cambiar te por se."},
             ]},
            {"id": "b1pc-mc", "type": "multiple-choice", "title": "Elige la Combinación Correcta",
             "items": [
                {"id": "b1pc3", "prompt": "\"Les envié los documentos a mis colegas.\" → ¿Cómo se combina?", "options": ["Les los envié.", "Se los envié.", "Los les envié."], "answerIndex": 1, "explanation": "Les se convierte en se antes de los, y el orden es indirecto + directo: se los envié."},
             ]},
            {"id": "b1pc-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1pc4", "incorrect": "Le las regalé a mi madre por su cumpleaños.", "answer": ["Se las regalé a mi madre por su cumpleaños."], "explanation": "Le se convierte en se antes de las, siguiendo la misma regla que con lo/la/los."},
             ]},
        ],
        "summary": [
            "El orden fijo de los pronombres combinados es siempre objeto indirecto + objeto directo.",
            "Le y les se convierten en se cuando van seguidos de lo, la, los o las, para evitar el choque de sonidos.",
            "Los dos pronombres combinados se mueven siempre juntos: antes del verbo conjugado, o pegados al final del infinitivo, gerundio o imperativo afirmativo.",
        ],
    },
    {
        "id": "b1-por-y-para",
        "level": "B1", "unit": "1", "order": 11, "skill": "grammar", "strand": "preposiciones",
        "title": "Por y Para",
        "subtitle": "Dos preposiciones que se traducen igual en muchos idiomas, pero significan cosas muy distintas.",
        "objectives": [
            "Usar por para causa, medio, intercambio y movimiento a través de un lugar",
            "Usar para para finalidad, destinatario, destino y plazo límite",
            "Distinguir por y para en frases donde ambas parecen posibles a primera vista",
        ],
        "content": {
            "intro": "Por y para es una de las distinciones más consultadas por cualquier estudiante de español, precisamente porque muchos idiomas usan una sola palabra donde el español distingue causa de finalidad.",
            "explanation": "<p>Una forma útil de recordarlo: <strong>por</strong> mira hacia atrás — la causa, el origen, el motivo de algo (<em>por qué</em> pasó); <strong>para</strong> mira hacia adelante — el objetivo, el destino, el resultado que se busca (<em>para qué</em> sirve). Esta intuición cubre la mayoría de los casos, aunque hay usos fijos que conviene memorizar aparte.</p>",
            "rules": [
                {"heading": "a) Usos de por", "body": "<ul><li>Causa/motivo: <em>Llegué tarde por el tráfico.</em></li><li>Medio: <em>Te llamo por teléfono.</em></li><li>Intercambio/precio: <em>Compré el coche por diez mil euros.</em></li><li>Movimiento a través de un lugar: <em>Caminamos por el parque.</em></li><li>Periodo aproximado de tiempo: <em>Nos vemos por la tarde.</em></li><li>Agente de la voz pasiva: <em>Escrito por Cervantes.</em></li></ul>"},
                {"heading": "b) Usos de para", "body": "<ul><li>Finalidad/propósito: <em>Estudio para aprender, no solo para aprobar.</em></li><li>Destinatario: <em>Este regalo es para ti.</em></li><li>Destino/dirección: <em>Salgo para Buenos Aires mañana.</em></li><li>Plazo límite: <em>Necesito esto para el viernes.</em></li><li>Opinión personal: <em>Para mí, esta es la mejor opción.</em></li></ul>"},
                {"heading": "c) Un mismo verbo, significado distinto", "body": "<ul><li><em>Trabajo por mi familia.</em> (motivo: por ellos, para ayudarlos)</li><li><em>Trabajo para mi familia.</em> (destinatario/empleador: ellos son quienes me emplean)</li></ul>"},
            ],
            "examples": [
                "Caminamos por la playa durante casi dos horas.",
                "Este libro es para mi hermana, le encanta leer.",
                "Cambié mi coche viejo por uno más nuevo.",
                "Necesito el informe listo para el lunes por la mañana.",
                "Gracias por tu ayuda con la mudanza.",
                "Salimos para el aeropuerto dentro de una hora.",
                "Para aprender bien un idioma, hay que practicar todos los días.",
                "Pasamos por tu casa antes de ir al cine.",
            ],
            "commonMistakes": [
                {"wrong": "Este regalo es por ti.", "right": "Este regalo es para ti.", "why": "El destinatario de algo siempre usa para, no por."},
                {"wrong": "Gracias para tu ayuda.", "right": "Gracias por tu ayuda.", "why": "Dar las gracias por un motivo o causa siempre usa por, no para."},
                {"wrong": "Necesito esto por el viernes.", "right": "Necesito esto para el viernes.", "why": "Un plazo límite en el futuro siempre usa para, no por."},
            ],
        },
        "exercises": [
            {"id": "b1pp-fill", "type": "fill-blank", "title": "Completa con Por o Para",
             "items": [
                {"id": "b1pp1", "prompt": "Este regalo es ___ mi madre.", "answers": [["para"]], "options": ["por", "para"], "explanation": "Destinatario de algo: siempre para."},
                {"id": "b1pp2", "prompt": "Llegamos tarde ___ el tráfico.", "answers": [["por"]], "options": ["por", "para"], "explanation": "Causa o motivo: siempre por."},
                {"id": "b1pp3", "prompt": "Necesito el proyecto terminado ___ el viernes.", "answers": [["para"]], "options": ["por", "para"], "explanation": "Plazo límite en el futuro: siempre para."},
             ]},
            {"id": "b1pp-mc", "type": "multiple-choice", "title": "Elige la Preposición Correcta",
             "items": [
                {"id": "b1pp4", "prompt": "\"Caminamos ___ el centro de la ciudad.\" (a través de)", "options": ["por", "para"], "answerIndex": 0, "explanation": "Movimiento a través de un lugar siempre usa por."},
                {"id": "b1pp5", "prompt": "\"___ mí, esta es la mejor solución.\" (opinión personal)", "options": ["Por", "Para"], "answerIndex": 1, "explanation": "Dar una opinión personal siempre usa para."},
             ]},
            {"id": "b1pp-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1pp6", "incorrect": "Salimos por Buenos Aires mañana por la mañana.", "answer": ["Salimos para Buenos Aires mañana por la mañana."], "explanation": "El destino de un viaje se expresa con para, no con por; por la mañana sí es correcto, ya que expresa un periodo de tiempo."},
            ]},
        ],
        "summary": [
            "Por mira hacia la causa, el motivo, el medio, el intercambio y el movimiento a través de un lugar.",
            "Para mira hacia la finalidad, el destinatario, el destino, el plazo límite y la opinión personal.",
            "Un mismo verbo puede cambiar de significado según se use por o para, así que conviene pensar siempre en la dirección: hacia atrás (por) o hacia adelante (para).",
        ],
    },
    {
        "id": "b1-oraciones-relativas",
        "level": "B1", "unit": "1", "order": 12, "skill": "grammar", "strand": "relativas",
        "title": "Oraciones Relativas: Que, Quien, Donde",
        "subtitle": "Cómo unir dos frases en una sola usando un pronombre o adverbio relativo.",
        "objectives": [
            "Usar que como el relativo más general, para personas y cosas",
            "Usar quien/quienes tras una preposición, y donde para lugares",
            "Distinguir oraciones relativas especificativas de las explicativas (con o sin comas)",
        ],
        "content": {
            "intro": "Las oraciones relativas evitan repetir el mismo sustantivo dos veces, uniendo dos ideas en una sola frase más fluida y natural.",
            "explanation": "<p><strong>Que</strong> es, con diferencia, el relativo más usado en español: sirve tanto para personas como para cosas, y funciona como sujeto u objeto de la oración relativa. <strong>Quien/quienes</strong> se usa casi siempre después de una preposición cuando se refiere a personas (<em>la persona con quien hablé</em>), y <strong>donde</strong> sustituye a un lugar (<em>la ciudad donde nací</em>).</p><p>Una distinción importante: las oraciones relativas <strong>especificativas</strong> (sin comas) restringen de qué se habla exactamente (<em>los estudiantes que aprobaron el examen</em> — solo esos, no todos); las <strong>explicativas</strong> (entre comas) añaden información extra sobre algo ya identificado (<em>mi hermano, que vive en Chile, viene a visitarnos</em> — solo tengo un hermano, y la información es adicional).</p>",
            "rules": [
                {"heading": "a) Que — el más general", "body": "<p>Para personas y cosas, como sujeto u objeto: <em>El libro que compré es muy interesante. La chica que vive al lado es simpática.</em></p>"},
                {"heading": "b) Quien/quienes — tras preposición, solo personas", "body": "<p><em>La persona con quien trabajo es muy amable. Los amigos con quienes viajé son de Perú.</em> (concuerda en número con el antecedente)</p>"},
                {"heading": "c) Donde — para lugares", "body": "<p><em>Este es el pueblo donde nací. No sé el restaurante donde quedamos.</em></p>"},
                {"heading": "d) Especificativa vs. explicativa", "body": "<p>Sin comas (especificativa): <em>Los alumnos que estudiaron aprobaron.</em> (solo algunos) Con comas (explicativa): <em>Los alumnos, que estudiaron mucho, aprobaron.</em> (todos, información añadida)</p>"},
            ],
            "examples": [
                "El coche que compré el año pasado ya tiene un problema.",
                "La mujer con quien hablé en la fiesta es escritora.",
                "Este es el barrio donde crecí de pequeño.",
                "Mi hermana, que vive en Argentina, viene a visitarnos en verano.",
                "Los libros que más me gustan son de misterio.",
                "El profesor con quien estudié español es excelente.",
                "No recuerdo el nombre del hotel donde nos alojamos.",
                "Los estudiantes que llegaron tarde no pudieron entrar al examen.",
            ],
            "commonMistakes": [
                {"wrong": "La persona que trabajo es muy amable.", "right": "La persona con quien trabajo es muy amable.", "why": "Después de una preposición como con, se prefiere quien para referirse a personas, no que solo."},
                {"wrong": "El pueblo que nací es muy pequeño.", "right": "El pueblo donde nací es muy pequeño.", "why": "Para lugares, se usa donde, no que, cuando el sentido es \"en el que\"."},
                {"wrong": "Mi hermano que vive en Chile, viene a visitarnos.", "right": "Mi hermano, que vive en Chile, viene a visitarnos.", "why": "Como solo hay un hermano y la información es adicional, la oración es explicativa y necesita comas en ambos lados."},
            ],
        },
        "exercises": [
            {"id": "b1or-fill", "type": "fill-blank", "title": "Completa con el Relativo Correcto",
             "items": [
                {"id": "b1or1", "prompt": "Este es el restaurante ___ celebramos mi cumpleaños.", "answers": [["donde"]], "options": ["donde", "que", "quien"], "explanation": "Restaurante es un lugar, así que corresponde donde."},
                {"id": "b1or2", "prompt": "La chica con ___ estudio español es de Brasil.", "answers": [["quien"]], "options": ["quien", "que", "donde"], "explanation": "Después de la preposición con, y refiriéndose a una persona, corresponde quien."},
                {"id": "b1or3", "prompt": "El libro ___ me regalaste me encantó.", "answers": [["que"]], "options": ["que", "quien", "donde"], "explanation": "Que es el relativo general, válido tanto para personas como para cosas."},
             ]},
            {"id": "b1or-mc", "type": "multiple-choice", "title": "¿Especificativa o Explicativa?",
             "items": [
                {"id": "b1or4", "prompt": "\"Los estudiantes que estudiaron aprobaron el examen.\" (sin comas) significa que...", "options": ["todos los estudiantes aprobaron", "solo los que estudiaron aprobaron", "nadie aprobó"], "answerIndex": 1, "explanation": "Sin comas, la oración relativa restringe de quiénes se habla: solo los que estudiaron."},
             ]},
            {"id": "b1or-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1or5", "incorrect": "El pueblo que nací tiene solo mil habitantes.", "answer": ["El pueblo donde nací tiene solo mil habitantes."], "explanation": "Para un lugar con el sentido de \"en el que\", se usa donde, no que."},
            ]},
        ],
        "summary": [
            "Que es el relativo más general, válido para personas y cosas como sujeto u objeto de la oración relativa.",
            "Quien/quienes se usa tras preposición para personas; donde sustituye a un lugar.",
            "Sin comas, la relativa especifica de quién o qué se habla exactamente; con comas, añade información extra sobre algo ya identificado.",
        ],
    },
    {
        "id": "b1-voseo-argentino-y-variedades",
        "level": "B1", "unit": "1", "order": 13, "skill": "grammar", "strand": "variacion",
        "title": "El Voseo Argentino y Otras Variedades del Español",
        "subtitle": "Vos hablás, vos tenés, vos sos: la segunda persona informal en gran parte de Sudamérica.",
        "objectives": [
            "Conjugar el presente de indicativo y el imperativo con vos",
            "Reconocer en qué países el voseo es la forma habitual",
            "Identificar otras diferencias léxicas frecuentes entre variedades del español",
        ],
        "content": {
            "intro": "El español no es un idioma monolítico: en Argentina, Uruguay, Paraguay y partes de Centroamérica, el pronombre vos sustituye a tú como forma informal, con su propia conjugación.",
            "explanation": "<p>El <strong>voseo</strong> usa el pronombre <strong>vos</strong> en lugar de <em>tú</em>, con una conjugación propia en presente: se toma el infinitivo, se quita la <strong>-r</strong> final, y se añade tilde en la última vocal (<em>hablar → vos hablás; comer → vos comés; vivir → vos vivís</em>). El verbo <strong>ser</strong> es irregular: <em>vos sos</em> (no vos eres). El imperativo afirmativo también es distinto: se quita la <strong>-r</strong> final del infinitivo y se mantiene la tilde (<em>hablá, comé, viví</em>).</p><p>Fuera de la gramática, el español varía mucho en vocabulario según la región: una misma cosa puede tener nombres distintos en España, México, Argentina o el Caribe. Reconocer estas variedades es tan importante como dominar la gramática estándar, porque te prepara para entender español real de cualquier país.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Tú frente a vos — presente e imperativo</caption><thead><tr><th>Verbo</th><th>tú (presente)</th><th>vos (presente)</th><th>vos (imperativo)</th></tr></thead><tbody><tr><td>hablar</td><td>hablas</td><td>hablás</td><td>hablá</td></tr><tr><td>comer</td><td>comes</td><td>comés</td><td>comé</td></tr><tr><td>vivir</td><td>vives</td><td>vivís</td><td>viví</td></tr><tr><td>ser</td><td>eres</td><td>sos</td><td>sé</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Formación del presente con vos", "body": "<p>Infinitivo sin -r + tilde en la última vocal: <em>hablar → hablás, tener → tenés, venir → venís.</em></p>"},
                {"heading": "b) Países donde el voseo es la norma", "body": "<p>Argentina, Uruguay, Paraguay, y en distintos grados en Centroamérica (sobre todo Costa Rica y partes de Nicaragua, Guatemala, El Salvador, Honduras).</p>"},
                {"heading": "c) Algunas diferencias léxicas frecuentes", "body": "<ul><li><em>autobús</em> (España) / <em>camión</em> (México) / <em>colectivo</em> (Argentina) / <em>guagua</em> (Caribe)</li><li><em>ordenador</em> (España) / <em>computadora</em> (América Latina)</li><li><em>coger</em> (España, \"tomar/agarrar\") tiene una connotación vulgar en varios países de América Latina, donde se prefiere <em>tomar</em> o <em>agarrar</em></li></ul>"},
            ],
            "examples": [
                "Vos hablás muy bien español, ¿dónde lo aprendiste?",
                "¿Vos querés venir con nosotros esta noche?",
                "Che, vení un momento, necesito tu ayuda.",
                "Vos sos de Buenos Aires, ¿no?",
                "Tomá el colectivo en la esquina, pasa cada diez minutos.",
                "En España se dice ordenador; en México, computadora.",
                "En Argentina, el autobús urbano se llama colectivo.",
                "Vos tenés razón, no lo había pensado así.",
            ],
            "commonMistakes": [
                {"wrong": "Vos hablas muy bien español.", "right": "Vos hablás muy bien español.", "why": "El voseo tiene su propia conjugación, con tilde en la última vocal (hablás), distinta de la forma de tú (hablas)."},
                {"wrong": "Vos eres de Argentina.", "right": "Vos sos de Argentina.", "why": "Ser es irregular en el voseo: sos, no eres, que corresponde a la forma de tú."},
                {"wrong": "pensar que el voseo es \"incorrecto\" o \"informal de mala calidad\"", "right": "reconocer el voseo como una norma regional plenamente correcta y estándar en varios países", "why": "El voseo es la forma habitual e incluso oficial en Argentina, Uruguay y Paraguay, no una desviación del español estándar."},
            ],
        },
        "exercises": [
            {"id": "b1vo-fill", "type": "fill-blank", "title": "Conjuga con Vos",
             "items": [
                {"id": "b1vo1", "prompt": "Vos ___ (hablar) muy bien inglés.", "answers": [["hablás"]], "options": ["hablás", "hablas", "hablái"], "explanation": "Vos + hablar = hablás, con tilde en la última vocal."},
                {"id": "b1vo2", "prompt": "¿Vos ___ (tener) tiempo para ayudarme hoy?", "answers": [["tenés"]], "options": ["tenés", "tienes", "tenís"], "explanation": "Vos + tener = tenés, sin el cambio de raíz de la forma de tú."},
             ]},
            {"id": "b1vo-mc", "type": "multiple-choice", "title": "Vocabulario Regional",
             "items": [
                {"id": "b1vo3", "prompt": "¿Cómo se dice \"computadora\" en España?", "options": ["ordenador", "computador", "máquina"], "answerIndex": 0, "explanation": "En España se usa ordenador; en América Latina, computadora."},
                {"id": "b1vo4", "prompt": "¿En qué países el voseo es la forma estándar de segunda persona informal?", "options": ["España y México", "Argentina, Uruguay y Paraguay", "Solo en Argentina"], "answerIndex": 1, "explanation": "El voseo es la norma estándar en Argentina, Uruguay y Paraguay, y frecuente también en partes de Centroamérica."},
             ]},
            {"id": "b1vo-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "b1vo5", "statement": "El voseo es una forma incorrecta o vulgar del español.", "answer": False, "explanation": "El voseo es una norma regional plenamente correcta, oficial y estándar en varios países hispanohablantes."},
            ]},
        ],
        "summary": [
            "El voseo usa vos en lugar de tú, con conjugación propia en presente (hablás, comés, vivís) e imperativo (hablá, comé, viví).",
            "Es la forma estándar en Argentina, Uruguay, Paraguay, y frecuente en partes de Centroamérica.",
            "El vocabulario también varía mucho por región; reconocer estas diferencias es clave para entender español real de cualquier país.",
        ],
    },
    {
        "id": "b1-conectores-y-marcadores-del-discurso",
        "level": "B1", "unit": "1", "order": 14, "skill": "functional", "strand": "conectores",
        "title": "Conectores y Marcadores del Discurso",
        "subtitle": "Sin embargo, además, por lo tanto, en primer lugar: para organizar un texto o una conversación más larga.",
        "objectives": [
            "Usar conectores de contraste, consecuencia y adición en un registro más formal",
            "Organizar una explicación con marcadores de orden (en primer lugar, por último)",
            "Reconocer conectores frecuentes en textos de opinión y argumentación sencilla",
        ],
        "content": {
            "intro": "A partir de B1 empiezas a construir textos y explicaciones más largas, y los conectores del discurso son la herramienta que mantiene esas ideas conectadas de forma clara y ordenada.",
            "explanation": "<p>Frente a los conectores básicos de A2 (y, pero, porque), en B1 conviene incorporar un registro algo más formal, típico de una explicación organizada, una opinión escrita o un discurso más cuidado. <strong>Sin embargo</strong> y <strong>no obstante</strong> contrastan como pero, pero en un registro más formal; <strong>por lo tanto</strong> y <strong>por consiguiente</strong> marcan consecuencia como entonces, también en un registro más formal.</p><p>Los marcadores de orden (<strong>en primer lugar, en segundo lugar, por último, finalmente</strong>) organizan una explicación en pasos, y son especialmente útiles para estructurar una opinión con varios argumentos.</p>",
            "rules": [
                {"heading": "a) Contraste formal", "body": "<p><em>sin embargo, no obstante</em>: <em>El plan parecía perfecto; sin embargo, surgieron varios problemas.</em></p>"},
                {"heading": "b) Consecuencia formal", "body": "<p><em>por lo tanto, por consiguiente</em>: <em>No estudió lo suficiente; por lo tanto, no aprobó el examen.</em></p>"},
                {"heading": "c) Adición formal", "body": "<p><em>además, asimismo, también</em>: <em>El hotel es cómodo; además, está muy bien situado.</em></p>"},
                {"heading": "d) Marcadores de orden", "body": "<p><em>en primer lugar, en segundo lugar, por un lado / por otro lado, por último, finalmente</em>: útiles para organizar varios argumentos en un texto de opinión.</p>"},
            ],
            "examples": [
                "El proyecto tenía buena pinta; sin embargo, se retrasó varios meses.",
                "No llegamos a tiempo; por lo tanto, perdimos el tren.",
                "El apartamento es pequeño; no obstante, está muy bien ubicado.",
                "En primer lugar, quiero agradecer a todos por venir hoy.",
                "Por un lado, me gusta el plan; por otro lado, me preocupa el costo.",
                "El curso es exigente; asimismo, es muy completo y bien organizado.",
                "Finalmente, quiero destacar el esfuerzo de todo el equipo.",
                "No teníamos suficiente dinero; por consiguiente, cambiamos de planes.",
            ],
            "commonMistakes": [
                {"wrong": "El plan era bueno, sin embargo funcionó perfectamente.", "right": "El plan era bueno y, además, funcionó perfectamente.", "why": "Sin embargo introduce un contraste; si la segunda idea confirma la primera en vez de contrastarla, corresponde un conector de adición como además."},
                {"wrong": "En primero lugar, quiero hablar del presupuesto.", "right": "En primer lugar, quiero hablar del presupuesto.", "why": "La expresión fija es en primer lugar, sin la o final de primero."},
                {"wrong": "Por lo tanto no estudió, suspendió el examen.", "right": "No estudió; por lo tanto, suspendió el examen.", "why": "Por lo tanto introduce la consecuencia, así que debe ir después de la causa, no antes."},
            ],
        },
        "exercises": [
            {"id": "b1cm-mc", "type": "multiple-choice", "title": "Elige el Conector Correcto",
             "items": [
                {"id": "b1cm1", "prompt": "\"El hotel es caro; ___, el servicio es excelente.\" (contraste)", "options": ["por lo tanto", "sin embargo", "además"], "answerIndex": 1, "explanation": "Sin embargo introduce un contraste entre las dos ideas."},
                {"id": "b1cm2", "prompt": "\"No estudiamos lo suficiente; ___ suspendimos el examen.\" (consecuencia)", "options": ["por lo tanto", "sin embargo", "asimismo"], "answerIndex": 0, "explanation": "Por lo tanto introduce la consecuencia lógica de la causa anterior."},
             ]},
            {"id": "b1cm-fill", "type": "fill-blank", "title": "Completa con el Marcador de Orden",
             "items": [
                {"id": "b1cm3", "prompt": "___, quiero hablar de los costos del proyecto. (para empezar una lista)", "answers": [["En primer lugar"]], "options": ["En primer lugar", "Por último", "Sin embargo"], "explanation": "En primer lugar introduce el primer punto de una explicación organizada."},
             ]},
            {"id": "b1cm-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b1cm4", "incorrect": "El curso es difícil, sin embargo aprendo mucho y me encanta.", "answer": ["El curso es difícil; sin embargo, aprendo mucho y me encanta. (correcto en cuanto al conector, solo revisar la puntuación)"], "explanation": "Sin embargo suele ir precedido de punto y coma o punto, y seguido de coma, para marcar con claridad la pausa del contraste."},
            ]},
        ],
        "summary": [
            "Sin embargo/no obstante contrastan en un registro formal; por lo tanto/por consiguiente marcan consecuencia; además/asimismo suman información.",
            "Los marcadores de orden (en primer lugar, por último, finalmente) organizan una explicación o una opinión en pasos claros.",
            "Elegir el conector equivocado puede invertir por completo la lógica de la frase, así que conviene pensar en la relación real entre las dos ideas antes de escribirlo.",
        ],
    },
]

# =======================================================================
# EXTRA_EXERCISES — bloques adicionales de práctica (lectura y ordenar
# frases) fusionados en cada lección por id.
# =======================================================================
EXTRA_EXERCISES = {
    "b1-perfecto-vs-indefinido-matices": [
        {"id": "b1x1-reading", "type": "reading-comprehension", "title": "Lectura: Dos Formas de Hablar del Pasado",
         "passage": "<p>Esta mañana he desayunado tarde porque me he dormido. Ayer, en cambio, desayuné a las siete en punto porque tenía una reunión temprano. Mi amiga mexicana me dijo: «Yo también desayuné tarde hoy», usando el indefinido para el mismo tipo de situación.</p>",
         "items": [
            {"id": "b1x1r1", "prompt": "¿Por qué la persona desayunó tarde esta mañana?", "options": ["Porque tenía una reunión", "Porque se durmió", "Porque no tenía hambre"], "answerIndex": 1, "explanation": "El texto dice: «porque me he dormido»."},
            {"id": "b1x1r2", "prompt": "¿A qué hora desayunó ayer?", "options": ["A las siete", "A las ocho", "A las nueve"], "answerIndex": 0, "explanation": "El texto dice: «desayuné a las siete en punto»."},
            {"id": "b1x1r3", "prompt": "¿Qué tiempo verbal usó la amiga mexicana para hablar de hoy?", "options": ["El perfecto compuesto", "El indefinido", "El imperfecto"], "answerIndex": 1, "explanation": "El texto dice que la amiga usó «desayuné», el indefinido, para hablar de hoy mismo."},
            {"id": "b1x1r4", "prompt": "¿El texto muestra una diferencia regional en el uso del pasado?", "options": ["Sí", "No"], "answerIndex": 0, "explanation": "El contraste entre \"he desayunado\" y \"desayuné\" para hechos de hoy ilustra la variación regional explicada en la lección."},
         ]},
        {"id": "b1x1-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x1o1", "prompt": "Ordena las palabras.", "words": ["Esta", "semana", "he", "trabajado", "mucho"], "explanation": "Periodo de tiempo no cerrado (esta semana) + haber + participio."},
            {"id": "b1x1o2", "prompt": "Ordena las palabras.", "words": ["El", "año", "pasado", "viví", "en", "Chile"], "explanation": "Marcador de tiempo cerrado (el año pasado) + verbo en indefinido."},
         ]},
    ],
    "b1-pluscuamperfecto": [
        {"id": "b1x2-reading", "type": "reading-comprehension", "title": "Lectura: Llegamos Tarde a la Fiesta",
         "passage": "<p>Cuando llegamos a la fiesta, ya se habían ido casi todos los invitados. Habíamos salido tarde de casa porque el coche no arrancaba. Nunca antes habíamos tenido tan mala suerte con un vehículo. Menos mal que algunos amigos todavía estaban allí cuando llegamos.</p>",
         "items": [
            {"id": "b1x2r1", "prompt": "¿Qué había pasado ya cuando llegaron a la fiesta?", "options": ["La fiesta no había empezado", "Casi todos los invitados se habían ido", "Nadie había llegado todavía"], "answerIndex": 1, "explanation": "El texto dice: «ya se habían ido casi todos los invitados»."},
            {"id": "b1x2r2", "prompt": "¿Por qué salieron tarde de casa?", "options": ["Porque se durmieron", "Porque el coche no arrancaba", "Porque olvidaron la dirección"], "answerIndex": 1, "explanation": "El texto dice: «porque el coche no arrancaba»."},
            {"id": "b1x2r3", "prompt": "¿Habían tenido antes tan mala suerte con un vehículo?", "options": ["Sí, muchas veces", "Nunca antes"], "answerIndex": 1, "explanation": "El texto dice: «Nunca antes habíamos tenido tan mala suerte»."},
            {"id": "b1x2r4", "prompt": "¿Encontraron a alguien conocido en la fiesta?", "options": ["Sí, algunos amigos", "No, estaba vacía"], "answerIndex": 0, "explanation": "El texto dice: «algunos amigos todavía estaban allí cuando llegamos»."},
         ]},
        {"id": "b1x2-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x2o1", "prompt": "Ordena las palabras.", "words": ["Cuando", "llegué", "el", "tren", "ya", "había", "salido"], "explanation": "Cuando + hecho puntual (indefinido) + hecho anterior (pluscuamperfecto)."},
            {"id": "b1x2o2", "prompt": "Ordena las palabras.", "words": ["Nunca", "antes", "habíamos", "visto", "algo", "así"], "explanation": "Nunca antes + pluscuamperfecto para expresar una experiencia anterior a un punto pasado."},
         ]},
    ],
    "b1-futuro-compuesto-y-condicional-simple": [
        {"id": "b1x3-reading", "type": "reading-comprehension", "title": "Lectura: Planificando el Proyecto",
         "passage": "<p>Para el viernes, ya habré terminado la primera parte del proyecto. Mi compañero dijo que él haría la segunda parte, pero todavía no la ha empezado. Serían las diez cuando me llamó para avisarme del retraso. Me gustaría terminar todo antes del fin de semana.</p>",
         "items": [
            {"id": "b1x3r1", "prompt": "¿Qué habrá terminado la persona para el viernes?", "options": ["Todo el proyecto", "La primera parte", "La segunda parte"], "answerIndex": 1, "explanation": "El texto dice: «Para el viernes, ya habré terminado la primera parte del proyecto»."},
            {"id": "b1x3r2", "prompt": "¿Qué dijo el compañero que haría?", "options": ["La primera parte", "La segunda parte", "Nada"], "answerIndex": 1, "explanation": "El texto dice: «Mi compañero dijo que él haría la segunda parte»."},
            {"id": "b1x3r3", "prompt": "¿A qué hora aproximadamente llamó el compañero?", "options": ["A las nueve", "A las diez", "A las once"], "answerIndex": 1, "explanation": "El texto dice: «Serían las diez cuando me llamó»."},
            {"id": "b1x3r4", "prompt": "¿Qué le gustaría a la persona?", "options": ["Cancelar el proyecto", "Terminar todo antes del fin de semana", "Trabajar solo"], "answerIndex": 1, "explanation": "El texto dice: «Me gustaría terminar todo antes del fin de semana»."},
         ]},
        {"id": "b1x3-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x3o1", "prompt": "Ordena las palabras.", "words": ["Para", "mañana", "ya", "habré", "acabado", "esto"], "explanation": "Para + momento futuro + futuro compuesto (habré + participio)."},
            {"id": "b1x3o2", "prompt": "Ordena las palabras.", "words": ["¿Podrías", "ayudarme", "con", "esto", "por", "favor"], "explanation": "Condicional simple para una petición cortés + infinitivo + complemento."},
         ]},
    ],
    "b1-condicional-cortesia-e-hipotesis": [
        {"id": "b1x4-reading", "type": "reading-comprehension", "title": "Lectura: Un Consejo entre Amigos",
         "passage": "<p>—¿Te importaría darme tu opinión sobre esto?<br>—Claro. Yo que tú, hablaría con tu jefe directamente.<br>—Si tuviera más confianza, lo haría mañana mismo.<br>—Pues yo en tu lugar no esperaría más. Cuanto antes, mejor.</p>",
         "items": [
            {"id": "b1x4r1", "prompt": "¿Qué le pide la primera persona a su amigo?", "options": ["Dinero", "Su opinión", "Ayuda con el trabajo"], "answerIndex": 1, "explanation": "El texto dice: «¿Te importaría darme tu opinión sobre esto?»."},
            {"id": "b1x4r2", "prompt": "¿Qué consejo le da el amigo?", "options": ["Que espere más tiempo", "Que hable con su jefe directamente", "Que no diga nada"], "answerIndex": 1, "explanation": "El texto dice: «Yo que tú, hablaría con tu jefe directamente»."},
            {"id": "b1x4r3", "prompt": "¿Qué necesitaría la primera persona para hacerlo mañana?", "options": ["Más tiempo", "Más confianza", "Más dinero"], "answerIndex": 1, "explanation": "El texto dice: «Si tuviera más confianza, lo haría mañana mismo»."},
            {"id": "b1x4r4", "prompt": "¿El amigo está de acuerdo con esperar más?", "options": ["Sí", "No"], "answerIndex": 1, "explanation": "El texto dice: «yo en tu lugar no esperaría más»."},
         ]},
        {"id": "b1x4-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x4o1", "prompt": "Ordena las palabras.", "words": ["¿Te", "importaría", "cerrar", "la", "puerta"], "explanation": "Petición cortés con condicional (importaría) + infinitivo + objeto."},
            {"id": "b1x4o2", "prompt": "Ordena las palabras.", "words": ["Yo", "que", "tú", "aceptaría", "esa", "oferta"], "explanation": "Yo que tú + condicional simple para dar un consejo."},
         ]},
    ],
    "b1-imperativo-negativo-y-pronombres": [
        {"id": "b1x5-reading", "type": "reading-comprehension", "title": "Lectura: Instrucciones para el Nuevo Empleado",
         "passage": "<p>No llegues tarde el primer día de trabajo. No hables mal de tus compañeros nunca. Si tienes dudas, no tengas miedo de preguntar. No le digas a nadie información confidencial sin permiso. Y sobre todo, no te olvides de sonreír.</p>",
         "items": [
            {"id": "b1x5r1", "prompt": "¿Qué no debe hacer el primer día de trabajo?", "options": ["Llegar tarde", "Sonreír", "Hacer preguntas"], "answerIndex": 0, "explanation": "El texto dice: «No llegues tarde el primer día de trabajo»."},
            {"id": "b1x5r2", "prompt": "¿Qué debe hacer si tiene dudas?", "options": ["Callarse", "No tener miedo de preguntar", "Buscar en internet"], "answerIndex": 1, "explanation": "El texto dice: «no tengas miedo de preguntar»."},
            {"id": "b1x5r3", "prompt": "¿Qué información no debe compartir sin permiso?", "options": ["Su opinión", "Información confidencial", "Su horario"], "answerIndex": 1, "explanation": "El texto dice: «No le digas a nadie información confidencial sin permiso»."},
            {"id": "b1x5r4", "prompt": "¿Qué recomendación cierra el texto?", "options": ["No olvidarse de sonreír", "No hablar mucho", "Trabajar muy rápido"], "answerIndex": 0, "explanation": "El texto termina: «no te olvides de sonreír»."},
         ]},
        {"id": "b1x5-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x5o1", "prompt": "Ordena las palabras.", "words": ["No", "le", "digas", "nada", "todavía"], "explanation": "No + pronombre indirecto + subjuntivo (digas) + objeto."},
            {"id": "b1x5o2", "prompt": "Ordena las palabras.", "words": ["No", "te", "preocupes", "por", "eso"], "explanation": "No + pronombre reflexivo + subjuntivo + complemento."},
         ]},
    ],
    "b1-subjuntivo-presente-formacion": [
        {"id": "b1x6-reading", "type": "reading-comprehension", "title": "Lectura: Deseos para el Nuevo Año",
         "passage": "<p>Espero que este año sea mejor que el anterior. Quiero que mi familia tenga buena salud y que todos podamos vernos más a menudo. Ojalá que consiga el trabajo que tanto deseo. Es importante que sigamos adelante, pase lo que pase.</p>",
         "items": [
            {"id": "b1x6r1", "prompt": "¿Qué espera la persona sobre este año?", "options": ["Que sea igual que el anterior", "Que sea mejor", "Que sea muy corto"], "answerIndex": 1, "explanation": "El texto dice: «Espero que este año sea mejor que el anterior»."},
            {"id": "b1x6r2", "prompt": "¿Qué desea para su familia?", "options": ["Más dinero", "Buena salud", "Un viaje juntos"], "answerIndex": 1, "explanation": "El texto dice: «Quiero que mi familia tenga buena salud»."},
            {"id": "b1x6r3", "prompt": "¿Qué espera conseguir la persona?", "options": ["Una casa nueva", "El trabajo que desea", "Un coche"], "answerIndex": 1, "explanation": "El texto dice: «Ojalá que consiga el trabajo que tanto deseo»."},
            {"id": "b1x6r4", "prompt": "¿Qué considera importante la persona al final?", "options": ["Descansar mucho", "Seguir adelante pase lo que pase", "No cambiar nada"], "answerIndex": 1, "explanation": "El texto termina: «Es importante que sigamos adelante, pase lo que pase»."},
         ]},
        {"id": "b1x6-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x6o1", "prompt": "Ordena las palabras.", "words": ["Espero", "que", "tengas", "un", "buen", "día"], "explanation": "Verbo de deseo + que + subjuntivo (tengas) + objeto."},
            {"id": "b1x6o2", "prompt": "Ordena las palabras.", "words": ["Ojalá", "que", "todo", "salga", "bien"], "explanation": "Ojalá + que + subjuntivo (salga) + adverbio."},
         ]},
    ],
    "b1-subjuntivo-deseo-duda-emocion": [
        {"id": "b1x7-reading", "type": "reading-comprehension", "title": "Lectura: Reacciones ante una Noticia",
         "passage": "<p>Me alegro de que hayas encontrado un piso tan bonito. Dudo que sea tan barato como dices, la verdad. Es una pena que no puedas mudarte antes de fin de mes. Espero que todo salga bien con la mudanza.</p>",
         "items": [
            {"id": "b1x7r1", "prompt": "¿De qué se alegra la persona?", "options": ["De un viaje", "De que su amigo haya encontrado piso", "De una fiesta"], "answerIndex": 1, "explanation": "El texto dice: «Me alegro de que hayas encontrado un piso tan bonito»."},
            {"id": "b1x7r2", "prompt": "¿Qué duda la persona sobre el piso?", "options": ["Que sea bonito", "Que sea tan barato", "Que esté disponible"], "answerIndex": 1, "explanation": "El texto dice: «Dudo que sea tan barato como dices»."},
            {"id": "b1x7r3", "prompt": "¿Qué es una pena, según el texto?", "options": ["Que el piso sea caro", "Que no pueda mudarse antes de fin de mes", "Que esté lejos"], "answerIndex": 1, "explanation": "El texto dice: «Es una pena que no puedas mudarte antes de fin de mes»."},
            {"id": "b1x7r4", "prompt": "¿Qué espera la persona sobre la mudanza?", "options": ["Que sea difícil", "Que todo salga bien", "Que se cancele"], "answerIndex": 1, "explanation": "El texto termina: «Espero que todo salga bien con la mudanza»."},
         ]},
        {"id": "b1x7-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x7o1", "prompt": "Ordena las palabras.", "words": ["Dudo", "que", "él", "tenga", "razón"], "explanation": "Dudar que + subjuntivo (tenga) + objeto."},
            {"id": "b1x7o2", "prompt": "Ordena las palabras.", "words": ["Me", "alegro", "de", "que", "vengas"], "explanation": "Alegrarse de que + subjuntivo (vengas)."},
         ]},
    ],
    "b1-voz-pasiva-y-pasiva-refleja": [
        {"id": "b1x8-reading", "type": "reading-comprehension", "title": "Lectura: Un Anuncio Inmobiliario",
         "passage": "<p>Se venden pisos nuevos en el centro de la ciudad. El edificio fue construido el año pasado por una empresa muy conocida. Se aceptan mascotas y se incluye una plaza de garaje. Aquí se habla español e inglés para atender a todo tipo de clientes.</p>",
         "items": [
            {"id": "b1x8r1", "prompt": "¿Qué se vende, según el anuncio?", "options": ["Coches", "Pisos nuevos", "Terrenos"], "answerIndex": 1, "explanation": "El texto dice: «Se venden pisos nuevos en el centro de la ciudad»."},
            {"id": "b1x8r2", "prompt": "¿Cuándo fue construido el edificio?", "options": ["Este año", "El año pasado", "Hace diez años"], "answerIndex": 1, "explanation": "El texto dice: «El edificio fue construido el año pasado»."},
            {"id": "b1x8r3", "prompt": "¿Se aceptan mascotas?", "options": ["Sí", "No"], "answerIndex": 0, "explanation": "El texto dice: «Se aceptan mascotas»."},
            {"id": "b1x8r4", "prompt": "¿Qué idiomas se hablan en la oficina?", "options": ["Solo español", "Español e inglés", "Solo inglés"], "answerIndex": 1, "explanation": "El texto dice: «se habla español e inglés»."},
         ]},
        {"id": "b1x8-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x8o1", "prompt": "Ordena las palabras.", "words": ["Se", "buscan", "camareros", "con", "experiencia"], "explanation": "Se + verbo (plural, concuerda con camareros) + complemento."},
            {"id": "b1x8o2", "prompt": "Ordena las palabras.", "words": ["El", "libro", "fue", "escrito", "por", "un", "autor", "famoso"], "explanation": "Voz pasiva con ser + participio + por + agente."},
         ]},
    ],
    "b1-estilo-indirecto-presente": [
        {"id": "b1x9-reading", "type": "reading-comprehension", "title": "Lectura: Un Mensaje de Voz",
         "passage": "<p>Mi hermano me dice que está en camino y que llegará en veinte minutos. Me pregunta si necesito algo del supermercado. También dice que su coche tiene un problema pequeño, pero que no es grave. Me pregunta dónde nos vemos exactamente.</p>",
         "items": [
            {"id": "b1x9r1", "prompt": "¿En cuánto tiempo dice que llegará el hermano?", "options": ["Diez minutos", "Veinte minutos", "Media hora"], "answerIndex": 1, "explanation": "El texto dice: «llegará en veinte minutos»."},
            {"id": "b1x9r2", "prompt": "¿Qué pregunta sobre el supermercado?", "options": ["Si van a ir juntos", "Si necesita algo", "Si está cerrado"], "answerIndex": 1, "explanation": "El texto dice: «Me pregunta si necesito algo del supermercado»."},
            {"id": "b1x9r3", "prompt": "¿Qué problema tiene el coche?", "options": ["Un problema grave", "Un problema pequeño", "No tiene ningún problema"], "answerIndex": 1, "explanation": "El texto dice: «su coche tiene un problema pequeño, pero que no es grave»."},
            {"id": "b1x9r4", "prompt": "¿Qué pregunta al final del mensaje?", "options": ["A qué hora llega", "Dónde se ven exactamente", "Qué van a comer"], "answerIndex": 1, "explanation": "El texto termina: «Me pregunta dónde nos vemos exactamente»."},
         ]},
        {"id": "b1x9-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x9o1", "prompt": "Ordena las palabras.", "words": ["Ella", "dice", "que", "está", "muy", "ocupada"], "explanation": "Sujeto + decir que + verbo en indicativo (informa de un hecho)."},
            {"id": "b1x9o2", "prompt": "Ordena las palabras.", "words": ["Me", "pregunta", "si", "voy", "a", "la", "fiesta"], "explanation": "Preguntar + si (pregunta de sí/no) + verbo en indicativo."},
         ]},
    ],
    "b1-pronombres-combinados": [
        {"id": "b1x10-reading", "type": "reading-comprehension", "title": "Lectura: Un Favor entre Vecinos",
         "passage": "<p>—Necesito el taladro que te presté la semana pasada. ¿Me lo puedes devolver hoy?<br>—Claro, te lo devuelvo esta tarde sin problema.<br>—Perfecto. Ah, y si necesitas la escalera, te la puedo prestar también.<br>—Muchas gracias, te lo agradezco mucho.</p>",
         "items": [
            {"id": "b1x10r1", "prompt": "¿Qué objeto pide de vuelta la primera persona?", "options": ["Una escalera", "Un taladro", "Un martillo"], "answerIndex": 1, "explanation": "El texto dice: «Necesito el taladro que te presté la semana pasada»."},
            {"id": "b1x10r2", "prompt": "¿Cuándo devolverá el taladro?", "options": ["Mañana", "Esta tarde", "La próxima semana"], "answerIndex": 1, "explanation": "El texto dice: «te lo devuelvo esta tarde»."},
            {"id": "b1x10r3", "prompt": "¿Qué otro objeto se ofrece a prestar?", "options": ["Un taladro", "Una escalera", "Una silla"], "answerIndex": 1, "explanation": "El texto dice: «si necesitas la escalera, te la puedo prestar también»."},
            {"id": "b1x10r4", "prompt": "¿Cómo termina la conversación?", "options": ["Con un desacuerdo", "Con un agradecimiento", "Con una despedida fría"], "answerIndex": 1, "explanation": "El texto termina: «te lo agradezco mucho»."},
         ]},
        {"id": "b1x10-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x10o1", "prompt": "Ordena las palabras.", "words": ["Se", "lo", "expliqué", "todo", "ayer"], "explanation": "Le se convierte en se ante lo, seguido del verbo en indefinido."},
            {"id": "b1x10o2", "prompt": "Ordena las palabras.", "words": ["¿Me", "lo", "puedes", "explicar", "otra", "vez"], "explanation": "Pronombres combinados antes del verbo conjugado + infinitivo."},
         ]},
    ],
    "b1-por-y-para": [
        {"id": "b1x11-reading", "type": "reading-comprehension", "title": "Lectura: Un Viaje de Trabajo",
         "passage": "<p>Salgo para Buenos Aires mañana por la mañana por motivos de trabajo. Compré el billete por internet, y pagué bastante poco por él. Necesito terminar el informe para el lunes, así que trabajaré durante el vuelo. Para mí, viajar por trabajo siempre es agotador.</p>",
         "items": [
            {"id": "b1x11r1", "prompt": "¿Adónde viaja la persona?", "options": ["A Madrid", "A Buenos Aires", "A Lima"], "answerIndex": 1, "explanation": "El texto dice: «Salgo para Buenos Aires mañana por la mañana»."},
            {"id": "b1x11r2", "prompt": "¿Cómo compró el billete?", "options": ["En una agencia", "Por internet", "Por teléfono"], "answerIndex": 1, "explanation": "El texto dice: «Compré el billete por internet»."},
            {"id": "b1x11r3", "prompt": "¿Para cuándo necesita terminar el informe?", "options": ["Para el viernes", "Para el lunes", "Para el domingo"], "answerIndex": 1, "explanation": "El texto dice: «Necesito terminar el informe para el lunes»."},
            {"id": "b1x11r4", "prompt": "¿Qué opina la persona sobre viajar por trabajo?", "options": ["Que es divertido", "Que es agotador", "Que es fácil"], "answerIndex": 1, "explanation": "El texto termina: «viajar por trabajo siempre es agotador»."},
         ]},
        {"id": "b1x11-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x11o1", "prompt": "Ordena las palabras.", "words": ["Este", "regalo", "es", "para", "ti"], "explanation": "Ser + para (destinatario) + pronombre."},
            {"id": "b1x11o2", "prompt": "Ordena las palabras.", "words": ["Caminamos", "por", "el", "parque", "toda", "la", "tarde"], "explanation": "Verbo + por (a través de un lugar) + complemento + duración."},
         ]},
    ],
    "b1-oraciones-relativas": [
        {"id": "b1x12-reading", "type": "reading-comprehension", "title": "Lectura: Recuerdos de la Infancia",
         "passage": "<p>El pueblo donde nací es muy pequeño, pero tiene mucho encanto. Mi mejor amigo, que ahora vive en otro país, siempre me visita en verano. La escuela donde estudié se llama igual que la calle principal. Los profesores con quienes aprendí español fueron excelentes.</p>",
         "items": [
            {"id": "b1x12r1", "prompt": "¿Cómo describe la persona su pueblo natal?", "options": ["Grande y moderno", "Pequeño con encanto", "Aburrido"], "answerIndex": 1, "explanation": "El texto dice: «es muy pequeño, pero tiene mucho encanto»."},
            {"id": "b1x12r2", "prompt": "¿Dónde vive ahora el mejor amigo?", "options": ["En el mismo pueblo", "En otro país", "En la capital"], "answerIndex": 1, "explanation": "El texto dice: «que ahora vive en otro país»."},
            {"id": "b1x12r3", "prompt": "¿Cómo se llama la escuela?", "options": ["Como el pueblo", "Igual que la calle principal", "No tiene nombre"], "answerIndex": 1, "explanation": "El texto dice: «se llama igual que la calle principal»."},
            {"id": "b1x12r4", "prompt": "¿Cómo describe a los profesores de español?", "options": ["Muy exigentes", "Excelentes", "Aburridos"], "answerIndex": 1, "explanation": "El texto termina: «fueron excelentes»."},
         ]},
        {"id": "b1x12-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x12o1", "prompt": "Ordena las palabras.", "words": ["Este", "es", "el", "libro", "que", "leí"], "explanation": "Demostrativo + ser + sustantivo + que (relativo general) + verbo."},
            {"id": "b1x12o2", "prompt": "Ordena las palabras.", "words": ["Ese", "es", "el", "pueblo", "donde", "nací"], "explanation": "Demostrativo + ser + sustantivo (lugar) + donde + verbo."},
         ]},
    ],
    "b1-voseo-argentino-y-variedades": [
        {"id": "b1x13-reading", "type": "reading-comprehension", "title": "Lectura: Un Mensaje desde Buenos Aires",
         "passage": "<p>Che, ¿vos podés venir a mi casa esta noche? Tenés que traer algo para comer, si querés. Acá en Buenos Aires solemos cenar bastante tarde. Vos sos de España, ¿no? Va a ser interesante comparar nuestras formas de hablar.</p>",
         "items": [
            {"id": "b1x13r1", "prompt": "¿Qué le pide la persona a su amigo?", "options": ["Que la llame", "Que venga a su casa esta noche", "Que traiga dinero"], "answerIndex": 1, "explanation": "El texto dice: «¿vos podés venir a mi casa esta noche?»."},
            {"id": "b1x13r2", "prompt": "¿Qué debe traer, si quiere?", "options": ["Bebida", "Algo para comer", "Música"], "answerIndex": 1, "explanation": "El texto dice: «Tenés que traer algo para comer, si querés»."},
            {"id": "b1x13r3", "prompt": "¿A qué hora suelen cenar en Buenos Aires, según el texto?", "options": ["Temprano", "Bastante tarde", "Al mediodía"], "answerIndex": 1, "explanation": "El texto dice: «solemos cenar bastante tarde»."},
            {"id": "b1x13r4", "prompt": "¿De dónde es la persona a quien escribe?", "options": ["De Argentina", "De España", "De México"], "answerIndex": 1, "explanation": "El texto dice: «Vos sos de España, ¿no?»."},
         ]},
        {"id": "b1x13-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x13o1", "prompt": "Ordena las palabras.", "words": ["Vos", "hablás", "muy", "bien", "español"], "explanation": "Vos + forma verbal de voseo (hablás) + adverbio + adjetivo."},
            {"id": "b1x13o2", "prompt": "Ordena las palabras.", "words": ["¿Vos", "tenés", "tiempo", "hoy"], "explanation": "Vos + tener en voseo (tenés) + objeto + adverbio."},
         ]},
    ],
    "b1-conectores-y-marcadores-del-discurso": [
        {"id": "b1x14-reading", "type": "reading-comprehension", "title": "Lectura: Una Opinión sobre el Teletrabajo",
         "passage": "<p>El teletrabajo tiene muchas ventajas; sin embargo, también presenta algunos problemas. Por un lado, ahorras tiempo de transporte; por otro lado, es fácil sentirse aislado. Por lo tanto, muchas empresas prefieren un modelo mixto. Además, este modelo permite más flexibilidad para todos.</p>",
         "items": [
            {"id": "b1x14r1", "prompt": "¿Qué conector introduce un contraste en el texto?", "options": ["Además", "Sin embargo", "Por lo tanto"], "answerIndex": 1, "explanation": "El texto usa «sin embargo» para contrastar las ventajas con los problemas."},
            {"id": "b1x14r2", "prompt": "¿Qué ventaja del teletrabajo se menciona?", "options": ["Más dinero", "Ahorrar tiempo de transporte", "Menos trabajo"], "answerIndex": 1, "explanation": "El texto dice: «ahorras tiempo de transporte»."},
            {"id": "b1x14r3", "prompt": "¿Qué modelo prefieren muchas empresas, según el texto?", "options": ["Totalmente presencial", "Totalmente remoto", "Un modelo mixto"], "answerIndex": 2, "explanation": "El texto dice: «muchas empresas prefieren un modelo mixto»."},
            {"id": "b1x14r4", "prompt": "¿Qué añade el modelo mixto, según el texto?", "options": ["Más control", "Más flexibilidad", "Más reuniones"], "answerIndex": 1, "explanation": "El texto termina: «este modelo permite más flexibilidad para todos»."},
         ]},
        {"id": "b1x14-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b1x14o1", "prompt": "Ordena las palabras.", "words": ["El", "plan", "es", "bueno", "sin", "embargo", "es", "caro"], "explanation": "Idea + sin embargo (contraste) + segunda idea."},
            {"id": "b1x14o2", "prompt": "Ordena las palabras.", "words": ["No", "estudió", "por", "lo", "tanto", "suspendió"], "explanation": "Causa + por lo tanto (consecuencia) + resultado."},
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
    "b1-perfecto-vs-indefinido-matices": [
        {"id": "b1y1-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y1c1", "incorrect": "He nacido en 1995 en Madrid.", "answer": ["Nací en 1995 en Madrid."], "explanation": "Un año concreto como marcador cerrado siempre pide indefinido."},
            {"id": "b1y1c2", "incorrect": "He viajado a Chile en 2015.", "answer": ["Viajé a Chile en 2015."], "explanation": "Un marcador de tiempo cerrado exige indefinido, sin importar la variedad regional."},
         ]},
        {"id": "b1y1-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y1t1", "prompt": "Escribe una frase sobre una experiencia de tu vida usando el perfecto compuesto.", "explanation": "Guardado para tu propio repaso — ejemplo: «He viajado a tres países distintos.»"},
         ]},
    ],
    "b1-pluscuamperfecto": [
        {"id": "b1y2-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y2c1", "incorrect": "Cuando llegué, la película ya empezó.", "answer": ["Cuando llegué, la película ya había empezado."], "explanation": "Un hecho anterior a otro hecho pasado necesita el pluscuamperfecto."},
            {"id": "b1y2c2", "incorrect": "Habíamos escribido la carta antes de salir.", "answer": ["Habíamos escrito la carta antes de salir."], "explanation": "Escribir mantiene su participio irregular escrito también en el pluscuamperfecto."},
         ]},
        {"id": "b1y2-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y2t1", "prompt": "Escribe una frase con \"nunca antes había...\"", "explanation": "Guardado para tu propio repaso — ejemplo: «Nunca antes había visto una tormenta así.»"},
         ]},
    ],
    "b1-futuro-compuesto-y-condicional-simple": [
        {"id": "b1y3-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y3c1", "incorrect": "¿Puedrías ayudarme?", "answer": ["¿Podrías ayudarme?"], "explanation": "Poder usa la raíz irregular podr- también en condicional."},
            {"id": "b1y3c2", "incorrect": "Para mañana, ya habré terminaré el proyecto.", "answer": ["Para mañana, ya habré terminado el proyecto."], "explanation": "El futuro compuesto necesita el participio, no otra forma conjugada."},
         ]},
        {"id": "b1y3-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y3t1", "prompt": "Escribe una petición cortés usando el condicional.", "explanation": "Guardado para tu propio repaso — ejemplo: «¿Podrías cerrar la ventana, por favor?»"},
         ]},
    ],
    "b1-condicional-cortesia-e-hipotesis": [
        {"id": "b1y4-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y4c1", "incorrect": "Si tengo más dinero, viajaría más.", "answer": ["Si tuviera más dinero, viajaría más."], "explanation": "Una condición hipotética en presente necesita el imperfecto de subjuntivo."},
            {"id": "b1y4c2", "incorrect": "Yo que tú hablo con ella.", "answer": ["Yo que tú, hablaría con ella."], "explanation": "El consejo con yo que tú se expresa en condicional."},
         ]},
        {"id": "b1y4-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y4t1", "prompt": "Escribe una frase con \"yo que tú\" dando un consejo.", "explanation": "Guardado para tu propio repaso — ejemplo: «Yo que tú, aceptaría esa oferta.»"},
         ]},
    ],
    "b1-imperativo-negativo-y-pronombres": [
        {"id": "b1y5-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y5c1", "incorrect": "No hablas tan alto.", "answer": ["No hables tan alto."], "explanation": "El imperativo negativo de tú usa la forma del subjuntivo."},
            {"id": "b1y5c2", "incorrect": "No hazlo ahora.", "answer": ["No lo hagas ahora."], "explanation": "En el imperativo negativo, el pronombre va antes del verbo."},
         ]},
        {"id": "b1y5-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y5t1", "prompt": "Escribe una instrucción negativa con \"no\" + subjuntivo.", "explanation": "Guardado para tu propio repaso — ejemplo: «No hables tan rápido, por favor.»"},
         ]},
    ],
    "b1-subjuntivo-presente-formacion": [
        {"id": "b1y6-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y6c1", "incorrect": "Espero que tienes razón.", "answer": ["Espero que tengas razón."], "explanation": "Esperar que necesita subjuntivo, no indicativo."},
            {"id": "b1y6c2", "incorrect": "Quiero que él es feliz.", "answer": ["Quiero que él sea feliz."], "explanation": "Ser es totalmente irregular en subjuntivo: sea."},
         ]},
        {"id": "b1y6-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y6t1", "prompt": "Escribe un deseo usando \"espero que\" + subjuntivo.", "explanation": "Guardado para tu propio repaso — ejemplo: «Espero que tengas un buen día.»"},
         ]},
    ],
    "b1-subjuntivo-deseo-duda-emocion": [
        {"id": "b1y7-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y7c1", "incorrect": "Creo que él tenga razón.", "answer": ["Creo que él tiene razón."], "explanation": "Creer en afirmativo expresa certeza y pide indicativo."},
            {"id": "b1y7c2", "incorrect": "Quiero que yo vaya al cine.", "answer": ["Quiero ir al cine."], "explanation": "Con un solo sujeto se usa el infinitivo, no que + subjuntivo."},
         ]},
        {"id": "b1y7-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y7t1", "prompt": "Escribe una frase con \"dudo que\" o \"me alegro de que\".", "explanation": "Guardado para tu propio repaso — ambas expresiones activan el subjuntivo."},
         ]},
    ],
    "b1-voz-pasiva-y-pasiva-refleja": [
        {"id": "b1y8-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y8c1", "incorrect": "Se vende pisos en esta zona.", "answer": ["Se venden pisos en esta zona."], "explanation": "El verbo debe concordar en plural con pisos."},
            {"id": "b1y8c2", "incorrect": "El libro fue escribido por un autor famoso.", "answer": ["El libro fue escrito por un autor famoso."], "explanation": "El participio de escribir es escrito, también en la voz pasiva."},
         ]},
        {"id": "b1y8-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y8t1", "prompt": "Escribe un cartel usando la pasiva refleja con \"se\".", "explanation": "Guardado para tu propio repaso — ejemplo: «Se buscan camareros con experiencia.»"},
         ]},
    ],
    "b1-estilo-indirecto-presente": [
        {"id": "b1y9-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y9c1", "incorrect": "Me pregunta que si voy a la fiesta.", "answer": ["Me pregunta si voy a la fiesta."], "explanation": "Con preguntas de sí/no se usa solo si, sin añadir que."},
            {"id": "b1y9c2", "incorrect": "Ella dice que \"está cansada\".", "answer": ["Ella dice que está cansada."], "explanation": "El estilo indirecto no usa comillas."},
         ]},
        {"id": "b1y9-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y9t1", "prompt": "Convierte a estilo indirecto: \"Estoy muy ocupado.\" (dicho por un amigo)", "answer": [["dice que está muy ocupado", "mi amigo dice que está muy ocupado"]], "explanation": "El presente en la cita se mantiene con el verbo introductor en presente."},
         ]},
    ],
    "b1-pronombres-combinados": [
        {"id": "b1y10-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y10c1", "incorrect": "Le lo di ayer por la tarde.", "answer": ["Se lo di ayer por la tarde."], "explanation": "Le se convierte en se antes de lo."},
            {"id": "b1y10c2", "incorrect": "Lo te digo mañana.", "answer": ["Te lo digo mañana."], "explanation": "El orden fijo es objeto indirecto primero, directo después."},
         ]},
        {"id": "b1y10-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y10t1", "prompt": "Escribe una frase con \"se lo\" o \"me lo\".", "explanation": "Guardado para tu propio repaso — ejemplo: «Se lo expliqué todo ayer.»"},
         ]},
    ],
    "b1-por-y-para": [
        {"id": "b1y11-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y11c1", "incorrect": "Este regalo es por ti.", "answer": ["Este regalo es para ti."], "explanation": "El destinatario de algo siempre usa para."},
            {"id": "b1y11c2", "incorrect": "Gracias para tu ayuda.", "answer": ["Gracias por tu ayuda."], "explanation": "Dar las gracias por un motivo usa por."},
         ]},
        {"id": "b1y11-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y11t1", "prompt": "Escribe una frase usando \"por\" para expresar una causa.", "explanation": "Guardado para tu propio repaso — ejemplo: «Llegué tarde por el tráfico.»"},
         ]},
    ],
    "b1-oraciones-relativas": [
        {"id": "b1y12-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y12c1", "incorrect": "La persona que trabajo es muy amable.", "answer": ["La persona con quien trabajo es muy amable."], "explanation": "Después de una preposición se prefiere quien para personas."},
            {"id": "b1y12c2", "incorrect": "El pueblo que nací es muy pequeño.", "answer": ["El pueblo donde nací es muy pequeño."], "explanation": "Para lugares se usa donde, no que."},
         ]},
        {"id": "b1y12-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y12t1", "prompt": "Escribe una frase con \"donde\" describiendo un lugar importante para ti.", "explanation": "Guardado para tu propio repaso — ejemplo: «Este es el pueblo donde nací.»"},
         ]},
    ],
    "b1-voseo-argentino-y-variedades": [
        {"id": "b1y13-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y13c1", "incorrect": "Vos hablas muy bien español.", "answer": ["Vos hablás muy bien español."], "explanation": "El voseo tiene su propia conjugación, con tilde en la última vocal."},
            {"id": "b1y13c2", "incorrect": "Vos eres de Argentina.", "answer": ["Vos sos de Argentina."], "explanation": "Ser es irregular en el voseo: sos, no eres."},
         ]},
        {"id": "b1y13-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y13t1", "prompt": "Escribe una frase usando el voseo argentino.", "explanation": "Guardado para tu propio repaso — ejemplo: «Vos tenés razón.»"},
         ]},
    ],
    "b1-conectores-y-marcadores-del-discurso": [
        {"id": "b1y14-correction", "type": "correction", "title": "Corrige los Errores",
         "items": [
            {"id": "b1y14c1", "incorrect": "En primero lugar, quiero hablar del presupuesto.", "answer": ["En primer lugar, quiero hablar del presupuesto."], "explanation": "La expresión fija es en primer lugar, sin la o final."},
            {"id": "b1y14c2", "incorrect": "Por lo tanto no estudió, suspendió el examen.", "answer": ["No estudió; por lo tanto, suspendió el examen."], "explanation": "Por lo tanto introduce la consecuencia, debe ir después de la causa."},
         ]},
        {"id": "b1y14-typing", "type": "typing", "title": "Practica",
         "items": [
            {"id": "b1y14t1", "prompt": "Escribe dos frases conectadas con \"sin embargo\".", "explanation": "Guardado para tu propio repaso — sin embargo introduce un contraste entre dos ideas."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES_2.get(_lesson["id"], []))
