# -*- coding: utf-8 -*-
"""C2 — datos del currículo de nivel de maestría. Ver curriculum/SCHEMA.md
para la forma exacta del JSON que esto compila (scripts/generate_curriculum.py
hace la compilación). Escrito como Python en vez de JSON a mano para que el
texto en español con comillas, tildes y ñ se lea con naturalidad.

Curso monolingüe: los ejemplos son strings simples en español, sin
traducción al inglés en ningún campo."""

OVERVIEW = (
    "El nivel C2 es la cumbre de este curso: ya no se trata de aprender "
    "gramática nueva, sino de refinar un dominio que ya es prácticamente "
    "completo. Trabajarás la sintaxis compleja y la subordinación múltiple, "
    "el registro literario y sus recursos estilísticos, los matices léxicos "
    "y los falsos amigos más sutiles, la riqueza de la variación regional "
    "del español, la cohesión de un discurso extenso, la modalidad y la "
    "atenuación en el registro formal, algunas estructuras arcaicas o "
    "literarias que todo lector culto reconoce, y la capacidad de "
    "transformar deliberadamente tu registro según la situación. Al "
    "terminar este nivel tendrás un dominio del español prácticamente "
    "indistinguible del de un hablante culto nativo, en casi cualquier "
    "contexto imaginable."
)

LESSONS = [
    {
        "id": "c2-sintaxis-compleja-y-subordinacion-multiple",
        "level": "C2", "unit": "1", "order": 1, "skill": "grammar", "strand": "sintaxis",
        "title": "Sintaxis Compleja y Subordinación Múltiple",
        "subtitle": "Cómo encadenar varias subordinadas sin perder claridad ni corrección.",
        "objectives": [
            "Construir frases con varios niveles de subordinación encadenada",
            "Mantener la concordancia y la coherencia verbal a través de subordinadas anidadas",
            "Reescribir una frase excesivamente compleja para ganar claridad sin perder matiz",
        ],
        "content": {
            "intro": "A este nivel ya dominas cada tipo de subordinada por separado; el reto ahora es combinarlas con precisión, porque un texto culto y elaborado rara vez avanza con frases simples una detrás de otra.",
            "explanation": "<p>Una frase compleja puede anidar una subordinada sustantiva dentro de una relativa, dentro a su vez de una condicional, sin perder la corrección gramatical si cada verbo respeta las reglas que ya conoces: modo (indicativo/subjuntivo) según la subordinada de la que dependa directamente, y concordancia de tiempos según el verbo del que depende, no según el verbo principal de toda la frase.</p><p>El riesgo real de la subordinación múltiple no es la incorrección, sino la <strong>pérdida de claridad</strong>: cuantos más niveles se anidan, más fácil es que el lector pierda el hilo de a qué se refiere cada pronombre o cada verbo. Un buen estilo culto sabe cuándo dividir una frase demasiado cargada en dos, sin sacrificar la precisión del contenido.</p>",
            "rules": [
                {"heading": "a) Cada subordinada obedece a su propio verbo regente", "body": "<p>En <em>Dudo que quienes lleguen tarde puedan entrar</em>, quienes lleguen depende de una relativa con antecedente indefinido (subjuntivo por eso), y puedan depende de dudar que (subjuntivo por eso) — dos razones distintas para el mismo modo, no una sola regla que se herede automáticamente.</p>"},
                {"heading": "b) Concordancia de tiempos en cadena", "body": "<p><em>Me confesó que temía que, si no llegábamos a tiempo, se cancelaría todo.</em> — cada verbo retrocede según el que lo rige directamente: confesó (pasado) rige temía (imperfecto); temía rige el condicional se cancelaría a través de la hipotética.</p>"},
                {"heading": "c) Cuándo dividir una frase demasiado cargada", "body": "<p>Si una frase acumula más de tres niveles de subordinación, suele ganar en claridad si se divide en dos oraciones independientes, aunque se pierda algo de la elegancia sintáctica de un único periodo.</p>"},
            ],
            "examples": [
                "Quienes deseen que su solicitud sea considerada deberán presentarla antes de que finalice el plazo.",
                "Me temo que, si no hubiéramos insistido, jamás nos habrían dicho la verdad.",
                "No hay nadie que crea que esta decisión, por difícil que parezca, no sea la más razonable.",
                "El informe, que se había redactado con la esperanza de que convenciera al comité, resultó insuficiente.",
                "Dudaba que quienes lo criticaban tan duramente hubieran leído realmente su obra completa.",
                "Aunque sabía que, de haber actuado antes, todo habría sido distinto, prefirió no lamentarse.",
                "Es poco probable que quien haya vivido eso pueda olvidarlo con facilidad.",
                "Explicó que, si bien el proyecto avanzaba, aún quedaban decisiones que tomar antes de julio.",
            ],
            "commonMistakes": [
                {"wrong": "asumir que un solo modo verbal se aplica a toda la cadena de subordinadas", "right": "evaluar el modo de cada subordinada según el verbo del que depende directamente", "why": "Cada subordinada obedece a su propio verbo regente, no a una regla global heredada del verbo principal de toda la frase."},
                {"wrong": "acumular cinco o seis niveles de subordinación en una sola frase sin pausas", "right": "dividir la idea en dos frases cuando la subordinación se vuelve excesiva", "why": "Más allá de cierto punto, la subordinación múltiple perjudica la claridad, incluso si cada verbo está gramaticalmente bien formado."},
                {"wrong": "Me confesó que temía que se cancela todo.", "right": "Me confesó que temía que se cancelaría/cancelara todo.", "why": "La concordancia de tiempos exige retroceder el verbo de la subordinada más profunda según el verbo pasado que la rige, no dejarlo en presente."},
            ],
        },
        "exercises": [
            {"id": "c2sc-mc", "type": "multiple-choice", "title": "Identifica la Razón del Modo Verbal",
             "items": [
                {"id": "c2sc1", "prompt": "En \"Dudo que quienes lleguen tarde puedan entrar\", ¿por qué \"lleguen\" está en subjuntivo?", "options": ["Por depender de dudar que", "Por tener un antecedente indefinido en la relativa", "Por concordancia de tiempos con puedan"], "answerIndex": 1, "explanation": "Lleguen depende de la relativa con antecedente indefinido (quienes), una razón distinta e independiente de por qué puedan está en subjuntivo."},
             ]},
            {"id": "c2sc-fill", "type": "fill-blank", "title": "Completa la Cadena de Subordinación",
             "items": [
                {"id": "c2sc2", "prompt": "Me confesó que temía que, si no llegábamos a tiempo, todo se ___ (cancelar).", "answers": [["cancelaría"], ["cancelara"], ["cancelase"]], "options": ["cancelaría", "cancelara", "cancela"], "explanation": "El condicional (o el imperfecto de subjuntivo, en un registro más literario) es el que corresponde a la apódosis de una hipotética dentro de una cadena de pasado."},
             ]},
            {"id": "c2sc-writing", "type": "writing", "title": "Reescribe para Ganar Claridad",
             "items": [
                {"id": "c2sc3", "prompt": "Reescribe esta frase, dividiéndola en dos oraciones más claras sin perder ningún matiz: \"El informe, que se había redactado con la esperanza de que convenciera al comité, que llevaba meses dudando de que el proyecto, tal como estaba planteado, pudiera tener éxito, resultó insuficiente.\""},
             ]},
        ],
        "summary": [
            "Cada subordinada dentro de una frase compleja obedece a su propio verbo regente, con su propia razón para el modo verbal.",
            "La concordancia de tiempos avanza en cadena: cada verbo retrocede según el verbo del que depende directamente.",
            "Más allá de tres o cuatro niveles de subordinación, suele ser mejor estilo dividir la frase en dos, sin perder precisión.",
        ],
    },
    {
        "id": "c2-registro-literario-y-recursos-estilisticos",
        "level": "C2", "unit": "1", "order": 2, "skill": "reading", "strand": "estilo",
        "title": "Registro Literario y Recursos Estilísticos",
        "subtitle": "Metáfora, hipérbole, anáfora y otros recursos que dan textura a un texto elaborado.",
        "objectives": [
            "Reconocer recursos estilísticos frecuentes en la prosa literaria y ensayística",
            "Distinguir el uso del hipérbaton para dar énfasis o musicalidad a una frase",
            "Analizar cómo el orden de palabras y el léxico elevado crean un efecto literario",
        ],
        "content": {
            "intro": "Un dominio de C2 incluye reconocer y apreciar cómo un texto literario o ensayístico se construye deliberadamente distinto de la prosa neutra, con recursos que un hablante de niveles anteriores rara vez encuentra fuera de la literatura.",
            "explanation": "<p>El <strong>hipérbaton</strong> altera el orden habitual de las palabras para dar énfasis o musicalidad: <em>Verde que te quiero verde</em> (Lorca) antepone el adjetivo al verbo de un modo que la prosa neutra jamás haría. La <strong>anáfora</strong> repite una palabra o estructura al inicio de frases sucesivas para crear ritmo e insistencia; la <strong>metáfora</strong> y la <strong>hipérbole</strong> (exageración deliberada) intensifican una idea más allá de su sentido literal.</p><p>El léxico elevado o poco frecuente (<em>ínclito, pergeñar, acendrado</em>) y las construcciones sintácticas menos habituales en el habla (el uso libre del pretérito anterior, el gerundio con valor de posterioridad) son marcas propias del registro literario más cuidado, y reconocerlas es clave para leer con verdadera profundidad autores clásicos y contemporáneos exigentes.</p>",
            "rules": [
                {"heading": "a) Hipérbaton", "body": "<p>Alteración del orden neutro sujeto-verbo-complemento para dar énfasis: <em>De los sus ojos tan fuertemente llorando</em> (Cantar de Mio Cid) en vez del orden neutro.</p>"},
                {"heading": "b) Anáfora", "body": "<p>Repetición al inicio de frases o versos sucesivos: <em>Nada teme, nada duda, nada espera.</em></p>"},
                {"heading": "c) Metáfora e hipérbole", "body": "<p>Metáfora: <em>sus palabras eran veneno.</em> Hipérbole: <em>te lo he dicho un millón de veces.</em></p>"},
                {"heading": "d) Léxico elevado y construcciones poco frecuentes", "body": "<p>Palabras de baja frecuencia (<em>ominoso, pergeñar, acendrado</em>) y estructuras arcaizantes (el pretérito anterior: <em>Apenas hubo terminado, se marchó</em>) marcan un registro literario o muy formal.</p>"},
            ],
            "examples": [
                "Del salón en el ángulo oscuro, de su dueño tal vez olvidada... (hipérbaton clásico)",
                "Nada se pierde, nada se destruye, todo se transforma.",
                "Sus ojos eran dos pozos sin fondo. (metáfora)",
                "Te he llamado mil veces y nunca contestas. (hipérbole)",
                "Apenas hubo salido el sol, se pusieron todos en marcha. (pretérito anterior, registro literario)",
                "Con acendrada paciencia, esperó el desenlace de aquella historia.",
                "En la casa, silencio; en la calle, silencio; en el pueblo entero, silencio. (anáfora)",
                "Aquel hombre, huraño y taciturno, apenas dirigía la palabra a nadie.",
            ],
            "commonMistakes": [
                {"wrong": "usar el hipérbaton o el léxico elevado en un correo de trabajo o una conversación cotidiana", "right": "reservar estos recursos para el registro literario o ensayístico deliberado", "why": "Estos recursos, fuera de un contexto literario o retórico, suenan afectados o forzados en el habla y la escritura cotidianas."},
                {"wrong": "confundir la hipérbole con una simple exageración descuidada", "right": "reconocer la hipérbole como un recurso deliberado y consciente para intensificar una idea", "why": "La hipérbole es un recurso retórico con función expresiva concreta, no un error de precisión."},
                {"wrong": "pensar que el pretérito anterior (hubo terminado) es intercambiable con el pluscuamperfecto en cualquier contexto", "right": "reconocer que el pretérito anterior es casi exclusivo del registro literario y arcaizante", "why": "En el español actual, el pluscuamperfecto (había terminado) sustituye al pretérito anterior en prácticamente todos los contextos fuera de la literatura."},
            ],
        },
        "exercises": [
            {"id": "c2rl-mc", "type": "multiple-choice", "title": "Identifica el Recurso Estilístico",
             "items": [
                {"id": "c2rl1", "prompt": "\"Sus palabras eran veneno puro\" es un ejemplo de...", "options": ["hipérbaton", "metáfora", "anáfora"], "answerIndex": 1, "explanation": "Se identifica una cosa (palabras) con otra (veneno) sin usar como: metáfora."},
                {"id": "c2rl2", "prompt": "\"Nada teme, nada duda, nada espera\" es un ejemplo de...", "options": ["anáfora", "hipérbole", "hipérbaton"], "answerIndex": 0, "explanation": "La repetición de nada al inicio de cada frase es una anáfora."},
             ]},
            {"id": "c2rl-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "c2rl3", "statement": "El pretérito anterior (hubo terminado) es de uso frecuente en la conversación cotidiana actual.", "answer": False, "explanation": "Es casi exclusivo del registro literario y arcaizante; el habla cotidiana usa el pluscuamperfecto (había terminado)."},
            ]},
            {"id": "c2rl-writing", "type": "writing", "title": "Practica el Recurso",
             "items": [
                {"id": "c2rl4", "prompt": "Escribe tres frases breves sobre el paso del tiempo usando un hipérbaton, una metáfora y una anáfora, uno por frase."},
            ]},
        ],
        "summary": [
            "El hipérbaton altera el orden neutro de las palabras para dar énfasis o musicalidad, propio de la poesía y la prosa elaborada.",
            "La anáfora repite una estructura al inicio de frases sucesivas para crear ritmo; la metáfora y la hipérbole intensifican una idea más allá de su sentido literal.",
            "El léxico elevado y construcciones como el pretérito anterior marcan un registro literario que rara vez aparece fuera de la literatura o el ensayo cuidado.",
        ],
    },
    {
        "id": "c2-matices-lexicos-y-falsos-amigos-avanzados",
        "level": "C2", "unit": "1", "order": 3, "skill": "vocabulary", "strand": "lexico",
        "title": "Matices Léxicos y Falsos Amigos Avanzados",
        "subtitle": "Palabras casi sinónimas con un matiz que las distingue, y falsos amigos que engañan incluso a niveles avanzados.",
        "objectives": [
            "Distinguir pares de palabras casi sinónimas por su matiz de intensidad, connotación o registro",
            "Reconocer falsos amigos avanzados entre el español y otros idiomas comunes",
            "Elegir la palabra más precisa según el matiz exacto que se quiere comunicar",
        ],
        "content": {
            "intro": "A este nivel, el vocabulario ya no falla por desconocimiento de palabras básicas, sino por no captar el matiz exacto que distingue palabras casi sinónimas — la diferencia entre un texto correcto y un texto verdaderamente preciso está aquí.",
            "explanation": "<p>Muchos pares de palabras parecen intercambiables en un diccionario bilingüe, pero llevan matices de <strong>intensidad</strong> (<em>miedo</em> frente a <em>pavor</em>, mucho más intenso), <strong>connotación</strong> (<em>flaco</em>, neutro o cercano a delgado en muchos países de América Latina, frente a <em>delgado</em>, más neutro en general, o <em>esquelético</em>, claramente negativo), o <strong>registro</strong> (<em>comenzar</em>, más formal, frente a <em>empezar</em>, neutro, frente a <em>arrancar</em>, coloquial en ciertos contextos).</p><p>Los <strong>falsos amigos avanzados</strong> son palabras que se parecen a otra lengua pero tienen un significado distinto y sutil: <em>actualmente</em> significa \"en este momento\", no \"en realidad\" (que se dice <em>en realidad</em> o <em>de hecho</em>); <em>sensible</em> significa \"que siente con facilidad\", no \"sensato\" (que se dice <em>sensato/a</em>); <em>embarazada</em> significa \"esperando un bebé\", nunca \"avergonzada\".</p>",
            "rules": [
                {"heading": "a) Matices de intensidad", "body": "<p><em>miedo &lt; temor &lt; pavor/terror</em>; <em>gustar &lt; encantar &lt; fascinar</em>; <em>triste &lt; afligido &lt; desolado</em>.</p>"},
                {"heading": "b) Matices de registro", "body": "<p><em>comenzar</em> (formal) / <em>empezar</em> (neutro) / <em>arrancar</em> (coloquial, con máquinas o de forma brusca); <em>fallecer</em> (formal) / <em>morir</em> (neutro) / <em>estirar la pata</em> (coloquial, incluso vulgar).</p>"},
                {"heading": "c) Falsos amigos avanzados frecuentes", "body": "<ul><li><em>actualmente</em> = \"ahora, en este momento\" (no \"en realidad\")</li><li><em>sensible</em> = \"que siente con facilidad\" (no \"sensato\")</li><li><em>embarazada</em> = \"esperando un bebé\" (no \"avergonzada\", que se dice <em>avergonzado/a</em>)</li><li><em>constipado</em> = \"resfriado\" (no \"estreñido\")</li><li><em>éxito</em> = \"resultado positivo\" (no \"salida\", que se dice <em>salida</em>)</li></ul>"},
            ],
            "examples": [
                "Sintió un pavor absoluto al ver la escena del accidente.",
                "En realidad, no estoy tan seguro de que esta sea la mejor opción.",
                "Actualmente vivo en Buenos Aires, aunque nací en Montevideo.",
                "Es una persona muy sensible: cualquier comentario la afecta profundamente.",
                "Mi tía está embarazada de su segundo hijo.",
                "Me sentí muy avergonzado después de aquel comentario tan torpe.",
                "El ministro fallecerá... el ministro falleció ayer tras una larga enfermedad. (registro formal para un anuncio oficial)",
                "La salida de emergencia está al fondo del pasillo.",
            ],
            "commonMistakes": [
                {"wrong": "Actualmente, no creo que eso sea verdad. (con el sentido de \"en realidad\")", "right": "En realidad, no creo que eso sea verdad.", "why": "Actualmente significa \"en este momento\", un falso amigo frecuente con el sentido de \"en realidad\" o \"de hecho\" en otros idiomas."},
                {"wrong": "Me sentí muy sensible después de decir esa tontería. (con el sentido de \"avergonzado\")", "right": "Me sentí muy avergonzado después de decir esa tontería.", "why": "Sensible en español significa \"que siente con facilidad\", no tiene relación con sentirse avergonzado."},
                {"wrong": "Estoy embarazada de haber llegado tarde a la reunión. (con el sentido de \"avergonzada\")", "right": "Estoy avergonzada de haber llegado tarde a la reunión.", "why": "Embarazada significa exclusivamente \"esperando un bebé\"; el falso amigo con \"avergonzada\" es uno de los más conocidos del español."},
            ],
        },
        "exercises": [
            {"id": "c2fa-mc", "type": "multiple-choice", "title": "Elige el Significado Correcto",
             "items": [
                {"id": "c2fa1", "prompt": "\"Actualmente\" en español significa...", "options": ["en realidad", "en este momento", "de manera precisa"], "answerIndex": 1, "explanation": "Actualmente es un falso amigo frecuente: significa \"ahora, en este momento\", no \"en realidad\"."},
                {"id": "c2fa2", "prompt": "\"Sensible\" en español significa...", "options": ["sensato", "que siente con facilidad", "razonable"], "answerIndex": 1, "explanation": "Sensible describe a alguien que siente las cosas con facilidad o intensidad, no a alguien sensato."},
             ]},
            {"id": "c2fa-fill", "type": "fill-blank", "title": "Elige la Palabra de Registro Adecuado",
             "items": [
                {"id": "c2fa3", "prompt": "En un anuncio oficial: \"El presidente ___ ayer a los 85 años.\" (formal)", "answers": [["falleció"]], "options": ["falleció", "murió", "estiró la pata"], "explanation": "Falleció es el término formal apropiado para un anuncio oficial."},
             ]},
            {"id": "c2fa-correction", "type": "correction", "title": "Corrige el Falso Amigo",
             "items": [
                {"id": "c2fa4", "incorrect": "Estoy tan embarazada por lo que dije en la reunión.", "answer": ["Estoy tan avergonzada por lo que dije en la reunión."], "explanation": "Embarazada significa \"esperando un bebé\", no \"avergonzada\": uno de los falsos amigos más conocidos del español."},
            ]},
        ],
        "summary": [
            "Pares de palabras casi sinónimas se distinguen por matices de intensidad (miedo/pavor) o de registro (empezar/comenzar/arrancar).",
            "Actualmente, sensible, embarazada y constipado son falsos amigos avanzados frecuentes con significados muy distintos a los que sugiere su parecido con otros idiomas.",
            "Elegir la palabra con el matiz exacto, y no solo una traducción aproximadamente correcta, es la marca de un dominio verdaderamente avanzado del léxico.",
        ],
    },
    {
        "id": "c2-variacion-regional",
        "level": "C2", "unit": "1", "order": 4, "skill": "vocabulary", "strand": "variacion",
        "title": "Variación Regional: España, México, Argentina, el Caribe",
        "subtitle": "Un mismo español, muchos acentos, léxicos y hasta gramáticas ligeramente distintas.",
        "objectives": [
            "Reconocer rasgos fonéticos característicos de las grandes zonas dialectales del español",
            "Identificar variación léxica y gramatical entre España, México, el Río de la Plata y el Caribe",
            "Adaptar la comprensión a un texto o audio de una variedad regional específica",
        ],
        "content": {
            "intro": "Después de dominar la gramática estándar en niveles anteriores, un hablante de C2 necesita poder entender y apreciar la enorme diversidad real del español hablado en más de veinte países.",
            "explanation": "<p>Fonéticamente, el <strong>seseo</strong> (pronunciar c/z igual que s) es la norma en toda América Latina y en el sur de España, frente al <strong>distingo</strong> del centro y norte de España (donde c/z suenan como \"th\" inglesa); el Caribe tiende a aspirar o perder la <strong>-s</strong> final de sílaba (<em>los dos</em> suena \"loh do\"), y el Río de la Plata pronuncia la <strong>ll/y</strong> con un sonido \"sh\" muy característico (<em>yo</em> suena \"sho\").</p><p>Léxicamente, cada región tiene su propio vocabulario cotidiano: <em>coche</em> (España) / <em>carro</em> (gran parte de América Latina) / <em>auto</em> (Río de la Plata, Chile); <em>ordenador</em> (España) / <em>computadora</em> (América Latina). Gramaticalmente, ya conoces el voseo rioplatense; el Caribe tiende a mantener el pronombre de sujeto incluso cuando no es necesario (<em>¿Qué tú quieres?</em> en vez de <em>¿Qué quieres?</em>), un rasgo característico de esa región.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Algunas diferencias regionales frecuentes</caption><thead><tr><th>Concepto</th><th>España</th><th>México</th><th>Río de la Plata</th></tr></thead><tbody><tr><td>coche</td><td>coche</td><td>carro</td><td>auto</td></tr><tr><td>computadora</td><td>ordenador</td><td>computadora</td><td>computadora</td></tr><tr><td>tú informal</td><td>tú</td><td>tú</td><td>vos</td></tr><tr><td>c/z</td><td>distingo ("th")</td><td>seseo</td><td>seseo</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Rasgos fonéticos principales", "body": "<ul><li>Seseo (América Latina, sur de España) vs. distingo (centro/norte de España)</li><li>Aspiración/pérdida de -s final (Caribe, Andalucía, Chile)</li><li>Yeísmo rehilado \"sh\" (Río de la Plata): ll/y suenan como \"sh\"</li></ul>"},
                {"heading": "b) Variación léxica frecuente", "body": "<p><em>coche/carro/auto, ordenador/computadora, autobús/camión/colectivo/guagua, jugo/zumo, palomitas/pochoclo/cotufas</em>.</p>"},
                {"heading": "c) Variación gramatical", "body": "<p>Voseo rioplatense; mantenimiento del pronombre de sujeto en preguntas en el Caribe (<em>¿Qué tú dices?</em>); uso de ustedes en vez de vosotros en toda América.</p>"},
            ],
            "examples": [
                "En España dicen zumo de naranja; en México, jugo de naranja.",
                "¿Qué tú piensas de todo esto? (rasgo caribeño frecuente)",
                "Che, ¿vos querés que vayamos al cine esta noche? (voseo rioplatense)",
                "En Argentina, la palabra calle suena distinta por el yeísmo con \"sh\".",
                "En el Caribe, es muy común aspirar la s final: \"los dos\" suena casi como \"loh dó\".",
                "En España se dice móvil; en América Latina, celular.",
                "En México se dice popote; en España, pajita o caña.",
                "En Chile y Argentina se dice auto; en España, coche; en México, carro.",
            ],
            "commonMistakes": [
                {"wrong": "pensar que existe un único \"español correcto\" y que las demás variedades son desviaciones", "right": "reconocer que todas las variedades regionales son igualmente válidas dentro de su propia norma", "why": "El español no tiene un único centro de prestigio: España, México, Argentina y el resto de países hispanohablantes tienen normas cultas propias y plenamente legítimas."},
                {"wrong": "sorprenderse o confundirse al no reconocer el seseo o el yeísmo con \"sh\" como parte normal del idioma", "right": "familiarizarse con estos rasgos como variación fonética estándar, no como error de pronunciación", "why": "El seseo es la pronunciación mayoritaria del español en el mundo, no una desviación del distingo del centro y norte de España."},
                {"wrong": "asumir que el vocabulario de una sola región (por ejemplo España) es el único correcto en todo el mundo hispanohablante", "right": "aprender el vocabulario equivalente de varias regiones para entender español real de cualquier país", "why": "Cada región tiene su propio vocabulario cotidiano igualmente válido; limitarse a uno solo dificulta la comprensión fuera de esa región."},
            ],
        },
        "exercises": [
            {"id": "c2vr-mc", "type": "multiple-choice", "title": "Reconoce la Variación Regional",
             "items": [
                {"id": "c2vr1", "prompt": "¿Cómo se llama el fenómeno de pronunciar c/z igual que s, mayoritario en el mundo hispanohablante?", "options": ["distingo", "seseo", "yeísmo"], "answerIndex": 1, "explanation": "El seseo es la pronunciación mayoritaria, propia de toda América Latina y el sur de España."},
                {"id": "c2vr2", "prompt": "¿En qué región es típico el voseo con formas como vos hablás?", "options": ["Centro de España", "México", "Río de la Plata"], "answerIndex": 2, "explanation": "El voseo es la norma estándar en Argentina, Uruguay y Paraguay, la región del Río de la Plata."},
             ]},
            {"id": "c2vr-fill", "type": "fill-blank", "title": "Vocabulario Regional",
             "items": [
                {"id": "c2vr3", "prompt": "En España se dice \"ordenador\"; en gran parte de América Latina se dice ___.", "answers": [["computadora"]], "options": ["computadora", "carro", "auto"], "explanation": "Computadora es el término equivalente usado en la mayoría de los países latinoamericanos."},
             ]},
            {"id": "c2vr-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "c2vr4", "statement": "Todas las variedades regionales del español son igualmente válidas dentro de su propia norma culta.", "answer": True, "explanation": "El español no tiene un único centro de prestigio: cada país o región hispanohablante tiene su propia norma culta legítima."},
            ]},
        ],
        "summary": [
            "El seseo, el distingo, la aspiración de -s y el yeísmo con sh son rasgos fonéticos regionales igualmente válidos, no errores de pronunciación.",
            "El vocabulario cotidiano varía mucho por región: coche/carro/auto, ordenador/computadora, y muchos más pares equivalentes.",
            "Ninguna variedad regional del español es más \"correcta\" que otra; todas tienen su propia norma culta plenamente legítima.",
        ],
    },
    {
        "id": "c2-cohesion-textual-en-discurso-extenso",
        "level": "C2", "unit": "1", "order": 5, "skill": "writing", "strand": "cohesion",
        "title": "Cohesión Textual en Discurso Extenso",
        "subtitle": "Cómo mantener un texto largo unido, coherente y sin repeticiones innecesarias.",
        "objectives": [
            "Usar mecanismos de referencia (pronombres, elipsis, sinónimos) para evitar repeticiones",
            "Mantener el hilo temático de un texto extenso mediante progresión temática controlada",
            "Revisar un texto propio para detectar rupturas de cohesión o ambigüedades referenciales",
        ],
        "content": {
            "intro": "Un texto extenso y bien escrito no es solo una sucesión de frases correctas: necesita mecanismos que las mantengan unidas, para que el lector nunca pierda de vista de qué o de quién se está hablando.",
            "explanation": "<p>La <strong>cohesión referencial</strong> evita repetir el mismo sustantivo constantemente usando pronombres, sinónimos, hiperónimos (una palabra más general: \"el animal\" en vez de repetir \"el perro\") o la <strong>elipsis</strong> (omitir un elemento ya mencionado cuando el contexto lo permite: <em>Juan llegó tarde y [Juan] se disculpó</em>).</p><p>La <strong>progresión temática</strong> organiza cómo avanza la información: cada frase nueva suele retomar algo ya mencionado (el tema) y añadir información nueva (el rema), que a menudo se convierte en el tema de la frase siguiente — así el texto avanza sin saltos bruscos. Un error frecuente incluso en escritores avanzados es la <strong>ambigüedad referencial</strong>: un pronombre que podría referirse a más de un antecedente, obligando al lector a releer para entender.</p>",
            "rules": [
                {"heading": "a) Mecanismos de referencia", "body": "<ul><li>Pronombres: <em>Ana llegó pronto. Ella siempre es puntual.</em></li><li>Sinónimos/hiperónimos: <em>el ensayo... el texto... esta obra...</em></li><li>Elipsis: <em>Marta cocinó y [Marta] limpió la cocina después.</em></li></ul>"},
                {"heading": "b) Progresión temática", "body": "<p>La información nueva de una frase (el rema) se convierte a menudo en el tema conocido de la frase siguiente, creando una cadena que avanza sin saltos: <em>El proyecto se aprobó en marzo. Ese mismo mes, el equipo empezó a trabajar.</em></p>"},
                {"heading": "c) Evitar la ambigüedad referencial", "body": "<p><em>Cuando Pedro habló con Luis, él le contó su plan.</em> (¿quién es él, Pedro o Luis?) — se resuelve nombrando explícitamente o reestructurando: <em>Cuando Pedro habló con Luis, este último le contó su plan.</em></p>"},
            ],
            "examples": [
                "El estudio analiza tres factores. El primero de ellos es el más determinante.",
                "María presentó su proyecto y, acto seguido, respondió a las preguntas del jurado.",
                "El autor plantea una hipótesis audaz; dicha hipótesis se sostiene a lo largo de todo el ensayo.",
                "Juan llamó a su hermano y le contó la noticia enseguida.",
                "La empresa lanzó el producto en enero. Ese mismo mes, las ventas se dispararon.",
                "Cuando Ana y Marta se encontraron, esta última le mostró las fotos del viaje.",
                "El informe recoge varios datos; estos confirman la tendencia observada el año anterior.",
                "El profesor explicó la teoría con claridad y, después, propuso varios ejercicios prácticos.",
            ],
            "commonMistakes": [
                {"wrong": "El perro corrió hacia el perro que estaba en el parque. (repetición innecesaria)", "right": "El perro corrió hacia el otro perro que estaba en el parque. / ... hacia el animal que estaba en el parque.", "why": "Repetir el mismo sustantivo sin necesidad rompe la fluidez del texto; conviene usar un pronombre, un sinónimo o un hiperónimo."},
                {"wrong": "Cuando Marcos habló con Luis, él le explicó el problema. (ambiguo: ¿quién explicó, Marcos o Luis?)", "right": "Cuando Marcos habló con Luis, este último le explicó el problema.", "why": "El pronombre él es ambiguo entre los dos antecedentes posibles; conviene precisar con este/este último o repetir el nombre."},
                {"wrong": "encadenar temas nuevos en cada frase sin retomar nada de la frase anterior", "right": "hacer que la información nueva de una frase se convierta en el tema conocido de la siguiente", "why": "Sin progresión temática, el texto se percibe como una lista de ideas sueltas, no como un discurso coherente y unido."},
            ],
        },
        "exercises": [
            {"id": "c2ct-mc", "type": "multiple-choice", "title": "Identifica el Problema de Cohesión",
             "items": [
                {"id": "c2ct1", "prompt": "\"Cuando Ana habló con Marta, ella le contó todo.\" ¿Cuál es el problema?", "options": ["Falta de progresión temática", "Ambigüedad referencial del pronombre ella", "Repetición excesiva de sustantivos"], "answerIndex": 1, "explanation": "Ella podría referirse tanto a Ana como a Marta, generando ambigüedad."},
             ]},
            {"id": "c2ct-writing", "type": "writing", "title": "Mejora la Cohesión",
             "items": [
                {"id": "c2ct2", "prompt": "Reescribe este fragmento para evitar la repetición y la ambigüedad: \"El estudio analiza el problema. El problema afecta a muchas personas. Cuando Laura leyó el estudio, ella se sorprendió mucho con el estudio.\""},
             ]},
            {"id": "c2ct-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "c2ct3", "statement": "La elipsis consiste en omitir un elemento ya mencionado cuando el contexto permite recuperarlo sin ambigüedad.", "answer": True, "explanation": "Es un mecanismo de cohesión que evita repeticiones innecesarias sin perder claridad."},
            ]},
        ],
        "summary": [
            "Los pronombres, sinónimos, hiperónimos y la elipsis evitan repeticiones innecesarias y dan cohesión a un texto extenso.",
            "La progresión temática avanza el discurso cuando la información nueva de una frase se convierte en el tema conocido de la siguiente.",
            "La ambigüedad referencial (un pronombre con más de un antecedente posible) es uno de los fallos de cohesión más frecuentes, incluso en escritores avanzados.",
        ],
    },
    {
        "id": "c2-modalidad-y-atenuacion-en-discurso-formal",
        "level": "C2", "unit": "1", "order": 6, "skill": "functional", "strand": "modalidad",
        "title": "Modalidad y Atenuación en Discurso Formal",
        "subtitle": "Cómo suavizar una afirmación, una crítica o un desacuerdo sin perder precisión.",
        "objectives": [
            "Usar verbos modales y expresiones de probabilidad para matizar el grado de certeza",
            "Aplicar estrategias de atenuación para suavizar una crítica o un desacuerdo en un registro formal",
            "Reconocer la diferencia entre atenuación genuina y ambigüedad evasiva no deseada",
        ],
        "content": {
            "intro": "Un hablante culto rara vez afirma algo de forma tajante en un contexto formal o académico: sabe matizar el grado de certeza y suavizar el desacuerdo sin perder claridad ni firmeza real en el fondo.",
            "explanation": "<p>La <strong>modalidad epistémica</strong> expresa el grado de certeza del hablante sobre lo que dice, mediante verbos modales (<em>podría, cabría, sería posible</em>), adverbios (<em>posiblemente, presumiblemente, en cierto modo</em>) o construcciones impersonales (<em>cabe pensar que, todo parece indicar que</em>). No es lo mismo afirmar <em>Esto es un error</em> que <em>Cabría pensar que esto podría ser un error</em> — la segunda deja espacio para el desacuerdo sin renunciar a expresar la idea.</p><p>La <strong>atenuación</strong> es una estrategia de cortesía especialmente valorada en el registro académico y profesional al criticar o discrepar: en vez de <em>Esto está mal</em>, se prefiere <em>Cabría reconsiderar este punto</em> o <em>Quizá convendría revisar este aspecto</em>. La clave es que la atenuación no oculta el mensaje real, solo lo presenta de forma menos confrontativa — distinta de una ambigüedad evasiva que de verdad esconde la opinión del hablante.</p>",
            "rules": [
                {"heading": "a) Verbos y expresiones de modalidad epistémica", "body": "<p><em>podría ser que, cabe la posibilidad de que, todo parece indicar que, se podría argumentar que, no cabe descartar que</em>.</p>"},
                {"heading": "b) Adverbios de atenuación", "body": "<p><em>posiblemente, presumiblemente, hasta cierto punto, en cierta medida, no del todo</em>: <em>El argumento es, hasta cierto punto, convincente.</em></p>"},
                {"heading": "c) Estrategias para atenuar una crítica", "body": "<ul><li>Verbo en condicional: <em>Convendría revisar esta parte.</em></li><li>Impersonalización: <em>Se podría objetar que falta un ejemplo más claro.</em></li><li>Reconocimiento previo: <em>Si bien el argumento tiene mérito, cabría matizar...</em></li></ul>"},
                {"heading": "d) Atenuación genuina vs. ambigüedad evasiva", "body": "<p>La atenuación matiza sin ocultar la opinión real; una ambigüedad evasiva deliberada, en cambio, impide saber qué piensa realmente el hablante — esto último no es un recurso de estilo válido en un texto argumentativo serio.</p>"},
            ],
            "examples": [
                "Cabría reconsiderar esta parte del argumento antes de publicarlo.",
                "Todo parece indicar que la hipótesis inicial no era del todo correcta.",
                "Se podría argumentar que el estudio adolece de una muestra demasiado pequeña.",
                "El planteamiento es, hasta cierto punto, razonable, aunque presenta algunas lagunas.",
                "No cabe descartar que existan otros factores no considerados en este análisis.",
                "Convendría, quizá, matizar esta afirmación con datos más recientes.",
                "Si bien el enfoque tiene mérito, cabría cuestionar algunas de sus premisas.",
                "Presumiblemente, el retraso se debió a factores externos al equipo.",
            ],
            "commonMistakes": [
                {"wrong": "Este argumento está completamente equivocado. (en una revisión académica formal)", "right": "Cabría reconsiderar algunos aspectos de este argumento.", "why": "En un registro académico o profesional formal, una crítica tajante suele atenuarse para mantener un tono constructivo y cortés, sin perder la sustancia de la observación."},
                {"wrong": "usar la atenuación para evitar por completo expresar una opinión clara", "right": "usar la atenuación para suavizar el tono sin ocultar la opinión de fondo", "why": "La atenuación matiza la forma, no debe convertirse en una excusa para no comunicar realmente lo que se piensa."},
                {"wrong": "Puede ser que esto sea un error, o tal vez no, no lo sé realmente. (ambigüedad evasiva, no atenuación)", "right": "Cabría considerar que esto podría ser un error, aunque el argumento central sigue siendo sólido.", "why": "La atenuación genuina sigue comunicando una posición clara; una ambigüedad evasiva simplemente elude tomar postura."},
            ],
        },
        "exercises": [
            {"id": "c2ma-mc", "type": "multiple-choice", "title": "Elige la Forma Más Atenuada",
             "items": [
                {"id": "c2ma1", "prompt": "¿Cuál de estas frases suaviza mejor una crítica en un contexto académico?", "options": ["Esto está mal.", "Cabría reconsiderar este punto.", "No tienes razón en absoluto."], "answerIndex": 1, "explanation": "Cabría reconsiderar suaviza la crítica sin perder su contenido real."},
             ]},
            {"id": "c2ma-fill", "type": "fill-blank", "title": "Completa con Modalidad Epistémica",
             "items": [
                {"id": "c2ma2", "prompt": "___ que la hipótesis inicial no fuera del todo correcta. (expresar posibilidad, no certeza)", "answers": [["Cabe la posibilidad de"], ["Podría ser"]], "options": ["Cabe la posibilidad de", "Es seguro"], "explanation": "Cabe la posibilidad de expresa un grado de certeza matizado, no una afirmación absoluta."},
             ]},
            {"id": "c2ma-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "c2ma3", "statement": "La atenuación genuina oculta por completo la opinión real del hablante.", "answer": False, "explanation": "La atenuación matiza el tono, pero sigue comunicando una posición clara; ocultar la opinión sería una ambigüedad evasiva, no atenuación."},
            ]},
        ],
        "summary": [
            "La modalidad epistémica (podría, cabría, todo parece indicar que) expresa el grado de certeza del hablante sobre lo que afirma.",
            "La atenuación suaviza una crítica o un desacuerdo en el registro formal mediante el condicional, la impersonalización o el reconocimiento previo del argumento contrario.",
            "La atenuación genuina sigue comunicando una posición clara; no debe confundirse con una ambigüedad evasiva que evita tomar postura.",
        ],
    },
    {
        "id": "c2-estructuras-arcaicas-o-literarias",
        "level": "C2", "unit": "1", "order": 7, "skill": "reading", "strand": "estilo",
        "title": "Estructuras Arcaicas o Literarias",
        "subtitle": "Formas que sobreviven en textos clásicos, religiosos o muy formales, y que un lector culto debe reconocer.",
        "objectives": [
            "Reconocer pronombres y formas verbales arcaicas frecuentes en textos clásicos",
            "Identificar el uso literario del futuro de subjuntivo, el vos reverencial y otras formas fosilizadas",
            "Leer con comprensión un fragmento breve de español clásico (Siglo de Oro) sin traducirlo mentalmente al español moderno",
        ],
        "content": {
            "intro": "Leer con soltura una obra clásica, un texto religioso o un documento histórico requiere reconocer formas que desaparecieron del español moderno hace siglos, pero que siguen definiendo buena parte de la tradición literaria en español.",
            "explanation": "<p>El español clásico (Siglo de Oro) usa pronombres y formas hoy desaparecidos: <strong>vos</strong> como tratamiento reverencial hacia una sola persona de alto rango (distinto del voseo moderno rioplatense), <strong>vuestra merced</strong> (origen histórico de <em>usted</em>), y formas verbales como <strong>habedes, sois</strong> (por sois) o el uso libre de <strong>facer</strong> por <em>hacer</em> en textos medievales.</p><p>También sobreviven construcciones como el <strong>futuro de subjuntivo</strong> (ya visto en B2) en textos religiosos y jurídicos antiguos, el uso de <strong>ca</strong> (por \"porque\") en textos medievales, y una sintaxis con mayor libertad en el orden de palabras que la prosa moderna. Reconocer estas formas, sin necesidad de producirlas, es lo que permite disfrutar plenamente del Quijote, la poesía del Siglo de Oro o los textos fundacionales de la lengua sin la sensación de estar leyendo un idioma distinto.</p>",
            "rules": [
                {"heading": "a) Vos reverencial (clásico, distinto del voseo moderno)", "body": "<p>En el Siglo de Oro, vos se dirigía formalmente a una sola persona de rango: <em>Vos, señor, sabéis bien lo que os digo.</em> — no debe confundirse con el voseo informal moderno de Argentina.</p>"},
                {"heading": "b) Vuestra merced y el origen de usted", "body": "<p><em>Vuestra merced</em> se abrevió con el tiempo hasta convertirse en <em>usted</em>; en textos clásicos aparece todavía en su forma completa como tratamiento de respeto.</p>"},
                {"heading": "c) Formas verbales y léxico medieval/clásico", "body": "<p><em>facer</em> (hacer), <em>fablar</em> (hablar), <em>ca</em> (porque), <em>maguer</em> (aunque) — vocabulario y morfología que desapareció del español estándar pero persiste en ediciones de textos medievales.</p>"},
                {"heading": "d) Leer sin traducir mentalmente", "body": "<p>El objetivo en C2 no es producir estas formas, sino reconocerlas con fluidez suficiente para seguir el sentido de un texto clásico sin detenerse en cada palabra desconocida.</p>"},
            ],
            "examples": [
                "Vos, señor caballero, sabéis bien la razón que me asiste. (vos reverencial clásico)",
                "Vuestra merced perdone mi atrevimiento al escribirle esta carta.",
                "Ca no hay mayor locura que la de quien todo lo quiere saber. (ca = porque, en texto medieval)",
                "Maguer fuese pobre, jamás perdió la dignidad. (maguer = aunque)",
                "El que hubiere de heredar esta hacienda deberá cumplir con lo aquí dispuesto. (futuro de subjuntivo, texto jurídico clásico)",
                "En un lugar de la Mancha, de cuyo nombre no quiero acordarme... (célebre apertura del Quijote)",
                "Fabló el caballero con gran cortesía a la dama que allí esperaba.",
                "Sois, sin duda, la persona más sabia que jamás he conocido. (sois con valor reverencial hacia una sola persona)",
            ],
            "commonMistakes": [
                {"wrong": "confundir el vos reverencial clásico con el voseo informal moderno de Argentina", "right": "distinguir ambos usos, siglos y funciones completamente distintas del mismo pronombre", "why": "El vos clásico era formal y reverencial hacia una sola persona de alto rango; el voseo moderno rioplatense es informal y cotidiano — comparten la forma pero no la función."},
                {"wrong": "intentar producir activamente facer, fablar o ca en una conversación o texto moderno", "right": "reconocer estas formas de forma pasiva al leer textos clásicos o medievales", "why": "Estas formas desaparecieron por completo del español actual; usarlas fuera de una cita o un texto deliberadamente arcaizante suena incomprensible o afectado."},
                {"wrong": "detenerse a traducir mentalmente cada palabra arcaica al español moderno", "right": "leer el texto clásico directamente, apoyándose en el contexto para las palabras menos frecuentes", "why": "Un dominio de C2 permite seguir el sentido general de un texto clásico con fluidez, sin necesidad de una traducción palabra por palabra."},
            ],
        },
        "exercises": [
            {"id": "c2ea-mc", "type": "multiple-choice", "title": "Reconoce la Forma Arcaica",
             "items": [
                {"id": "c2ea1", "prompt": "En el español clásico, \"vuestra merced\" es el origen histórico de...", "options": ["tú", "usted", "vos (voseo moderno)"], "answerIndex": 1, "explanation": "Vuestra merced se abrevió con el tiempo hasta dar la forma moderna usted."},
                {"id": "c2ea2", "prompt": "\"Ca\" en un texto medieval significa...", "options": ["porque", "aunque", "cuando"], "answerIndex": 0, "explanation": "Ca es una conjunción causal medieval, equivalente a porque."},
             ]},
            {"id": "c2ea-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "c2ea3", "statement": "El vos reverencial del español clásico es exactamente el mismo fenómeno que el voseo informal argentino moderno.", "answer": False, "explanation": "Comparten la forma del pronombre pero cumplen funciones históricas y sociales completamente distintas."},
            ]},
            {"id": "c2ea-reading", "type": "reading-comprehension", "title": "Comprensión de un Fragmento Clásico",
             "passage": "\"Vuestra merced, señor hidalgo, perdone mi atrevimiento, ca no hallé otro modo de haceros llegar esta nueva: sois, sin duda, la persona a quien más debo en esta vida, y maguer el tiempo y la distancia, jamás olvidé vuestra bondad.\"",
             "items": [
                {"id": "c2ea4", "prompt": "¿A quién se dirige el narrador con \"vuestra merced\" y \"sois\"?", "options": ["A varias personas a la vez", "A una sola persona, con tratamiento reverencial", "A sí mismo"], "answerIndex": 1, "explanation": "Tanto vuestra merced como sois (con valor reverencial) se dirigen formalmente a una sola persona de respeto."},
             ]},
        ],
        "summary": [
            "El vos reverencial clásico, distinto del voseo moderno, se dirigía formalmente a una sola persona de alto rango.",
            "Vuestra merced es el origen histórico de usted; facer, fablar, ca y maguer son léxico y morfología medievales hoy desaparecidos del uso activo.",
            "El objetivo en C2 es reconocer estas formas con fluidez al leer, no producirlas activamente en el español contemporáneo.",
        ],
    },
    {
        "id": "c2-dominio-del-registro-y-transformacion-estilistica",
        "level": "C2", "unit": "1", "order": 8, "skill": "writing", "strand": "registro",
        "title": "Dominio del Registro y Transformación Estilística",
        "subtitle": "La destreza final: reescribir un mismo contenido en cualquier registro, a voluntad.",
        "objectives": [
            "Transformar un mismo contenido entre registro coloquial, estándar, formal y literario",
            "Justificar las decisiones léxicas y sintácticas detrás de cada transformación de registro",
            "Evaluar la coherencia interna de registro en un texto propio o ajeno",
        ],
        "content": {
            "intro": "Esta lección cierra el curso reuniendo todo lo trabajado en los niveles anteriores en una sola destreza: la capacidad de tomar una misma idea y expresarla en el registro exacto que la situación exige, a voluntad y sin esfuerzo aparente.",
            "explanation": "<p>Dominar el registro no es memorizar una lista de fórmulas fijas, sino entender qué elige cada registro en cuatro planos a la vez: el <strong>léxico</strong> (coloquial, neutro, culto o técnico), la <strong>sintaxis</strong> (frases cortas y simples frente a periodos largos y subordinados), la <strong>morfología del trato</strong> (tú/vos/usted, y las fórmulas que cada uno exige), y los <strong>recursos retóricos</strong> (desde una metáfora coloquial hasta un hipérbaton literario).</p><p>La prueba real de este dominio es poder tomar una sola idea —por ejemplo, que un proyecto se retrasó— y producir, sin perder el contenido exacto, una versión coloquial (<em>Al final la cosa se atrasó, qué se le va a hacer</em>), una estándar (<em>El proyecto se retrasó por motivos ajenos al equipo</em>), una formal (<em>Lamentamos informarle de que el proyecto ha sufrido una demora</em>), y hasta una con matiz literario (<em>El destino, caprichoso como siempre, quiso posponer aquello que tanto habíamos anhelado</em>).</p>",
            "rules": [
                {"heading": "a) Los cuatro planos del registro", "body": "<ul><li>Léxico: coloquial &lt; neutro &lt; culto/técnico</li><li>Sintaxis: frases simples &lt; periodos complejos y subordinados</li><li>Trato: tú/vos &lt; usted &lt; fórmulas reverenciales</li><li>Recursos retóricos: ninguno &lt; metáfora/ironía leve &lt; recursos literarios elaborados</li></ul>"},
                {"heading": "b) Coherencia interna de registro", "body": "<p>Un texto bien escrito mantiene el mismo registro en todos sus planos a la vez; mezclar un léxico muy culto con un trato de tú informal, o una sintaxis muy simple con fórmulas reverenciales, produce un efecto extraño o involuntariamente cómico.</p>"},
                {"heading": "c) El objetivo final: elegir, no improvisar", "body": "<p>Un hablante de C2 no cae en un registro por defecto: elige conscientemente cuál usar según el destinatario, el propósito y el contexto, y sabe transformar deliberadamente entre uno y otro cuando la situación lo exige.</p>"},
            ],
            "examples": [
                "Coloquial: Che, al final se nos complicó todo con la mudanza, un lío total.",
                "Estándar: Al final tuvimos varios problemas con la mudanza y se complicó bastante.",
                "Formal: Lamentamos comunicarle que, debido a diversos inconvenientes, la mudanza se ha visto considerablemente complicada.",
                "Literario: La mudanza, que tantas esperanzas había despertado, se convirtió en un cúmulo de contratiempos imprevistos.",
                "Coloquial: Oye, ¿me puedes echar una mano con esto un segundo?",
                "Formal: ¿Sería tan amable de prestarme su ayuda con este asunto?",
                "Estándar: Este año las ventas bajaron bastante respecto al anterior.",
                "Formal: Durante el presente ejercicio, se ha registrado un descenso notable en las cifras de ventas respecto al periodo anterior.",
            ],
            "commonMistakes": [
                {"wrong": "Estimado señor: oye, necesito que me ayudes con esto. (mezcla de fórmula formal con trato informal)", "right": "Estimado señor: le escribo para solicitar su ayuda con este asunto.", "why": "Mezclar una fórmula de apertura formal con un trato informal (oye, tú) rompe la coherencia interna del registro y suena incongruente."},
                {"wrong": "usar siempre el mismo registro por defecto, sin adaptarlo al destinatario o al propósito", "right": "elegir de forma consciente el registro más adecuado para cada situación concreta", "why": "El dominio real de C2 se demuestra en la capacidad de transformar el registro a voluntad, no en dominar uno solo, por elaborado que sea."},
                {"wrong": "pensar que un registro más culto o literario es siempre \"mejor\" que uno coloquial", "right": "reconocer que cada registro es apropiado según el contexto, sin jerarquía de valor entre ellos", "why": "Un mensaje coloquial entre amigos escrito en registro literario resultaría tan inadecuado como un informe técnico escrito en un tono demasiado coloquial."},
            ],
        },
        "exercises": [
            {"id": "c2dr-mc", "type": "multiple-choice", "title": "Identifica el Registro",
             "items": [
                {"id": "c2dr1", "prompt": "\"Lamentamos comunicarle que su solicitud ha sido desestimada.\" pertenece a un registro...", "options": ["coloquial", "formal", "literario"], "answerIndex": 1, "explanation": "El vocabulario preciso (lamentamos, desestimada) y la fórmula de cortesía marcan un registro formal."},
                {"id": "c2dr2", "prompt": "\"Al final no nos dieron el trabajo, una pena.\" pertenece a un registro...", "options": ["coloquial", "formal", "arcaizante"], "answerIndex": 0, "explanation": "El vocabulario simple y directo, sin fórmulas de cortesía, marca un registro coloquial."},
             ]},
            {"id": "c2dr-writing", "type": "writing", "title": "Transforma el Registro",
             "items": [
                {"id": "c2dr3", "prompt": "Toma esta idea en registro estándar — \"El vuelo se canceló por el mal tiempo y tuvimos que quedarnos una noche más en el aeropuerto\" — y reescríbela en registro coloquial y luego en registro formal, manteniendo exactamente el mismo contenido."},
            ]},
            {"id": "c2dr-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "c2dr4", "statement": "Un registro literario o culto es siempre objetivamente mejor que uno coloquial.", "answer": False, "explanation": "Cada registro es apropiado según el contexto; no existe una jerarquía de valor entre ellos, solo adecuación o inadecuación a la situación."},
            ]},
        ],
        "summary": [
            "El registro se define en cuatro planos a la vez: léxico, sintaxis, trato (tú/usted) y recursos retóricos, y todos deben ser coherentes entre sí.",
            "Un hablante de C2 puede transformar deliberadamente un mismo contenido entre registro coloquial, estándar, formal y literario, sin perder el sentido exacto.",
            "Ningún registro es intrínsecamente mejor que otro: la destreza real está en elegir conscientemente el más adecuado para cada situación, no en dominar uno solo.",
        ],
    },
]

# =======================================================================
# EXTRA_EXERCISES — bloques adicionales de práctica (lectura y ordenar
# frases) fusionados en cada lección por id.
# =======================================================================
EXTRA_EXERCISES = {
    "c2-sintaxis-compleja-y-subordinacion-multiple": [
        {"id": "c2x1-reading", "type": "reading-comprehension", "title": "Lectura: Un Párrafo Complejo",
         "passage": "<p>Quienes deseen que su solicitud sea considerada deberán presentarla antes de que finalice el plazo, algo que, por difícil que parezca, muchos candidatos no logran cumplir. Dudo que quienes lo critican tan duramente hayan leído realmente su propuesta completa.</p>",
         "items": [
            {"id": "c2x1r1", "prompt": "¿Qué deben hacer quienes deseen que su solicitud sea considerada?", "options": ["Esperar una respuesta", "Presentarla antes de que finalice el plazo", "Llamar por teléfono"], "answerIndex": 1, "explanation": "El texto dice: «deberán presentarla antes de que finalice el plazo»."},
            {"id": "c2x1r2", "prompt": "¿Muchos candidatos logran cumplir ese requisito?", "options": ["Sí, casi todos", "No, muchos no lo logran"], "answerIndex": 1, "explanation": "El texto dice: «muchos candidatos no logran cumplir» ese requisito."},
            {"id": "c2x1r3", "prompt": "¿Qué duda expresa la persona sobre los críticos?", "options": ["Que hayan leído la propuesta completa", "Que existan realmente", "Que tengan razón siempre"], "answerIndex": 0, "explanation": "El texto dice: «Dudo que quienes lo critican... hayan leído realmente su propuesta completa»."},
            {"id": "c2x1r4", "prompt": "¿Por qué \"lleguen\" o \"deseen\" van en subjuntivo en este tipo de frases?", "options": ["Porque el antecedente es indefinido/general", "Porque siempre se usa subjuntivo con quienes", "Por error gramatical"], "answerIndex": 0, "explanation": "Quienes con un antecedente indefinido o general activa el subjuntivo en la relativa."},
         ]},
        {"id": "c2x1-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c2x1o1", "prompt": "Ordena las palabras.", "words": ["Quienes", "lleguen", "tarde", "no", "podrán", "entrar"], "explanation": "Quienes con antecedente indefinido + subjuntivo (lleguen) + consecuencia."},
            {"id": "c2x1o2", "prompt": "Ordena las palabras.", "words": ["Dudo", "que", "esto", "sea", "una", "coincidencia"], "explanation": "Dudar que + subjuntivo (sea)."},
         ]},
    ],
    "c2-registro-literario-y-recursos-estilisticos": [
        {"id": "c2x2-reading", "type": "reading-comprehension", "title": "Lectura: Un Fragmento Poético",
         "passage": "<p>Nada teme, nada duda, nada espera aquel que ha encontrado la paz interior. Sus palabras eran veneno puro, capaces de herir sin dejar marca visible. Con acendrada paciencia, esperó el desenlace de aquella historia que tantas vidas había marcado.</p>",
         "items": [
            {"id": "c2x2r1", "prompt": "¿Qué recurso estilístico es la repetición de \"nada\"?", "options": ["Metáfora", "Anáfora", "Hipérbole"], "answerIndex": 1, "explanation": "La repetición de una palabra al inicio de frases sucesivas es una anáfora."},
            {"id": "c2x2r2", "prompt": "¿Qué figura retórica es \"sus palabras eran veneno puro\"?", "options": ["Metáfora", "Hipérbaton", "Anáfora"], "answerIndex": 0, "explanation": "Se identifica una cosa (palabras) con otra (veneno) sin usar \"como\": es una metáfora."},
            {"id": "c2x2r3", "prompt": "¿Qué esperaba la persona con acendrada paciencia?", "options": ["El desenlace de una historia", "Una respuesta", "Un viaje"], "answerIndex": 0, "explanation": "El texto dice: «esperó el desenlace de aquella historia»."},
            {"id": "c2x2r4", "prompt": "¿El registro de este texto es literario o coloquial?", "options": ["Literario", "Coloquial"], "answerIndex": 0, "explanation": "El vocabulario elevado (acendrada, desenlace) y los recursos retóricos marcan un registro claramente literario."},
         ]},
        {"id": "c2x2-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c2x2o1", "prompt": "Ordena las palabras.", "words": ["Nada", "teme", "quien", "nada", "posee"], "explanation": "Estructura con anáfora (nada... nada) propia del registro literario."},
            {"id": "c2x2o2", "prompt": "Ordena las palabras.", "words": ["Con", "acendrada", "paciencia", "esperó", "el", "final"], "explanation": "Complemento con adjetivo elevado + verbo + objeto."},
         ]},
    ],
    "c2-matices-lexicos-y-falsos-amigos-avanzados": [
        {"id": "c2x3-reading", "type": "reading-comprehension", "title": "Lectura: Un Malentendido por un Falso Amigo",
         "passage": "<p>Actualmente vivo en Montevideo, aunque nací en Buenos Aires. En realidad, no estoy tan seguro de que esta sea la mejor decisión. Me sentí muy avergonzado después de aquel comentario torpe en la reunión. Mi tía está embarazada de su segundo hijo.</p>",
         "items": [
            {"id": "c2x3r1", "prompt": "¿Qué significa \"actualmente\" en el texto?", "options": ["En realidad", "En este momento", "De manera precisa"], "answerIndex": 1, "explanation": "Actualmente significa «ahora, en este momento», no «en realidad»."},
            {"id": "c2x3r2", "prompt": "¿Dónde nació la persona?", "options": ["En Montevideo", "En Buenos Aires", "No lo dice"], "answerIndex": 1, "explanation": "El texto dice: «aunque nací en Buenos Aires»."},
            {"id": "c2x3r3", "prompt": "¿Por qué se sintió avergonzada la persona?", "options": ["Por un comentario torpe", "Por llegar tarde", "Por perder algo"], "answerIndex": 0, "explanation": "El texto dice: «Me sentí muy avergonzado después de aquel comentario torpe»."},
            {"id": "c2x3r4", "prompt": "¿Qué significa que la tía \"está embarazada\"?", "options": ["Que está avergonzada", "Que espera un bebé", "Que está ocupada"], "answerIndex": 1, "explanation": "Embarazada significa exclusivamente «esperando un bebé», uno de los falsos amigos más conocidos del español."},
         ]},
        {"id": "c2x3-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c2x3o1", "prompt": "Ordena las palabras.", "words": ["En", "realidad", "no", "estoy", "de", "acuerdo"], "explanation": "En realidad (no actualmente) para expresar un matiz de verdad frente a la apariencia."},
            {"id": "c2x3o2", "prompt": "Ordena las palabras.", "words": ["Me", "sentí", "avergonzado", "por", "el", "error"], "explanation": "Sentirse + avergonzado (no embarazado) + causa."},
         ]},
    ],
    "c2-variacion-regional": [
        {"id": "c2x4-reading", "type": "reading-comprehension", "title": "Lectura: Un Recorrido por el Español del Mundo",
         "passage": "<p>En España, el distingo separa la pronunciación de c/z de la s; en América Latina predomina el seseo. En el Caribe es común aspirar la s final, mientras que en el Río de la Plata el yeísmo suena como «sh». Cada variedad es igual de válida y refleja la riqueza del idioma.</p>",
         "items": [
            {"id": "c2x4r1", "prompt": "¿Qué es el distingo, según el texto?", "options": ["Pronunciar c/z igual que s", "Separar la pronunciación de c/z de la s", "No pronunciar la s final"], "answerIndex": 1, "explanation": "El texto dice: «el distingo separa la pronunciación de c/z de la s»."},
            {"id": "c2x4r2", "prompt": "¿Qué predomina en América Latina?", "options": ["El distingo", "El seseo", "El yeísmo con sh"], "answerIndex": 1, "explanation": "El texto dice: «en América Latina predomina el seseo»."},
            {"id": "c2x4r3", "prompt": "¿Qué es común en el Caribe?", "options": ["Aspirar la s final", "El distingo", "El yeísmo con sh"], "answerIndex": 0, "explanation": "El texto dice: «En el Caribe es común aspirar la s final»."},
            {"id": "c2x4r4", "prompt": "¿El texto considera una variedad más correcta que otra?", "options": ["Sí, el distingo es superior", "No, todas son igual de válidas"], "answerIndex": 1, "explanation": "El texto termina: «Cada variedad es igual de válida y refleja la riqueza del idioma»."},
         ]},
        {"id": "c2x4-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c2x4o1", "prompt": "Ordena las palabras.", "words": ["En", "Argentina", "el", "yeísmo", "suena", "distinto"], "explanation": "Complemento de lugar + sujeto + verbo + adjetivo."},
            {"id": "c2x4o2", "prompt": "Ordena las palabras.", "words": ["El", "seseo", "es", "mayoritario", "en", "el", "mundo", "hispanohablante"], "explanation": "Sujeto + ser + adjetivo + complemento de lugar."},
         ]},
    ],
    "c2-cohesion-textual-en-discurso-extenso": [
        {"id": "c2x5-reading", "type": "reading-comprehension", "title": "Lectura: Un Texto Bien Cohesionado",
         "passage": "<p>El estudio analiza tres factores determinantes en el fenómeno observado. El primero de ellos se relaciona con las condiciones económicas locales. Estas, a su vez, influyen directamente en las decisiones que toman las familias. Dicha influencia explica gran parte de los resultados obtenidos.</p>",
         "items": [
            {"id": "c2x5r1", "prompt": "¿Cuántos factores analiza el estudio?", "options": ["Dos", "Tres", "Cuatro"], "answerIndex": 1, "explanation": "El texto dice: «analiza tres factores determinantes»."},
            {"id": "c2x5r2", "prompt": "¿Con qué se relaciona el primer factor?", "options": ["Con la educación", "Con las condiciones económicas locales", "Con la política"], "answerIndex": 1, "explanation": "El texto dice: «El primero de ellos se relaciona con las condiciones económicas locales»."},
            {"id": "c2x5r3", "prompt": "¿A qué influyen esas condiciones, según el texto?", "options": ["A las decisiones de las familias", "Al clima", "A los precios"], "answerIndex": 0, "explanation": "El texto dice: «influyen directamente en las decisiones que toman las familias»."},
            {"id": "c2x5r4", "prompt": "¿Qué palabra retoma la idea anterior para dar cohesión al texto?", "options": ["Estas", "Un nuevo tema", "Nada, cada frase es independiente"], "answerIndex": 0, "explanation": "«Estas» retoma «las condiciones económicas locales» mencionadas antes, dando cohesión al texto."},
         ]},
        {"id": "c2x5-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c2x5o1", "prompt": "Ordena las palabras.", "words": ["El", "informe", "recoge", "varios", "datos", "relevantes"], "explanation": "Sujeto + verbo + objeto con adjetivo."},
            {"id": "c2x5o2", "prompt": "Ordena las palabras.", "words": ["Dicha", "hipótesis", "se", "sostiene", "a", "lo", "largo", "del", "texto"], "explanation": "Dicha (mecanismo de cohesión) + sustantivo + verbo reflexivo + complemento."},
         ]},
    ],
    "c2-modalidad-y-atenuacion-en-discurso-formal": [
        {"id": "c2x6-reading", "type": "reading-comprehension", "title": "Lectura: Una Revisión Cortés",
         "passage": "<p>Cabría reconsiderar esta parte del argumento antes de publicarlo. Todo parece indicar que la hipótesis inicial no era del todo correcta. Se podría argumentar que el estudio adolece de una muestra demasiado pequeña. Convendría, quizá, matizar esta afirmación con datos más recientes.</p>",
         "items": [
            {"id": "c2x6r1", "prompt": "¿Qué sugiere la primera frase?", "options": ["Publicar el argumento tal cual", "Reconsiderar esa parte del argumento", "Eliminar el argumento completamente"], "answerIndex": 1, "explanation": "El texto dice: «Cabría reconsiderar esta parte del argumento antes de publicarlo»."},
            {"id": "c2x6r2", "prompt": "¿Qué parece indicar la evidencia?", "options": ["Que la hipótesis era correcta", "Que la hipótesis no era del todo correcta", "Que no hay ninguna hipótesis"], "answerIndex": 1, "explanation": "El texto dice: «Todo parece indicar que la hipótesis inicial no era del todo correcta»."},
            {"id": "c2x6r3", "prompt": "¿Qué problema podría tener el estudio?", "options": ["Una muestra demasiado pequeña", "Falta de financiamiento", "Demasiados datos"], "answerIndex": 0, "explanation": "El texto dice: «el estudio adolece de una muestra demasiado pequeña»."},
            {"id": "c2x6r4", "prompt": "¿El texto afirma sus críticas de forma tajante o atenuada?", "options": ["De forma tajante", "De forma atenuada"], "answerIndex": 1, "explanation": "Expresiones como cabría, parece indicar y se podría argumentar suavizan el tono de la crítica."},
         ]},
        {"id": "c2x6-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c2x6o1", "prompt": "Ordena las palabras.", "words": ["Cabe", "la", "posibilidad", "de", "que", "esto", "cambie"], "explanation": "Cabe la posibilidad de que + subjuntivo, expresión de modalidad epistémica."},
            {"id": "c2x6o2", "prompt": "Ordena las palabras.", "words": ["Convendría", "revisar", "este", "punto", "con", "calma"], "explanation": "Convendría + infinitivo, forma atenuada de sugerir una acción."},
         ]},
    ],
    "c2-estructuras-arcaicas-o-literarias": [
        {"id": "c2x7-reading", "type": "reading-comprehension", "title": "Lectura: Un Fragmento Clásico",
         "passage": "<p>Vuestra merced, señor hidalgo, perdone mi atrevimiento, ca no hallé otro modo de haceros llegar esta nueva: sois, sin duda, la persona a quien más debo en esta vida, y maguer el tiempo y la distancia, jamás olvidé vuestra bondad.</p>",
         "items": [
            {"id": "c2x7r1", "prompt": "¿A quién se dirige el narrador con \"vuestra merced\"?", "options": ["A varias personas", "A una sola persona con tratamiento reverencial", "A sí mismo"], "answerIndex": 1, "explanation": "Vuestra merced es un tratamiento formal dirigido a una sola persona de respeto."},
            {"id": "c2x7r2", "prompt": "¿Qué significa \"ca\" en este texto medieval?", "options": ["Porque", "Cuando", "Como"], "answerIndex": 0, "explanation": "Ca es una conjunción causal medieval, equivalente a «porque»."},
            {"id": "c2x7r3", "prompt": "¿Qué significa \"maguer\"?", "options": ["Porque", "Aunque", "Nunca"], "answerIndex": 1, "explanation": "Maguer es un arcaísmo que significa «aunque»."},
            {"id": "c2x7r4", "prompt": "¿El narrador olvidó la bondad de esa persona?", "options": ["Sí", "No, nunca la olvidó"], "answerIndex": 1, "explanation": "El texto dice: «jamás olvidé vuestra bondad»."},
         ]},
        {"id": "c2x7-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c2x7o1", "prompt": "Ordena las palabras.", "words": ["Vuestra", "merced", "perdone", "mi", "atrevimiento"], "explanation": "Tratamiento reverencial clásico + verbo + objeto."},
            {"id": "c2x7o2", "prompt": "Ordena las palabras.", "words": ["Sois", "sin", "duda", "muy", "sabio"], "explanation": "Sois (valor reverencial hacia una sola persona) + expresión + adjetivo."},
         ]},
    ],
    "c2-dominio-del-registro-y-transformacion-estilistica": [
        {"id": "c2x8-reading", "type": "reading-comprehension", "title": "Lectura: La Misma Idea, Tres Registros",
         "passage": "<p>Coloquial: Che, al final se nos complicó todo con la mudanza, un lío total.<br>Estándar: Al final tuvimos varios problemas con la mudanza y se complicó bastante.<br>Formal: Lamentamos comunicarle que, debido a diversos inconvenientes, la mudanza se ha visto considerablemente complicada.</p>",
         "items": [
            {"id": "c2x8r1", "prompt": "¿Cuál de las tres versiones es la más coloquial?", "options": ["La primera", "La segunda", "La tercera"], "answerIndex": 0, "explanation": "La primera versión usa che y un lío total, marcas de registro coloquial."},
            {"id": "c2x8r2", "prompt": "¿Qué versión usa la fórmula \"Lamentamos comunicarle\"?", "options": ["La coloquial", "La estándar", "La formal"], "answerIndex": 2, "explanation": "Esa fórmula es propia del registro formal, usada en la tercera versión."},
            {"id": "c2x8r3", "prompt": "¿Las tres versiones comunican la misma idea de fondo?", "options": ["Sí", "No, son ideas distintas"], "answerIndex": 0, "explanation": "Las tres versiones describen el mismo hecho (problemas con la mudanza) en distinto registro."},
            {"id": "c2x8r4", "prompt": "¿Qué distingue principalmente a las tres versiones entre sí?", "options": ["El contenido", "El registro (vocabulario, tono, formalidad)", "El idioma"], "answerIndex": 1, "explanation": "Las tres versiones cambian de registro, no de contenido ni de idioma."},
         ]},
        {"id": "c2x8-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c2x8o1", "prompt": "Ordena las palabras.", "words": ["¿Sería", "tan", "amable", "de", "ayudarme"], "explanation": "Fórmula de cortesía muy formal con condicional (sería) + infinitivo."},
            {"id": "c2x8o2", "prompt": "Ordena las palabras.", "words": ["Oye", "¿me", "puedes", "echar", "una", "mano"], "explanation": "Registro coloquial: oye + petición directa con expresión idiomática."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
