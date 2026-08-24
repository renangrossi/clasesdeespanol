# -*- coding: utf-8 -*-
"""B2 — datos del currículo de nivel intermedio alto. Ver curriculum/SCHEMA.md
para la forma exacta del JSON que esto compila (scripts/generate_curriculum.py
hace la compilación). Escrito como Python en vez de JSON a mano para que el
texto en español con comillas, tildes y ñ se lea con naturalidad.

Curso monolingüe: los ejemplos son strings simples en español, sin
traducción al inglés en ningún campo."""

OVERVIEW = (
    "El nivel B2 completa el sistema del subjuntivo con el imperfecto y las "
    "oraciones condicionales, y profundiza en cuándo el indicativo cede el "
    "paso al subjuntivo en oraciones sustantivas, relativas y adverbiales. "
    "También verás las perífrasis verbales, los usos más avanzados de ser y "
    "estar, la pasiva y las construcciones con se en más profundidad, el "
    "estilo indirecto en todos los tiempos, conectores argumentativos más "
    "sofisticados, colocaciones y expresiones idiomáticas, y la diferencia "
    "entre el registro formal e informal. Al terminar este nivel podrás "
    "interactuar con fluidez y espontaneidad, y argumentar tus ideas con "
    "claridad y matices."
)

LESSONS = [
    {
        "id": "b2-imperfecto-de-subjuntivo",
        "level": "B2", "unit": "1", "order": 1, "skill": "grammar", "strand": "subjuntivo",
        "title": "El Imperfecto de Subjuntivo",
        "subtitle": "Cantara/cantase: el subjuntivo para el pasado, y para hipótesis en el presente.",
        "objectives": [
            "Formar el imperfecto de subjuntivo a partir de la tercera persona plural del pretérito indefinido",
            "Reconocer las dos formas alternativas (-ra y -se) y su uso regional",
            "Usar el imperfecto de subjuntivo en subordinadas cuando el verbo principal está en pasado",
        ],
        "content": {
            "intro": "El subjuntivo no se queda solo en el presente: cuando el verbo principal de la frase está en un tiempo pasado, la subordinada necesita su propio subjuntivo de pasado.",
            "explanation": "<p>La formación es muy regular una vez que conoces el truco: se toma la <strong>tercera persona plural del pretérito indefinido</strong> (ellos hablaron, ellos tuvieron, ellos fueron), se le quita <strong>-ron</strong>, y se añaden las terminaciones <strong>-ra, -ras, -ra, -ramos (con tilde), -rais, -ran</strong>. Como se parte del indefinido, cualquier irregularidad de ese tiempo (tuvieron, fueron, dijeron) se hereda automáticamente.</p><p>Existe una forma alternativa igual de correcta con <strong>-se</strong> (hablase, tuviese, fuese), más frecuente en España y en registros escritos o literarios, mientras que la forma en <strong>-ra</strong> es la más usada en el habla cotidiana de todo el mundo hispanohablante. Se usa siempre que el verbo principal esté en un tiempo pasado y la situación exija subjuntivo (deseo, duda, emoción) — la misma lógica del presente de subjuntivo, pero trasladada al pasado.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Imperfecto de subjuntivo — hablar, tener, ser</caption><thead><tr><th>Sujeto</th><th>hablar</th><th>tener</th><th>ser</th></tr></thead><tbody><tr><td>yo</td><td>hablara / hablase</td><td>tuviera / tuviese</td><td>fuera / fuese</td></tr><tr><td>tú</td><td>hablaras</td><td>tuvieras</td><td>fueras</td></tr><tr><td>él/ella/usted</td><td>hablara</td><td>tuviera</td><td>fuera</td></tr><tr><td>nosotros/as</td><td>habláramos</td><td>tuviéramos</td><td>fuéramos</td></tr><tr><td>vosotros/as</td><td>hablarais</td><td>tuvierais</td><td>fuerais</td></tr><tr><td>ellos/as/ustedes</td><td>hablaran</td><td>tuvieran</td><td>fueran</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Formación a partir del indefinido", "body": "<p>ellos hablaron → hablara-; ellos tuvieron → tuviera-; ellos fueron → fuera-; se añaden las terminaciones -a, -as, -a, -amos (con tilde), -ais, -an.</p>"},
                {"heading": "b) Concordancia de tiempos (pasado → imperfecto de subjuntivo)", "body": "<p><em>Quería que vinieras conmigo.</em> (quería: imperfecto de indicativo → vinieras: imperfecto de subjuntivo) <em>Dudaba que fuera verdad.</em></p>"},
                {"heading": "c) -ra vs. -se", "body": "<p>Ambas formas son intercambiables en la mayoría de los contextos; -ra es más frecuente en el habla de todo el mundo hispanohablante, -se aparece más en España y en la escritura formal.</p>"},
            ],
            "examples": [
                "Le pedí que me ayudara con la mudanza.",
                "No creía que fuera tan tarde ya.",
                "Esperábamos que hicierais buen viaje.",
                "Me sorprendió que ella no supiera la noticia.",
                "Ojalá tuviéramos más tiempo para terminar esto.",
                "Mis padres querían que estudiase medicina.",
                "Dudábamos que llegasen a tiempo al aeropuerto.",
                "Nos alegramos de que vinieras a visitarnos.",
            ],
            "commonMistakes": [
                {"wrong": "Quería que tú vengas conmigo.", "right": "Quería que tú vinieras conmigo.", "why": "Si el verbo principal está en pasado (quería), la subordinada necesita el imperfecto de subjuntivo, no el presente."},
                {"wrong": "Esperaba que ellos tenieran suerte.", "right": "Esperaba que ellos tuvieran suerte.", "why": "El imperfecto de subjuntivo hereda la raíz irregular del indefinido (tuvieron), no la raíz regular del infinitivo."},
                {"wrong": "Nosotros hablaramos con calma.", "right": "Nosotros habláramos con calma.", "why": "La forma de nosotros siempre lleva tilde en la vocal antes de -mos: habláramos, tuviéramos, fuéramos."},
            ],
        },
        "exercises": [
            {"id": "b2is-fill", "type": "fill-blank", "title": "Completa con el Imperfecto de Subjuntivo",
             "items": [
                {"id": "b2is1", "prompt": "Quería que tú ___ (venir) a la fiesta.", "answers": [["vinieras"], ["vinieses"]], "options": ["vinieras", "vienes", "vendrías"], "explanation": "Verbo principal en pasado (quería) + subordinada de deseo: imperfecto de subjuntivo."},
                {"id": "b2is2", "prompt": "No creía que ellos ___ (tener) razón.", "answers": [["tuvieran"], ["tuviesen"]], "options": ["tuvieran", "tienen", "tendrían"], "explanation": "No creer en pasado exige imperfecto de subjuntivo en la subordinada."},
             ]},
            {"id": "b2is-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "b2is3", "prompt": "El imperfecto de subjuntivo de \"decir\" para \"yo\" es...", "options": ["dijera", "decira", "diciera"], "answerIndex": 0, "explanation": "Se parte de ellos dijeron, se quita -ron y se añade -a: dijera."},
             ]},
            {"id": "b2is-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2is4", "incorrect": "Esperaba que hiciera buen tiempo... esperaba que hace buen tiempo.", "answer": ["Esperaba que hiciera buen tiempo."], "explanation": "Con el verbo principal en pasado, la subordinada de deseo necesita el imperfecto de subjuntivo, no el presente de indicativo."},
            ]},
        ],
        "summary": [
            "El imperfecto de subjuntivo se forma a partir de la tercera persona plural del indefinido, quitando -ron y añadiendo -ra/-se + terminaciones.",
            "Se usa en la subordinada cuando el verbo principal está en un tiempo pasado y la frase exige subjuntivo.",
            "Las formas en -ra y -se son intercambiables; -ra es más frecuente en el habla, -se en España y en la escritura formal.",
        ],
    },
    {
        "id": "b2-condicionales-con-si-subjuntivo",
        "level": "B2", "unit": "1", "order": 2, "skill": "grammar", "strand": "condicionales",
        "title": "Condicionales con Si + Subjuntivo",
        "subtitle": "Tres tipos de condicional: real, potencial e irreal de pasado.",
        "objectives": [
            "Distinguir la condicional real (si + presente) de la potencial (si + imperfecto de subjuntivo)",
            "Formar la condicional irreal de pasado con si + pluscuamperfecto de subjuntivo",
            "Elegir el tipo de condicional adecuado según la probabilidad real de la condición",
        ],
        "content": {
            "intro": "El español organiza las condicionales según cuán probable o real consideres la condición — no es una simple traducción palabra por palabra desde otros idiomas, sino un sistema con su propia lógica interna.",
            "explanation": "<p>La <strong>condicional real</strong> (si + presente de indicativo, + presente/futuro/imperativo) describe una condición posible y probable: <em>Si llueve, nos quedamos en casa.</em> La <strong>condicional potencial</strong> (si + imperfecto de subjuntivo, + condicional simple) describe una condición poco probable, contraria a la realidad actual, o puramente hipotética: <em>Si tuviera más dinero, viajaría más.</em></p><p>La <strong>condicional irreal de pasado</strong> (si + pluscuamperfecto de subjuntivo, + condicional compuesto) describe una condición que no se cumplió en el pasado y ya no tiene remedio: <em>Si hubiera estudiado más, habría aprobado el examen</em> (pero no estudió, y ya suspendió). Nunca se usa el condicional simple ni el presente de subjuntivo dentro de la parte introducida por si.</p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Los tres tipos de condicional con si</caption><thead><tr><th>Tipo</th><th>Prótasis (si...)</th><th>Apódosis (consecuencia)</th></tr></thead><tbody><tr><td>Real</td><td>si + presente de indicativo</td><td>presente / futuro / imperativo</td></tr><tr><td>Potencial</td><td>si + imperfecto de subjuntivo</td><td>condicional simple</td></tr><tr><td>Irreal de pasado</td><td>si + pluscuamperfecto de subjuntivo</td><td>condicional compuesto</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Real: condición probable", "body": "<p><em>Si tengo tiempo, te llamo esta tarde.</em> / <em>Si tienes hambre, come algo.</em></p>"},
                {"heading": "b) Potencial: condición poco probable o hipotética", "body": "<p><em>Si fuera rico, no trabajaría nunca más.</em> / <em>Si vivieras aquí, nos veríamos más a menudo.</em></p>"},
                {"heading": "c) Irreal de pasado: condición que no se cumplió", "body": "<p><em>Si hubieras llegado antes, habrías visto a tu hermano.</em> (pero llegaste tarde, y ya no lo viste)</p>"},
                {"heading": "d) Nunca condicional ni presente de subjuntivo tras si", "body": "<p><em>Si tendría dinero</em> es incorrecto; la forma correcta siempre es <em>si tuviera dinero.</em></p>"},
            ],
            "examples": [
                "Si apruebo el examen, celebraremos con una cena.",
                "Si fuera tú, no aceptaría esa oferta de trabajo.",
                "Si hubiéramos salido antes, no habríamos perdido el vuelo.",
                "Si tienes tiempo esta tarde, pásate por casa.",
                "Si tuviera un jardín más grande, plantaría más árboles.",
                "Si hubiera sabido la verdad, habría actuado diferente.",
                "Si necesitas ayuda, avísame sin problema.",
                "Si no hubieras llamado, me habría preocupado mucho.",
            ],
            "commonMistakes": [
                {"wrong": "Si tendría más tiempo, viajaría más.", "right": "Si tuviera más tiempo, viajaría más.", "why": "Nunca se usa el condicional simple dentro de la parte introducida por si; se necesita el imperfecto de subjuntivo."},
                {"wrong": "Si hubiera estudiado más, aprobaría el examen.", "right": "Si hubiera estudiado más, habría aprobado el examen.", "why": "La condicional irreal de pasado necesita el condicional compuesto en la consecuencia, no el condicional simple."},
                {"wrong": "Si llueve mañana, nos quedaríamos en casa.", "right": "Si llueve mañana, nos quedamos en casa.", "why": "La condicional real usa presente en ambas partes (o futuro), no condicional, que corresponde a la potencial."},
            ],
        },
        "exercises": [
            {"id": "b2ci-fill", "type": "fill-blank", "title": "Completa la Condicional",
             "items": [
                {"id": "b2ci1", "prompt": "Si ___ (yo - tener) más vacaciones, ___ (viajar) por toda Sudamérica.", "answers": [["tuviera"], ["viajaría"]], "options": ["tuviera", "viajaría"], "explanation": "Condicional potencial: si + imperfecto de subjuntivo + condicional simple."},
                {"id": "b2ci2", "prompt": "Si ___ (nosotros - saber) la verdad antes, ___ (actuar) de otra manera.", "answers": [["hubiéramos sabido"], ["habríamos actuado"]], "options": ["hubiéramos sabido", "habríamos actuado"], "explanation": "Condicional irreal de pasado: si + pluscuamperfecto de subjuntivo + condicional compuesto."},
             ]},
            {"id": "b2ci-mc", "type": "multiple-choice", "title": "Identifica el Tipo de Condicional",
             "items": [
                {"id": "b2ci3", "prompt": "\"Si estudias todos los días, aprenderás mucho más rápido.\" es una condicional...", "options": ["real", "potencial", "irreal de pasado"], "answerIndex": 0, "explanation": "Presente + futuro describe una condición real y probable."},
             ]},
            {"id": "b2ci-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2ci4", "incorrect": "Si fueras más paciente, habrías conseguido el trabajo.", "answer": ["Si hubieras sido más paciente, habrías conseguido el trabajo."], "explanation": "La apódosis está en condicional compuesto, así que la prótasis debe ir en pluscuamperfecto de subjuntivo, no en imperfecto de subjuntivo."},
            ]},
        ],
        "summary": [
            "La condicional real usa si + presente, con presente/futuro/imperativo en la consecuencia, para condiciones probables.",
            "La condicional potencial usa si + imperfecto de subjuntivo + condicional simple, para condiciones poco probables o hipotéticas.",
            "La condicional irreal de pasado usa si + pluscuamperfecto de subjuntivo + condicional compuesto, para condiciones que ya no se cumplieron.",
        ],
    },
    {
        "id": "b2-subjuntivo-vs-indicativo-sustantivas",
        "level": "B2", "unit": "1", "order": 3, "skill": "grammar", "strand": "subjuntivo",
        "title": "Subjuntivo vs. Indicativo en Oraciones Sustantivas",
        "subtitle": "Cómo saber, sin dudar, si el verbo de la subordinada va en indicativo o en subjuntivo.",
        "objectives": [
            "Clasificar expresiones impersonales según exijan indicativo o subjuntivo",
            "Reconocer los verbos de información/comunicación que alternan según su significado",
            "Aplicar la prueba de la certeza para decidir entre indicativo y subjuntivo",
        ],
        "content": {
            "intro": "Ya conoces los grandes grupos (deseo, duda, emoción) que activan el subjuntivo; en B2 toca afinar los casos más sutiles y las expresiones impersonales, que son extremadamente frecuentes en español.",
            "explanation": "<p>La prueba más fiable es preguntarse: <strong>¿el hablante presenta esto como un hecho cierto y real, o como algo deseado, dudoso, valorado o no confirmado?</strong> Si es un hecho cierto, va indicativo; si no, va subjuntivo. Las expresiones impersonales de certeza (<em>es verdad que, es evidente que, está claro que</em>) piden indicativo; las de valoración u opinión no factual (<em>es importante que, es una lástima que, es posible que</em>) piden subjuntivo.</p><p>Verbos como <strong>decir, contar, comentar</strong> alternan según su significado: cuando informan de un hecho, van con indicativo (<em>Me dijo que llegaba tarde</em>); cuando dan una orden o instrucción, van con subjuntivo (<em>Me dijo que llegara temprano</em>).</p>",
            "rules": [
                {"heading": "a) Expresiones impersonales de certeza → indicativo", "body": "<p><em>es verdad que, es evidente que, está claro que, es seguro que</em> + indicativo: <em>Es evidente que ella tiene razón.</em></p>"},
                {"heading": "b) Expresiones impersonales de valoración/duda → subjuntivo", "body": "<p><em>es importante que, es una lástima que, es posible que, es raro que, más vale que</em> + subjuntivo: <em>Es una lástima que no puedas venir.</em></p>"},
                {"heading": "c) Decir/comentar: informar vs. mandar", "body": "<p>Informar (indicativo): <em>Me dijo que estaba cansada.</em> Mandar/pedir (subjuntivo): <em>Me dijo que descansara un poco.</em></p>"},
                {"heading": "d) Negar la certeza convierte el indicativo en subjuntivo", "body": "<p><em>Es verdad que viene</em> (indicativo) → <em>No es verdad que venga</em> (subjuntivo, porque la negación elimina la certeza).</p>"},
            ],
            "examples": [
                "Es evidente que este plan no va a funcionar así.",
                "Es una lástima que no hayas podido venir a la boda.",
                "Está claro que ella sabe más de lo que dice.",
                "Es posible que lleguemos un poco tarde a la cena.",
                "Me comentó que el proyecto salía bien, aunque con retraso.",
                "El jefe pidió que termináramos el informe antes del viernes.",
                "No es cierto que él haya dicho eso.",
                "Más vale que llames antes de presentarte sin avisar.",
            ],
            "commonMistakes": [
                {"wrong": "Es evidente que ella tenga razón.", "right": "Es evidente que ella tiene razón.", "why": "Es evidente que presenta un hecho como cierto y exige indicativo, no subjuntivo."},
                {"wrong": "Es importante que tú vienes a la reunión.", "right": "Es importante que tú vengas a la reunión.", "why": "Es importante que valora, no afirma un hecho como certeza objetiva: exige subjuntivo."},
                {"wrong": "Me dijo que viniera a las ocho (informando de un hecho, no una orden).", "right": "Me dijo que venía a las ocho.", "why": "Si decir solo informa de un hecho (a qué hora venía), corresponde el indicativo; el subjuntivo se reserva para cuando decir da una orden o petición."},
            ],
        },
        "exercises": [
            {"id": "b2sv-fill", "type": "fill-blank", "title": "Completa con Indicativo o Subjuntivo",
             "items": [
                {"id": "b2sv1", "prompt": "Es verdad que ella ___ (tener) mucha experiencia.", "answers": [["tiene"]], "options": ["tiene", "tenga", "tendría"], "explanation": "Es verdad que presenta un hecho cierto: indicativo."},
                {"id": "b2sv2", "prompt": "Es una lástima que no ___ (poder, tú) quedarte más tiempo.", "answers": [["puedas"]], "options": ["puedas", "puedes", "podrás"], "explanation": "Es una lástima que valora emocionalmente el hecho: subjuntivo."},
             ]},
            {"id": "b2sv-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "b2sv3", "prompt": "\"No es cierto que él ___ toda la verdad.\"", "options": ["dice", "diga", "dirá"], "answerIndex": 1, "explanation": "La negación de no es cierto que elimina la certeza y exige subjuntivo."},
             ]},
            {"id": "b2sv-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2sv4", "incorrect": "Está claro que ella tenga toda la razón en esto.", "answer": ["Está claro que ella tiene toda la razón en esto."], "explanation": "Está claro que presenta un hecho como cierto: exige indicativo, no subjuntivo."},
            ]},
        ],
        "summary": [
            "Las expresiones impersonales de certeza (es verdad que, es evidente que) piden indicativo; las de valoración o duda (es importante que, es posible que) piden subjuntivo.",
            "Decir y verbos similares alternan: informan con indicativo, mandan u ordenan con subjuntivo.",
            "Negar una expresión de certeza elimina esa certeza y convierte el verbo de indicativo a subjuntivo.",
        ],
    },
    {
        "id": "b2-subjuntivo-relativas-y-adverbiales",
        "level": "B2", "unit": "1", "order": 4, "skill": "grammar", "strand": "subjuntivo",
        "title": "El Subjuntivo en Relativas y Adverbiales",
        "subtitle": "Cuando el antecedente es desconocido, y con conjunciones que siempre exigen subjuntivo.",
        "objectives": [
            "Usar el subjuntivo en oraciones relativas cuando el antecedente es desconocido o inexistente",
            "Reconocer las conjunciones adverbiales que siempre exigen subjuntivo",
            "Distinguir cuándo aunque va con indicativo y cuándo va con subjuntivo",
        ],
        "content": {
            "intro": "El subjuntivo no solo aparece en subordinadas sustantivas: también gobierna oraciones relativas cuando no se está seguro de que algo exista, y una serie de conjunciones adverbiales que llevan subjuntivo de forma automática.",
            "explanation": "<p>En una oración relativa, si el antecedente (la persona o cosa de la que se habla) es <strong>conocido y específico</strong>, se usa indicativo; si es <strong>desconocido, indefinido o inexistente</strong>, se usa subjuntivo: <em>Busco un piso que tiene terraza</em> (existe, ya lo vi) frente a <em>Busco un piso que tenga terraza</em> (no sé si existe tal piso, es una búsqueda abierta).</p><p>Un grupo de conjunciones exige subjuntivo siempre, sin importar el contexto, porque introducen una finalidad, condición o hecho todavía no realizado: <strong>para que, sin que, a menos que, con tal de que, en caso de que, antes de que</strong>. La conjunción <strong>aunque</strong> es especial: con indicativo presenta el obstáculo como un hecho real (<em>Aunque llueve, salimos</em>); con subjuntivo, como una posibilidad o algo no confirmado (<em>Aunque llueva, saldremos</em>).</p>",
            "rules": [
                {"heading": "a) Relativas con antecedente conocido → indicativo", "body": "<p><em>Tengo un amigo que habla cinco idiomas.</em> (existe, lo conozco)</p>"},
                {"heading": "b) Relativas con antecedente desconocido/inexistente → subjuntivo", "body": "<p><em>Necesito un amigo que hable cinco idiomas.</em> (no sé si existe tal persona) <em>No hay nadie que sepa la respuesta.</em> (antecedente inexistente)</p>"},
                {"heading": "c) Conjunciones que siempre exigen subjuntivo", "body": "<p><em>para que, sin que, a menos que, con tal de que, en caso de que, antes de que</em>: <em>Te lo explico para que lo entiendas bien.</em></p>"},
                {"heading": "d) Aunque: depende de si el hablante da el hecho por real", "body": "<p>Indicativo (hecho real, conocido): <em>Aunque hace frío, voy a salir a correr.</em> Subjuntivo (posibilidad, no confirmado): <em>Aunque haga frío mañana, voy a salir a correr.</em></p>"},
            ],
            "examples": [
                "Busco un trabajo que me permita viajar con frecuencia.",
                "Conozco a alguien que puede arreglar tu computadora.",
                "No hay ningún restaurante por aquí que esté abierto ahora.",
                "Te doy la llave para que entres cuando quieras.",
                "No voy a firmar nada sin que me lo expliques todo bien.",
                "Aunque tenga poco tiempo, intentaré ayudarte con esto.",
                "Aunque llovió toda la noche, el partido se jugó igual.",
                "Avísame en caso de que necesites algo más.",
            ],
            "commonMistakes": [
                {"wrong": "Busco una casa que tiene jardín. (sin saber si existe)", "right": "Busco una casa que tenga jardín.", "why": "Como no se sabe si tal casa existe, el antecedente es indefinido y exige subjuntivo."},
                {"wrong": "Te lo explico para que lo entiendes.", "right": "Te lo explico para que lo entiendas.", "why": "Para que siempre exige subjuntivo, sin excepción, en cualquier contexto."},
                {"wrong": "Aunque hace mucho frío ahora mismo, quizá salga igual (dando el hecho por cierto pero usando subjuntivo por error).", "right": "Aunque hace mucho frío ahora mismo, quizá salga igual.", "why": "Si el frío es un hecho real y confirmado en este momento, aunque debe llevar indicativo (hace), no subjuntivo."},
            ],
        },
        "exercises": [
            {"id": "b2sr-fill", "type": "fill-blank", "title": "Completa con Indicativo o Subjuntivo",
             "items": [
                {"id": "b2sr1", "prompt": "Tengo un vecino que ___ (hablar) tres idiomas. (existe, lo conozco)", "answers": [["habla"]], "options": ["habla", "hable", "hablará"], "explanation": "Antecedente conocido y específico: indicativo."},
                {"id": "b2sr2", "prompt": "Necesito un vecino que me ___ (poder) ayudar con la mudanza. (no sé si existe)", "answers": [["pueda"]], "options": ["pueda", "puede", "podrá"], "explanation": "Antecedente desconocido o hipotético: subjuntivo."},
             ]},
            {"id": "b2sr-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "b2sr3", "prompt": "\"Te ayudo con tal de que me ___ un favor a mí también.\"", "options": ["haces", "hagas", "harás"], "answerIndex": 1, "explanation": "Con tal de que siempre exige subjuntivo."},
             ]},
            {"id": "b2sr-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2sr4", "incorrect": "No hay nadie aquí que sabe la respuesta.", "answer": ["No hay nadie aquí que sepa la respuesta."], "explanation": "Un antecedente inexistente (nadie) siempre exige subjuntivo en la oración relativa."},
            ]},
        ],
        "summary": [
            "El antecedente conocido y específico exige indicativo en la relativa; el desconocido, indefinido o inexistente exige subjuntivo.",
            "Para que, sin que, a menos que, con tal de que, en caso de que y antes de que siempre exigen subjuntivo, en cualquier contexto.",
            "Aunque lleva indicativo cuando el hablante da el hecho por real y confirmado, y subjuntivo cuando lo presenta como una posibilidad no confirmada.",
        ],
    },
    {
        "id": "b2-perifrasis-verbales",
        "level": "B2", "unit": "1", "order": 5, "skill": "grammar", "strand": "perifrasis",
        "title": "Perífrasis Verbales",
        "subtitle": "Verbo conjugado + (preposición) + infinitivo/gerundio/participio: matices de aspecto que un solo verbo no puede dar.",
        "objectives": [
            "Reconocer la estructura de una perífrasis verbal (auxiliar + enlace opcional + forma no personal)",
            "Usar perífrasis frecuentes de infinitivo, gerundio y participio con su matiz propio",
            "Distinguir el significado de perífrasis parecidas entre sí (dejar de vs. acabar de, llevar + gerundio vs. seguir + gerundio)",
        ],
        "content": {
            "intro": "Las perífrasis verbales combinan dos verbos para expresar matices de tiempo, aspecto o modalidad que un solo verbo conjugado no puede transmitir por sí solo — cuanto más las domines, más natural sonará tu español.",
            "explanation": "<p>Una perífrasis tiene siempre un <strong>verbo auxiliar conjugado</strong> (que pierde su significado literal), a veces un <strong>enlace</strong> (una preposición o <em>que</em>), y una <strong>forma no personal</strong> del verbo principal (infinitivo, gerundio o participio) que aporta el significado real de la acción. Las de <strong>infinitivo</strong> suelen marcar el momento de la acción (empezar a, dejar de, acabar de, volver a); las de <strong>gerundio</strong> marcan que la acción está en desarrollo (estar, seguir, llevar + gerundio); las de <strong>participio</strong> marcan un resultado (tener + participio).</p>",
            "rules": [
                {"heading": "a) Perífrasis de infinitivo", "body": "<ul><li><em>empezar a + infinitivo</em>: <em>Empezó a llover de repente.</em></li><li><em>dejar de + infinitivo</em> (interrumpir un hábito): <em>Dejé de fumar hace un año.</em></li><li><em>acabar de + infinitivo</em> (pasado muy reciente): <em>Acabo de llegar a casa.</em></li><li><em>volver a + infinitivo</em> (repetir): <em>Volvió a llamar por tercera vez.</em></li><li><em>llevar + gerundio</em> (duración hasta ahora): <em>Llevo dos años estudiando español.</em></li></ul>"},
                {"heading": "b) Perífrasis de gerundio", "body": "<ul><li><em>estar + gerundio</em> (acción en curso): <em>Estoy escribiendo un correo.</em></li><li><em>seguir + gerundio</em> (continuar): <em>Sigue trabajando en el mismo lugar.</em></li><li><em>ir + gerundio</em> (progreso gradual): <em>Va mejorando poco a poco.</em></li></ul>"},
                {"heading": "c) Perífrasis de participio", "body": "<p><em>tener + participio</em> (resultado acumulado, concuerda con el objeto): <em>Tengo escritas ya diez páginas.</em></p>"},
            ],
            "examples": [
                "Acabo de terminar el informe hace cinco minutos.",
                "Llevo tres horas esperando el autobús.",
                "Dejó de trabajar allí el año pasado.",
                "Volví a leer el mismo libro después de tantos años.",
                "Sigo pensando que fue la mejor decisión posible.",
                "Va aprendiendo cada vez más rápido con la práctica.",
                "Tengo pensadas varias opciones para las vacaciones.",
                "Empezó a estudiar árabe el mes pasado.",
            ],
            "commonMistakes": [
                {"wrong": "Acabo llegar a casa.", "right": "Acabo de llegar a casa.", "why": "Acabar de + infinitivo necesita el enlace de; sin él, el verbo pierde el sentido de perífrasis de pasado reciente."},
                {"wrong": "Llevo estudiando español dos años.", "right": "Llevo dos años estudiando español.", "why": "En llevar + tiempo + gerundio, la expresión de tiempo va normalmente entre llevar y el gerundio, no después de este."},
                {"wrong": "Tengo escrito ya diez páginas.", "right": "Tengo escritas ya diez páginas.", "why": "En tener + participio, el participio concuerda en género y número con el objeto directo: páginas (femenino plural) pide escritas."},
            ],
        },
        "exercises": [
            {"id": "b2pv-fill", "type": "fill-blank", "title": "Completa con la Perífrasis Correcta",
             "items": [
                {"id": "b2pv1", "prompt": "___ (Yo - acabar) de hablar con mi hermana por teléfono.", "answers": [["Acabo"]], "options": ["Acabo", "Dejo", "Sigo"], "explanation": "Acabar de + infinitivo expresa un pasado muy reciente."},
                {"id": "b2pv2", "prompt": "Ella ___ (llevar) cinco años viviendo en Madrid.", "answers": [["lleva"]], "options": ["lleva", "sigue", "va"], "explanation": "Llevar + tiempo + gerundio expresa una duración que continúa hasta ahora."},
             ]},
            {"id": "b2pv-mc", "type": "multiple-choice", "title": "Elige la Perífrasis Correcta",
             "items": [
                {"id": "b2pv3", "prompt": "¿Cuál expresa que una acción se interrumpió y ya no continúa?", "options": ["seguir + gerundio", "dejar de + infinitivo", "volver a + infinitivo"], "answerIndex": 1, "explanation": "Dejar de + infinitivo expresa la interrupción de un hábito o acción."},
                {"id": "b2pv4", "prompt": "¿Cuál expresa que una acción se repite después de un tiempo?", "options": ["volver a + infinitivo", "acabar de + infinitivo", "estar + gerundio"], "answerIndex": 0, "explanation": "Volver a + infinitivo expresa la repetición de una acción."},
             ]},
            {"id": "b2pv-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2pv5", "incorrect": "Dejé fumar hace dos años.", "answer": ["Dejé de fumar hace dos años."], "explanation": "Dejar de + infinitivo necesita siempre el enlace de."},
            ]},
        ],
        "summary": [
            "Una perífrasis verbal combina un auxiliar conjugado, a veces un enlace, y una forma no personal que aporta el significado real.",
            "Las de infinitivo marcan el momento de la acción (empezar a, dejar de, acabar de, volver a); las de gerundio, que está en desarrollo; las de participio, un resultado.",
            "En tener + participio, el participio concuerda en género y número con el objeto, a diferencia del participio invariable de haber + participio.",
        ],
    },
    {
        "id": "b2-ser-y-estar-avanzado",
        "level": "B2", "unit": "1", "order": 6, "skill": "grammar", "strand": "verbos",
        "title": "Ser y Estar — Usos Avanzados",
        "subtitle": "Estar + adjetivo con valor de \"parecer/resultar\", ser para eventos, y otros matices más allá de lo básico.",
        "objectives": [
            "Usar estar con adjetivos para expresar una impresión subjetiva en el momento",
            "Usar ser para localizar eventos y estar para localizar lugares y objetos",
            "Explicar el cambio de significado de más adjetivos según se usen con ser o estar",
        ],
        "content": {
            "intro": "Más allá de la distinción básica entre identidad/característica (ser) y ubicación/estado (estar), estos dos verbos tienen usos más sutiles que un hablante de nivel avanzado debe dominar.",
            "explanation": "<p>Un uso muy frecuente de <strong>estar + adjetivo</strong> no describe un cambio real, sino una <strong>impresión subjetiva</strong> del hablante en el momento en que habla: <em>¡Qué guapa estás hoy!</em> no implica que normalmente no lo sea, sino que hoy causa esa impresión especial. Con <strong>eventos</strong> (una fiesta, una reunión, un examen), se usa <strong>ser</strong> para preguntar dónde tienen lugar, aunque para objetos y personas se use estar: <em>La boda es en la playa</em> frente a <em>La playa está cerca del pueblo.</em></p><p>Otros pares de adjetivos cambian de significado de forma más sutil que bueno/listo: <em>ser rico</em> (tener mucho dinero) frente a <em>estar rico</em> (saber delicioso, hablando de comida); <em>ser vivo</em> (astuto) frente a <em>estar vivo</em> (con vida, no muerto).</p>",
            "rules": [
                {"heading": "a) Estar + adjetivo: impresión subjetiva", "body": "<p><em>¡Qué joven estás en esta foto!</em> (impresión, no cambio real de edad) <em>La sopa está buenísima hoy.</em> (impresión sobre esta sopa en concreto)</p>"},
                {"heading": "b) Ser para eventos, estar para lugares/objetos/personas", "body": "<p><em>¿Dónde es la fiesta?</em> (evento) frente a <em>¿Dónde está la casa?</em> (lugar físico)</p>"},
                {"heading": "c) Más pares de adjetivos con significado distinto", "body": "<ul><li><em>ser rico</em> (dinero) / <em>estar rico</em> (sabor)</li><li><em>ser vivo</em> (astuto) / <em>estar vivo</em> (con vida)</li><li><em>ser malo</em> (mala persona/de mala calidad) / <em>estar malo</em> (enfermo, o en mal estado un alimento)</li><li><em>ser negro</em> (color) / <em>estar negro</em> (bronceado, o furioso, según el contexto)</li></ul>"},
            ],
            "examples": [
                "¡Qué elegante estás con ese traje nuevo!",
                "La conferencia es en el auditorio principal de la universidad.",
                "El hospital está a dos calles de aquí.",
                "Este plato está buenísimo, ¿qué le pusiste?",
                "Mi abuelo es muy vivo para su edad, nada se le escapa.",
                "El perro sigue vivo a pesar de todo lo que pasó.",
                "Estoy negro de tanto tomar el sol en la playa.",
                "La reunión es a las diez en la sala de conferencias.",
            ],
            "commonMistakes": [
                {"wrong": "¿Dónde está la fiesta de cumpleaños?", "right": "¿Dónde es la fiesta de cumpleaños?", "why": "Para localizar un evento (no un objeto o lugar físico en sí), se usa ser, no estar."},
                {"wrong": "Esta comida es muy rica hoy, mejor que ayer.", "right": "Esta comida está muy rica hoy, mejor que ayer.", "why": "El sabor de una comida en un momento concreto se describe con estar, no con ser (que indicaría riqueza económica)."},
                {"wrong": "Mi tío está muy vivo, siempre encuentra una solución.", "right": "Mi tío es muy vivo, siempre encuentra una solución.", "why": "Ser vivo describe astucia como característica; estar vivo se refiere solo a estar con vida."},
            ],
        },
        "exercises": [
            {"id": "b2se-mc", "type": "multiple-choice", "title": "Elige Ser o Estar",
             "items": [
                {"id": "b2se1", "prompt": "¿Dónde ___ el concierto de esta noche?", "options": ["es", "está"], "answerIndex": 0, "explanation": "Localizar un evento siempre usa ser."},
                {"id": "b2se2", "prompt": "Este postre ___ delicioso, ¿lo hiciste tú?", "options": ["es", "está"], "answerIndex": 1, "explanation": "El sabor percibido en el momento se expresa con estar."},
                {"id": "b2se3", "prompt": "Mi jefa ___ muy viva, siempre anticipa los problemas.", "options": ["es", "está"], "answerIndex": 0, "explanation": "Ser vivo describe astucia como característica de la persona."},
             ]},
            {"id": "b2se-fill", "type": "fill-blank", "title": "Completa con Ser o Estar",
             "items": [
                {"id": "b2se4", "prompt": "¡Qué guapo ___ (tú) con ese corte de pelo!", "answers": [["estás"]], "options": ["estás", "eres"], "explanation": "Impresión subjetiva del hablante en el momento: estar."},
             ]},
            {"id": "b2se-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2se5", "incorrect": "La reunión está en la sala tres esta tarde.", "answer": ["La reunión es en la sala tres esta tarde."], "explanation": "Localizar un evento como una reunión siempre usa ser, no estar."},
            ]},
        ],
        "summary": [
            "Estar + adjetivo puede expresar una impresión subjetiva del hablante en el momento, sin implicar un cambio real.",
            "Ser localiza eventos (dónde es la fiesta); estar localiza lugares, objetos y personas (dónde está la casa).",
            "Varios pares de adjetivos (rico, vivo, malo, negro) cambian de significado según se combinen con ser o con estar.",
        ],
    },
    {
        "id": "b2-pasiva-avanzada-y-se",
        "level": "B2", "unit": "1", "order": 7, "skill": "grammar", "strand": "voz-pasiva",
        "title": "Pasiva Avanzada y Construcciones con Se",
        "subtitle": "Se + verbo con complemento indirecto: el se de los sucesos involuntarios.",
        "objectives": [
            "Formar construcciones con se para expresar sucesos involuntarios o accidentales",
            "Distinguir el se accidental del se reflexivo y de la pasiva refleja",
            "Reconocer los distintos valores de se en un texto (reflexivo, recíproco, pasivo, accidental)",
        ],
        "content": {
            "intro": "El pronombre se en español tiene varios usos distintos, y uno de los más interesantes es el que describe algo que le pasa a alguien sin que esa persona lo haya causado a propósito.",
            "explanation": "<p>La construcción <strong>se + pronombre de objeto indirecto + verbo</strong> presenta un hecho como accidental o involuntario, quitando la responsabilidad directa del sujeto: <em>Se me rompió el vaso</em> (en vez de \"rompí el vaso\", que sonaría como si lo hubiera hecho a propósito). El verbo concuerda con lo que se rompió/perdió/olvidó, no con la persona.</p><p>Es importante distinguir los distintos valores de <strong>se</strong> en español: <strong>reflexivo</strong> (<em>Ella se lava las manos</em> — a sí misma), <strong>recíproco</strong> (<em>Se abrazaron al despedirse</em> — el uno al otro), <strong>pasiva refleja</strong> (<em>Se venden pisos</em>) y <strong>accidental</strong> (<em>Se me olvidaron las llaves</em>) — cuatro construcciones distintas con la misma partícula.</p>",
            "rules": [
                {"heading": "a) Estructura del se accidental", "body": "<p>se + me/te/le/nos/os/les + verbo (concordado con lo que sucede) + sujeto real: <em>Se le cayeron los papeles.</em> (a él/ella, sin querer, se cayeron los papeles)</p>"},
                {"heading": "b) Verbos frecuentes en esta construcción", "body": "<p><em>caer, romper, perder, olvidar, quedar, acabar/terminar</em>: <em>Se nos acabó la leche. Se te olvidó el paraguas.</em></p>"},
                {"heading": "c) Los cuatro valores de se", "body": "<ul><li>Reflexivo: <em>Me visto rápido.</em></li><li>Recíproco: <em>Se escriben cartas todas las semanas.</em></li><li>Pasiva refleja: <em>Se necesita personal con experiencia.</em></li><li>Accidental: <em>Se me perdió el teléfono.</em></li></ul>"},
            ],
            "examples": [
                "Se me rompió el teléfono sin querer esta mañana.",
                "Se nos olvidaron las llaves dentro del coche.",
                "A ella se le cayó el café encima del vestido.",
                "Se les acabó el tiempo antes de terminar el examen.",
                "Se me perdió la cartera en algún lugar del centro.",
                "Se te quedó el libro en mi casa la semana pasada.",
                "Se nos hizo tarde y perdimos el autobús.",
                "Se le rompieron los pantalones nuevos el primer día.",
            ],
            "commonMistakes": [
                {"wrong": "Me rompí el vaso.", "right": "Se me rompió el vaso.", "why": "Para presentar un hecho como accidental, sin intención, se usa la construcción con se + pronombre de objeto indirecto, no un verbo reflexivo directo."},
                {"wrong": "Se me rompieron el vaso.", "right": "Se me rompió el vaso.", "why": "El verbo debe concordar con lo que sucede (el vaso, singular), no con la persona afectada."},
                {"wrong": "Se olvidó a mí las llaves.", "right": "Se me olvidaron las llaves.", "why": "La persona afectada se marca con el pronombre de objeto indirecto (me), no con a mí + verbo sin pronombre."},
            ],
        },
        "exercises": [
            {"id": "b2pa-fill", "type": "fill-blank", "title": "Completa con Se + Pronombre",
             "items": [
                {"id": "b2pa1", "prompt": "___ (a mí) ___ (romper) los platos sin querer.", "answers": [["Se"], ["me rompieron"]], "options": ["Se", "me rompieron"], "explanation": "Se + me + verbo concordado en plural con los platos: se me rompieron."},
                {"id": "b2pa2", "prompt": "___ (a nosotros) ___ (acabar) la paciencia con este proyecto.", "answers": [["Se"], ["nos acabó"]], "options": ["Se", "nos acabó"], "explanation": "Se + nos + verbo concordado en singular con la paciencia: se nos acabó."},
             ]},
            {"id": "b2pa-mc", "type": "multiple-choice", "title": "Identifica el Valor de Se",
             "items": [
                {"id": "b2pa3", "prompt": "\"Se abrazaron con mucha emoción al reencontrarse.\" es un se...", "options": ["reflexivo", "recíproco", "accidental"], "answerIndex": 1, "explanation": "El uno al otro: valor recíproco."},
                {"id": "b2pa4", "prompt": "\"Se me quedaron las gafas en el tren.\" es un se...", "options": ["reflexivo", "pasiva refleja", "accidental"], "answerIndex": 2, "explanation": "Un hecho presentado como accidental o involuntario: valor accidental."},
             ]},
            {"id": "b2pa-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2pa5", "incorrect": "Se me cayó los libros de las manos.", "answer": ["Se me cayeron los libros de las manos."], "explanation": "El verbo debe concordar en plural con los libros, no quedarse en singular."},
            ]},
        ],
        "summary": [
            "La construcción se + objeto indirecto + verbo presenta un hecho como accidental, quitando responsabilidad directa al sujeto.",
            "El verbo concuerda con lo que sucede (el objeto real), nunca con la persona afectada.",
            "Se tiene al menos cuatro valores distintos en español: reflexivo, recíproco, pasiva refleja y accidental.",
        ],
    },
    {
        "id": "b2-estilo-indirecto-todos-los-tiempos",
        "level": "B2", "unit": "1", "order": 8, "skill": "grammar", "strand": "estilo-indirecto",
        "title": "Estilo Indirecto en Todos los Tiempos",
        "subtitle": "Cómo cambian los tiempos verbales cuando el verbo introductor está en pasado.",
        "objectives": [
            "Aplicar la concordancia de tiempos completa al reportar desde un verbo introductor en pasado",
            "Transformar imperativos en estilo indirecto usando el imperfecto de subjuntivo",
            "Ajustar marcadores de tiempo y lugar al cambiar de estilo directo a indirecto",
        ],
        "content": {
            "intro": "En B1 viste el estilo indirecto con el verbo introductor en presente, donde casi nada cambia de tiempo verbal; ahora toca el caso más complejo y más frecuente en la narración: cuando ese verbo introductor está en pasado.",
            "explanation": "<p>Cuando el verbo introductor está en pasado (<em>dijo que...</em>), el tiempo verbal de la subordinada retrocede un paso según una tabla fija de correspondencias: el presente pasa a imperfecto, el pretérito perfecto/indefinido pasa a pluscuamperfecto, el futuro pasa a condicional, y el imperativo pasa a imperfecto de subjuntivo.</p><p>Además de los tiempos verbales, también cambian los marcadores de tiempo y lugar para reflejar la nueva perspectiva: <em>hoy → ese día, mañana → al día siguiente, ayer → el día anterior, aquí → allí, este → aquel.</em></p>",
            "table": '<div class="table-scroll"><table class="ref-table"><caption>Cambios de tiempo verbal (verbo introductor en pasado)</caption><thead><tr><th>Estilo directo</th><th>Estilo indirecto</th></tr></thead><tbody><tr><td>presente</td><td>imperfecto</td></tr><tr><td>pretérito perfecto/indefinido</td><td>pluscuamperfecto</td></tr><tr><td>futuro simple</td><td>condicional simple</td></tr><tr><td>imperativo</td><td>imperfecto de subjuntivo</td></tr></tbody></table></div>',
            "rules": [
                {"heading": "a) Presente → imperfecto", "body": "<p>\"Estoy cansada\" → <em>Dijo que estaba cansada.</em></p>"},
                {"heading": "b) Pretérito → pluscuamperfecto", "body": "<p>\"Llegué tarde\" → <em>Me contó que había llegado tarde.</em></p>"},
                {"heading": "c) Futuro → condicional", "body": "<p>\"Vendré mañana\" → <em>Prometió que vendría al día siguiente.</em></p>"},
                {"heading": "d) Imperativo → imperfecto de subjuntivo", "body": "<p>\"Cierra la puerta\" → <em>Me pidió que cerrara la puerta.</em></p>"},
                {"heading": "e) Marcadores de tiempo y lugar", "body": "<p><em>hoy → ese día/aquel día, ayer → el día anterior, mañana → al día siguiente, aquí → allí, este → aquel.</em></p>"},
            ],
            "examples": [
                "Me dijo que estaba muy ocupada esa semana.",
                "Contó que había viajado a Chile el año anterior.",
                "Prometió que me llamaría al día siguiente.",
                "El profesor nos pidió que entregáramos la tarea a tiempo.",
                "Explicó que no podía venir ese día por trabajo.",
                "Nos avisó que llegaría un poco más tarde de lo normal.",
                "Dijo que había estado allí varias veces antes.",
                "Me pidió que la esperara un momento en la entrada.",
            ],
            "commonMistakes": [
                {"wrong": "Me dijo que está cansada.", "right": "Me dijo que estaba cansada.", "why": "Con el verbo introductor en pasado (dijo), el presente de la cita original retrocede a imperfecto."},
                {"wrong": "Prometió que vendrá mañana.", "right": "Prometió que vendría al día siguiente.", "why": "El futuro retrocede a condicional, y mañana cambia a al día siguiente para reflejar el nuevo punto de vista temporal."},
                {"wrong": "Me pidió que cierre la puerta.", "right": "Me pidió que cerrara la puerta.", "why": "Un imperativo en estilo indirecto con verbo introductor en pasado se convierte en imperfecto de subjuntivo, no en presente de subjuntivo."},
            ],
        },
        "exercises": [
            {"id": "b2ei2-fill", "type": "fill-blank", "title": "Transforma a Estilo Indirecto (Pasado)",
             "items": [
                {"id": "b2ei2a", "prompt": "Ana dijo: \"Vivo en Sevilla.\" → Ana dijo que ___ en Sevilla.", "answers": [["vivía"]], "options": ["vivía", "vive", "viviría"], "explanation": "Presente en la cita original retrocede a imperfecto con el verbo introductor en pasado."},
                {"id": "b2ei2b", "prompt": "Juan prometió: \"Llamaré mañana.\" → Juan prometió que ___ al día siguiente.", "answers": [["llamaría"]], "options": ["llamaría", "llama", "llamará"], "explanation": "Futuro en la cita original retrocede a condicional."},
             ]},
            {"id": "b2ei2-mc", "type": "multiple-choice", "title": "Elige la Transformación Correcta",
             "items": [
                {"id": "b2ei2c", "prompt": "\"Cierra la puerta\", dijo el profesor. → en estilo indirecto...", "options": ["Dijo que cerrara la puerta.", "Dijo que cierre la puerta.", "Dijo que cierra la puerta."], "answerIndex": 0, "explanation": "El imperativo se transforma en imperfecto de subjuntivo con el verbo introductor en pasado."},
             ]},
            {"id": "b2ei2-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2ei2d", "incorrect": "Me contó que ha viajado mucho de joven.", "answer": ["Me contó que había viajado mucho de joven."], "explanation": "El pretérito perfecto de la cita original retrocede a pluscuamperfecto con el verbo introductor en pasado."},
            ]},
        ],
        "summary": [
            "Con el verbo introductor en pasado, el presente retrocede a imperfecto, el pretérito a pluscuamperfecto, el futuro a condicional y el imperativo a imperfecto de subjuntivo.",
            "Los marcadores de tiempo y lugar también cambian: hoy/ayer/mañana pasan a ese día/el día anterior/al día siguiente, aquí a allí.",
            "Esta concordancia de tiempos completa es clave para narrar conversaciones pasadas con precisión.",
        ],
    },
    {
        "id": "b2-conectores-argumentativos-avanzados",
        "level": "B2", "unit": "1", "order": 9, "skill": "functional", "strand": "conectores",
        "title": "Conectores Argumentativos Avanzados",
        "subtitle": "Ahora bien, de hecho, en cambio, dicho de otro modo: para argumentar con precisión y matiz.",
        "objectives": [
            "Usar conectores de matización y reformulación en un argumento",
            "Distinguir en cambio (contraste) de por el contrario (contraste más fuerte)",
            "Construir un párrafo argumentativo breve con varios conectores encadenados",
        ],
        "content": {
            "intro": "Argumentar con matices — reconocer una objeción, reformular una idea, precisar un punto — requiere un repertorio de conectores más amplio del que usabas en B1, propio de un discurso más elaborado.",
            "explanation": "<p><strong>Ahora bien</strong> introduce una matización o una objeción parcial a lo dicho antes, sin negarlo del todo: <em>El plan es bueno; ahora bien, necesita más presupuesto.</em> <strong>De hecho</strong> refuerza una idea con un dato o ejemplo concreto. <strong>En cambio</strong> contrasta dos elementos de forma neutra, mientras que <strong>por el contrario</strong> marca una oposición mucho más fuerte y directa.</p><p>Los conectores de reformulación (<strong>es decir, dicho de otro modo, en otras palabras</strong>) permiten explicar la misma idea con palabras distintas, muy útiles para aclarar un punto complejo sin repetir literalmente lo ya dicho.</p>",
            "rules": [
                {"heading": "a) Matización/objeción parcial", "body": "<p><em>ahora bien, si bien es cierto que...</em>: <em>El proyecto avanza bien; ahora bien, todavía faltan varios detalles por resolver.</em></p>"},
                {"heading": "b) Refuerzo con un dato", "body": "<p><em>de hecho, en efecto</em>: <em>El curso es exigente; de hecho, muchos estudiantes lo abandonan a mitad de camino.</em></p>"},
                {"heading": "c) Contraste neutro vs. contraste fuerte", "body": "<p><em>en cambio</em> (neutro): <em>A mí me gusta el café; a ella, en cambio, le gusta más el té.</em> <em>por el contrario</em> (fuerte): <em>No solo no mejoró la situación; por el contrario, empeoró notablemente.</em></p>"},
                {"heading": "d) Reformulación", "body": "<p><em>es decir, dicho de otro modo, en otras palabras</em>: <em>El proyecto se pospone; es decir, no se cancela, solo se retrasa.</em></p>"},
            ],
            "examples": [
                "La propuesta tiene mucho potencial; ahora bien, requiere más tiempo de análisis.",
                "El curso es intensivo; de hecho, cubre en tres meses lo de un año normal.",
                "A mí me encanta viajar solo; a mi hermano, en cambio, le gusta viajar en grupo.",
                "No mejoró con el nuevo horario; por el contrario, empeoró bastante.",
                "El proyecto se aplaza; es decir, seguirá adelante, pero más tarde de lo previsto.",
                "Dicho de otro modo, no se trata de un problema técnico, sino de organización.",
                "Si bien es cierto que el precio es alto, la calidad también lo justifica.",
                "En efecto, los datos confirman exactamente lo que habíamos anticipado.",
            ],
            "commonMistakes": [
                {"wrong": "El plan es bueno; por el contrario, necesita ajustes menores.", "right": "El plan es bueno; ahora bien, necesita ajustes menores.", "why": "Por el contrario marca una oposición fuerte; aquí solo hay una matización parcial, que corresponde a ahora bien."},
                {"wrong": "A ella le gusta el té; por el contrario, a mí también me gusta el té.", "right": "A ella le gusta el té; a mí, en cambio, me gusta más el café.", "why": "Por el contrario y en cambio requieren una verdadera oposición entre las dos ideas, no una coincidencia."},
                {"wrong": "El proyecto se retrasa, de hecho se cancela.", "right": "El proyecto se retrasa; es decir, no se cancela, solo se pospone.", "why": "De hecho refuerza con un dato en la misma dirección; para reformular o precisar el sentido, corresponde es decir."},
            ],
        },
        "exercises": [
            {"id": "b2ca-mc", "type": "multiple-choice", "title": "Elige el Conector Correcto",
             "items": [
                {"id": "b2ca1", "prompt": "\"El equipo trabajó muy bien; ___, terminaron el proyecto antes de lo previsto.\" (refuerzo con dato)", "options": ["de hecho", "en cambio", "ahora bien"], "answerIndex": 0, "explanation": "De hecho refuerza la idea anterior con un dato concreto."},
                {"id": "b2ca2", "prompt": "\"No solo no ayudó; ___, complicó todavía más la situación.\" (oposición fuerte)", "options": ["en cambio", "por el contrario", "es decir"], "answerIndex": 1, "explanation": "Por el contrario marca una oposición fuerte y directa."},
             ]},
            {"id": "b2ca-fill", "type": "fill-blank", "title": "Completa con el Conector de Reformulación",
             "items": [
                {"id": "b2ca3", "prompt": "El curso no se cancela; ___, se traslada a otra fecha.", "answers": [["es decir"], ["dicho de otro modo"], ["en otras palabras"]], "options": ["es decir", "por el contrario"], "explanation": "Es decir reformula o precisa una idea ya expresada."},
             ]},
            {"id": "b2ca-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2ca4", "incorrect": "El plan es sólido; sin embargo, es exactamente lo que necesitábamos.", "answer": ["El plan es sólido; de hecho, es exactamente lo que necesitábamos."], "explanation": "Sin embargo introduce un contraste; aquí la segunda idea refuerza la primera, así que corresponde de hecho."},
            ]},
        ],
        "summary": [
            "Ahora bien introduce una matización u objeción parcial; de hecho refuerza una idea con un dato concreto.",
            "En cambio marca un contraste neutro; por el contrario marca una oposición mucho más fuerte y directa.",
            "Es decir, dicho de otro modo y en otras palabras reformulan una idea ya expresada para aclararla, sin negarla.",
        ],
    },
    {
        "id": "b2-colocaciones-y-expresiones-idiomaticas",
        "level": "B2", "unit": "1", "order": 10, "skill": "vocabulary", "strand": "colocaciones",
        "title": "Colocaciones y Expresiones Idiomáticas",
        "subtitle": "Combinaciones fijas de palabras que un hablante nativo usa sin pensar, y que hay que aprender como bloques enteros.",
        "objectives": [
            "Reconocer colocaciones frecuentes (verbo + sustantivo) que no se forman libremente",
            "Usar expresiones idiomáticas comunes en su contexto adecuado",
            "Evitar traducir palabra por palabra combinaciones que en español funcionan de otra manera",
        ],
        "content": {
            "intro": "Una colocación es una combinación de palabras que los hablantes nativos usan casi siempre juntas, aunque otras combinaciones lógicamente parecidas suenen raras o incorrectas — dominarlas es lo que hace que un español suene natural en vez de \"traducido\".",
            "explanation": "<p>Muchos verbos se combinan de forma fija con ciertos sustantivos: se dice <strong>tomar una decisión</strong>, no \"hacer una decisión\"; se dice <strong>prestar atención</strong>, no \"pagar atención\"; se dice <strong>dar un paseo</strong>, no \"hacer un paseo\". Estas combinaciones no siguen una lógica que se pueda deducir, así que se memorizan como bloques completos, igual que el vocabulario mismo.</p><p>Las expresiones idiomáticas van un paso más allá: su significado no se puede deducir de las palabras por separado. <em>Costar un ojo de la cara</em> significa ser muy caro; <em>meter la pata</em> significa cometer un error o decir algo inoportuno; <em>estar en las nubes</em> significa estar distraído.</p>",
            "rules": [
                {"heading": "a) Colocaciones verbo + sustantivo frecuentes", "body": "<ul><li><em>tomar una decisión, tomar en cuenta, tomar el pelo (engañar/burlarse)</em></li><li><em>prestar atención, dar las gracias, dar un paseo, dar la razón</em></li><li><em>hacer caso, hacer falta, hacer la compra</em></li><li><em>tener en cuenta, tener lugar, tener ganas de</em></li></ul>"},
                {"heading": "b) Expresiones idiomáticas frecuentes", "body": "<ul><li><em>costar un ojo de la cara</em> — ser muy caro</li><li><em>meter la pata</em> — cometer un error, decir algo inoportuno</li><li><em>estar en las nubes</em> — estar distraído</li><li><em>no tener pelos en la lengua</em> — hablar con total franqueza</li><li><em>tirar la toalla</em> — rendirse, abandonar algo</li></ul>"},
                {"heading": "c) Colocaciones adjetivo + sustantivo", "body": "<p><em>error garrafal</em> (error muy grave), <em>lluvia torrencial</em>, <em>éxito rotundo</em> — el adjetivo intensificador cambia según el sustantivo, y no todas las combinaciones suenan naturales aunque el significado parezca el mismo.</p>"},
            ],
            "examples": [
                "Tuvimos que tomar una decisión difícil sobre el proyecto.",
                "Ese abrigo de diseñador debió de costarle un ojo de la cara.",
                "Metí la pata al mencionar su exnovio delante de todos.",
                "Últimamente estás en las nubes, ¿en qué piensas tanto?",
                "Ella nunca tiene pelos en la lengua para decir lo que piensa.",
                "Después de tantos intentos fallidos, decidió tirar la toalla.",
                "Es importante tener en cuenta la opinión de todo el equipo.",
                "El evento tendrá lugar en el salón principal del hotel.",
            ],
            "commonMistakes": [
                {"wrong": "Hicimos una decisión importante ayer.", "right": "Tomamos una decisión importante ayer.", "why": "En español, decisión se combina con tomar, no con hacer, aunque en otros idiomas se use un verbo equivalente a hacer."},
                {"wrong": "Necesitas pagar más atención en clase.", "right": "Necesitas prestar más atención en clase.", "why": "Atención se combina con prestar, no con pagar, aunque en otros idiomas se use un verbo equivalente a pagar."},
                {"wrong": "El nuevo restaurante cuesta un brazo de la cara.", "right": "El nuevo restaurante cuesta un ojo de la cara.", "why": "La expresión fija es costar un ojo de la cara; cambiar la palabra ojo rompe la expresión y suena extraño para un hablante nativo."},
            ],
        },
        "exercises": [
            {"id": "b2co-fill", "type": "fill-blank", "title": "Completa la Colocación",
             "items": [
                {"id": "b2co1", "prompt": "Necesitamos ___ una decisión antes del viernes.", "answers": [["tomar"]], "options": ["tomar", "hacer", "dar"], "explanation": "La colocación fija es tomar una decisión."},
                {"id": "b2co2", "prompt": "Por favor, ___ atención a las instrucciones.", "answers": [["presta"]], "options": ["presta", "paga", "toma"], "explanation": "La colocación fija es prestar atención."},
             ]},
            {"id": "b2co-mc", "type": "multiple-choice", "title": "¿Qué Significa la Expresión?",
             "items": [
                {"id": "b2co3", "prompt": "\"Meter la pata\" significa...", "options": ["tener mucho éxito", "cometer un error o decir algo inoportuno", "trabajar muy rápido"], "answerIndex": 1, "explanation": "Meter la pata significa cometer un error, especialmente al hablar en un momento inoportuno."},
                {"id": "b2co4", "prompt": "\"Estar en las nubes\" significa...", "options": ["estar muy feliz", "estar distraído", "estar muy ocupado"], "answerIndex": 1, "explanation": "Estar en las nubes significa estar distraído, sin prestar atención a lo que ocurre alrededor."},
             ]},
            {"id": "b2co-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2co5", "incorrect": "Ese coche debe de costar un brazo entero.", "answer": ["Ese coche debe de costar un ojo de la cara."], "explanation": "La expresión fija en español es costar un ojo de la cara, no un brazo."},
            ]},
        ],
        "summary": [
            "Las colocaciones son combinaciones fijas (tomar una decisión, prestar atención, dar un paseo) que se memorizan como bloques, no se deducen lógicamente.",
            "Las expresiones idiomáticas (costar un ojo de la cara, meter la pata, estar en las nubes) tienen un significado que no se deduce de las palabras por separado.",
            "Traducir estas combinaciones palabra por palabra desde otro idioma casi nunca funciona en español.",
        ],
    },
    {
        "id": "b2-registro-formal-e-informal",
        "level": "B2", "unit": "1", "order": 11, "skill": "functional", "strand": "registro",
        "title": "Registro Formal e Informal",
        "subtitle": "Cómo adaptar tu español según la situación: un correo de trabajo no suena igual que un mensaje a un amigo.",
        "objectives": [
            "Reconocer marcas léxicas y gramaticales del registro formal frente al informal",
            "Escribir un correo formal con las fórmulas de apertura y cierre adecuadas",
            "Adaptar el vocabulario y las estructuras según el contexto y el interlocutor",
        ],
        "content": {
            "intro": "El mismo mensaje puede expresarse de maneras muy distintas según a quién te dirijas — un hablante avanzado no solo domina la gramática, sino que sabe elegir el registro adecuado para cada situación.",
            "explanation": "<p>El registro <strong>formal</strong> usa <strong>usted/ustedes</strong>, evita contracciones informales y muletillas, prefiere un vocabulario más preciso y estructuras más completas, y sigue fórmulas fijas de cortesía en cartas y correos. El registro <strong>informal</strong> usa <strong>tú/vos</strong>, permite frases más cortas, muletillas (<em>pues, o sea, bueno</em>), y un vocabulario más coloquial, incluso con jerga regional.</p><p>En un correo formal, las fórmulas de apertura (<em>Estimado/a señor/a..., Le escribo para...</em>) y cierre (<em>Quedo a la espera de su respuesta. Atentamente,</em>) tienen un peso importante; en un mensaje informal a un amigo, esas mismas fórmulas sonarían distantes y hasta extrañas.</p>",
            "rules": [
                {"heading": "a) Marcas del registro formal", "body": "<ul><li>Usted/ustedes en vez de tú/vos</li><li>Vocabulario preciso: <em>solicitar</em> en vez de <em>pedir</em>, <em>informar</em> en vez de <em>contar</em></li><li>Estructuras completas, sin abreviar: <em>no obstante</em> en vez de <em>pero bueno</em></li></ul>"},
                {"heading": "b) Marcas del registro informal", "body": "<ul><li>Tú/vos, diminutivos afectivos (<em>un ratito, ahorita</em>)</li><li>Muletillas: <em>pues, o sea, bueno, la verdad es que</em></li><li>Vocabulario coloquial y expresiones regionales</li></ul>"},
                {"heading": "c) Fórmulas fijas de un correo formal", "body": "<p>Apertura: <em>Estimado/a Sr./Sra. [apellido]: / A quien corresponda:</em> Cierre: <em>Quedo a la espera de su respuesta. Atentamente, / Un cordial saludo,</em></p>"},
                {"heading": "d) Fórmulas de un mensaje informal", "body": "<p>Apertura: <em>¡Hola! / ¿Qué tal?</em> Cierre: <em>Un abrazo. / Nos vemos pronto. / ¡Cuídate!</em></p>"},
            ],
            "examples": [
                "Estimada señora Fernández: Le escribo para solicitar información sobre el curso.",
                "¡Hola, Marcos! ¿Qué tal todo por allá? Cuéntame cómo te va con el nuevo trabajo.",
                "Quedo a la espera de su respuesta. Atentamente, Laura Gómez.",
                "Oye, ¿nos vemos mañana para tomar un café o qué?",
                "Le agradecería que me confirmara la fecha de la reunión.",
                "Bueno, la verdad es que no tengo ni idea de qué hacer todavía.",
                "Por la presente, deseo comunicarle mi decisión de renunciar al puesto.",
                "Nos vemos el sábado, ¡un abrazo enorme!",
            ],
            "commonMistakes": [
                {"wrong": "Hola, quería pedirte información sobre el puesto de trabajo. (en un correo dirigido a un director de recursos humanos desconocido)", "right": "Estimado/a señor/a: Le escribo para solicitar información sobre el puesto de trabajo.", "why": "Un correo formal a un desconocido en un contexto profesional necesita una fórmula de apertura formal y el verbo solicitar en vez del más coloquial pedir."},
                {"wrong": "Le escribo para contarle que necesito el informe antes del jueves.", "right": "Le escribo para informarle de que necesito el informe antes del jueves.", "why": "En un registro formal, informar de es más preciso que el más coloquial contar."},
                {"wrong": "Un abrazo, Sr. Gómez. (cierre informal en un correo muy formal)", "right": "Atentamente, [nombre]. / Un cordial saludo, [nombre].", "why": "Un abrazo es un cierre informal; en un correo formal corresponde una fórmula como atentamente o un cordial saludo."},
            ],
        },
        "exercises": [
            {"id": "b2rf-mc", "type": "multiple-choice", "title": "Elige el Registro Adecuado",
             "items": [
                {"id": "b2rf1", "prompt": "¿Cuál es la fórmula de apertura adecuada para un correo formal a un desconocido?", "options": ["¡Hola! ¿Qué tal?", "Estimado/a señor/a:", "Oye, ¿cómo estás?"], "answerIndex": 1, "explanation": "Estimado/a señor/a: es la fórmula estándar para abrir un correo formal a alguien que no conoces."},
                {"id": "b2rf2", "prompt": "¿Cuál de estas frases pertenece a un registro informal?", "options": ["Le agradecería su pronta respuesta.", "Bueno, la verdad es que no sé qué decirte.", "Quedo a la espera de su confirmación."], "answerIndex": 1, "explanation": "Las muletillas como bueno y la verdad es que son típicas del registro informal."},
             ]},
            {"id": "b2rf-fill", "type": "fill-blank", "title": "Transforma al Registro Formal",
             "items": [
                {"id": "b2rf3", "prompt": "\"Te cuento que llego un poco tarde.\" en registro formal: \"Le ___ que llegaré un poco tarde.\"", "answers": [["informo"], ["comunico"]], "options": ["informo", "cuento"], "explanation": "Informar/comunicar son más precisos y formales que el coloquial contar."},
             ]},
            {"id": "b2rf-correction", "type": "correction", "title": "Corrige los Errores",
             "items": [
                {"id": "b2rf4", "incorrect": "Estimado señor López: Oye, necesito el documento urgente.", "answer": ["Estimado señor López: Le escribo para solicitar el documento con urgencia."], "explanation": "Oye es una muletilla informal que no combina con la fórmula de apertura formal; en un correo formal se mantiene el registro coherente en todo el texto."},
            ]},
        ],
        "summary": [
            "El registro formal usa usted, vocabulario preciso y estructuras completas; el informal usa tú/vos, muletillas y vocabulario coloquial.",
            "Un correo formal sigue fórmulas fijas de apertura (estimado/a) y cierre (atentamente); un mensaje informal usa fórmulas mucho más libres.",
            "Es importante mantener el mismo registro de forma coherente en todo un texto, sin mezclar fórmulas formales e informales.",
        ],
    },
    {
        "id": "b2-futuro-de-subjuntivo",
        "level": "B2", "unit": "1", "order": 12, "skill": "grammar", "strand": "subjuntivo",
        "title": "El Futuro de Subjuntivo (Introducción)",
        "subtitle": "Hablare, hablares, hablare...: un tiempo casi extinto, pero vivo en el lenguaje jurídico y en refranes.",
        "objectives": [
            "Reconocer la forma del futuro de subjuntivo y su relación con el imperfecto de subjuntivo",
            "Explicar en qué contextos sobrevive este tiempo hoy en día",
            "Identificar el futuro de subjuntivo en refranes, textos legales y el registro arcaizante",
        ],
        "content": {
            "intro": "El futuro de subjuntivo es una curiosidad histórica del español: prácticamente desapareció del habla y la escritura cotidiana, pero sigue vivo en el lenguaje jurídico, en refranes y en textos con un tono deliberadamente arcaico o solemne.",
            "explanation": "<p>Se forma igual que el imperfecto de subjuntivo, pero sustituyendo las terminaciones <strong>-ra</strong> por <strong>-re</strong>: <em>hablare, hablares, hablare, habláremos, hablareis, hablaren</em>. En el español medieval y clásico se usaba para expresar una condición futura hipotética, con un matiz parecido al presente de subjuntivo pero proyectado hacia el futuro.</p><p>Hoy en día, su uso está prácticamente restringido a textos legales y constitucionales (<em>Quien incumpliere esta norma será sancionado</em>), a algunos refranes fosilizados (<em>Adonde fueres, haz lo que vieres</em>), y a un registro deliberadamente arcaizante o literario. No es necesario aprender a producirlo activamente, pero conviene reconocerlo si aparece en un texto legal, un refrán o una novela histórica.</p>",
            "rules": [
                {"heading": "a) Formación (a partir del imperfecto de subjuntivo)", "body": "<p>Se sustituye -ra por -re: hablara → hablare; tuviera → tuviere; fuera → fuere.</p>"},
                {"heading": "b) Uso casi exclusivo en textos jurídicos", "body": "<p><em>El que faltare a esta obligación incurrirá en responsabilidad. Quien resultare elegido asumirá el cargo de inmediato.</em></p>"},
                {"heading": "c) Refranes que lo conservan", "body": "<p><em>Adonde fueres, haz lo que vieres.</em> (adáptate a las costumbres del lugar donde estés)</p>"},
                {"heading": "d) No es necesario usarlo activamente", "body": "<p>En el español de hoy, tanto en el habla como en la escritura general, el presente de subjuntivo o el presente de indicativo sustituyen naturalmente al futuro de subjuntivo en cualquier contexto cotidiano.</p>"},
            ],
            "examples": [
                "El que incumpliere el contrato deberá pagar una indemnización.",
                "Adonde fueres, haz lo que vieres.",
                "Quien resultare ganador del concurso recibirá el premio.",
                "Si alguien objetare esta decisión, deberá presentarlo por escrito.",
                "El funcionario que faltare sin justificación será sancionado.",
                "Cualquiera que necesitare más información puede consultar el reglamento.",
                "Si no hubiere objeciones, se dará por aprobada la propuesta.",
                "El que quisiere participar deberá inscribirse antes del plazo.",
            ],
            "commonMistakes": [
                {"wrong": "usar el futuro de subjuntivo en una conversación cotidiana o un correo informal", "right": "usar el presente de subjuntivo o de indicativo en su lugar", "why": "El futuro de subjuntivo desapareció del habla cotidiana; usarlo fuera de un contexto legal o deliberadamente arcaico suena forzado o extraño."},
                {"wrong": "confundir el futuro de subjuntivo (hablare) con el futuro simple de indicativo (hablaré)", "right": "distinguir ambas formas por su terminación y su uso", "why": "Se diferencian solo por una letra (hablare/hablaré) pero son tiempos completamente distintos, con usos y frecuencia muy diferentes."},
                {"wrong": "pensar que el futuro de subjuntivo ya no existe en absoluto en español moderno", "right": "reconocer que sobrevive en textos legales, refranes y registro arcaizante", "why": "Aunque prácticamente desapareció del habla cotidiana, sigue siendo productivo en el lenguaje jurídico actual."},
            ],
        },
        "exercises": [
            {"id": "b2fs2-mc", "type": "multiple-choice", "title": "¿Dónde Aparece el Futuro de Subjuntivo?",
             "items": [
                {"id": "b2fs2a", "prompt": "¿En qué tipo de texto es más probable encontrar el futuro de subjuntivo hoy en día?", "options": ["Un mensaje de texto entre amigos", "Un documento legal o constitucional", "Una receta de cocina"], "answerIndex": 1, "explanation": "El futuro de subjuntivo sobrevive casi exclusivamente en el lenguaje jurídico y en registros arcaizantes."},
                {"id": "b2fs2b", "prompt": "¿Cuál es la terminación característica del futuro de subjuntivo?", "options": ["-ra", "-re", "-se"], "answerIndex": 1, "explanation": "El futuro de subjuntivo sustituye la -ra del imperfecto de subjuntivo por -re."},
             ]},
            {"id": "b2fs2-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "b2fs2c", "statement": "Es necesario dominar el futuro de subjuntivo para hablar español con fluidez hoy en día.", "answer": False, "explanation": "Basta con reconocerlo pasivamente; en el habla cotidiana, el presente de subjuntivo o de indicativo lo sustituyen por completo."},
                {"id": "b2fs2d", "statement": "El refrán \"Adonde fueres, haz lo que vieres\" contiene ejemplos de futuro de subjuntivo.", "answer": True, "explanation": "Fueres y vieres son formas de futuro de subjuntivo, conservadas en este refrán tradicional."},
             ]},
        ],
        "summary": [
            "El futuro de subjuntivo se forma como el imperfecto de subjuntivo, sustituyendo -ra por -re.",
            "Hoy sobrevive casi exclusivamente en textos legales y constitucionales, en algunos refranes fosilizados y en registro arcaizante.",
            "No es necesario producirlo activamente: el presente de subjuntivo o de indicativo lo sustituyen con normalidad en el español actual.",
        ],
    },
]

# =======================================================================
# EXTRA_EXERCISES — bloques adicionales de práctica (lectura y ordenar
# frases) fusionados en cada lección por id.
# =======================================================================
EXTRA_EXERCISES = {
    "b2-imperfecto-de-subjuntivo": [
        {"id": "b2x1-reading", "type": "reading-comprehension", "title": "Lectura: Si Yo Fuera Tú",
         "passage": "<p>Mi madre siempre quería que estudiara medicina, pero yo prefería el arte. Ella dudaba que pudiera vivir de la pintura. Con el tiempo, esperaba que encontrara mi propio camino, aunque al principio le costara aceptarlo. Ahora está orgullosa de que haya seguido mi pasión.</p>",
         "items": [
            {"id": "b2x1r1", "prompt": "¿Qué quería la madre que estudiara la persona?", "options": ["Arte", "Medicina", "Derecho"], "answerIndex": 1, "explanation": "El texto dice: «Mi madre siempre quería que estudiara medicina»."},
            {"id": "b2x1r2", "prompt": "¿Qué dudaba la madre?", "options": ["Que fuera feliz", "Que pudiera vivir de la pintura", "Que terminara los estudios"], "answerIndex": 1, "explanation": "El texto dice: «Ella dudaba que pudiera vivir de la pintura»."},
            {"id": "b2x1r3", "prompt": "¿Qué esperaba la madre con el tiempo?", "options": ["Que cambiara de opinión", "Que encontrara su propio camino", "Que se hiciera médica"], "answerIndex": 1, "explanation": "El texto dice: «esperaba que encontrara mi propio camino»."},
            {"id": "b2x1r4", "prompt": "¿Cómo se siente la madre ahora?", "options": ["Decepcionada", "Orgullosa", "Indiferente"], "answerIndex": 1, "explanation": "El texto termina: «Ahora está orgullosa de que haya seguido mi pasión»."},
         ]},
        {"id": "b2x1-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x1o1", "prompt": "Ordena las palabras.", "words": ["Quería", "que", "vinieras", "conmigo", "al", "cine"], "explanation": "Verbo principal en pasado + que + imperfecto de subjuntivo (vinieras)."},
            {"id": "b2x1o2", "prompt": "Ordena las palabras.", "words": ["Dudaba", "que", "ellos", "supieran", "la", "verdad"], "explanation": "Dudar en pasado + que + imperfecto de subjuntivo (supieran)."},
         ]},
    ],
    "b2-condicionales-con-si-subjuntivo": [
        {"id": "b2x2-reading", "type": "reading-comprehension", "title": "Lectura: Decisiones y Consecuencias",
         "passage": "<p>Si tuviera más tiempo libre, aprendería a tocar el piano. Si hubiera aceptado ese trabajo en su momento, ahora viviría en otra ciudad. Pero si sigo estudiando cada día, en un año hablaré español con fluidez. Si hubiera empezado antes, ya estaría más avanzado.</p>",
         "items": [
            {"id": "b2x2r1", "prompt": "¿Qué haría la persona si tuviera más tiempo libre?", "options": ["Viajaría más", "Aprendería a tocar el piano", "Trabajaría menos"], "answerIndex": 1, "explanation": "El texto dice: «Si tuviera más tiempo libre, aprendería a tocar el piano»."},
            {"id": "b2x2r2", "prompt": "¿Dónde viviría si hubiera aceptado ese trabajo?", "options": ["En el extranjero", "En otra ciudad", "En el mismo lugar"], "answerIndex": 1, "explanation": "El texto dice: «ahora viviría en otra ciudad»."},
            {"id": "b2x2r3", "prompt": "¿Qué condición real menciona sobre el español?", "options": ["Si deja de estudiar", "Si sigue estudiando cada día", "Si viaja a España"], "answerIndex": 1, "explanation": "El texto dice: «si sigo estudiando cada día, en un año hablaré español con fluidez»."},
            {"id": "b2x2r4", "prompt": "¿Qué tipo de condicional es \"Si hubiera empezado antes, ya estaría más avanzado\"?", "options": ["Real", "Potencial", "Irreal de pasado con consecuencia en presente"], "answerIndex": 2, "explanation": "Prótasis con pluscuamperfecto de subjuntivo y consecuencia en condicional simple: condicional mixta."},
         ]},
        {"id": "b2x2-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x2o1", "prompt": "Ordena las palabras.", "words": ["Si", "fuera", "rico", "viajaría", "por", "el", "mundo"], "explanation": "Si + imperfecto de subjuntivo + condicional simple (condicional potencial)."},
            {"id": "b2x2o2", "prompt": "Ordena las palabras.", "words": ["Si", "hubieras", "llamado", "habría", "contestado"], "explanation": "Si + pluscuamperfecto de subjuntivo + condicional compuesto (irreal de pasado)."},
         ]},
    ],
    "b2-subjuntivo-vs-indicativo-sustantivas": [
        {"id": "b2x3-reading", "type": "reading-comprehension", "title": "Lectura: Certezas y Dudas",
         "passage": "<p>Es evidente que este proyecto tiene mucho potencial. Es importante que todos participemos activamente. No es cierto que el presupuesto se haya reducido, como algunos dicen. Está claro que necesitamos más tiempo para terminarlo bien.</p>",
         "items": [
            {"id": "b2x3r1", "prompt": "¿Qué es evidente sobre el proyecto?", "options": ["Que es muy caro", "Que tiene mucho potencial", "Que va a fracasar"], "answerIndex": 1, "explanation": "El texto dice: «Es evidente que este proyecto tiene mucho potencial»."},
            {"id": "b2x3r2", "prompt": "¿Qué es importante que hagan todos?", "options": ["Que descansen", "Que participen activamente", "Que se vayan"], "answerIndex": 1, "explanation": "El texto dice: «Es importante que todos participemos activamente»."},
            {"id": "b2x3r3", "prompt": "¿Es cierto que el presupuesto se haya reducido?", "options": ["Sí", "No, según el texto"], "answerIndex": 1, "explanation": "El texto dice: «No es cierto que el presupuesto se haya reducido»."},
            {"id": "b2x3r4", "prompt": "¿Qué necesitan, según el texto?", "options": ["Más dinero", "Más tiempo", "Más personal"], "answerIndex": 1, "explanation": "El texto termina: «necesitamos más tiempo para terminarlo bien»."},
         ]},
        {"id": "b2x3-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x3o1", "prompt": "Ordena las palabras.", "words": ["Es", "evidente", "que", "ella", "tiene", "razón"], "explanation": "Expresión de certeza + que + indicativo (tiene)."},
            {"id": "b2x3o2", "prompt": "Ordena las palabras.", "words": ["Es", "una", "lástima", "que", "no", "vengas"], "explanation": "Expresión de valoración + que + subjuntivo (vengas)."},
         ]},
    ],
    "b2-subjuntivo-relativas-y-adverbiales": [
        {"id": "b2x4-reading", "type": "reading-comprehension", "title": "Lectura: En Busca de un Trabajo Ideal",
         "passage": "<p>Busco un trabajo que me permita viajar con frecuencia. No conozco a nadie que tenga la experiencia que necesito para este proyecto. Te lo explico para que entiendas bien la situación. Aunque llueva mañana, saldremos igual a hacer las entrevistas.</p>",
         "items": [
            {"id": "b2x4r1", "prompt": "¿Qué tipo de trabajo busca la persona?", "options": ["Uno bien pagado", "Uno que permita viajar", "Uno cerca de casa"], "answerIndex": 1, "explanation": "El texto dice: «Busco un trabajo que me permita viajar con frecuencia»."},
            {"id": "b2x4r2", "prompt": "¿Conoce a alguien con la experiencia necesaria?", "options": ["Sí", "No"], "answerIndex": 1, "explanation": "El texto dice: «No conozco a nadie que tenga la experiencia que necesito»."},
            {"id": "b2x4r3", "prompt": "¿Para qué le explica la situación?", "options": ["Para que se preocupe", "Para que entienda bien", "Para que se vaya"], "answerIndex": 1, "explanation": "El texto dice: «Te lo explico para que entiendas bien la situación»."},
            {"id": "b2x4r4", "prompt": "¿Qué pasará aunque llueva mañana?", "options": ["Cancelarán las entrevistas", "Saldrán igual a hacerlas", "Las pospondrán"], "answerIndex": 1, "explanation": "El texto termina: «Aunque llueva mañana, saldremos igual a hacer las entrevistas»."},
         ]},
        {"id": "b2x4-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x4o1", "prompt": "Ordena las palabras.", "words": ["Necesito", "un", "amigo", "que", "hable", "francés"], "explanation": "Antecedente indefinido (un amigo) + relativa en subjuntivo (hable)."},
            {"id": "b2x4o2", "prompt": "Ordena las palabras.", "words": ["Te", "ayudo", "con", "tal", "de", "que", "estudies"], "explanation": "Con tal de que + subjuntivo, siempre exige subjuntivo."},
         ]},
    ],
    "b2-perifrasis-verbales": [
        {"id": "b2x5-reading", "type": "reading-comprehension", "title": "Lectura: Cambios en la Rutina",
         "passage": "<p>Llevo tres años estudiando español y sigo aprendiendo cosas nuevas cada día. Acabo de terminar un curso avanzado, así que voy a empezar otro más especializado pronto. Dejé de estudiar francés porque no tenía tiempo para los dos idiomas a la vez.</p>",
         "items": [
            {"id": "b2x5r1", "prompt": "¿Cuánto tiempo lleva estudiando español la persona?", "options": ["Un año", "Tres años", "Cinco años"], "answerIndex": 1, "explanation": "El texto dice: «Llevo tres años estudiando español»."},
            {"id": "b2x5r2", "prompt": "¿Qué acaba de terminar?", "options": ["Un examen", "Un curso avanzado", "Una carrera"], "answerIndex": 1, "explanation": "El texto dice: «Acabo de terminar un curso avanzado»."},
            {"id": "b2x5r3", "prompt": "¿Por qué dejó de estudiar francés?", "options": ["Porque no le gustaba", "Porque no tenía tiempo para los dos idiomas", "Porque era muy difícil"], "answerIndex": 1, "explanation": "El texto dice: «no tenía tiempo para los dos idiomas a la vez»."},
            {"id": "b2x5r4", "prompt": "¿Qué va a hacer pronto?", "options": ["Dejar de estudiar", "Empezar otro curso más especializado", "Viajar a España"], "answerIndex": 1, "explanation": "El texto dice: «voy a empezar otro más especializado pronto»."},
         ]},
        {"id": "b2x5-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x5o1", "prompt": "Ordena las palabras.", "words": ["Llevo", "dos", "horas", "esperando", "el", "autobús"], "explanation": "Llevar + tiempo + gerundio, expresa duración hasta ahora."},
            {"id": "b2x5o2", "prompt": "Ordena las palabras.", "words": ["Volvió", "a", "llamar", "por", "tercera", "vez"], "explanation": "Volver a + infinitivo, expresa repetición de una acción."},
         ]},
    ],
    "b2-ser-y-estar-avanzado": [
        {"id": "b2x6-reading", "type": "reading-comprehension", "title": "Lectura: Impresiones del Momento",
         "passage": "<p>¡Qué elegante estás hoy! ¿Es una ocasión especial? La reunión es en la sala principal a las cuatro. Este postre está buenísimo, ¿lo hiciste tú misma? Mi tío es muy vivo para su edad; siempre encuentra una solución rápida a cualquier problema.</p>",
         "items": [
            {"id": "b2x6r1", "prompt": "¿Qué comentario hace sobre la ropa de la otra persona?", "options": ["Que es fea", "Que está muy elegante hoy", "Que es incómoda"], "answerIndex": 1, "explanation": "El texto dice: «¡Qué elegante estás hoy!»."},
            {"id": "b2x6r2", "prompt": "¿Dónde es la reunión?", "options": ["En la sala principal", "En la cocina", "En otro edificio"], "answerIndex": 0, "explanation": "El texto dice: «La reunión es en la sala principal a las cuatro»."},
            {"id": "b2x6r3", "prompt": "¿Qué opina sobre el postre?", "options": ["Que está buenísimo", "Que está muy dulce", "Que no le gusta"], "answerIndex": 0, "explanation": "El texto dice: «Este postre está buenísimo»."},
            {"id": "b2x6r4", "prompt": "¿Qué significa que el tío \"es muy vivo\"?", "options": ["Que está con vida", "Que es astuto", "Que es joven"], "answerIndex": 1, "explanation": "Ser vivo describe astucia como característica de la persona, no el hecho de estar con vida."},
         ]},
        {"id": "b2x6-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x6o1", "prompt": "Ordena las palabras.", "words": ["¿Dónde", "es", "la", "fiesta", "de", "hoy"], "explanation": "Localizar un evento siempre usa ser."},
            {"id": "b2x6o2", "prompt": "Ordena las palabras.", "words": ["Esta", "sopa", "está", "riquísima", "hoy"], "explanation": "Estar + adjetivo para el sabor percibido en el momento."},
         ]},
    ],
    "b2-pasiva-avanzada-y-se": [
        {"id": "b2x7-reading", "type": "reading-comprehension", "title": "Lectura: Un Día de Torpezas",
         "passage": "<p>Se me rompió el teléfono esta mañana sin querer. Se nos olvidaron las llaves dentro del coche otra vez. A mi hermano se le cayó el café encima de la camisa nueva. Se nos hizo tarde y por eso perdimos el autobús de las ocho.</p>",
         "items": [
            {"id": "b2x7r1", "prompt": "¿Qué se le rompió a la persona esta mañana?", "options": ["El teléfono", "Las llaves", "La camisa"], "answerIndex": 0, "explanation": "El texto dice: «Se me rompió el teléfono esta mañana»."},
            {"id": "b2x7r2", "prompt": "¿Qué se les olvidó dentro del coche?", "options": ["El teléfono", "Las llaves", "El café"], "answerIndex": 1, "explanation": "El texto dice: «Se nos olvidaron las llaves dentro del coche»."},
            {"id": "b2x7r3", "prompt": "¿A quién se le cayó el café?", "options": ["A la persona que habla", "A su hermano", "A un desconocido"], "answerIndex": 1, "explanation": "El texto dice: «A mi hermano se le cayó el café»."},
            {"id": "b2x7r4", "prompt": "¿Por qué perdieron el autobús?", "options": ["Porque llegaron temprano", "Porque se les hizo tarde", "Porque no tenían dinero"], "answerIndex": 1, "explanation": "El texto dice: «Se nos hizo tarde y por eso perdimos el autobús»."},
         ]},
        {"id": "b2x7-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x7o1", "prompt": "Ordena las palabras.", "words": ["Se", "me", "olvidó", "el", "paraguas", "en", "casa"], "explanation": "Se + pronombre indirecto + verbo (concuerda con el paraguas, singular)."},
            {"id": "b2x7o2", "prompt": "Ordena las palabras.", "words": ["Se", "nos", "acabó", "la", "leche", "hoy"], "explanation": "Se + pronombre + verbo concordado con la leche (singular)."},
         ]},
    ],
    "b2-estilo-indirecto-todos-los-tiempos": [
        {"id": "b2x8-reading", "type": "reading-comprehension", "title": "Lectura: Recordando una Conversación",
         "passage": "<p>Me dijo que estaba muy ocupada esa semana. Me contó que había viajado a Chile el año anterior con su familia. Prometió que me llamaría al día siguiente para darme más detalles. También me pidió que la esperara un momento en la entrada.</p>",
         "items": [
            {"id": "b2x8r1", "prompt": "¿Cómo dijo que estaba esa semana?", "options": ["Tranquila", "Muy ocupada", "De vacaciones"], "answerIndex": 1, "explanation": "El texto dice: «Me dijo que estaba muy ocupada esa semana»."},
            {"id": "b2x8r2", "prompt": "¿Adónde había viajado el año anterior?", "options": ["A Perú", "A Chile", "A Argentina"], "answerIndex": 1, "explanation": "El texto dice: «había viajado a Chile el año anterior»."},
            {"id": "b2x8r3", "prompt": "¿Qué prometió hacer?", "options": ["Escribir un correo", "Llamar al día siguiente", "Visitarla pronto"], "answerIndex": 1, "explanation": "El texto dice: «Prometió que me llamaría al día siguiente»."},
            {"id": "b2x8r4", "prompt": "¿Qué le pidió al final?", "options": ["Que la llamara", "Que la esperara en la entrada", "Que se fuera"], "answerIndex": 1, "explanation": "El texto termina: «me pidió que la esperara un momento en la entrada»."},
         ]},
        {"id": "b2x8-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x8o1", "prompt": "Ordena las palabras.", "words": ["Dijo", "que", "vendría", "al", "día", "siguiente"], "explanation": "Futuro en la cita original retrocede a condicional en estilo indirecto pasado."},
            {"id": "b2x8o2", "prompt": "Ordena las palabras.", "words": ["Me", "pidió", "que", "cerrara", "la", "puerta"], "explanation": "Imperativo en estilo indirecto pasado se convierte en imperfecto de subjuntivo."},
         ]},
    ],
    "b2-conectores-argumentativos-avanzados": [
        {"id": "b2x9-reading", "type": "reading-comprehension", "title": "Lectura: Un Análisis Breve",
         "passage": "<p>El proyecto avanza bien; ahora bien, todavía faltan detalles por resolver. De hecho, el equipo ha superado varias expectativas iniciales. A mí me gusta el enfoque actual; a mi colega, en cambio, le preocupa el presupuesto. Por el contrario, otros miembros piensan que todo va perfecto.</p>",
         "items": [
            {"id": "b2x9r1", "prompt": "¿Qué matización se hace sobre el avance del proyecto?", "options": ["Que ya está terminado", "Que faltan detalles por resolver", "Que va muy mal"], "answerIndex": 1, "explanation": "El texto dice: «ahora bien, todavía faltan detalles por resolver»."},
            {"id": "b2x9r2", "prompt": "¿Qué refuerza el conector \"de hecho\"?", "options": ["Una duda", "Que el equipo ha superado expectativas", "Un problema nuevo"], "answerIndex": 1, "explanation": "El texto dice: «De hecho, el equipo ha superado varias expectativas»."},
            {"id": "b2x9r3", "prompt": "¿Qué le preocupa al colega?", "options": ["El enfoque", "El presupuesto", "El tiempo"], "answerIndex": 1, "explanation": "El texto dice: «a mi colega, en cambio, le preocupa el presupuesto»."},
            {"id": "b2x9r4", "prompt": "¿Qué opinan otros miembros, según el texto?", "options": ["Que todo va mal", "Que todo va perfecto", "Que no opinan"], "answerIndex": 1, "explanation": "El texto termina: «otros miembros piensan que todo va perfecto»."},
         ]},
        {"id": "b2x9-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x9o1", "prompt": "Ordena las palabras.", "words": ["El", "plan", "es", "bueno", "ahora", "bien", "es", "caro"], "explanation": "Idea + ahora bien (matización) + segunda idea."},
            {"id": "b2x9o2", "prompt": "Ordena las palabras.", "words": ["No", "ayudó", "por", "el", "contrario", "empeoró"], "explanation": "Idea negativa + por el contrario (oposición fuerte) + consecuencia."},
         ]},
    ],
    "b2-colocaciones-y-expresiones-idiomaticas": [
        {"id": "b2x10-reading", "type": "reading-comprehension", "title": "Lectura: Un Mal Día en la Oficina",
         "passage": "<p>Tuve que tomar una decisión difícil sobre el proyecto. Metí la pata al mencionar un tema delicado en la reunión. Mi jefe estaba en las nubes toda la mañana, así que no prestó mucha atención. Al final, decidí no tirar la toalla y seguir trabajando duro.</p>",
         "items": [
            {"id": "b2x10r1", "prompt": "¿Qué tuvo que hacer la persona sobre el proyecto?", "options": ["Cancelarlo", "Tomar una decisión difícil", "Empezarlo de nuevo"], "answerIndex": 1, "explanation": "El texto dice: «Tuve que tomar una decisión difícil sobre el proyecto»."},
            {"id": "b2x10r2", "prompt": "¿Qué significa \"metí la pata\"?", "options": ["Tuve mucho éxito", "Cometí un error inoportuno", "Llegué tarde"], "answerIndex": 1, "explanation": "Meter la pata significa cometer un error, especialmente al hablar en un momento inoportuno."},
            {"id": "b2x10r3", "prompt": "¿Cómo estaba el jefe esa mañana?", "options": ["Muy atento", "En las nubes (distraído)", "De mal humor"], "answerIndex": 1, "explanation": "El texto dice: «Mi jefe estaba en las nubes toda la mañana»."},
            {"id": "b2x10r4", "prompt": "¿Qué decidió al final la persona?", "options": ["Rendirse", "No tirar la toalla", "Cambiar de trabajo"], "answerIndex": 1, "explanation": "El texto termina: «decidí no tirar la toalla y seguir trabajando duro»."},
         ]},
        {"id": "b2x10-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x10o1", "prompt": "Ordena las palabras.", "words": ["Necesitamos", "tomar", "una", "decisión", "pronto"], "explanation": "Colocación fija: tomar una decisión."},
            {"id": "b2x10o2", "prompt": "Ordena las palabras.", "words": ["Ese", "coche", "cuesta", "un", "ojo", "de", "la", "cara"], "explanation": "Expresión idiomática fija: costar un ojo de la cara."},
         ]},
    ],
    "b2-registro-formal-e-informal": [
        {"id": "b2x11-reading", "type": "reading-comprehension", "title": "Lectura: Dos Correos Distintos",
         "passage": "<p>Correo 1: Estimado señor López, le escribo para solicitar información sobre el curso. Quedo a la espera de su respuesta. Atentamente, Laura Gómez.<br>Correo 2: ¡Hola, Marcos! ¿Qué tal todo? Cuéntame cómo te va con el nuevo trabajo. ¡Un abrazo!</p>",
         "items": [
            {"id": "b2x11r1", "prompt": "¿Cuál de los dos correos es formal?", "options": ["El correo 1", "El correo 2", "Ninguno"], "answerIndex": 0, "explanation": "El correo 1 usa fórmulas formales como «Estimado señor» y «Atentamente»."},
            {"id": "b2x11r2", "prompt": "¿Qué solicita Laura en su correo?", "options": ["Un trabajo", "Información sobre el curso", "Una reunión"], "answerIndex": 1, "explanation": "El texto dice: «le escribo para solicitar información sobre el curso»."},
            {"id": "b2x11r3", "prompt": "¿Qué fórmula de cierre usa el correo formal?", "options": ["Un abrazo", "Atentamente", "Hasta pronto"], "answerIndex": 1, "explanation": "El correo 1 termina con «Atentamente, Laura Gómez»."},
            {"id": "b2x11r4", "prompt": "¿Qué le pregunta la persona a Marcos en el correo informal?", "options": ["Por su salud", "Cómo le va con el nuevo trabajo", "Por su familia"], "answerIndex": 1, "explanation": "El texto dice: «Cuéntame cómo te va con el nuevo trabajo»."},
         ]},
        {"id": "b2x11-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x11o1", "prompt": "Ordena las palabras.", "words": ["Le", "escribo", "para", "solicitar", "información"], "explanation": "Registro formal: le (usted) + verbo + para + solicitar (más formal que pedir)."},
            {"id": "b2x11o2", "prompt": "Ordena las palabras.", "words": ["Oye", "¿nos", "vemos", "mañana", "o", "qué"], "explanation": "Registro informal con muletilla (oye) al inicio."},
         ]},
    ],
    "b2-futuro-de-subjuntivo": [
        {"id": "b2x12-reading", "type": "reading-comprehension", "title": "Lectura: Un Fragmento de Reglamento",
         "passage": "<p>El que incumpliere esta norma deberá pagar una indemnización según lo establecido. Quien resultare elegido asumirá el cargo de inmediato. Si no hubiere objeciones, se dará por aprobada la propuesta. Estas formas ya casi no se usan en el habla cotidiana.</p>",
         "items": [
            {"id": "b2x12r1", "prompt": "¿Qué debe pagar quien incumpla la norma?", "options": ["Una multa fija", "Una indemnización", "Nada"], "answerIndex": 1, "explanation": "El texto dice: «deberá pagar una indemnización»."},
            {"id": "b2x12r2", "prompt": "¿Qué pasa si no hay objeciones?", "options": ["Se rechaza la propuesta", "Se da por aprobada la propuesta", "Se pospone la decisión"], "answerIndex": 1, "explanation": "El texto dice: «Si no hubiere objeciones, se dará por aprobada la propuesta»."},
            {"id": "b2x12r3", "prompt": "¿En qué tipo de texto es más probable encontrar estas formas verbales?", "options": ["Un mensaje de texto", "Un documento legal", "Una receta de cocina"], "answerIndex": 1, "explanation": "El texto explica que son formas de un reglamento, propias del lenguaje jurídico."},
            {"id": "b2x12r4", "prompt": "¿Estas formas se usan mucho en el habla cotidiana?", "options": ["Sí, mucho", "Casi no se usan"], "answerIndex": 1, "explanation": "El texto termina: «Estas formas ya casi no se usan en el habla cotidiana»."},
         ]},
        {"id": "b2x12-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "b2x12o1", "prompt": "Ordena las palabras.", "words": ["El", "que", "faltare", "será", "sancionado"], "explanation": "El que + futuro de subjuntivo (faltare) + consecuencia."},
            {"id": "b2x12o2", "prompt": "Ordena las palabras.", "words": ["Adonde", "fueres", "haz", "lo", "que", "vieres"], "explanation": "Refrán tradicional que conserva el futuro de subjuntivo (fueres, vieres)."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
