# -*- coding: utf-8 -*-
"""C1 — Currículo avanzado (Academia de Español de Renan el Profesor)."""

OVERVIEW = (
    "En el nivel C1, el estudiante ya domina el subjuntivo básico y las estructuras "
    "principales del español; ahora afina matices finos del modo subjuntivo, incorpora "
    "el pluscuamperfecto de subjuntivo y las condicionales complejas, aprende a construir "
    "un discurso cohesionado con conectores avanzados y nominalización propia del registro "
    "académico y profesional, y explora con respeto la riqueza dialectal del español — "
    "desde el voseo rioplatense hasta el ustedeo colombiano — junto con los recursos de "
    "atenuación, cortesía e ironía que distinguen a un hablante verdaderamente fluido."
)

LESSONS = [
    {
        "id": "c1-pluscuamperfecto-de-subjuntivo",
        "level": "C1", "unit": "1", "order": 1, "skill": "grammar", "strand": "subjuntivo",
        "title": "El Pluscuamperfecto de Subjuntivo",
        "subtitle": "Hubiera hablado / hubiese hablado — el tiempo compuesto que cierra el sistema del subjuntivo.",
        "objectives": [
            "Formar el pluscuamperfecto de subjuntivo con hubiera/hubiese más el participio pasado.",
            "Usar este tiempo para expresar una acción anterior a otra acción pasada dentro de una oración subordinada.",
            "Reconocer su uso en las condicionales irreales de pasado y en los deseos o arrepentimientos no cumplidos.",
        ],
        "content": {
            "intro": "El pluscuamperfecto de subjuntivo es el tiempo compuesto que permite hablar, dentro del modo subjuntivo, de algo que ya había ocurrido antes de otro momento del pasado.",
            "explanation": "<p>Se forma con el imperfecto de subjuntivo de haber (<em>hubiera</em> o <em>hubiese</em>, ambas formas plenamente intercambiables en casi todos los contextos) más el participio pasado: <em>hubiera hablado, hubiese comido, hubieran vivido</em>. Aparece en subordinadas que dependen de un verbo principal en pasado que expresa duda, deseo o emoción, cuando la acción subordinada es anterior a esa referencia temporal: <em>Dudaba que hubieran llegado a tiempo.</em></p><p>Su uso más frecuente, sin embargo, está en las condicionales irreales de pasado, donde ocupa la prótasis (la parte con \"si\"): <em>Si hubiera sabido la verdad, habría actuado de otra manera.</em> También expresa deseos o arrepentimientos sobre algo que ya no se puede cambiar, especialmente con \"ojalá\": <em>Ojalá hubiera llegado antes.</em></p>",
            "rules": [
                {"heading": "a) Formación", "body": "<p>hubiera/hubiese, hubieras/hubieses, hubiera/hubiese, hubiéramos/hubiésemos, hubierais/hubieseis, hubieran/hubiesen + participio. Participios irregulares frecuentes: hecho, dicho, puesto, escrito, visto, roto, vuelto, abierto, muerto.</p>"},
                {"heading": "b) Uso en subordinadas", "body": "<p>Tras un verbo principal en pasado que expresa duda, deseo o emoción, cuando la acción subordinada ocurrió antes: <em>No creía que hubieran terminado tan rápido.</em> <em>Me alegré de que hubieras venido.</em></p>"},
                {"heading": "c) Condicionales irreales de pasado", "body": "<p>Si + pluscuamperfecto de subjuntivo, condicional compuesto: <em>Si hubiera estudiado más, habría aprobado el examen.</em> En el habla cotidiana también se acepta la variante con pluscuamperfecto de subjuntivo en ambas partes: <em>Si hubiera estudiado más, hubiera aprobado el examen.</em></p>"},
                {"heading": "d) Deseos y arrepentimientos con ojalá", "body": "<p><em>Ojalá + pluscuamperfecto de subjuntivo</em> expresa un deseo sobre algo que ya no puede cambiarse: <em>Ojalá hubiera sabido la verdad antes.</em></p>"},
            ],
            "examples": [
                "Si hubiera sabido que venías, habría preparado algo especial.",
                "No creía que hubieran terminado el proyecto tan rápido.",
                "Ojalá hubiese llegado a tiempo a la reunión.",
                "Me habría gustado que me hubieras avisado antes.",
                "Era la mejor película que hubiera visto en años.",
                "Si hubiéramos reservado con antelación, no habríamos pagado tanto.",
                "Dudaba que hubiese dicho eso en serio.",
                "Ojalá hubiéramos aprovechado mejor el tiempo.",
            ],
            "commonMistakes": [
                {"wrong": "Si había sabido, habría venido.", "right": "Si hubiera sabido, habría venido.", "why": "La condición irreal de pasado exige el pluscuamperfecto de subjuntivo en la prótasis, no el pluscuamperfecto de indicativo."},
                {"wrong": "Ojalá haya sabido la verdad antes.", "right": "Ojalá hubiera sabido la verdad antes.", "why": "Un deseo sobre algo que ya no se puede cambiar en el pasado requiere el pluscuamperfecto de subjuntivo, no el pretérito perfecto de subjuntivo, que se reserva para el pasado reciente o el futuro."},
                {"wrong": "Era la mejor película que hubiera vistado.", "right": "Era la mejor película que hubiera visto.", "why": "El verbo ver tiene un participio irregular, visto, no la forma regularizada vistado."},
            ],
        },
        "exercises": [
            {"id": "c1l1-fill", "type": "fill-blank", "title": "Completa con el Pluscuamperfecto de Subjuntivo",
             "instructions": "Elige la forma correcta para cada espacio.",
             "items": [
                {"id": "c1l1i1", "prompt": "Si ___ (saber) la verdad, te lo habría dicho.", "answers": [["hubiera sabido", "hubiese sabido"]], "options": ["hubiera sabido", "he sabido", "sabía"], "explanation": "Prótasis de una condicional irreal de pasado: pluscuamperfecto de subjuntivo."},
                {"id": "c1l1i2", "prompt": "No pensé que ellos ___ (llegar) tan temprano.", "answers": [["hubieran llegado", "hubiesen llegado"]], "options": ["hubieran llegado", "habían llegado", "llegaron"], "explanation": "Duda sobre un hecho anterior al verbo principal en pasado: pluscuamperfecto de subjuntivo."},
                {"id": "c1l1i3", "prompt": "Ojalá ___ (yo - estudiar) más para el examen de ayer.", "answers": [["hubiera estudiado", "hubiese estudiado"]], "options": ["hubiera estudiado", "estudié", "estudiaría"], "explanation": "Ojalá + pluscuamperfecto de subjuntivo expresa un arrepentimiento sobre el pasado."},
                {"id": "c1l1i4", "prompt": "Era el mejor concierto que ___ (ver) en mi vida.", "answers": [["hubiera visto", "hubiese visto"]], "options": ["hubiera visto", "he visto", "había visto"], "explanation": "Superlativo relativo en contexto pasado: pluscuamperfecto de subjuntivo."},
             ]},
            {"id": "c1l1-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "c1l1i5", "prompt": "Si tú me lo ___, te habría ayudado sin dudarlo.", "options": ["hubieras pedido", "pedías", "pedirías"], "answerIndex": 0, "explanation": "La prótasis de una condicional irreal de pasado nunca lleva condicional ni imperfecto de indicativo."},
                {"id": "c1l1i6", "prompt": "Si ___ la puerta a tiempo, habríamos entrado antes de que empezara a llover.", "options": ["hubiéramos abrido", "hubiéramos abierto", "habíamos abierto"], "answerIndex": 1, "explanation": "Abrir tiene un participio irregular: abierto, no abrido."},
                {"id": "c1l1i7", "prompt": "Si hubiera llovido, ___ el partido.", "options": ["habrían cancelado", "cancelan", "cancelaban"], "answerIndex": 0, "explanation": "La apódosis de una condicional irreal de pasado va en condicional compuesto."},
                {"id": "c1l1i8", "prompt": "\"Ojalá hubiera llegado a tiempo\" expresa...", "options": ["un deseo sobre el futuro", "un arrepentimiento sobre algo que ya no puede cambiarse", "una orden cortés"], "answerIndex": 1, "explanation": "Ojalá + pluscuamperfecto de subjuntivo se usa para lamentar algo del pasado que ya no tiene solución."},
             ]},
            {"id": "c1l1-correction", "type": "correction", "title": "Corrige el Error",
             "items": [
                {"id": "c1l1i9", "incorrect": "Si había estudiado más, habría aprobado.", "answer": ["Si hubiera estudiado más, habría aprobado.", "Si hubiese estudiado más, habría aprobado."], "explanation": "La prótasis de una condicional irreal de pasado exige el pluscuamperfecto de subjuntivo, no el de indicativo."},
                {"id": "c1l1i10", "incorrect": "Ojalá haya sabido la verdad antes.", "answer": ["Ojalá hubiera sabido la verdad antes.", "Ojalá hubiese sabido la verdad antes."], "explanation": "Un deseo irrealizable sobre el pasado requiere el pluscuamperfecto de subjuntivo."},
                {"id": "c1l1i11", "incorrect": "Era la mejor película que había visto.", "answer": ["Era la mejor película que hubiera visto.", "Era la mejor película que hubiese visto."], "explanation": "El superlativo relativo en contexto pasado dispara el subjuntivo, aquí en su forma compuesta."},
             ]},
        ],
        "summary": [
            "El pluscuamperfecto de subjuntivo se forma con hubiera/hubiese más el participio pasado, dos formas intercambiables.",
            "Expresa una acción anterior a otro punto del pasado dentro de una subordinada, y ocupa la prótasis de las condicionales irreales de pasado.",
            "Con ojalá, comunica un deseo o un arrepentimiento sobre algo que ya no puede cambiarse.",
        ],
    },
    {
        "id": "c1-condicionales-complejas",
        "level": "C1", "unit": "1", "order": 2, "skill": "grammar", "strand": "condicionales",
        "title": "Condicionales Complejas: los Cuatro Tipos",
        "subtitle": "Real, potencial, irreal de pasado y condicionales mixtas: cómo elegir el tiempo verbal correcto en cada mitad de la oración.",
        "objectives": [
            "Distinguir los cuatro tipos de oraciones condicionales según el grado de realidad de la condición.",
            "Elegir el tiempo verbal correcto en la prótasis y en la apódosis de cada tipo.",
            "Construir condicionales mixtas que combinan una condición pasada con una consecuencia presente.",
        ],
        "content": {
            "intro": "El español distingue con precisión el grado de realidad de una condición mediante cuatro estructuras distintas, cada una con su propia combinación de tiempos verbales.",
            "explanation": "<p>El tipo 1 (real o probable) expresa una condición posible o habitual: si + presente de indicativo, con presente, futuro o imperativo en la consecuencia: <em>Si llueve, no salimos.</em> El tipo 2 (potencial o irreal de presente) expresa una condición improbable o contraria a la realidad actual: si + imperfecto de subjuntivo, condicional simple: <em>Si tuviera dinero, viajaría más.</em></p><p>El tipo 3 (irreal de pasado) expresa una condición que no se cumplió: si + pluscuamperfecto de subjuntivo, condicional compuesto: <em>Si hubiera sabido, habría venido.</em> Las condicionales mixtas combinan una prótasis de un tiempo con una apódosis de otro cuando el momento de la condición y el de la consecuencia no coinciden, típicamente una condición pasada con una consecuencia presente: <em>Si hubiera aceptado ese trabajo, ahora viviría en otra ciudad.</em></p>",
            "rules": [
                {"heading": "a) Tipo 1 — real/probable", "body": "<p>Si + presente de indicativo, presente/futuro/imperativo: <em>Si estudias, apruebas.</em> <em>Si tienes hambre, come algo.</em></p>"},
                {"heading": "b) Tipo 2 — potencial/irreal de presente", "body": "<p>Si + imperfecto de subjuntivo, condicional simple: <em>Si fuera rico, no trabajaría.</em></p>"},
                {"heading": "c) Tipo 3 — irreal de pasado", "body": "<p>Si + pluscuamperfecto de subjuntivo, condicional compuesto: <em>Si hubiera llovido, habríamos cancelado.</em></p>"},
                {"heading": "d) Condicionales mixtas", "body": "<p>Prótasis de un tiempo, apódosis de otro, cuando los momentos no coinciden: <em>Si hubiera nacido en otro país, hablaría otro idioma.</em> (condición pasada, consecuencia presente)</p>"},
            ],
            "examples": [
                "Si tienes hambre, hay fruta en la cocina.",
                "Si me lo pidieras, lo haría sin dudarlo.",
                "Si hubiéramos salido antes, no habríamos perdido el tren.",
                "Si no hubiera tomado esa decisión, ahora no estaría aquí.",
                "Si apruebas el examen, te invito a cenar.",
                "Si tuviéramos más tiempo, visitaríamos el museo.",
                "Si hubieras confiado en mí, todo habría sido más fácil.",
                "Si fuera más ordenado, no perdería las llaves todos los días.",
            ],
            "commonMistakes": [
                {"wrong": "Si tendría dinero, viajaría más.", "right": "Si tuviera dinero, viajaría más.", "why": "La prótasis nunca lleva condicional; el tipo potencial exige imperfecto de subjuntivo en la parte con \"si\"."},
                {"wrong": "Si hubiera sabido, vendría.", "right": "Si hubiera sabido, habría venido.", "why": "Cuando tanto la condición como la consecuencia pertenecen por completo al pasado, la apódosis debe ir en condicional compuesto, no en condicional simple."},
                {"wrong": "Si llueva, no salimos.", "right": "Si llueve, no salimos.", "why": "La condicional de tipo real usa presente de indicativo después de \"si\", nunca presente de subjuntivo."},
            ],
        },
        "exercises": [
            {"id": "c1l2-mc", "type": "multiple-choice", "title": "Identifica el Tipo Correcto",
             "items": [
                {"id": "c1l2i1", "prompt": "\"Si ___ tiempo, te ayudo con la mudanza.\" (condición real, presente)", "options": ["tengo", "tuviera", "hubiera tenido"], "answerIndex": 0, "explanation": "Condición real y probable: presente de indicativo."},
                {"id": "c1l2i2", "prompt": "\"Si ___ más paciente, no discutiríamos tanto.\" (condición contraria a la realidad actual)", "options": ["soy", "fuera", "hubiera sido"], "answerIndex": 1, "explanation": "Condición potencial/irreal de presente: imperfecto de subjuntivo."},
                {"id": "c1l2i3", "prompt": "\"Si me lo ___ antes, no habría llegado tarde.\" (condición que no se cumplió en el pasado)", "options": ["dices", "dijeras", "hubieras dicho"], "answerIndex": 2, "explanation": "Condición irreal de pasado: pluscuamperfecto de subjuntivo."},
                {"id": "c1l2i4", "prompt": "\"Si no hubiera aceptado ese trabajo, ahora ___ en otra ciudad.\" (consecuencia en el presente)", "options": ["viviría", "habría vivido", "viva"], "answerIndex": 0, "explanation": "Condicional mixta: prótasis pasada, apódosis presente, por lo que se usa el condicional simple."},
             ]},
            {"id": "c1l2-fill", "type": "fill-blank", "title": "Completa la Condicional",
             "items": [
                {"id": "c1l2i5", "prompt": "Si ___ (yo - poder), iría contigo.", "answers": [["pudiera", "pudiese"]], "options": ["pudiera", "puedo", "podría"], "explanation": "Tipo potencial: imperfecto de subjuntivo en la prótasis."},
                {"id": "c1l2i6", "prompt": "Si no ___ (nosotros - perder) el vuelo, ya estaríamos en el hotel.", "answers": [["hubiéramos perdido", "hubiésemos perdido"]], "options": ["hubiéramos perdido", "perdimos", "perderíamos"], "explanation": "Condicional mixta: condición pasada con consecuencia presente."},
                {"id": "c1l2i7", "prompt": "Si ___ (tú - querer), podemos salir esta tarde.", "answers": [["quieres"]], "options": ["quieres", "quisieras", "quisiste"], "explanation": "Condición real, referida al presente/futuro: presente de indicativo."},
                {"id": "c1l2i8", "prompt": "Si me ___ (avisar) a tiempo, habríamos cambiado los planes.", "answers": [["hubieras avisado", "hubieses avisado"]], "options": ["hubieras avisado", "avisabas", "avisarías"], "explanation": "Condición irreal de pasado: pluscuamperfecto de subjuntivo."},
             ]},
            {"id": "c1l2-ordering", "type": "ordering", "title": "Ordena la Oración",
             "instructions": "Ordena las palabras para formar una oración condicional correcta.",
             "items": [
                {"id": "c1l2i9", "prompt": "Forma una condicional de tipo real.", "words": ["Si", "estudias", "todos", "los", "días", "aprenderás", "más", "rápido"], "explanation": "Si + presente de indicativo, futuro simple en la consecuencia."},
                {"id": "c1l2i10", "prompt": "Forma una condicional potencial.", "words": ["Si", "tuviera", "más", "vacaciones", "viajaría", "por", "toda", "Sudamérica"], "explanation": "Si + imperfecto de subjuntivo, condicional simple."},
                {"id": "c1l2i11", "prompt": "Forma una condicional irreal de pasado.", "words": ["Si", "hubiéramos", "reservado", "antes", "habríamos", "pagado", "menos"], "explanation": "Si + pluscuamperfecto de subjuntivo, condicional compuesto."},
             ]},
        ],
        "summary": [
            "El tipo real (si + presente, presente/futuro) expresa una condición posible o habitual.",
            "El tipo potencial (si + imperfecto de subjuntivo, condicional simple) y el tipo irreal de pasado (si + pluscuamperfecto de subjuntivo, condicional compuesto) expresan condiciones contrarias a la realidad presente o pasada.",
            "Las condicionales mixtas combinan tiempos de dos tipos distintos cuando el momento de la condición y el de la consecuencia no coinciden.",
        ],
    },
    {
        "id": "c1-matices-del-subjuntivo",
        "level": "C1", "unit": "1", "order": 3, "skill": "grammar", "strand": "subjuntivo",
        "title": "Matices del Subjuntivo: Percepción, Negación y Grados de Certeza",
        "subtitle": "Por qué \"veo que llueve\" usa indicativo y \"no veo que llueva\" usa subjuntivo — el subjuntivo como marcador de certeza.",
        "objectives": [
            "Reconocer cómo la negación de un verbo de percepción o de opinión desencadena el subjuntivo en la subordinada.",
            "Distinguir entre expresiones de certeza total, que piden indicativo, y expresiones de duda o certeza parcial, que piden subjuntivo.",
            "Usar correctamente verbos como ver, creer, pensar y parecer en sus formas afirmativa y negativa.",
        ],
        "content": {
            "intro": "El uso del subjuntivo no depende solo de una lista fija de verbos que lo activan, sino del grado de certeza que el hablante realmente comunica en cada momento.",
            "explanation": "<p>Verbos como <em>ver, creer, pensar, parecer, suponer</em> llevan indicativo en la subordinada cuando se usan en afirmativa, porque comunican una certeza asumida por el hablante: <em>Veo que estás cansado.</em> Cuando se niegan, la certeza desaparece y el verbo subordinado pasa a subjuntivo: <em>No veo que estés cansado.</em> Esta alternancia también afecta a estructuras con \"quizá(s)\", \"tal vez\" y \"posiblemente\", donde el subjuntivo marca mayor duda y el indicativo, mayor confianza del hablante en lo que dice.</p><p>Es un matiz, no una regla mecánica: dos hablantes pueden elegir indicativo o subjuntivo con la misma palabra según cuánta seguridad quieran transmitir, y ese margen de elección es precisamente lo que distingue el uso avanzado del uso mecánico del subjuntivo.</p>",
            "rules": [
                {"heading": "a) Verbos de percepción/opinión en afirmativa", "body": "<p>Piden indicativo: <em>Noto que has cambiado.</em> <em>Me parece que tiene razón.</em></p>"},
                {"heading": "b) Los mismos verbos negados", "body": "<p>Piden subjuntivo: <em>No noto que hayas cambiado.</em> <em>No me parece que tenga razón.</em></p>"},
                {"heading": "c) Quizá(s), tal vez, posiblemente", "body": "<p>Subjuntivo cuando expresan más duda; indicativo cuando expresan más confianza: <em>Quizá venga</em> (dudoso) frente a <em>Quizá viene</em> (más seguro).</p>"},
                {"heading": "d) Preguntas con verbos de opinión", "body": "<p>Pueden llevar subjuntivo si la pregunta busca genuinamente confirmar algo incierto: <em>¿Crees que sea buena idea?</em> frente a la pregunta más neutra <em>¿Crees que es buena idea?</em></p>"},
            ],
            "examples": [
                "Veo que has terminado el informe.",
                "No veo que hayas terminado el informe todavía.",
                "Me parece que el plan funciona.",
                "No me parece que el plan funcione tan bien como dicen.",
                "Quizá tengamos suerte esta vez.",
                "Quizá tenemos razón, pero conviene comprobarlo.",
                "No creo que sea tan complicado como parece.",
                "¿Piensas que valga la pena intentarlo?",
            ],
            "commonMistakes": [
                {"wrong": "No veo que has terminado.", "right": "No veo que hayas terminado.", "why": "Al negar un verbo de percepción, la subordinada pierde la certeza asumida y exige subjuntivo."},
                {"wrong": "Creo que tenga razón.", "right": "Creo que tiene razón.", "why": "\"Creer\" en afirmativa expresa una certeza asumida por el hablante y pide indicativo; el subjuntivo solo aparece al negarlo: \"no creo que tenga razón\"."},
                {"wrong": "Usar siempre indicativo con \"quizá\", sin ningún matiz de duda.", "right": "Alternar \"quizá venga\" (duda) y \"quizá viene\" (confianza) según la intención real.", "why": "La elección entre indicativo y subjuntivo con \"quizá\" comunica un matiz real de certeza; no es una elección libre de significado."},
            ],
        },
        "exercises": [
            {"id": "c1l3-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "c1l3i1", "statement": "En la frase \"No veo que estés listo\", el verbo subordinado debe ir en subjuntivo.", "answer": True, "explanation": "La negación de un verbo de percepción elimina la certeza y exige subjuntivo en la subordinada."},
                {"id": "c1l3i2", "statement": "El verbo \"creer\" en afirmativa siempre exige subjuntivo en la subordinada.", "answer": False, "explanation": "En afirmativa, \"creer\" expresa una certeza asumida y pide indicativo; el subjuntivo aparece al negarlo."},
                {"id": "c1l3i3", "statement": "Con \"quizá\", el uso del subjuntivo o del indicativo puede cambiar el grado de certeza que se comunica.", "answer": True, "explanation": "El subjuntivo con \"quizá\" marca más duda; el indicativo, más confianza del hablante."},
                {"id": "c1l3i4", "statement": "La negación de un verbo de opinión nunca afecta al modo del verbo subordinado.", "answer": False, "explanation": "La negación es precisamente lo que dispara el cambio de indicativo a subjuntivo en estos verbos."},
             ]},
            {"id": "c1l3-fill", "type": "fill-blank", "title": "Completa Según el Grado de Certeza",
             "items": [
                {"id": "c1l3i5", "prompt": "Veo que ___ (tú - estar) muy ocupado hoy.", "answers": [["estás"]], "options": ["estás", "estés"], "explanation": "Percepción afirmativa: indicativo."},
                {"id": "c1l3i6", "prompt": "No veo que ___ (tú - estar) tan ocupado como dices.", "answers": [["estés"]], "options": ["estás", "estés"], "explanation": "Percepción negada: subjuntivo."},
                {"id": "c1l3i7", "prompt": "No me parece que la propuesta ___ (ser) tan mala.", "answers": [["sea"]], "options": ["es", "sea"], "explanation": "Opinión negada: subjuntivo."},
                {"id": "c1l3i8", "prompt": "Me parece que la propuesta ___ (ser) razonable.", "answers": [["es"]], "options": ["es", "sea"], "explanation": "Opinión afirmativa: indicativo."},
             ]},
            {"id": "c1l3-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "c1l3i9", "prompt": "\"Quizá ___ razón, pero conviene comprobarlo.\" (el hablante está bastante seguro)", "options": ["tengamos", "tenemos", "tener"], "answerIndex": 1, "explanation": "El indicativo con quizá comunica más confianza del hablante."},
                {"id": "c1l3i10", "prompt": "\"No pienso que eso ___ verdad.\"", "options": ["es", "sea", "será"], "answerIndex": 1, "explanation": "La negación de un verbo de opinión dispara el subjuntivo."},
                {"id": "c1l3i11", "prompt": "\"Supongo que ya lo ___.\" (afirmación asumida como cierta)", "options": ["sepan", "saben", "sabrían"], "answerIndex": 1, "explanation": "\"Suponer\" en afirmativa pide indicativo por expresar una certeza asumida."},
                {"id": "c1l3i12", "prompt": "\"¿Crees que ___ buena idea?\" (pregunta que busca confirmar algo genuinamente incierto)", "options": ["es", "sea", "será"], "answerIndex": 1, "explanation": "En una pregunta que expresa duda genuina, es posible usar subjuntivo."},
             ]},
        ],
        "summary": [
            "Los verbos de percepción y opinión en afirmativa piden indicativo porque comunican una certeza asumida.",
            "Al negarlos, la certeza desaparece y la subordinada pasa a subjuntivo.",
            "Con \"quizá\", \"tal vez\" y \"posiblemente\", la elección entre indicativo y subjuntivo comunica un matiz real de mayor o menor certeza.",
        ],
    },
    {
        "id": "c1-construcciones-enfaticas",
        "level": "C1", "unit": "1", "order": 4, "skill": "grammar", "strand": "relieve",
        "title": "Construcciones Enfáticas y de Relieve",
        "subtitle": "\"Lo que pasa es que...\", \"es que...\", \"fue entonces cuando...\" — cómo destacar la parte más importante de una idea.",
        "objectives": [
            "Usar estructuras de relieve para destacar un elemento concreto de la oración.",
            "Distinguir el matiz explicativo de \"es que\" del valor enfático de \"lo que pasa es que\".",
            "Construir oraciones escindidas con \"fue... cuando/donde/quien\" para poner el foco en un elemento temporal, espacial o personal.",
        ],
        "content": {
            "intro": "Las construcciones enfáticas reorganizan una oración normal para colocar en primer plano justo el elemento que el hablante quiere resaltar, algo que el español no logra solo con la entonación.",
            "explanation": "<p>El español dispone de estructuras sintácticas dedicadas a destacar un elemento: las oraciones escindidas o hendidas (<em>fue entonces cuando..., fue él quien..., fue en Madrid donde...</em>) aíslan el elemento enfatizado en una cláusula con \"ser\" y lo relacionan con el resto mediante un relativo (que, quien, donde, cuando). Expresiones fijas como <em>lo que pasa es que...</em> y <em>es que...</em> cumplen una función distinta: introducen una explicación o justificación, a menudo con matiz aclaratorio, muy frecuentes en el registro oral.</p><p>La variante <em>lo que + verbo + es</em> realza como punto central del argumento toda una idea, no solo un elemento: <em>Lo que necesitamos es más tiempo.</em></p>",
            "rules": [
                {"heading": "a) Oraciones escindidas", "body": "<p>Fue + elemento enfatizado + quien/que/donde/cuando + resto de la oración: <em>Fue mi hermana quien me lo contó.</em> <em>Fue en ese momento cuando entendí todo.</em></p>"},
                {"heading": "b) \"Es que...\"", "body": "<p>Introduce una justificación o excusa, normalmente en respuesta a algo: <em>¿Por qué no viniste? — Es que se me olvidó por completo.</em></p>"},
                {"heading": "c) \"Lo que pasa es que...\"", "body": "<p>Realza toda una explicación como el punto central del argumento: <em>Lo que pasa es que nadie nos avisó a tiempo.</em></p>"},
                {"heading": "d) \"Lo que + verbo + es\"", "body": "<p><em>Lo que necesitamos es más tiempo.</em> <em>Lo que me molesta es la falta de comunicación.</em></p>"},
            ],
            "examples": [
                "Fue mi profesora quien me animó a seguir estudiando.",
                "Fue en ese viaje cuando decidí cambiar de carrera.",
                "Es que no tuve tiempo de avisarte antes.",
                "Lo que pasa es que el sistema lleva días fallando.",
                "Lo que más me sorprendió fue su sinceridad.",
                "Fue así como conseguimos convencerlo.",
                "Lo que necesitamos ahora es un poco de calma.",
                "Es que, sinceramente, no me convence el plan.",
            ],
            "commonMistakes": [
                {"wrong": "Fue mi hermana que me lo contó.", "right": "Fue mi hermana quien me lo contó.", "why": "Cuando el elemento enfatizado es una persona, el registro cuidado prefiere \"quien\" en la cláusula relativa, aunque \"que\" se oye en el habla informal."},
                {"wrong": "Usar \"es que\" para abrir una conversación sin ningún contexto previo.", "right": "Reservar \"es que\" para justificar o explicar algo ya mencionado.", "why": "\"Es que\" presupone una pregunta o un reproche implícito; usarlo sin ese contexto suena descontextualizado."},
                {"wrong": "Lo que pasa que nadie avisó.", "right": "Lo que pasa es que nadie avisó.", "why": "La construcción fija requiere el verbo \"es\" entre \"lo que pasa\" y la cláusula con \"que\"; no puede omitirse."},
            ],
        },
        "exercises": [
            {"id": "c1l4-mc", "type": "multiple-choice", "title": "Elige la Construcción Correcta",
             "items": [
                {"id": "c1l4i1", "prompt": "\"___ me convenció de estudiar español fue mi abuela.\"", "options": ["Lo que", "Es que", "Fue que"], "answerIndex": 0, "explanation": "\"Lo que + verbo + es/fue\" enfatiza toda una idea."},
                {"id": "c1l4i2", "prompt": "\"¿Por qué llegaste tarde? — ___ perdí el autobús.\"", "options": ["Fue que", "Es que", "Lo que pasa"], "answerIndex": 1, "explanation": "\"Es que\" introduce una justificación en respuesta a una pregunta."},
                {"id": "c1l4i3", "prompt": "\"___ en ese bar donde nos conocimos.\"", "options": ["Es", "Fue", "Era"], "answerIndex": 1, "explanation": "La oración escindida temporal/espacial usa \"fue\" seguido de \"donde\"."},
                {"id": "c1l4i4", "prompt": "\"Lo que pasa ___ que nadie revisó los datos antes de enviarlos.\"", "options": ["es", "fue", "sea"], "answerIndex": 0, "explanation": "La construcción fija exige el presente \"es\" en este contexto habitual, salvo que todo el relato esté en pasado."},
             ]},
            {"id": "c1l4-correction", "type": "correction", "title": "Corrige la Construcción",
             "items": [
                {"id": "c1l4i5", "incorrect": "Lo que pasa que nadie avisó a tiempo.", "answer": ["Lo que pasa es que nadie avisó a tiempo."], "explanation": "Falta el verbo \"es\" en la construcción fija \"lo que pasa es que\"."},
                {"id": "c1l4i6", "incorrect": "Fue el jefe que tomó la decisión final.", "answer": ["Fue el jefe quien tomó la decisión final."], "explanation": "Con una persona como elemento enfatizado, el registro cuidado prefiere \"quien\"."},
                {"id": "c1l4i7", "incorrect": "Fue ayer que llegamos, en la tarde donde encontramos la casa vacía.", "answer": ["Fue ayer cuando llegamos, por la tarde, y encontramos la casa vacía."], "explanation": "El elemento temporal enfatizado con \"fue\" se relaciona con \"cuando\", no con \"que\" ni con \"donde\"."},
             ]},
            {"id": "c1l4-matching", "type": "matching", "title": "Relaciona la Función con el Ejemplo",
             "items": [
                {"id": "c1l4i8", "prompt": "Relaciona cada función con la oración que la ilustra.", "pairs": [
                    {"left": "Justificar una acción", "right": "Es que se me hizo tarde por el tráfico."},
                    {"left": "Destacar a la persona responsable", "right": "Fue mi tutor quien me recomendó este libro."},
                    {"left": "Destacar el momento exacto", "right": "Fue entonces cuando comprendí mi error."},
                    {"left": "Presentar una explicación central", "right": "Lo que pasa es que el servidor lleva horas caído."},
                ], "explanation": "Cada estructura de relieve cumple una función discursiva distinta, aunque todas comparten el recurso de destacar un elemento."},
             ]},
        ],
        "summary": [
            "Las oraciones escindidas (fue... quien/que/donde/cuando) aíslan y destacan un elemento concreto de la oración.",
            "\"Es que\" introduce una justificación en respuesta a algo ya mencionado; \"lo que pasa es que\" presenta una explicación como punto central del argumento.",
            "Estas construcciones son un recurso sintáctico, no solo tonal, para dar relieve a la parte más importante de una idea.",
        ],
    },
    {
        "id": "c1-nominalizacion-y-estilo-academico",
        "level": "C1", "unit": "1", "order": 5, "skill": "writing", "strand": "registro-academico",
        "title": "Nominalización y Estilo Académico",
        "subtitle": "Convertir verbos y adjetivos en sustantivos para lograr un registro más formal y objetivo.",
        "objectives": [
            "Transformar verbos y adjetivos en sustantivos abstractos mediante los sufijos más productivos del español.",
            "Reescribir oraciones con verbos personales en construcciones nominalizadas propias del registro académico.",
            "Reconocer cuándo la nominalización aporta precisión y cuándo simplemente complica innecesariamente una frase.",
        ],
        "content": {
            "intro": "La nominalización — convertir una acción o una cualidad en un sustantivo — es uno de los recursos más característicos del español académico y profesional escrito.",
            "explanation": "<p>Convertir un verbo en sustantivo (<em>analizar → el análisis, decidir → la decisión, implementar → la implementación</em>) o un adjetivo en sustantivo (<em>eficaz → la eficacia, complejo → la complejidad</em>) permite condensar información y desplazar el foco de quién actúa hacia el proceso o el resultado en sí, algo típico de informes, artículos y textos expositivos. Los sufijos más productivos son -ción/-sión (comunicación, decisión), -miento (crecimiento, conocimiento), -dad/-idad (viabilidad, complejidad) y -eza (certeza, pobreza).</p><p>Este recurso no debe abusarse: en exceso, produce un estilo denso y poco natural, conocido informalmente como \"nominalitis\". Un buen texto académico alterna nominalizaciones con verbos personales para mantener la claridad.</p>",
            "rules": [
                {"heading": "a) Sufijos verbo → sustantivo", "body": "<p>-ción/-sión (organizar → organización, decidir → decisión), -miento (establecer → establecimiento), -ancia/-encia (tolerar → tolerancia), -aje (aprender → aprendizaje, forma irregular).</p>"},
                {"heading": "b) Sufijos adjetivo → sustantivo", "body": "<p>-dad/-idad (posible → posibilidad), -eza (pobre → pobreza), -ismo (real → realismo).</p>"},
                {"heading": "c) Uso típico en registro académico", "body": "<p>Sustituir \"Los investigadores decidieron cambiar el método\" por \"La decisión de cambiar el método...\" desplaza el foco de la acción al resultado, apto para resúmenes y conclusiones.</p>"},
                {"heading": "d) Moderación", "body": "<p>Alternar nominalizaciones con verbos conjugados evita un estilo excesivamente denso; conviene reservarlas para las ideas centrales del texto.</p>"},
            ],
            "examples": [
                "La implementación del nuevo sistema mejoró la eficiencia del equipo.",
                "Su decisión de renunciar sorprendió a todos.",
                "La complejidad del problema exige un análisis detallado.",
                "El crecimiento económico se desaceleró el año pasado.",
                "La viabilidad del proyecto depende de la financiación disponible.",
                "El desconocimiento de las normas generó varios errores.",
                "La resolución del conflicto tomó varias semanas.",
                "Su insistencia en revisar los datos evitó un error grave.",
            ],
            "commonMistakes": [
                {"wrong": "La analización de los datos tomó tres días.", "right": "El análisis de los datos tomó tres días.", "why": "El sustantivo correcto derivado de \"analizar\" es \"el análisis\", no la forma regularizada \"analización\"."},
                {"wrong": "La realización de la implementación de la decisión de cambio tomó semanas.", "right": "Implementar la decisión de cambio tomó semanas.", "why": "Encadenar demasiadas nominalizaciones produce un estilo artificialmente denso y difícil de seguir, incluso en registro formal."},
                {"wrong": "La aparición del problema fue debido a un fallo del servidor.", "right": "La aparición del problema se debió a un fallo del servidor.", "why": "El verbo que acompaña a una nominalización con sujeto de este tipo debe ser \"deberse a\", no \"ser debido a\", en el registro cuidado."},
            ],
        },
        "exercises": [
            {"id": "c1l5-typing", "type": "typing", "title": "Convierte el Verbo en Sustantivo",
             "instructions": "Escribe el sustantivo derivado de cada verbo.",
             "items": [
                {"id": "c1l5i1", "prompt": "Escribe el sustantivo derivado del verbo \"decidir\".", "answer": ["decisión", "la decisión"], "explanation": "Decidir → la decisión."},
                {"id": "c1l5i2", "prompt": "Escribe el sustantivo derivado del verbo \"analizar\".", "answer": ["análisis", "el análisis"], "explanation": "Analizar → el análisis (forma irregular, invariable en número)."},
                {"id": "c1l5i3", "prompt": "Escribe el sustantivo derivado del verbo \"crecer\".", "answer": ["crecimiento", "el crecimiento"], "explanation": "Crecer → el crecimiento."},
                {"id": "c1l5i4", "prompt": "Escribe el sustantivo derivado del verbo \"resolver\".", "answer": ["resolución", "la resolución"], "explanation": "Resolver → la resolución."},
                {"id": "c1l5i5", "prompt": "Escribe el sustantivo derivado del verbo \"establecer\".", "answer": ["establecimiento", "el establecimiento"], "explanation": "Establecer → el establecimiento."},
             ]},
            {"id": "c1l5-mc", "type": "multiple-choice", "title": "Elige la Nominalización Correcta",
             "items": [
                {"id": "c1l5i6", "prompt": "\"La ___ del proyecto depende de la financiación disponible.\" (de viable)", "options": ["viabilidad", "viableza", "viabilización"], "answerIndex": 0, "explanation": "Viable → la viabilidad, con el sufijo -idad."},
                {"id": "c1l5i7", "prompt": "\"El ___ de las normas generó varios errores.\" (de desconocer)", "options": ["desconocido", "desconocimiento", "desconocencia"], "answerIndex": 1, "explanation": "Desconocer → el desconocimiento, con el sufijo -miento."},
                {"id": "c1l5i8", "prompt": "Elige la versión de registro más académico.", "options": ["Los investigadores decidieron cambiar el método porque los datos no cuadraban.", "La decisión de cambiar el método respondió a inconsistencias en los datos.", "Cambiaron el método porque los números no cuadraban."], "answerIndex": 1, "explanation": "La nominalización desplaza el foco de quién actúa hacia el proceso, propio del registro académico."},
                {"id": "c1l5i9", "prompt": "¿Cuál de estas frases abusa de la nominalización hasta volverse poco clara?", "options": ["El análisis reveló varios errores.", "La realización de la implementación de la evaluación de resultados se retrasó.", "La complejidad del caso exigió más tiempo."], "answerIndex": 1, "explanation": "Encadenar varias nominalizaciones seguidas produce un estilo artificialmente denso, conocido como \"nominalitis\"."},
             ]},
            {"id": "c1l5-fill", "type": "fill-blank", "title": "Completa con la Nominalización",
             "items": [
                {"id": "c1l5i10", "prompt": "La ___ (crecer) económico se desaceleró el año pasado.", "answers": [["crecimiento"]], "options": ["crecimiento", "creciente", "crecencia"], "explanation": "Crecer → el crecimiento."},
                {"id": "c1l5i11", "prompt": "La ___ (complejo) del problema exige un análisis detallado.", "answers": [["complejidad"]], "options": ["complejidad", "complejeza", "complejismo"], "explanation": "Complejo → la complejidad."},
                {"id": "c1l5i12", "prompt": "Su ___ (insistir) en revisar los datos evitó un error grave.", "answers": [["insistencia"]], "options": ["insistencia", "insistimiento", "insistidad"], "explanation": "Insistir → la insistencia."},
             ]},
        ],
        "summary": [
            "La nominalización convierte verbos y adjetivos en sustantivos abstractos mediante sufijos como -ción, -miento, -dad y -eza.",
            "Este recurso desplaza el foco de quién actúa hacia el proceso o el resultado, típico del registro académico y profesional.",
            "Usado en exceso, produce un estilo artificialmente denso; conviene alternarlo con verbos personales.",
        ],
    },
    {
        "id": "c1-conectores-textuales-avanzados",
        "level": "C1", "unit": "1", "order": 6, "skill": "writing", "strand": "discurso",
        "title": "Conectores Textuales Avanzados",
        "subtitle": "Asimismo, cabe destacar, en última instancia, dicho esto — los engranajes del discurso formal escrito.",
        "objectives": [
            "Emplear conectores avanzados de adición, contraste, causa-consecuencia y cierre en textos formales.",
            "Elegir el conector adecuado según la relación lógica exacta entre dos ideas.",
            "Estructurar un párrafo argumentativo breve usando una secuencia coherente de conectores.",
        ],
        "content": {
            "intro": "Un texto de nivel C1 se distingue menos por el vocabulario aislado que por la precisión con la que enlaza sus ideas mediante conectores.",
            "explanation": "<p>Más allá de \"y\", \"pero\" y \"porque\", el español académico y formal dispone de un repertorio amplio de conectores: de adición (<em>asimismo, además, por otra parte</em>), de contraste (<em>no obstante, sin embargo, con todo</em>), de causa-consecuencia (<em>dado que, por consiguiente, de ahí que</em> — este último exige subjuntivo) y de cierre o recapitulación (<em>en última instancia, en definitiva, dicho esto</em>). Cada uno marca una relación lógica precisa; usarlos correctamente evita repetir siempre las mismas palabras y hace el argumento más fácil de seguir.</p><p>\"Cabe destacar/señalar/mencionar\" introduce un dato que el autor considera relevante dentro del argumento, mientras que \"dicho esto\" marca una transición hacia una idea que matiza o contrasta con lo dicho justo antes.</p>",
            "rules": [
                {"heading": "a) Adición", "body": "<p>asimismo, además, por otra parte, cabe añadir: <em>El estudio confirma la hipótesis; asimismo, abre nuevas preguntas.</em></p>"},
                {"heading": "b) Contraste", "body": "<p>no obstante, sin embargo, con todo, aun así: <em>Los resultados son prometedores; no obstante, se necesita más investigación.</em></p>"},
                {"heading": "c) Causa-consecuencia", "body": "<p>dado que, puesto que (causa); por consiguiente, de ahí que + subjuntivo (consecuencia): <em>De ahí que sea necesario revisar el plan.</em></p>"},
                {"heading": "d) Cierre y recapitulación", "body": "<p>en última instancia, en definitiva, dicho esto, cabe concluir que: <em>Dicho esto, conviene matizar la conclusión anterior.</em></p>"},
            ],
            "examples": [
                "El proyecto cumplió los plazos; asimismo, se mantuvo dentro del presupuesto.",
                "Los datos son claros; sin embargo, conviene interpretarlos con cautela.",
                "Dado que los recursos son limitados, hay que priorizar.",
                "El error fue evidente, de ahí que se revisara todo el protocolo.",
                "Cabe destacar que ningún participante abandonó el estudio.",
                "En última instancia, la decisión depende de la dirección.",
                "Dicho esto, no conviene descartar otras alternativas.",
                "En definitiva, los beneficios superan a los riesgos.",
            ],
            "commonMistakes": [
                {"wrong": "De ahí que es necesario revisar el plan.", "right": "De ahí que sea necesario revisar el plan.", "why": "\"De ahí que\" es una de las pocas expresiones consecutivas que exige subjuntivo en la cláusula que introduce."},
                {"wrong": "Usar \"sin embargo\" para añadir información en vez de contrastarla.", "right": "Usar \"asimismo/además\" para añadir, y reservar \"sin embargo\" para el contraste real.", "why": "Confundir conectores de adición y de contraste invierte la relación lógica que el lector espera entre las dos ideas."},
                {"wrong": "Cabe destacar que, no obstante, el estudio tiene limitaciones.", "right": "Cabe destacar que el estudio tiene limitaciones.", "why": "Acumular varios conectores con funciones parecidas en la misma frase resulta redundante y confunde la relación lógica que se quiere marcar."},
            ],
        },
        "exercises": [
            {"id": "c1l6-mc", "type": "multiple-choice", "title": "Elige el Conector Correcto",
             "items": [
                {"id": "c1l6i1", "prompt": "\"El estudio confirma la hipótesis; ___, abre nuevas líneas de investigación.\" (añadir información)", "options": ["sin embargo", "asimismo", "por consiguiente"], "answerIndex": 1, "explanation": "Asimismo introduce una idea adicional, no un contraste ni una consecuencia."},
                {"id": "c1l6i2", "prompt": "\"Los resultados son buenos; ___, el tamaño de la muestra es pequeño.\" (contrastar)", "options": ["además", "sin embargo", "de ahí que"], "answerIndex": 1, "explanation": "Sin embargo marca un contraste con la idea anterior."},
                {"id": "c1l6i3", "prompt": "\"El sistema falló varias veces, ___ se decidiera reemplazarlo por completo.\" (consecuencia, con subjuntivo)", "options": ["por consiguiente", "de ahí que", "dado que"], "answerIndex": 1, "explanation": "\"De ahí que\" introduce una consecuencia y exige subjuntivo en la cláusula siguiente."},
                {"id": "c1l6i4", "prompt": "\"___, conviene matizar lo dicho anteriormente.\" (transición hacia una idea que matiza lo previo)", "options": ["Dicho esto", "Por otra parte", "Dado que"], "answerIndex": 0, "explanation": "\"Dicho esto\" marca una transición hacia una idea que matiza o contrasta con lo anterior."},
             ]},
            {"id": "c1l6-fill", "type": "fill-blank", "title": "Completa con el Conector Adecuado",
             "items": [
                {"id": "c1l6i5", "prompt": "___ los recursos son limitados, hay que priorizar las tareas más urgentes.", "answers": [["Dado que", "Puesto que"]], "options": ["Dado que", "Sin embargo", "En definitiva"], "explanation": "Conector de causa."},
                {"id": "c1l6i6", "prompt": "Cabe ___ que ningún participante abandonó el estudio.", "answers": [["destacar", "señalar", "mencionar"]], "options": ["destacar", "concluir", "añadir"], "explanation": "\"Cabe destacar/señalar/mencionar que\" introduce un dato relevante."},
                {"id": "c1l6i7", "prompt": "El costo aumentó; ___, se revisó todo el presupuesto.", "answers": [["por consiguiente", "de ahí que"]], "options": ["por consiguiente", "asimismo", "no obstante"], "explanation": "Conector de consecuencia."},
             ]},
            {"id": "c1l6-matching", "type": "matching", "title": "Relaciona el Conector con su Función",
             "items": [
                {"id": "c1l6i8", "prompt": "Relaciona cada conector con la función que cumple en un texto formal.", "pairs": [
                    {"left": "asimismo", "right": "Adición"},
                    {"left": "no obstante", "right": "Contraste"},
                    {"left": "de ahí que", "right": "Consecuencia (exige subjuntivo)"},
                    {"left": "en última instancia", "right": "Cierre o recapitulación"},
                ], "explanation": "Cada conector marca una relación lógica precisa entre dos ideas del texto."},
             ]},
        ],
        "summary": [
            "El repertorio de conectores formales incluye adición (asimismo), contraste (no obstante), causa-consecuencia (dado que, de ahí que) y cierre (en última instancia, dicho esto).",
            "\"De ahí que\" es una de las pocas expresiones consecutivas que exige subjuntivo en la cláusula que introduce.",
            "Elegir el conector según la relación lógica exacta, y no acumular varios con la misma función, hace el argumento más claro.",
        ],
    },
    {
        "id": "c1-perifrasis-verbales-avanzadas",
        "level": "C1", "unit": "1", "order": 7, "skill": "grammar", "strand": "perifrasis",
        "title": "Perífrasis Verbales Avanzadas",
        "subtitle": "Venir + gerundio, dejar de, echar a, ponerse a — matices de inicio, proceso y fin de una acción.",
        "objectives": [
            "Reconocer el matiz aspectual (inicio, desarrollo o fin de una acción) de distintas perífrasis verbales avanzadas.",
            "Usar correctamente perífrasis incoativas (echar a, ponerse a, romper a) y terminativas (dejar de, acabar de, llegar a).",
            "Distinguir venir + gerundio de llevar + gerundio y estar + gerundio.",
        ],
        "content": {
            "intro": "Más allá de estar + gerundio, el español dispone de un conjunto rico de perífrasis verbales que precisan si una acción está empezando, en curso, terminando o alcanzando un resultado.",
            "explanation": "<p>Las perífrasis incoativas marcan el inicio de una acción, a menudo de forma súbita o inesperada: <em>ponerse a</em> (general), <em>echar a</em> (con verbos de movimiento: echar a correr, echar a reír), <em>romper a</em> (más brusco, con llorar/reír: romper a llorar). Las perífrasis terminativas marcan el final o el resultado: <em>dejar de + infinitivo</em> (interrupción: dejar de fumar), <em>acabar de + infinitivo</em> (pasado reciente: acabo de llegar), <em>llegar a + infinitivo</em> (alcanzar un grado o resultado: llegó a ser director).</p><p><em>Venir + gerundio</em> describe un proceso que se desarrolla de forma progresiva desde el pasado hasta el presente, a menudo con matiz de acumulación: <em>Vengo diciéndotelo desde hace meses.</em> Se diferencia de <em>llevar + gerundio</em>, que enfatiza la duración medida (<em>Llevo dos años estudiando español</em>), y de <em>estar + gerundio</em>, que describe una acción puntual en curso ahora mismo.</p>",
            "rules": [
                {"heading": "a) Incoativas", "body": "<p>ponerse a (neutra), echar a (movimiento: echar a andar/correr), romper a (brusca, con llorar/reír).</p>"},
                {"heading": "b) Terminativas", "body": "<p>dejar de (interrupción), acabar de (pasado inmediato), llegar a (resultado alcanzado, a veces inesperado).</p>"},
                {"heading": "c) Venir + gerundio", "body": "<p>Proceso acumulativo desde el pasado hasta ahora, con frecuencia repetido o insistente: <em>El precio viene subiendo desde enero.</em></p>"},
                {"heading": "d) Venir/llevar/estar + gerundio", "body": "<p>Llevar mide duración exacta; estar marca el presente puntual; venir enfatiza el desarrollo progresivo y a menudo insistente del proceso.</p>"},
            ],
            "examples": [
                "Al ver la sorpresa, se echó a reír sin poder controlarse.",
                "Después del accidente, dejó de conducir de noche.",
                "Acabamos de recibir la confirmación del vuelo.",
                "Con los años, llegó a convertirse en un referente del sector.",
                "Los precios vienen subiendo desde hace varios meses.",
                "Se puso a llover justo cuando salimos de casa.",
                "Llevo tres horas esperando una respuesta.",
                "El niño rompió a llorar al ver que se había roto el juguete.",
            ],
            "commonMistakes": [
                {"wrong": "Se echó a llover de repente.", "right": "Se puso a llover de repente.", "why": "\"Echar a\" se combina sobre todo con verbos de movimiento (correr, andar, volar); con fenómenos como llover se prefiere \"ponerse a\"."},
                {"wrong": "Vengo a decírtelo desde hace meses.", "right": "Vengo diciéndotelo desde hace meses.", "why": "El matiz de proceso acumulativo requiere el gerundio, no \"a + infinitivo\", que es una perífrasis distinta con otro significado."},
                {"wrong": "Dejé fumar hace un año.", "right": "Dejé de fumar hace un año.", "why": "\"Dejar de + infinitivo\" requiere obligatoriamente la preposición \"de\"; omitirla es un error frecuente."},
            ],
        },
        "exercises": [
            {"id": "c1l7-fill", "type": "fill-blank", "title": "Completa con la Perífrasis Correcta",
             "items": [
                {"id": "c1l7i1", "prompt": "Al escuchar la broma, ___ (echar a) reír todos a la vez.", "answers": [["se echaron a"]], "options": ["se echaron a", "se rompieron a", "se pusieron"], "explanation": "Echar a + infinitivo, con un verbo de movimiento/reacción súbita."},
                {"id": "c1l7i2", "prompt": "___ (acabar de) llegar cuando empezó a sonar el teléfono.", "answers": [["Acababa de", "Acabábamos de"]], "options": ["Acababa de", "Dejaba de", "Venía de"], "explanation": "Acabar de + infinitivo expresa pasado reciente."},
                {"id": "c1l7i3", "prompt": "El precio del alquiler ___ (venir) subiendo desde hace dos años.", "answers": [["viene"]], "options": ["viene", "lleva", "está"], "explanation": "Venir + gerundio marca un proceso acumulativo y progresivo."},
                {"id": "c1l7i4", "prompt": "___ (dejar) fumar el año pasado y se siente mucho mejor.", "answers": [["Dejó de"]], "options": ["Dejó de", "Dejó", "Acabó"], "explanation": "Dejar de + infinitivo exige la preposición \"de\"."},
             ]},
            {"id": "c1l7-mc", "type": "multiple-choice", "title": "Elige la Perífrasis Correcta",
             "items": [
                {"id": "c1l7i5", "prompt": "\"Después de años de esfuerzo, ___ ser directora de la empresa.\"", "options": ["llegó a", "dejó de", "acabó de"], "answerIndex": 0, "explanation": "\"Llegar a + infinitivo\" expresa alcanzar un resultado o un grado, a veces inesperado."},
                {"id": "c1l7i6", "prompt": "\"___ tres años trabajando en el mismo proyecto.\" (énfasis en la duración exacta)", "options": ["Vengo", "Llevo", "Estoy"], "answerIndex": 1, "explanation": "\"Llevar + gerundio\" enfatiza la duración medida de una acción."},
                {"id": "c1l7i7", "prompt": "\"Justo cuando salíamos, ___ llover con fuerza.\"", "options": ["se echó a", "se puso a", "acabó de"], "answerIndex": 1, "explanation": "\"Ponerse a\" es la perífrasis incoativa general, apta para fenómenos meteorológicos."},
                {"id": "c1l7i8", "prompt": "\"El niño ___ llorar al caerse de la bicicleta.\" (inicio brusco)", "options": ["rompió a", "vino a", "acabó de"], "answerIndex": 0, "explanation": "\"Romper a\" marca un inicio brusco, típico con llorar y reír."},
             ]},
            {"id": "c1l7-correction", "type": "correction", "title": "Corrige la Perífrasis",
             "items": [
                {"id": "c1l7i9", "incorrect": "Dejé fumar hace dos años.", "answer": ["Dejé de fumar hace dos años."], "explanation": "\"Dejar de + infinitivo\" requiere obligatoriamente la preposición \"de\"."},
                {"id": "c1l7i10", "incorrect": "Vengo a decírselo desde hace semanas, pero no me escucha.", "answer": ["Vengo diciéndoselo desde hace semanas, pero no me escucha."], "explanation": "El proceso acumulativo requiere gerundio, no \"a + infinitivo\"."},
                {"id": "c1l7i11", "incorrect": "Se echó a llover apenas salimos de casa.", "answer": ["Se puso a llover apenas salimos de casa."], "explanation": "\"Echar a\" se usa con verbos de movimiento; con fenómenos meteorológicos se prefiere \"ponerse a\"."},
             ]},
        ],
        "summary": [
            "Las perífrasis incoativas (ponerse a, echar a, romper a) marcan el inicio de una acción, con distintos matices de brusquedad y contexto.",
            "Las perífrasis terminativas (dejar de, acabar de, llegar a) marcan la interrupción, el pasado reciente o el resultado alcanzado.",
            "Venir + gerundio enfatiza un proceso acumulativo desde el pasado, distinto de la duración medida de llevar + gerundio y del presente puntual de estar + gerundio.",
        ],
    },
    {
        "id": "c1-voseo-ustedeo-y-variacion-dialectal",
        "level": "C1", "unit": "1", "order": 8, "skill": "functional", "strand": "variacion-dialectal",
        "title": "Voseo, Ustedeo y Variación Dialectal Hispanoamericana",
        "subtitle": "Cómo cambia el trato entre tú, vos y usted según el país, y por qué toda América usa \"ustedes\" donde España usa \"vosotros\".",
        "objectives": [
            "Reconocer las formas verbales propias del voseo rioplatense y centroamericano frente al tuteo.",
            "Identificar en qué países y contextos predomina el voseo, el tuteo o el ustedeo generalizado.",
            "Explicar por qué \"vosotros\" prácticamente no se usa en América Latina y qué forma ocupa su lugar.",
        ],
        "content": {
            "intro": "El español no tiene un único sistema de tratamiento: la elección entre tú, vos y usted varía de país en país, e incluso dentro de un mismo país según la región y el contexto social.",
            "explanation": "<p>El <strong>voseo</strong> — el uso de \"vos\" en lugar de \"tú\" — es la norma en Argentina, Uruguay, Paraguay y buena parte de Centroamérica (Costa Rica, Nicaragua, y con distinta intensidad en otros países), y convive con el tuteo en varias regiones de Colombia, Venezuela, Chile y Bolivia, entre otras. El voseo rioplatense conjuga el presente con el acento desplazado a la última sílaba: <em>vos hablás, vos comés, vos vivís</em> (frente a tú hablas, tú comes, tú vives), y usa el imperativo <em>hablá, comé, viví</em>. Los pronombres de objeto y posesivo siguen siendo los de \"tú\" (te, tu, tuyo); solo cambian el pronombre sujeto y ciertas formas verbales.</p><p>El <strong>ustedeo</strong> — usar \"usted\" incluso en contextos familiares o informales — es habitual en buena parte de Colombia, Costa Rica y algunas zonas de Centroamérica, donde no siempre marca distancia, sino a veces cercanía o cariño, al contrario de lo que suele ocurrir en España. Un rasgo compartido por todo el español americano, frente a España, es que <strong>\"vosotros\" prácticamente no se usa</strong>: en toda América Latina, \"ustedes\" cubre tanto el plural formal como el informal de \"tú/vos\", con la conjugación de tercera persona del plural (<em>ustedes hablan, ustedes comen</em>) incluso al dirigirse a un grupo de amigos.</p>",
            "rules": [
                {"heading": "a) Voseo rioplatense (Argentina, Uruguay, Paraguay)", "body": "<p>vos + presente con acento en la última sílaba (vos hablás, vos tenés, vos podés) e imperativo (hablá, tené, pedí).</p>"},
                {"heading": "b) Voseo centroamericano", "body": "<p>Presente similar (vos hablás/comés), con variantes según el país; convive con el tuteo en el habla urbana de algunos países.</p>"},
                {"heading": "c) Ustedeo", "body": "<p>Uso de \"usted\" en contextos informales, especialmente en Colombia y Costa Rica, sin implicar necesariamente distancia o formalidad, a diferencia del uso peninsular.</p>"},
                {"heading": "d) Ustedes universal en América", "body": "<p>Sustituye por completo a \"vosotros\", tanto para el plural formal como informal, con conjugación de tercera persona (ustedes son, ustedes tienen).</p>"},
            ],
            "examples": [
                "Vos sabés que siempre podés contar conmigo.",
                "¿Vos querés que te ayude con eso?",
                "Tú sabes que siempre puedes contar conmigo.",
                "¿Usted necesita algo más?",
                "Chicos, ¿ustedes vienen a la fiesta?",
                "Vosotros venís a la fiesta, ¿no?",
                "En Argentina se dice \"vení acá\"; en España, \"ven aquí\".",
                "Ninguna forma es más correcta que otra: son variedades igualmente válidas del español.",
            ],
            "commonMistakes": [
                {"wrong": "Pensar que el voseo es una forma incorrecta o rural del tuteo.", "right": "Reconocer el voseo como una norma culta y plenamente válida en varios países.", "why": "El voseo rioplatense y centroamericano es la forma estándar y prestigiosa en sus países, no una desviación del tuteo."},
                {"wrong": "Vosotros tenéis razón. (en un contexto hablado latinoamericano)", "right": "Ustedes tienen razón.", "why": "En el español de América, \"vosotros\" prácticamente no se usa en el habla cotidiana; su lugar lo ocupa siempre \"ustedes\", incluso en contextos informales."},
                {"wrong": "Vos hablas muy bien español.", "right": "Vos hablás muy bien español.", "why": "El voseo rioplatense tiene su propia conjugación en presente e imperativo, distinta de la del tuteo; no consiste solo en cambiar el pronombre."},
            ],
        },
        "exercises": [
            {"id": "c1l8-tf", "type": "true-false", "title": "Verdadero o Falso",
             "items": [
                {"id": "c1l8i1", "statement": "En Argentina, el voseo es la forma estándar y prestigiosa de tratamiento informal.", "answer": True, "explanation": "El voseo rioplatense es la norma culta en Argentina, Uruguay y Paraguay, no una desviación del tuteo."},
                {"id": "c1l8i2", "statement": "En toda América Latina se usa \"vosotros\" para el plural informal, igual que en España.", "answer": False, "explanation": "En América Latina, \"ustedes\" sustituye por completo a \"vosotros\", tanto en contextos formales como informales."},
                {"id": "c1l8i3", "statement": "En algunos países como Colombia, usar \"usted\" puede expresar cercanía o cariño, no solo distancia.", "answer": True, "explanation": "El ustedeo en ciertas regiones colombianas no implica necesariamente formalidad, a diferencia del uso peninsular."},
                {"id": "c1l8i4", "statement": "El voseo cambia únicamente el pronombre sujeto, sin afectar a la conjugación verbal.", "answer": False, "explanation": "El voseo rioplatense tiene su propia conjugación en presente e imperativo, con el acento desplazado a la última sílaba."},
                {"id": "c1l8i5", "statement": "El uso de \"vos\" en vez de \"tú\" está limitado a Argentina y no aparece en ningún otro país.", "answer": False, "explanation": "El voseo también es la norma en Uruguay y Paraguay, y convive con el tuteo en gran parte de Centroamérica."},
             ]},
            {"id": "c1l8-mc", "type": "multiple-choice", "title": "Elige la Forma Correcta",
             "items": [
                {"id": "c1l8i6", "prompt": "¿Cuál es la conjugación de \"hablar\" en voseo rioplatense, presente, segunda persona?", "options": ["hablas", "hablás", "habláis"], "answerIndex": 1, "explanation": "El voseo rioplatense desplaza el acento a la última sílaba: vos hablás."},
                {"id": "c1l8i7", "prompt": "¿Qué forma sustituye a \"vosotros\" en todo el español de América?", "options": ["ustedes", "vos", "ellos"], "answerIndex": 0, "explanation": "\"Ustedes\" cubre el plural formal e informal en toda América Latina."},
                {"id": "c1l8i8", "prompt": "¿Cuál es el imperativo de \"comer\" en voseo rioplatense?", "options": ["come", "comé", "comed"], "answerIndex": 1, "explanation": "El imperativo del voseo rioplatense también desplaza el acento a la última sílaba."},
                {"id": "c1l8i9", "prompt": "El pronombre de objeto directo que corresponde a \"vos\" es...", "options": ["os", "te", "le"], "answerIndex": 1, "explanation": "El voseo conserva los pronombres de objeto y posesivo de \"tú\" (te, tu, tuyo); solo cambian el pronombre sujeto y ciertas formas verbales."},
             ]},
            {"id": "c1l8-matching", "type": "matching", "title": "Relaciona el País con el Trato Predominante",
             "items": [
                {"id": "c1l8i10", "prompt": "Relaciona cada país o región con el trato que predomina en su habla cotidiana.", "pairs": [
                    {"left": "Argentina", "right": "Voseo rioplatense (vos hablás)"},
                    {"left": "España", "right": "Tuteo y vosotros en el plural informal"},
                    {"left": "México", "right": "Tuteo, con ustedes como único plural"},
                    {"left": "Costa Rica", "right": "Convivencia de voseo y ustedeo cercano"},
                ], "explanation": "El trato varía según el país; ninguna variedad es más correcta que otra, todas son normas válidas del español."},
             ]},
        ],
        "summary": [
            "El voseo (vos hablás, vos tenés) es la norma culta y prestigiosa en Argentina, Uruguay, Paraguay y buena parte de Centroamérica, no una forma incorrecta del tuteo.",
            "El ustedeo, frecuente en Colombia y Costa Rica, puede expresar cercanía en vez de distancia formal.",
            "En toda América Latina, \"ustedes\" sustituye por completo a \"vosotros\", que prácticamente no se usa fuera de España.",
        ],
    },
    {
        "id": "c1-ironia-atenuacion-y-cortesia",
        "level": "C1", "unit": "1", "order": 9, "skill": "functional", "strand": "pragmatica",
        "title": "Ironía, Atenuación y Cortesía Lingüística",
        "subtitle": "Podría ser que..., no sé si..., más bien... — cómo suavizar una afirmación sin perder claridad.",
        "objectives": [
            "Usar recursos de atenuación (podría ser que, no sé si, más bien, en cierto modo) para suavizar una opinión o una crítica.",
            "Reconocer marcas de ironía en el discurso oral y escrito y su función social.",
            "Elegir el grado de cortesía adecuado al pedir, corregir o disentir de alguien en distintos contextos.",
        ],
        "content": {
            "intro": "Hablar con fluidez incluye saber cuándo y cómo suavizar lo que se dice: el español dispone de recursos específicos para atenuar una crítica, expresar duda con tacto o pedir algo sin sonar brusco.",
            "explanation": "<p>La atenuación reduce el impacto de una afirmación, una petición o una crítica sin cambiar su contenido esencial: expresiones como <em>podría ser que, no sé si, quizá sería mejor, más bien, en cierto modo, hasta cierto punto</em> introducen un margen de duda o suavizan el tono. El condicional también cumple esta función cortés: <em>¿Podrías cerrar la ventana?</em> suena más suave que el imperativo directo \"Cierra la ventana\".</p><p>La ironía, por su parte, dice literalmente lo contrario de lo que se quiere comunicar, apoyándose en el tono, el contexto compartido y a veces en marcadores como \"menudo/vaya\" (<em>¡Menuda ayuda!</em>, dicho cuando alguien no ayudó en absoluto). Reconocerla exige atender al contexto, no solo a las palabras.</p>",
            "rules": [
                {"heading": "a) Atenuadores de opinión", "body": "<p>podría ser que, no sé si, hasta cierto punto, en cierto modo, más bien: <em>No sé si es la mejor opción, pero podría funcionar.</em></p>"},
                {"heading": "b) Peticiones corteses con condicional", "body": "<p>¿Podrías...?, ¿Te importaría...?, ¿Sería posible...? — mucho más suaves que el imperativo directo.</p>"},
                {"heading": "c) Atenuar una crítica", "body": "<p>\"Quizá convendría revisar esto\" en lugar de \"Esto está mal.\"</p>"},
                {"heading": "d) Marcadores de ironía", "body": "<p>\"vaya/menudo + sustantivo\" (¡Vaya suerte la mía!, dicho con mala suerte real), y afirmaciones exageradas cuyo contexto revela lo contrario.</p>"},
            ],
            "examples": [
                "No sé si esta es la mejor manera de plantearlo, pero lo intentaré.",
                "Podría ser que me esté equivocando, aunque no lo creo.",
                "¿Te importaría bajar un poco el volumen?",
                "Quizá convendría revisar los números antes de enviarlos.",
                "Más bien creo que el problema está en otra parte.",
                "¡Menuda suerte la mía, otra vez lloviendo el día de la excursión!",
                "¿Sería posible posponer la reunión unos minutos?",
                "Hasta cierto punto tienes razón, aunque yo lo vería de otra forma.",
            ],
            "commonMistakes": [
                {"wrong": "Cierra la ventana. (a un desconocido, sin ningún atenuante)", "right": "¿Podrías cerrar la ventana, por favor?", "why": "El imperativo directo sin ningún recurso de cortesía puede sonar brusco fuera del ámbito de mucha confianza; el condicional o \"por favor\" suavizan la petición."},
                {"wrong": "Interpretar \"¡Menuda ayuda!\" siempre de forma literal, como un elogio real.", "right": "Reconocer, según el tono y el contexto, que a menudo es irónico y significa justo lo contrario.", "why": "La ironía se identifica por el contexto y la entonación, no por el significado literal de las palabras."},
                {"wrong": "No sé si tal vez podría ser que quizá funcionara.", "right": "No sé si podría funcionar.", "why": "Acumular demasiados atenuadores en la misma frase diluye el mensaje hasta volverlo ambiguo, lo contrario de la cortesía eficaz."},
            ],
        },
        "exercises": [
            {"id": "c1l9-mc", "type": "multiple-choice", "title": "Elige la Opción Más Cortés",
             "items": [
                {"id": "c1l9i1", "prompt": "Quieres pedirle a un compañero que baje la voz. ¿Qué opción es más cortés?", "options": ["Baja la voz.", "¿Te importaría bajar un poco la voz?", "Silencio."], "answerIndex": 1, "explanation": "El condicional y la pregunta suavizan considerablemente la petición."},
                {"id": "c1l9i2", "prompt": "Quieres señalar un error sin sonar duro. Elige la opción más atenuada.", "options": ["Esto está mal.", "Quizá convendría revisar esto.", "Esto es un desastre."], "answerIndex": 1, "explanation": "\"Quizá convendría\" introduce la crítica con un margen de duda que la suaviza."},
                {"id": "c1l9i3", "prompt": "\"¡Vaya suerte la mía!\" dicho después de perder el autobús es un ejemplo de...", "options": ["cortesía", "ironía", "nominalización"], "answerIndex": 1, "explanation": "La expresión dice lo contrario de lo que se quiere comunicar; el contexto revela que en realidad tuvo mala suerte."},
                {"id": "c1l9i4", "prompt": "¿Cuál de estas peticiones es la más directa, sin ningún atenuante?", "options": ["¿Sería posible que me ayudaras?", "¿Te importaría ayudarme?", "Ayúdame."], "answerIndex": 2, "explanation": "El imperativo sin ningún recurso de cortesía es la forma más directa de las tres."},
             ]},
            {"id": "c1l9-fill", "type": "fill-blank", "title": "Completa con el Atenuador Adecuado",
             "items": [
                {"id": "c1l9i5", "prompt": "___ esta sea la mejor solución, pero al menos vale la pena intentarlo.", "answers": [["No sé si", "Podría ser que"]], "options": ["No sé si", "Sin duda", "Claramente"], "explanation": "Atenuador de opinión que introduce un margen de duda."},
                {"id": "c1l9i6", "prompt": "¿___ posible cambiar la reunión para mañana?", "answers": [["Sería"]], "options": ["Sería", "Es", "Fue"], "explanation": "El condicional \"sería\" suaviza la petición."},
                {"id": "c1l9i7", "prompt": "___ cierto punto entiendo tu postura, aunque no la comparto del todo.", "answers": [["Hasta"]], "options": ["Hasta", "Desde", "Sobre"], "explanation": "\"Hasta cierto punto\" atenúa una afirmación de acuerdo parcial."},
             ]},
            {"id": "c1l9-correction", "type": "correction", "title": "Suaviza la Frase",
             "items": [
                {"id": "c1l9i8", "incorrect": "Estás equivocado.", "answer": ["Podría ser que estés equivocado.", "No sé si tienes toda la razón en esto."], "explanation": "Un atenuador reduce el impacto directo de una afirmación que podría sonar como una acusación."},
                {"id": "c1l9i9", "incorrect": "Dame el informe ahora mismo.", "answer": ["¿Podrías darme el informe, por favor?", "¿Te importaría pasarme el informe cuando puedas?"], "explanation": "El condicional y \"por favor\" transforman una orden directa en una petición cortés."},
                {"id": "c1l9i10", "incorrect": "Este plan es un desastre.", "answer": ["Quizá convendría revisar este plan.", "Más bien creo que este plan tiene algunos problemas."], "explanation": "Atenuar una crítica dura la hace más fácil de aceptar sin perder el mensaje central."},
             ]},
        ],
        "summary": [
            "Los atenuadores (podría ser que, no sé si, hasta cierto punto) suavizan una opinión o una crítica sin cambiar su contenido esencial.",
            "El condicional en las peticiones (¿podrías...?, ¿te importaría...?) es mucho más cortés que el imperativo directo.",
            "La ironía comunica lo contrario de lo dicho literalmente, y se reconoce por el tono y el contexto, no por las palabras en sí.",
        ],
    },
    {
        "id": "c1-espanol-academico-y-profesional",
        "level": "C1", "unit": "1", "order": 10, "skill": "writing", "strand": "profesional",
        "title": "Español para Fines Específicos: Registro Académico y Profesional",
        "subtitle": "Vocabulario y estructuras para informes, correos formales y presentaciones.",
        "objectives": [
            "Redactar un correo electrónico formal con las fórmulas de apertura, cuerpo y cierre adecuadas.",
            "Usar el vocabulario y las estructuras propias de un informe en registro objetivo.",
            "Emplear fórmulas típicas de una presentación oral formal para introducir, desarrollar y cerrar un tema.",
        ],
        "content": {
            "intro": "El español profesional exige un repertorio propio de fórmulas fijas y de estructuras textuales que van más allá de la gramática general del idioma.",
            "explanation": "<p>Un correo formal sigue una estructura predecible: fórmula de apertura (<em>Estimado/a Sr./Sra. [Apellido]:, En relación con...</em>), cuerpo claro y directo, y cierre convencional (<em>Quedo a la espera de su respuesta. Atentamente,</em>). Un informe organiza la información en secciones reconocibles — introducción, desarrollo o análisis, y conclusión — con un lenguaje objetivo que evita la primera persona cuando es posible (<em>se concluye que...</em> en vez de <em>yo concluyo que...</em>).</p><p>Una presentación oral formal necesita fórmulas propias para guiar a la audiencia: para introducir el tema (<em>El objetivo de esta presentación es...</em>), para pasar de un punto a otro (<em>Pasando al siguiente punto..., Esto nos lleva a...</em>) y para cerrar (<em>A modo de conclusión..., Para resumir...</em>). Dominar estas fórmulas fijas es tan importante como la gramática para sonar profesional en español.</p>",
            "rules": [
                {"heading": "a) Correo formal — apertura y cierre", "body": "<p>Apertura: \"Estimado/a Sr./Sra. [Apellido]:\", \"En referencia a su mensaje anterior...\". Cierre: \"Quedo a su disposición para cualquier consulta.\", \"Atentamente / Un cordial saludo.\"</p>"},
                {"heading": "b) Informe — estructura objetiva", "body": "<p>\"El presente informe tiene como objetivo...\", \"A continuación se analizan los resultados...\", \"En conclusión, se recomienda...\"</p>"},
                {"heading": "c) Presentación oral — transiciones", "body": "<p>\"Antes de continuar, me gustaría destacar...\", \"Esto nos lleva al siguiente punto...\", \"Para finalizar, quisiera resaltar...\"</p>"},
                {"heading": "d) Evitar coloquialismos", "body": "<p>Sustituir \"un montón de\" por \"numerosos/as\"; \"vale\" por \"de acuerdo\"; \"o sea\" por \"es decir\", en estos tres contextos formales.</p>"},
            ],
            "examples": [
                "Estimada Sra. Gómez: Le escribo en relación con la propuesta enviada la semana pasada.",
                "Quedo a la espera de sus comentarios. Atentamente, Renan.",
                "El presente informe analiza los resultados obtenidos durante el primer trimestre.",
                "A continuación se detallan las principales conclusiones del estudio.",
                "El objetivo de esta presentación es exponer los avances del proyecto.",
                "Pasando al siguiente punto, conviene revisar el calendario propuesto.",
                "A modo de conclusión, los datos confirman la viabilidad del plan.",
                "Le agradezco de antemano su atención y quedo pendiente de su respuesta.",
            ],
            "commonMistakes": [
                {"wrong": "Hola, quería preguntarte una cosa... (al inicio de un correo formal a un desconocido)", "right": "Estimado/a [Nombre/Apellido]: Le escribo para...", "why": "Un correo formal exige una fórmula de apertura convencional, no un saludo coloquial reservado para contextos de confianza."},
                {"wrong": "Yo pienso que los resultados están bien. (en un informe)", "right": "Los resultados obtenidos se consideran satisfactorios.", "why": "El registro de un informe prefiere estructuras impersonales u objetivas en lugar de la primera persona, para transmitir mayor neutralidad."},
                {"wrong": "Cerrar un correo formal con \"Besos\" o \"Chao\".", "right": "Cerrar con \"Atentamente\" o \"Un cordial saludo\".", "why": "Las fórmulas de cierre informales no son apropiadas en correspondencia profesional, incluso si el resto del mensaje es cordial."},
            ],
        },
        "exercises": [
            {"id": "c1l10-fill", "type": "fill-blank", "title": "Completa la Fórmula Formal",
             "items": [
                {"id": "c1l10i1", "prompt": "___ Sr. Martínez: Le escribo para solicitar información adicional.", "answers": [["Estimado"]], "options": ["Estimado", "Hola", "Querido"], "explanation": "Fórmula de apertura convencional en un correo formal."},
                {"id": "c1l10i2", "prompt": "Quedo a la ___ de su respuesta.", "answers": [["espera"]], "options": ["espera", "vista", "orden"], "explanation": "\"Quedar a la espera de\" es una fórmula fija de cierre formal."},
                {"id": "c1l10i3", "prompt": "El presente informe tiene como ___ evaluar los resultados del trimestre.", "answers": [["objetivo"]], "options": ["objetivo", "sueño", "gusto"], "explanation": "Fórmula típica de introducción a un informe."},
                {"id": "c1l10i4", "prompt": "___ al siguiente punto, conviene revisar el presupuesto disponible.", "answers": [["Pasando"]], "options": ["Pasando", "Saltando", "Corriendo"], "explanation": "Fórmula de transición típica de una presentación oral formal."},
             ]},
            {"id": "c1l10-mc", "type": "multiple-choice", "title": "Elige la Opción Más Formal",
             "items": [
                {"id": "c1l10i5", "prompt": "¿Cuál es el cierre más apropiado para un correo formal?", "options": ["Chao, nos vemos.", "Atentamente,", "Besos,"], "answerIndex": 1, "explanation": "\"Atentamente\" es la fórmula de cierre estándar en correspondencia profesional."},
                {"id": "c1l10i6", "prompt": "¿Cuál de estas frases es más apropiada para un informe?", "options": ["Yo creo que salió todo bien.", "Se concluye que los objetivos se cumplieron satisfactoriamente.", "Nos fue genial, la verdad."], "answerIndex": 1, "explanation": "El registro de un informe prefiere estructuras impersonales y objetivas."},
                {"id": "c1l10i7", "prompt": "¿Cuál es la forma más formal de decir \"un montón de gente\"?", "options": ["un montón de gente", "numerosas personas", "tela de gente"], "answerIndex": 1, "explanation": "\"Numerosas personas\" es la variante de registro formal."},
                {"id": "c1l10i8", "prompt": "¿Qué fórmula es apropiada para cerrar una presentación oral formal?", "options": ["Bueno, ya está, eso es todo.", "A modo de conclusión, quisiera resaltar los puntos principales.", "Ya, chau, gracias."], "answerIndex": 1, "explanation": "Las fórmulas de cierre de una presentación formal marcan claramente la transición hacia el final."},
             ]},
            {"id": "c1l10-typing", "type": "typing", "title": "Reescribe en Registro Formal",
             "instructions": "Reescribe cada frase coloquial en un registro formal apropiado para un correo o un informe.",
             "items": [
                {"id": "c1l10i9", "prompt": "Reescribe de forma formal: \"Hola, quería preguntarte una cosa sobre el proyecto.\"", "answer": ["Estimado/a: le escribo para consultarle sobre el proyecto.", "Le escribo para realizar una consulta sobre el proyecto."], "explanation": "Un correo formal sustituye el saludo coloquial por una fórmula de apertura convencional."},
                {"id": "c1l10i10", "prompt": "Reescribe de forma formal: \"Creo que hicimos un buen trabajo este trimestre.\"", "answer": ["Se considera que el trabajo realizado durante el trimestre fue satisfactorio.", "Los resultados del trimestre se consideran satisfactorios."], "explanation": "El registro de informe prefiere estructuras objetivas, evitando la primera persona cuando es posible."},
                {"id": "c1l10i11", "prompt": "Reescribe de forma formal: \"Nos vemos, cualquier cosa me avisas.\"", "answer": ["Quedo a su disposición para cualquier consulta. Atentamente.", "Quedo a la espera de sus noticias. Un cordial saludo."], "explanation": "Las despedidas informales se sustituyen por fórmulas de cierre convencionales en correspondencia profesional."},
             ]},
        ],
        "summary": [
            "Un correo formal sigue una estructura fija: apertura convencional, cuerpo claro y una fórmula de cierre reconocible.",
            "Un informe organiza la información en introducción, desarrollo y conclusión, con un lenguaje objetivo que evita la primera persona.",
            "Una presentación oral formal se apoya en fórmulas fijas para introducir, enlazar y cerrar cada punto del discurso.",
        ],
    },
]

# =======================================================================
# EXTRA_EXERCISES — bloques adicionales de práctica (lectura y ordenar
# frases) fusionados en cada lección por id.
# =======================================================================
EXTRA_EXERCISES = {
    "c1-pluscuamperfecto-de-subjuntivo": [
        {"id": "c1x1-reading", "type": "reading-comprehension", "title": "Lectura: Un Arrepentimiento",
         "passage": "<p>Si hubiera sabido lo difícil que sería el examen, habría estudiado mucho más. Ojalá hubiéramos reservado los billetes antes, porque ahora están agotados. Era el mejor concierto que hubiera visto en años, aunque el sonido no fuera perfecto.</p>",
         "items": [
            {"id": "c1x1r1", "prompt": "¿Qué habría hecho la persona si hubiera sabido la dificultad del examen?", "options": ["No presentarse", "Estudiar mucho más", "Pedir ayuda"], "answerIndex": 1, "explanation": "El texto dice: «habría estudiado mucho más»."},
            {"id": "c1x1r2", "prompt": "¿Por qué se lamenta sobre los billetes?", "options": ["Porque eran muy caros", "Porque ahora están agotados", "Porque los perdieron"], "answerIndex": 1, "explanation": "El texto dice: «ahora están agotados»."},
            {"id": "c1x1r3", "prompt": "¿Cómo describe el concierto?", "options": ["El peor que había visto", "El mejor que hubiera visto en años", "Un concierto normal"], "answerIndex": 1, "explanation": "El texto dice: «Era el mejor concierto que hubiera visto en años»."},
            {"id": "c1x1r4", "prompt": "¿El sonido del concierto era perfecto?", "options": ["Sí", "No del todo"], "answerIndex": 1, "explanation": "El texto dice: «aunque el sonido no fuera perfecto»."},
         ]},
        {"id": "c1x1-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x1o1", "prompt": "Ordena las palabras.", "words": ["Si", "hubiera", "estudiado", "más", "habría", "aprobado"], "explanation": "Condicional irreal de pasado: si + pluscuamperfecto de subjuntivo + condicional compuesto."},
            {"id": "c1x1o2", "prompt": "Ordena las palabras.", "words": ["Ojalá", "hubiera", "llegado", "a", "tiempo"], "explanation": "Ojalá + pluscuamperfecto de subjuntivo expresa un arrepentimiento sobre el pasado."},
         ]},
    ],
    "c1-condicionales-complejas": [
        {"id": "c1x2-reading", "type": "reading-comprehension", "title": "Lectura: Cuatro Escenarios",
         "passage": "<p>Si tengo tiempo esta tarde, te ayudo con la mudanza sin problema. Si fuera más paciente, discutiríamos mucho menos. Si me lo hubieras dicho antes, no habría llegado tarde. Si no hubiera aceptado ese trabajo, ahora viviría en otra ciudad.</p>",
         "items": [
            {"id": "c1x2r1", "prompt": "¿Qué tipo de condición es \"Si tengo tiempo esta tarde\"?", "options": ["Real", "Potencial", "Irreal de pasado"], "answerIndex": 0, "explanation": "Presente de indicativo en la prótasis indica una condición real y probable."},
            {"id": "c1x2r2", "prompt": "¿Qué pasaría si la persona fuera más paciente?", "options": ["Discutirían más", "Discutirían menos", "No cambiaría nada"], "answerIndex": 1, "explanation": "El texto dice: «discutiríamos mucho menos»."},
            {"id": "c1x2r3", "prompt": "¿Por qué llegó tarde la persona?", "options": ["Porque no se lo dijeron a tiempo", "Porque se durmió", "Porque el tráfico era denso"], "answerIndex": 0, "explanation": "El texto implica que si se lo hubieran dicho antes, no habría llegado tarde — es decir, no se lo dijeron a tiempo."},
            {"id": "c1x2r4", "prompt": "¿Qué tipo de condicional es la última frase, con prótasis pasada y consecuencia presente?", "options": ["Real", "Potencial pura", "Mixta"], "answerIndex": 2, "explanation": "Prótasis con pluscuamperfecto de subjuntivo y consecuencia con condicional simple: condicional mixta."},
         ]},
        {"id": "c1x2-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x2o1", "prompt": "Ordena las palabras.", "words": ["Si", "estudias", "todos", "los", "días", "aprenderás", "rápido"], "explanation": "Condicional real: si + presente, futuro en la consecuencia."},
            {"id": "c1x2o2", "prompt": "Ordena las palabras.", "words": ["Si", "no", "hubiera", "aceptado", "viviría", "aquí"], "explanation": "Condicional mixta: prótasis pasada, consecuencia en presente con condicional simple."},
         ]},
    ],
    "c1-matices-del-subjuntivo": [
        {"id": "c1x3-reading", "type": "reading-comprehension", "title": "Lectura: Percepciones y Certezas",
         "passage": "<p>No veo que estés realmente listo para este cambio tan grande. No creo que sea tan difícil como parece al principio. Quizá tengas razón sobre el proyecto, aunque no estoy completamente seguro. Es raro que no haya llamado todavía, normalmente es muy puntual.</p>",
         "items": [
            {"id": "c1x3r1", "prompt": "¿Qué percibe la persona sobre el cambio?", "options": ["Que está listo", "Que no está listo", "No dice nada"], "answerIndex": 1, "explanation": "El texto dice: «No veo que estés realmente listo para este cambio»."},
            {"id": "c1x3r2", "prompt": "¿Qué opina sobre la dificultad del proyecto?", "options": ["Que es muy difícil", "Que no es tan difícil", "No tiene opinión"], "answerIndex": 1, "explanation": "El texto dice: «No creo que sea tan difícil como parece»."},
            {"id": "c1x3r3", "prompt": "¿Está completamente seguro de que la otra persona tiene razón?", "options": ["Sí, totalmente", "No del todo"], "answerIndex": 1, "explanation": "El texto dice: «aunque no estoy completamente seguro»."},
            {"id": "c1x3r4", "prompt": "¿Por qué le parece raro que no haya llamado?", "options": ["Porque nunca llama", "Porque normalmente es muy puntual", "Porque está de vacaciones"], "answerIndex": 1, "explanation": "El texto dice: «normalmente es muy puntual»."},
         ]},
        {"id": "c1x3-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x3o1", "prompt": "Ordena las palabras.", "words": ["No", "veo", "que", "esto", "tenga", "sentido"], "explanation": "Negación de percepción + subjuntivo (tenga)."},
            {"id": "c1x3o2", "prompt": "Ordena las palabras.", "words": ["Quizá", "llueva", "esta", "tarde", "no", "estoy", "seguro"], "explanation": "Quizá con subjuntivo expresa más duda que certeza."},
         ]},
    ],
    "c1-construcciones-enfaticas": [
        {"id": "c1x4-reading", "type": "reading-comprehension", "title": "Lectura: Aclarando un Malentendido",
         "passage": "<p>Lo que realmente me molestó fue el tono con el que me hablaste. Es que no tuve tiempo de avisarte antes, lo siento mucho. Lo que pasó fue muy distinto a lo que imaginas. Fue precisamente por eso por lo que decidí llamarte enseguida.</p>",
         "items": [
            {"id": "c1x4r1", "prompt": "¿Qué molestó realmente a la persona?", "options": ["El contenido del mensaje", "El tono con el que le hablaron", "La hora de la llamada"], "answerIndex": 1, "explanation": "El texto dice: «Lo que realmente me molestó fue el tono con el que me hablaste»."},
            {"id": "c1x4r2", "prompt": "¿Por qué no avisó antes?", "options": ["Porque no quiso", "Porque no tuvo tiempo", "Porque se olvidó"], "answerIndex": 1, "explanation": "El texto dice: «Es que no tuve tiempo de avisarte antes»."},
            {"id": "c1x4r3", "prompt": "¿Lo que pasó fue como imaginaba la otra persona?", "options": ["Sí, exactamente", "No, fue muy distinto"], "answerIndex": 1, "explanation": "El texto dice: «Lo que pasó fue muy distinto a lo que imaginas»."},
            {"id": "c1x4r4", "prompt": "¿Por qué decidió llamar enseguida?", "options": ["Por costumbre", "Precisamente por lo que pasó", "Por casualidad"], "answerIndex": 1, "explanation": "El texto termina: «Fue precisamente por eso por lo que decidí llamarte enseguida»."},
         ]},
        {"id": "c1x4-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x4o1", "prompt": "Ordena las palabras.", "words": ["Lo", "que", "necesito", "es", "más", "tiempo"], "explanation": "Construcción enfática: lo que + verbo + es + lo destacado."},
            {"id": "c1x4o2", "prompt": "Ordena las palabras.", "words": ["Es", "que", "no", "pude", "venir", "antes"], "explanation": "Es que + explicación, fórmula típica para justificar algo."},
         ]},
    ],
    "c1-nominalizacion-y-estilo-academico": [
        {"id": "c1x5-reading", "type": "reading-comprehension", "title": "Lectura: Un Resumen Académico",
         "passage": "<p>La implementación de esta política requiere una evaluación cuidadosa de sus consecuencias. El análisis de los datos revela una tendencia clara hacia la digitalización. La reducción del presupuesto podría afectar la calidad de la investigación. Se recomienda la revisión periódica de estos indicadores.</p>",
         "items": [
            {"id": "c1x5r1", "prompt": "¿Qué requiere la implementación de la política?", "options": ["Aprobación inmediata", "Una evaluación cuidadosa", "Más financiamiento"], "answerIndex": 1, "explanation": "El texto dice: «requiere una evaluación cuidadosa de sus consecuencias»."},
            {"id": "c1x5r2", "prompt": "¿Qué tendencia revela el análisis de los datos?", "options": ["Hacia la digitalización", "Hacia la reducción de personal", "Hacia la expansión"], "answerIndex": 0, "explanation": "El texto dice: «revela una tendencia clara hacia la digitalización»."},
            {"id": "c1x5r3", "prompt": "¿Qué podría afectar la calidad de la investigación?", "options": ["El exceso de personal", "La reducción del presupuesto", "La falta de tiempo"], "answerIndex": 1, "explanation": "El texto dice: «La reducción del presupuesto podría afectar la calidad»."},
            {"id": "c1x5r4", "prompt": "¿Qué se recomienda al final?", "options": ["Eliminar los indicadores", "La revisión periódica de los indicadores", "Ignorar los datos"], "answerIndex": 1, "explanation": "El texto termina: «Se recomienda la revisión periódica de estos indicadores»."},
         ]},
        {"id": "c1x5-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x5o1", "prompt": "Ordena las palabras.", "words": ["La", "implementación", "requiere", "más", "recursos"], "explanation": "Nominalización (implementación) como sujeto + verbo + objeto."},
            {"id": "c1x5o2", "prompt": "Ordena las palabras.", "words": ["Se", "recomienda", "la", "revisión", "del", "informe"], "explanation": "Se recomienda + nominalización (revisión) como objeto."},
         ]},
    ],
    "c1-conectores-textuales-avanzados": [
        {"id": "c1x6-reading", "type": "reading-comprehension", "title": "Lectura: Un Argumento Estructurado",
         "passage": "<p>En primer lugar, cabe destacar el impacto positivo de esta medida en la economía local. Asimismo, no cabe duda de que ha generado empleo en la región. No obstante, algunos expertos señalan riesgos a largo plazo. En definitiva, se trata de una decisión con luces y sombras.</p>",
         "items": [
            {"id": "c1x6r1", "prompt": "¿Qué se destaca en primer lugar?", "options": ["El impacto negativo", "El impacto positivo en la economía", "Los riesgos"], "answerIndex": 1, "explanation": "El texto dice: «cabe destacar el impacto positivo de esta medida en la economía local»."},
            {"id": "c1x6r2", "prompt": "¿Qué ha generado la medida, según el texto?", "options": ["Desempleo", "Empleo en la región", "Inflación"], "answerIndex": 1, "explanation": "El texto dice: «ha generado empleo en la región»."},
            {"id": "c1x6r3", "prompt": "¿Qué señalan algunos expertos?", "options": ["Que todo es perfecto", "Riesgos a largo plazo", "Que no hay ningún riesgo"], "answerIndex": 1, "explanation": "El texto dice: «algunos expertos señalan riesgos a largo plazo»."},
            {"id": "c1x6r4", "prompt": "¿Cómo se describe la decisión al final?", "options": ["Completamente positiva", "Con luces y sombras", "Un fracaso total"], "answerIndex": 1, "explanation": "El texto termina: «se trata de una decisión con luces y sombras»."},
         ]},
        {"id": "c1x6-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x6o1", "prompt": "Ordena las palabras.", "words": ["En", "primer", "lugar", "quiero", "agradecer", "a", "todos"], "explanation": "Conector de orden + verbo + objeto."},
            {"id": "c1x6o2", "prompt": "Ordena las palabras.", "words": ["No", "cabe", "duda", "de", "que", "funciona"], "explanation": "Expresión de certeza + de que + indicativo."},
         ]},
    ],
    "c1-perifrasis-verbales-avanzadas": [
        {"id": "c1x7-reading", "type": "reading-comprehension", "title": "Lectura: Un Proceso en Marcha",
         "passage": "<p>Venimos observando esta tendencia desde hace varios meses. El equipo lleva analizados más de mil casos hasta ahora. Debe de haber una razón lógica detrás de este comportamiento. Estamos por terminar la primera fase del estudio.</p>",
         "items": [
            {"id": "c1x7r1", "prompt": "¿Desde cuándo observan esta tendencia?", "options": ["Desde ayer", "Desde hace varios meses", "Desde hace años"], "answerIndex": 1, "explanation": "El texto dice: «Venimos observando esta tendencia desde hace varios meses»."},
            {"id": "c1x7r2", "prompt": "¿Cuántos casos ha analizado el equipo?", "options": ["Cientos", "Más de mil", "Menos de cien"], "answerIndex": 1, "explanation": "El texto dice: «lleva analizados más de mil casos»."},
            {"id": "c1x7r3", "prompt": "¿Qué expresa \"debe de haber una razón\"?", "options": ["Una obligación", "Una suposición", "Una orden"], "answerIndex": 1, "explanation": "Deber de + infinitivo expresa una suposición o probabilidad, no obligación."},
            {"id": "c1x7r4", "prompt": "¿En qué fase está el estudio, según el texto?", "options": ["A punto de terminar la primera fase", "Recién empezado", "Completamente terminado"], "answerIndex": 0, "explanation": "El texto termina: «Estamos por terminar la primera fase del estudio»."},
         ]},
        {"id": "c1x7-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x7o1", "prompt": "Ordena las palabras.", "words": ["Venimos", "trabajando", "en", "esto", "juntos"], "explanation": "Venir + gerundio expresa un proceso progresivo desde el pasado."},
            {"id": "c1x7o2", "prompt": "Ordena las palabras.", "words": ["Debe", "de", "estar", "muy", "cansado", "hoy"], "explanation": "Deber de + infinitivo, suposición sobre un estado presente."},
         ]},
    ],
    "c1-voseo-ustedeo-y-variacion-dialectal": [
        {"id": "c1x8-reading", "type": "reading-comprehension", "title": "Lectura: Variedades del Español",
         "passage": "<p>En Colombia, muchas personas usan \"usted\" incluso con familiares cercanos, un fenómeno llamado ustedeo. En Argentina, el voseo (vos tenés, vos podés) reemplaza casi por completo al tuteo. En España, el vosotros sigue siendo la forma habitual del plural informal, algo que sorprende a muchos hispanohablantes de América.</p>",
         "items": [
            {"id": "c1x8r1", "prompt": "¿Qué es el ustedeo, según el texto?", "options": ["Usar tú con desconocidos", "Usar usted incluso con familiares cercanos", "No usar ningún pronombre"], "answerIndex": 1, "explanation": "El texto dice: «muchas personas usan «usted» incluso con familiares cercanos, un fenómeno llamado ustedeo»."},
            {"id": "c1x8r2", "prompt": "¿Qué reemplaza casi por completo el voseo en Argentina?", "options": ["Al ustedeo", "Al tuteo", "Al vosotros"], "answerIndex": 1, "explanation": "El texto dice: «el voseo... reemplaza casi por completo al tuteo»."},
            {"id": "c1x8r3", "prompt": "¿Dónde sigue siendo habitual el vosotros?", "options": ["En Colombia", "En Argentina", "En España"], "answerIndex": 2, "explanation": "El texto dice: «En España, el vosotros sigue siendo la forma habitual del plural informal»."},
            {"id": "c1x8r4", "prompt": "¿A quién sorprende el uso de vosotros?", "options": ["A los españoles", "A muchos hispanohablantes de América", "A nadie"], "answerIndex": 1, "explanation": "El texto termina: «algo que sorprende a muchos hispanohablantes de América»."},
         ]},
        {"id": "c1x8-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x8o1", "prompt": "Ordena las palabras.", "words": ["Vos", "tenés", "toda", "la", "razón"], "explanation": "Voseo argentino: vos + tener conjugado en voseo (tenés)."},
            {"id": "c1x8o2", "prompt": "Ordena las palabras.", "words": ["Usted", "sabe", "mejor", "que", "nadie"], "explanation": "Ustedeo: usted con verbo en tercera persona, incluso en contexto cercano."},
         ]},
    ],
    "c1-ironia-atenuacion-y-cortesia": [
        {"id": "c1x9-reading", "type": "reading-comprehension", "title": "Lectura: Un Comentario con Doble Sentido",
         "passage": "<p>«¡Qué puntual llegas!», le dijo con una sonrisa, aunque había llegado con una hora de retraso. Cabría considerar otras opciones antes de decidir. Quizás no sea el momento más adecuado para esta conversación. En cierto modo, entiendo tu punto de vista, aunque no lo comparta del todo.</p>",
         "items": [
            {"id": "c1x9r1", "prompt": "¿Qué tono tiene el comentario \"¡Qué puntual llegas!\"?", "options": ["Sincero", "Irónico", "Neutro"], "answerIndex": 1, "explanation": "Dado que la persona llegó con retraso, el comentario es irónico, no literal."},
            {"id": "c1x9r2", "prompt": "¿Qué recomienda la frase \"cabría considerar otras opciones\"?", "options": ["Decidir inmediatamente", "Pensar en otras posibilidades primero", "No hacer nada"], "answerIndex": 1, "explanation": "Cabría considerar es una forma atenuada de sugerir que se piense en alternativas."},
            {"id": "c1x9r3", "prompt": "¿La persona está segura de que es el momento adecuado?", "options": ["Sí, totalmente", "No, lo duda"], "answerIndex": 1, "explanation": "El texto dice: «Quizás no sea el momento más adecuado»."},
            {"id": "c1x9r4", "prompt": "¿Comparte del todo el punto de vista del otro?", "options": ["Sí, completamente", "No del todo"], "answerIndex": 1, "explanation": "El texto termina: «aunque no lo comparta del todo»."},
         ]},
        {"id": "c1x9-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x9o1", "prompt": "Ordena las palabras.", "words": ["Cabría", "reconsiderar", "esta", "parte", "del", "plan"], "explanation": "Cabría + infinitivo, forma atenuada de sugerir una revisión."},
            {"id": "c1x9o2", "prompt": "Ordena las palabras.", "words": ["En", "cierto", "modo", "tienes", "razón"], "explanation": "En cierto modo + indicativo, atenuación de un acuerdo parcial."},
         ]},
    ],
    "c1-espanol-academico-y-profesional": [
        {"id": "c1x10-reading", "type": "reading-comprehension", "title": "Lectura: Un Correo Profesional Formal",
         "passage": "<p>Estimados señores: Por medio de la presente, deseo formalizar mi solicitud de participación en el programa de becas. Adjunto encontrarán la documentación requerida. Quedo a su entera disposición para cualquier aclaración adicional. Sin otro particular, les saluda atentamente.</p>",
         "items": [
            {"id": "c1x10r1", "prompt": "¿Qué desea formalizar la persona?", "options": ["Una queja", "Su solicitud de participación en el programa de becas", "Una renuncia"], "answerIndex": 1, "explanation": "El texto dice: «deseo formalizar mi solicitud de participación en el programa de becas»."},
            {"id": "c1x10r2", "prompt": "¿Qué se adjunta al correo?", "options": ["Una carta de recomendación", "La documentación requerida", "Un currículum"], "answerIndex": 1, "explanation": "El texto dice: «Adjunto encontrarán la documentación requerida»."},
            {"id": "c1x10r3", "prompt": "¿Para qué queda a disposición la persona?", "options": ["Para una entrevista", "Para cualquier aclaración adicional", "Para pagar una cuota"], "answerIndex": 1, "explanation": "El texto dice: «Quedo a su entera disposición para cualquier aclaración adicional»."},
            {"id": "c1x10r4", "prompt": "¿Qué fórmula de cierre usa el correo?", "options": ["Un abrazo", "Sin otro particular, les saluda atentamente", "Hasta pronto"], "answerIndex": 1, "explanation": "El texto termina: «Sin otro particular, les saluda atentamente»."},
         ]},
        {"id": "c1x10-order", "type": "ordering", "title": "Ordena la Frase",
         "items": [
            {"id": "c1x10o1", "prompt": "Ordena las palabras.", "words": ["Por", "medio", "de", "la", "presente", "solicito", "información"], "explanation": "Fórmula formal fija (por medio de la presente) + verbo + objeto."},
            {"id": "c1x10o2", "prompt": "Ordena las palabras.", "words": ["Quedo", "a", "su", "entera", "disposición"], "explanation": "Fórmula de cortesía formal fija, común al cierre de correos profesionales."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
