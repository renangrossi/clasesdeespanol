#!/usr/bin/env python3
"""
Construye levels/{nivel}.html: la página hub de cada nivel del MCER —
resumen, la cuadrícula ordenada de tarjetas de lección, una llamada a la
acción hacia "Ponte a Prueba" y una sección compacta de Vocabulario (dos
tablas de palabras por tema, cada una con ejercicios).

Uso:
    python3 scripts/build_level_pages.py
"""
import json
import sys
from pathlib import Path
from string import ascii_uppercase

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = "../"

LEVEL_META = {
    "Pre-A1": ("Supervivencia", "Primer contacto con el español — el alfabeto, los sonidos, saludos y los primeros verbos para sobrevivir en clase."),
    "A1": ("Principiante", "Frases básicas y expresiones cotidianas para necesidades inmediatas — saludos, género, ser/estar, el presente de indicativo."),
    "A2": ("Elemental", "Intercambios sencillos y directos sobre temas familiares — verbos irregulares, el pretérito indefinido, verbos reflexivos, comparativos."),
    "B1": ("Intermedio", "Español cotidiano e independiente — el imperfecto, pronombres indirectos y combinados, futuro, condicional e imperativo."),
    "B2": ("Intermedio Alto", "Interacción fluida y espontánea — el subjuntivo, oraciones condicionales, estilo indirecto, la voz pasiva."),
    "C1": ("Avanzado", "Lengua flexible y eficaz para la vida profesional y académica — el sistema completo del subjuntivo, registro y conectores."),
    "C2": ("Maestría", "Dominio preciso y matizado del español — sintaxis compleja, registro literario, matices léxicos y la verdadera variedad del idioma."),
}

# Dos temas de vocabulario compactos por nivel: (título del tema, [ (palabra, categoría, significado, ejemplo), ... ])
VOCAB = {
    "Pre-A1": [
        ("Saludos y Cortesía", [
            ("hola / adiós", "expresión", "saludo de llegada / de despedida", "¡Hola! ¿Cómo estás?"),
            ("buenos días", "expresión", "saludo hasta el mediodía", "Buenos días, profesor."),
            ("por favor / gracias", "expresión", "pedir con cortesía / agradecer", "Un café, por favor. Gracias."),
            ("de nada", "expresión", "respuesta a un agradecimiento", "—Gracias. —De nada."),
            ("perdón / disculpe", "expresión", "pedir disculpas con cortesía", "Perdón, ¿dónde está el baño?"),
            ("¿cómo te llamas?", "expresión", "preguntar el nombre", "¿Cómo te llamas? Me llamo Ana."),
            ("mucho gusto", "expresión", "al conocer a alguien", "Mucho gusto, soy Carlos."),
            ("sí / no", "adverbio", "afirmación / negación", "¿Hablas español? Sí, un poco."),
        ]),
        ("Objetos de la Clase", [
            ("el lápiz", "sustantivo", "instrumento para escribir con mina", "Necesito un lápiz para el examen."),
            ("el cuaderno", "sustantivo", "libreta para escribir", "Escribo la tarea en mi cuaderno."),
            ("la mochila", "sustantivo", "bolsa para llevar los libros", "Mi mochila es azul y muy grande."),
            ("la pizarra", "sustantivo", "superficie para escribir en clase", "El profesor escribe en la pizarra."),
            ("el libro", "sustantivo", "material de lectura o estudio", "Este libro de español es muy bueno."),
            ("la silla / la mesa", "sustantivo", "mueble para sentarse / para trabajar", "Pon el libro sobre la mesa."),
            ("la ventana / la puerta", "sustantivo", "abertura para luz / para entrar y salir", "Abre la ventana, por favor."),
            ("el profesor / la profesora", "sustantivo", "persona que enseña", "La profesora explica muy bien."),
        ]),
    ],
    "A1": [
        ("La Familia", [
            ("la madre / la mamá", "sustantivo", "madre", "Mi madre trabaja en un hospital."),
            ("el padre / el papá", "sustantivo", "padre", "Mi padre cocina muy bien."),
            ("el hermano / la hermana", "sustantivo", "hermano/a", "Tengo un hermano mayor."),
            ("los abuelos", "sustantivo", "padres de los padres", "Mis abuelos viven en el campo."),
            ("el hijo / la hija", "sustantivo", "hijo/a", "Tienen dos hijos pequeños."),
            ("el esposo / la esposa", "sustantivo", "marido / mujer", "Mi esposo es profesor."),
            ("casado/a", "adjetivo", "que tiene cónyuge", "¿Estás casada?"),
            ("tener hambre / sed", "expresión", "necesitar comer / beber", "Tengo hambre, ¿comemos?"),
        ]),
        ("La Comida de Cada Día", [
            ("el pan", "sustantivo", "alimento básico de harina", "Compro pan todas las mañanas."),
            ("el agua", "sustantivo", "líquido esencial para vivir", "Quisiera un vaso de agua."),
            ("la fruta", "sustantivo", "alimento vegetal dulce", "Como fruta todos los días."),
            ("la verdura", "sustantivo", "vegetales comestibles", "No me gusta la verdura cocida."),
            ("el queso", "sustantivo", "producto lácteo sólido", "El queso manchego es muy famoso."),
            ("la carne", "sustantivo", "alimento de origen animal", "No como carne los viernes."),
            ("dulce / salado", "adjetivo", "con sabor a azúcar / a sal", "Prefiero lo salado antes que lo dulce."),
            ("el desayuno / la cena", "sustantivo", "primera comida / última comida del día", "El desayuno es la comida más importante."),
        ]),
    ],
    "A2": [
        ("Los Viajes", [
            ("el aeropuerto", "sustantivo", "lugar de despegue y aterrizaje", "Llegamos al aeropuerto con tiempo de sobra."),
            ("el billete / el boleto", "sustantivo", "documento para viajar", "Compré dos boletos para Lima."),
            ("la maleta", "sustantivo", "equipaje para viajar", "Mi maleta pesa demasiado."),
            ("el vuelo", "sustantivo", "trayecto en avión", "El vuelo se canceló por el clima."),
            ("reservar", "verbo", "asegurar un lugar con antelación", "Reservé el hotel por internet."),
            ("salir / llegar", "verbo", "partir de un lugar / arribar a otro", "El tren sale a las nueve."),
            ("el pasaporte", "sustantivo", "documento de identidad para viajar", "¡No olvides el pasaporte!"),
            ("el destino", "sustantivo", "lugar al que se viaja", "Cartagena es nuestro próximo destino."),
        ]),
        ("En el Restaurante", [
            ("el menú / la carta", "sustantivo", "lista de platos disponibles", "¿Puedo ver la carta, por favor?"),
            ("la cuenta", "sustantivo", "el total a pagar", "La cuenta, por favor."),
            ("reservar una mesa", "expresión", "apartar una mesa con antelación", "Reservé una mesa para dos."),
            ("el camarero / la camarera", "sustantivo", "persona que atiende las mesas", "El camarero es muy amable."),
            ("recomendar", "verbo", "sugerir algo a alguien", "¿Qué me recomienda usted?"),
            ("el primer plato / el segundo plato", "sustantivo", "entrada / plato principal", "De primero, quiero la sopa."),
            ("la guarnición", "sustantivo", "acompañamiento de un plato", "Como guarnición, prefiero ensalada."),
            ("la cuenta está mal", "expresión", "hay un error en el cobro", "Disculpe, creo que la cuenta está mal."),
        ]),
    ],
    "B1": [
        ("El Trabajo", [
            ("la entrevista de trabajo", "sustantivo", "reunión para evaluar a un candidato", "Tengo una entrevista de trabajo mañana."),
            ("contratar", "verbo", "dar empleo a alguien", "La empresa contrató a tres personas."),
            ("despedir / renunciar", "verbo", "quitar el empleo / dejar el empleo", "Renunció después de diez años."),
            ("el sueldo", "sustantivo", "pago mensual por un trabajo", "El sueldo subió este año."),
            ("el plazo", "sustantivo", "fecha límite", "El plazo del proyecto es el viernes."),
            ("el/la colega", "sustantivo", "compañero de trabajo", "Mis colegas son muy simpáticos."),
            ("hacer horas extra", "expresión", "trabajar más del horario normal", "Hice horas extra toda la semana."),
            ("la carrera profesional", "sustantivo", "trayectoria de trabajo", "Quiere avanzar en su carrera en este sector."),
        ]),
        ("La Salud", [
            ("el médico / la médica", "sustantivo", "profesional de la salud", "Tengo que ir al médico hoy."),
            ("la fiebre", "sustantivo", "temperatura corporal elevada", "Tengo fiebre desde anoche."),
            ("el dolor de cabeza", "sustantivo", "malestar en la cabeza", "Tengo un fuerte dolor de cabeza."),
            ("la receta médica", "sustantivo", "documento para comprar medicamentos", "El médico me dio una receta."),
            ("recuperarse", "verbo", "sanar, mejorar de salud", "Espero recuperarme pronto."),
            ("la sala de urgencias", "sustantivo", "área de atención médica inmediata", "Fuimos a la sala de urgencias."),
            ("doler", "verbo", "causar dolor", "Me duele mucho la espalda."),
            ("la farmacia", "sustantivo", "tienda de medicamentos", "La farmacia está abierta hasta tarde."),
        ]),
    ],
    "B2": [
        ("Los Medios de Comunicación", [
            ("la noticia", "sustantivo", "información de actualidad", "Esta noticia me sorprendió mucho."),
            ("el periódico", "sustantivo", "publicación diaria de noticias", "Leo el periódico todas las mañanas."),
            ("la opinión pública", "sustantivo", "el sentir general de la sociedad", "La opinión pública está dividida."),
            ("difundir", "verbo", "hacer llegar algo a muchas personas", "La noticia se difundió rápidamente."),
            ("la fuente", "sustantivo", "origen de una información", "Hay que verificar la fuente."),
            ("las redes sociales", "sustantivo", "plataformas de comunicación digital", "Las redes sociales influyen en la opinión pública."),
            ("un artículo de fondo", "expresión", "texto periodístico analítico y extenso", "Leí un excelente artículo de fondo."),
            ("la fiabilidad", "sustantivo", "grado de confianza que merece algo", "Hay que evaluar la fiabilidad de la fuente."),
        ]),
        ("El Medio Ambiente", [
            ("el calentamiento global", "sustantivo", "aumento de la temperatura del planeta", "El calentamiento global preocupa a los científicos."),
            ("sostenible", "adjetivo", "que se puede mantener en el tiempo", "Buscamos soluciones más sostenibles."),
            ("las energías renovables", "sustantivo", "energía de fuentes naturales inagotables", "Invierten en energías renovables."),
            ("la contaminación", "sustantivo", "presencia de sustancias dañinas", "La contaminación del aire es un problema serio."),
            ("reducir", "verbo", "disminuir en cantidad", "Debemos reducir los residuos."),
            ("el reciclaje", "sustantivo", "reutilización de materiales", "El reciclaje es obligatorio aquí."),
            ("la huella ecológica", "expresión", "impacto ambiental de una persona", "Quiere reducir su huella ecológica."),
            ("proteger el medio ambiente", "expresión", "cuidar la naturaleza", "Las nuevas leyes protegen el medio ambiente."),
        ]),
    ],
    "C1": [
        ("Expresiones Idiomáticas", [
            ("costar un ojo de la cara", "expresión", "ser muy caro", "Ese coche debió de costarle un ojo de la cara."),
            ("meter la pata", "expresión", "cometer un error inoportuno", "Metí la pata al mencionar ese tema."),
            ("matar dos pájaros de un tiro", "expresión", "resolver dos cosas con una sola acción", "Así matamos dos pájaros de un tiro."),
            ("estar sin blanca", "expresión", "no tener dinero", "No puedo salir, estoy sin blanca."),
            ("hacerse el sueco", "expresión", "fingir no entender algo", "Siempre se hace el sueco cuando le conviene."),
            ("romper el hielo", "expresión", "superar la incomodidad inicial", "Un chiste puede romper el hielo."),
            ("estar en las nubes", "expresión", "estar distraído", "Hoy está completamente en las nubes."),
            ("ser como el pez en el agua", "expresión", "sentirse cómodo en un entorno", "En ese ambiente se siente como el pez en el agua."),
        ]),
        ("Registro Profesional", [
            ("el marco normativo", "sustantivo", "conjunto de leyes vigentes", "El marco normativo cambió recientemente."),
            ("en relación con", "expresión", "con respecto a", "En relación con su solicitud..."),
            ("tomar nota de", "expresión", "registrar algo mentalmente o por escrito", "Tomamos nota de sus observaciones."),
            ("de conformidad con", "expresión", "según lo establecido por", "De conformidad con la normativa vigente..."),
            ("el interlocutor", "sustantivo", "la otra parte en una conversación", "Nuestro interlocutor propuso una alternativa."),
            ("la respuesta / el feedback", "sustantivo", "reacción o valoración recibida", "Esperamos su pronta respuesta."),
            ("se adjunta", "expresión", "se incluye junto al mensaje", "Se adjunta el documento solicitado."),
            ("reciba un cordial saludo", "expresión", "fórmula de cierre formal", "Reciba un cordial saludo."),
        ]),
    ],
    "C2": [
        ("Matices Abstractos", [
            ("la ambivalencia", "sustantivo", "coexistencia de sentimientos opuestos", "Siente cierta ambivalencia ante la decisión."),
            ("la paradoja", "sustantivo", "contradicción aparente", "Es una verdadera paradoja de la modernidad."),
            ("intrínseco", "adjetivo", "propio de algo por su naturaleza", "El valor intrínseco de la obra es indiscutible."),
            ("el matiz", "sustantivo", "diferencia sutil de sentido", "Cada palabra tiene sus propios matices."),
            ("la incongruencia", "sustantivo", "falta de coherencia", "Hay una incongruencia en su razonamiento."),
            ("preeminente", "adjetivo", "que sobresale entre los demás", "Es una figura preeminente en su campo."),
            ("el legado", "sustantivo", "herencia cultural o material", "El legado cultural de la ciudad es inmenso."),
            ("emblemático", "adjetivo", "representativo de algo", "Es un caso emblemático del problema."),
        ]),
        ("El Lenguaje Literario", [
            ("la trama", "sustantivo", "estructura argumental de una obra", "La trama narrativa es compleja."),
            ("evocar", "verbo", "traer algo a la mente", "El texto evoca imágenes muy vívidas."),
            ("la metáfora", "sustantivo", "figura retórica de identificación", "Usa con frecuencia metáforas marinas."),
            ("el registro", "sustantivo", "nivel de formalidad del lenguaje", "El registro cambia de un capítulo a otro."),
            ("melancólico", "adjetivo", "con tristeza serena y profunda", "El final tiene un tono melancólico."),
            ("la prosa", "sustantivo", "forma de escritura sin verso", "Su prosa es densa y precisa."),
            ("el íncipit", "sustantivo", "las primeras líneas de un texto", "El íncipit de la novela es memorable."),
            ("impregnar", "verbo", "penetrar por completo algo", "Un sentimiento de nostalgia impregna todo el libro."),
        ]),
    ],
}

# Texto de lectura, guion de escucha, consigna de escritura y de conversación por nivel.
READING = {
    "Pre-A1": ("Un Saludo en la Calle", "<p>—¡Hola! Buenos días.</p><p>—¡Hola! ¿Cómo estás?</p><p>—Muy bien, gracias. ¿Y tú?</p><p>—Bien también. Me llamo Sofía.</p><p>—Mucho gusto, Sofía. Yo soy David.</p><p>—Mucho gusto, David. ¡Hasta luego!</p><p>—¡Adiós!</p>"),
    "A1": ("Un Día de Marco", "<p>Me llamo Marco y vivo en Sevilla. Todas las mañanas me despierto a las siete y desayuno un café con una tostada. Después voy al trabajo en bicicleta, porque no está lejos de mi casa.</p><p>Al mediodía como con mis compañeros en un bar pequeño cerca de la oficina. Por la noche, después del trabajo, me gusta dar un paseo o ver una película con mi esposa. Nos acostamos alrededor de las once.</p>"),
    "A2": ("Un Fin de Semana en Sevilla", "<p>El fin de semana pasado fui a Sevilla con dos amigas. Salimos el viernes por la noche y llegamos tarde, pero no importaba: ¡estábamos demasiado emocionadas! El sábado por la mañana visitamos la Catedral y luego caminamos junto al río Guadalquivir.</p><p>Por la tarde llovía, así que entramos en un pequeño museo que no conocíamos. Por la noche comimos tapas en un bar recomendado por una amiga del lugar. El domingo, antes de volver a casa, compramos algunos recuerdos en el mercado.</p>"),
    "B1": ("Cambiar de Trabajo a los Treinta Años", "<p>Cuando tenía veintiocho años, trabajaba en un banco. Era un trabajo seguro y bien pagado, pero no me hacía feliz. Cada mañana me despertaba con un peso en el estómago. Un día, después de una larga reflexión, decidí renunciar y seguir mi verdadera pasión: la fotografía.</p><p>Mis padres estaban preocupados, y al principio yo también tenía miedo de haber tomado la decisión equivocada. Sin embargo, después de dos años de trabajo duro, logré construir una pequeña clientela. Hoy no gano lo que ganaba en el banco, pero me despierto feliz.</p>"),
    "B2": ("El Debate sobre el Teletrabajo", "<p>Desde que muchas empresas hispanohablantes adoptaron el teletrabajo de forma permanente, el debate público se ha centrado en las ventajas y desventajas de esta transformación. Por un lado, sus defensores destacan la mayor flexibilidad, la reducción de los desplazamientos y un mejor equilibrio entre la vida personal y la profesional.</p><p>Por otro lado, sus críticos señalan que el trabajo remoto puede debilitar los vínculos entre compañeros y dificultar la formación de los nuevos empleados. Además, no todas las profesiones se prestan a este modelo: quien trabaja en el sector industrial o sanitario, por ejemplo, no tiene la misma posibilidad de elegir. El verdadero equilibrio, según muchos expertos, está en un modelo híbrido, capaz de combinar autonomía y colaboración directa.</p>"),
    "C1": ("La Memoria y los Idiomas", "<p>Quien aprende un idioma extranjero en la edad adulta desarrolla a menudo una relación singular con su propia memoria lingüística. Algunos investigadores sostienen que cada lengua que hablamos activa, en cierto sentido, una versión ligeramente distinta de nosotros mismos: el tono, las referencias culturales, incluso el humor cambian según el idioma utilizado.</p><p>No sorprende, entonces, que muchos bilingües afirmen sentirse \"más directos\" en una lengua y \"más cautelosos\" en otra, o que ciertas emociones resulten más fáciles de expresar en una lengua aprendida que en la materna — como si la distancia lingüística ofreciera una suerte de protección emocional.</p>"),
    "C2": ("Sobre el Tiempo y la Lentitud", "<p>Existe, en la cultura contemporánea, una silenciosa nostalgia por lo que antes se llamaba simplemente \"el tiempo\" — no entendido como un recurso que optimizar, sino como una dimensión que habitar. La retórica de la productividad, tan omnipresente en el discurso público actual, parece haber erosionado la posibilidad misma de una experiencia sin finalidad declarada: leer sin un propósito concreto, caminar sin un destino preciso, conversar sin una agenda.</p><p>No es casualidad que movimientos como el \"slow living\" hayan encontrado, en los últimos años, un eco tan amplio: en el fondo, no proponen nada revolucionario, sino la recuperación de un ritmo que el ser humano conoció durante casi toda su historia, y que solo recientemente ha empezado a percibir como un lujo en vez de como una normalidad.</p>"),
}

LISTENING = {
    "Pre-A1": ("En la Cafetería", "<p><strong>Camarero:</strong> ¡Buenos días! ¿Qué va a tomar?<br><strong>Cliente:</strong> Buenos días. Un café con leche, por favor.<br><strong>Camarero:</strong> Muy bien. ¿Algo más?<br><strong>Cliente:</strong> No, gracias, así está bien. ¿Cuánto es?<br><strong>Camarero:</strong> Son dos euros.<br><strong>Cliente:</strong> Aquí tiene. ¡Gracias, adiós!<br><strong>Camarero:</strong> Gracias a usted, ¡buen día!</p>"),
    "A1": ("En el Café", "<p><strong>Camarero:</strong> ¡Buenos días! ¿Qué va a tomar?<br><strong>Cliente:</strong> Buenos días. Quisiera un cortado y una tostada, por favor.<br><strong>Camarero:</strong> Enseguida. ¿Algo de beber también?<br><strong>Cliente:</strong> No, gracias, así está bien. ¿Cuánto es?<br><strong>Camarero:</strong> Son tres euros con cincuenta.<br><strong>Cliente:</strong> Aquí tiene. ¡Gracias, adiós!<br><strong>Camarero:</strong> Gracias a usted, ¡buen día!</p>"),
    "A2": ("Reservar una Mesa por Teléfono", "<p><strong>Restaurante:</strong> Restaurante Casa Luis, buenas tardes.<br><strong>Cliente:</strong> Buenas tardes, quisiera reservar una mesa para esta noche, si es posible.<br><strong>Restaurante:</strong> Claro, ¿para cuántas personas?<br><strong>Cliente:</strong> Para cuatro personas, alrededor de las ocho.<br><strong>Restaurante:</strong> Perfecto, tenemos una mesa libre. ¿A nombre de quién, disculpe?<br><strong>Cliente:</strong> A nombre de Blanco.<br><strong>Restaurante:</strong> Muy bien, señor Blanco, lo esperamos a las ocho.</p>"),
    "B1": ("Una Entrevista de Trabajo", "<p><strong>Entrevistadora:</strong> Bueno, cuénteme un poco sobre su experiencia anterior.<br><strong>Candidato:</strong> Trabajé tres años como asistente de marketing en una empresa de Madrid. Me ocupaba sobre todo de las redes sociales y las campañas publicitarias.<br><strong>Entrevistadora:</strong> Interesante. ¿Y por qué decidió dejar ese trabajo?<br><strong>Candidato:</strong> Buscaba nuevos retos, y este puesto me parece más alineado con mis objetivos a largo plazo.<br><strong>Entrevistadora:</strong> Entiendo. ¿Tiene alguna pregunta para mí?<br><strong>Candidato:</strong> Sí, quería preguntar cómo está estructurado el equipo.</p>"),
    "B2": ("Un Podcast sobre el Tráfico en la Ciudad", "<p><strong>Presentador:</strong> Hoy hablamos de un tema que nos afecta a muchos: el tráfico en las grandes ciudades. Conmigo está una experta en movilidad urbana.<br><strong>Experta:</strong> Gracias por la invitación. El punto central es que las ciudades hispanohablantes, históricamente, no fueron diseñadas para el tráfico automovilístico actual.<br><strong>Presentador:</strong> Entonces, según usted, ¿cuál es la solución?<br><strong>Experta:</strong> No creo que exista una única solución. Habría que invertir más en el transporte público y, al mismo tiempo, incentivar el uso de la bicicleta, especialmente en los centros históricos.<br><strong>Presentador:</strong> ¿Y los ciudadanos estarían dispuestos a prescindir del coche?<br><strong>Experta:</strong> Con la infraestructura adecuada, creo que sí.</p>"),
    "C1": ("Una Entrevista sobre una Nueva Novela", "<p><strong>Periodista:</strong> Su última novela aborda temas bastante complejos: la memoria, la identidad, el exilio. ¿De dónde nace esta elección?<br><strong>Autora:</strong> En realidad nace de una pregunta muy personal: ¿qué queda de nosotros cuando dejamos el lugar donde crecimos? No quería escribir un ensayo, sino contar esta pregunta a través de una historia.<br><strong>Periodista:</strong> ¿Hay un elemento autobiográfico?<br><strong>Autora:</strong> Sin duda, aunque preferí transfigurarlo a través de la ficción. Creo que la narrativa permite decir ciertas verdades con más libertad que el ensayo.</p>"),
    "C2": ("Una Conferencia sobre la Evolución de la Lengua", "<p><strong>Ponente:</strong> Lo que a menudo se olvida al hablar de \"pureza\" lingüística es que toda lengua viva está, por definición, en permanente transformación. El propio español, tal como lo conocemos hoy, es el resultado de siglos de contactos, préstamos y readaptaciones.<br><strong>Moderadora:</strong> Sin embargo, algunos sostienen que la influencia del inglés representa una amenaza particular...<br><strong>Ponente:</strong> Es una postura comprensible, pero poco fundamentada históricamente. Cada época ha tenido su propia lengua \"amenazante\" — el francés en el siglo XIX, por ejemplo. La lengua, en todo caso, debe observarse, no defenderse como si fuera un monumento inmóvil.</p>"),
}

WRITING = {
    "Pre-A1": "Escribe 3-4 frases muy simples para presentarte: tu nombre, tu nacionalidad y un saludo de despedida. Usa ser y al menos un verbo más.",
    "A1": "Escribe 5-6 frases sencillas presentándote: tu nombre, de dónde eres, tu edad, tu familia y algo que te gusta. Usa ser, tener y el presente de al menos dos verbos regulares.",
    "A2": "Escribe un párrafo corto (6-8 frases) sobre tus últimas vacaciones, usando el pretérito indefinido. Menciona a dónde fuiste, qué hiciste y cómo te sentiste — intenta usar al menos un verbo con ser y otro con tener.",
    "B1": "Escribe una narración corta (8-10 frases) sobre algo inesperado que te haya pasado. Usa tanto el pretérito indefinido como el imperfecto — recuerda: el imperfecto da el contexto, el indefinido hace avanzar la historia.",
    "B2": "Escribe un párrafo de opinión corto (10-12 frases) sobre un tema que te importe (la tecnología, el medio ambiente, el teletrabajo...). Usa al menos dos disparadores de subjuntivo (pienso que, es importante que, dudo que) y una oración hipotética.",
    "C1": "Escribe un correo formal (10-12 frases) solicitando información a una empresa o institución. Usa un registro formal apropiado en todo el texto, al menos un conector avanzado (sin embargo, dado que, por consiguiente), y una fórmula de apertura y cierre adecuadas.",
    "C2": "Escribe un párrafo argumentativo corto (12-15 frases) defendiendo una postura sobre un tema debatido. Estructúralo con una tesis clara, una concesión al punto de vista contrario (es cierto que...) y una réplica (sin embargo...). Busca una sintaxis variada y cohesionada — evita repetir el mismo sustantivo dos veces seguidas.",
}

SPEAKING = {
    "Pre-A1": ["Preséntate en treinta segundos: tu nombre y de dónde eres.", "Saluda a un compañero y pregúntale su nombre."],
    "A1": ["Descríbete en un minuto: nombre, edad, nacionalidad, familia y qué haces.", "Hazle tres preguntas a un compañero usando palabras interrogativas (dónde, cuándo, cómo, por qué)."],
    "A2": ["Cuéntale a un compañero tu semana típica usando adverbios de frecuencia (siempre, a menudo, a veces).", "Describe tus últimas vacaciones usando el pretérito indefinido."],
    "B1": ["Discute qué harías si te ganaras la lotería, usando el condicional.", "Dale a un compañero indicaciones e instrucciones usando el imperativo, tanto informal como formal."],
    "B2": ["Debate un tema de actualidad con un compañero, usando disparadores de subjuntivo para expresar opinión y duda.", "Describe una situación hipotética (\"Si pudiera cambiar una cosa de mi ciudad...\") usando el periodo hipotético."],
    "C1": ["Da una breve charla persuasiva (2 minutos) sobre un tema de tu elección, usando conectores avanzados.", "Representa una queja formal y su respuesta cortés y atenuada."],
    "C2": ["Debate un tema con matices, usando deliberadamente expresiones de atenuación (parece que, no estoy del todo de acuerdo) para suavizar tus afirmaciones.", "Resume en voz alta un artículo o una noticia breve en menos de un minuto, con tus propias palabras."],
}


def esc(s):
    import html
    return html.escape(s, quote=False)


def lesson_cards(level_slug, nav_list):
    cards = []
    for i, entry in enumerate(nav_list):
        idx = ascii_uppercase[i] if i < 26 else str(i + 1)
        lesson = json.loads((REPO_ROOT / "curriculum" / level_slug / f"{entry['slug']}.json").read_text(encoding="utf-8"))
        cards.append(f"""<article class="lesson-card">
            <span class="lesson-card__index" aria-hidden="true">{idx}</span>
            <h3><a class="lesson-card__title-link" href="{level_slug}/{entry['slug']}.html">{esc(lesson['title'])}</a></h3>
            <p>{esc(lesson['subtitle'])}</p>
        </article>""")
    return "".join(cards)


def vocab_section(level_code, level_slug):
    themes = VOCAB.get(level_code, [])
    blocks = []
    for ti, (theme_title, words) in enumerate(themes):
        rows = "".join(
            f"<tr><td><strong>{esc(w)}</strong></td><td class=\"text-muted\">{esc(pos)}</td><td>{esc(meaning)}</td><td><em>{esc(ex_sentence)}</em></td></tr>"
            for w, pos, meaning, ex_sentence in words
        )
        opts = [w for w, *_ in words][:6]
        items = []
        for i, (w, pos, meaning, ex_sentence) in enumerate(words[:4]):
            item_opts = opts if w in opts else opts + [w]
            items.append({
                "id": f"{level_slug}v{ti}i{i}",
                "prompt": f"¿Qué palabra significa «{meaning}»?",
                "options": item_opts,
                "answerIndex": item_opts.index(w),
                "explanation": f"{w} significa {meaning}.",
            })
        ex_block = {"id": f"{level_slug}-vocab-{ti}-mc", "type": "multiple-choice", "title": "Relaciona el Significado", "items": items}
        blocks.append(f"""<div class="card" style="margin-bottom:var(--space-lg);">
            <h3>{esc(theme_title)}</h3>
            <div class="table-scroll">
                <table class="ref-table">
                    <thead><tr><th>Palabra</th><th>Categoría</th><th>Significado</th><th>Ejemplo</th></tr></thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
            <div style="margin-top:var(--space-md);"><div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex_block, ensure_ascii=False)}</script></div></div>
        </div>""")
    return f"""<section id="vocabulary" class="section section--tight" aria-labelledby="vocabulary-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="vocabulary-heading">Vocabulario</h2>
                <p>Grupos de palabras por tema para situaciones reales, cada uno con frases de ejemplo y una comprobación rápida.</p>
            </div>
            {"".join(blocks)}
        </div>
    </section>"""


def reading_section(level_code, level_slug):
    title, passage = READING[level_code]
    ex = {
        "id": f"{level_slug}-reading-mc", "type": "true-false", "title": "Comprueba tu Comprensión",
        "instructions": "Según el texto de arriba, marca cada afirmación como verdadera o falsa.",
        "items": [
            {"id": f"{level_slug}rd1", "statement": "El texto está escrito en primera persona o como un diálogo directo entre personas.", "answer": True, "explanation": "El texto usa formas de yo/nosotros o un intercambio directo entre los hablantes."},
        ],
    }
    return f"""<section id="reading" class="section section--surface" aria-labelledby="reading-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code} &middot; Lectura</p>
                <h2 id="reading-heading">{esc(title)}</h2>
            </div>
            <div class="card"><div class="prose">{passage}</div></div>
            <div style="margin-top:var(--space-md);"><div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex, ensure_ascii=False)}</script></div></div>
        </div>
    </section>"""


def listening_section(level_code):
    title, script = LISTENING[level_code]
    return f"""<section id="listening" class="section section--tight" aria-labelledby="listening-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code} &middot; Escucha (guion)</p>
                <h2 id="listening-heading">{esc(title)}</h2>
                <p>Todavía no hay grabación de audio &mdash; lee este intercambio como un diálogo de escucha e imagina el ritmo del habla real.</p>
            </div>
            <div class="card"><div class="prose">{script}</div></div>
        </div>
    </section>"""


def writing_speaking_section(level_code):
    prompt = WRITING[level_code]
    speaking_items = "".join(f"<li>{esc(p)}</li>" for p in SPEAKING[level_code])
    return f"""<section id="writing" class="section section--surface" aria-labelledby="writing-heading">
        <div class="section__inner split">
            <div>
                <p class="eyebrow">{level_code} &middot; Escritura</p>
                <h2 id="writing-heading">Tarea de Escritura Guiada</h2>
                <p style="max-width:56ch;">{esc(prompt)}</p>
            </div>
            <div class="card card--feature" id="speaking">
                <p class="eyebrow">{level_code} &middot; Conversación</p>
                <h3 style="font-size:var(--step-0);">Temas de Conversación</h3>
                <ul class="summary-list">{speaking_items}</ul>
            </div>
        </div>
    </section>"""


def build(level_code, level_slug):
    name, blurb = LEVEL_META[level_code]
    nav_map = json.loads((REPO_ROOT / "scripts" / "lesson_nav_map.json").read_text(encoding="utf-8"))
    nav_list = nav_map.get(level_slug, [])
    index = json.loads((REPO_ROOT / "curriculum" / "index.json").read_text(encoding="utf-8"))
    overview = index["levels"][level_code.upper()]["overview"]

    title = f"{level_code} — {name} — Renan el Profesor · Curso de Español"
    description = f"{level_code} {name}: {blurb}"[:300]
    breadcrumb = (
        f'<li><a href="{REL}index.html">Inicio</a></li>'
        f'<li aria-current="page">Niveles</li>'
        f'<li aria-current="page">{level_code} {name}</li>'
    )
    page_header = f"""<div class="page-header">
        {site_chrome.STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">Vamos a aprender</p>
                <h1>{level_code} &mdash; {esc(name)}</h1>
                <p class="page-header__lede">{esc(blurb)}</p>
            </div>
        </div>
    </div>"""
    toc = ('<div class="level-toc" data-scrollspy><div class="level-toc__inner">'
           '<a href="#lessons">Lecciones</a><a href="#test-yourself">Ponte a Prueba</a>'
           '<a href="#vocabulary">Vocabulario</a><a href="#reading">Lectura</a>'
           '<a href="#listening">Escucha</a><a href="#writing">Escritura</a>'
           '<a href="#speaking">Conversación</a></div></div>')

    overview_section = f"""<section class="section section--tight" aria-labelledby="overview-heading">
        <div class="section__inner">
            <h2 id="overview-heading" class="visually-hidden">Resumen</h2>
            <p style="max-width:62ch;font-size:var(--step-0);color:var(--color-text-muted);">{esc(overview)}</p>
        </div>
    </section>"""

    lessons_section = f"""<section id="lessons" class="section section--surface" aria-labelledby="grammar-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="grammar-heading">Lecciones</h2>
                <p>{len(nav_list)} lecciones, en orden &mdash; cada una se apoya en la anterior.</p>
            </div>
            <div class="grid">{lesson_cards(level_slug, nav_list)}</div>
        </div>
    </section>"""

    ty_section = f"""<section id="test-yourself" class="section section--tight" aria-labelledby="ty-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="ty-heading">Ponte a Prueba</h2>
                <p>Un repaso único y completo de todos los temas de gramática de {level_code} &mdash; todos los ejercicios de todas las lecciones, mezclados.</p>
            </div>
            <a class="btn btn--accent" href="{level_slug}/test-yourself.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="15" r="6"/><path d="m9 10-3-7"/><path d="m15 10 3-7"/><path d="M9.5 15.5 12 17l2.5-1.5"/></svg>Empezar el repaso</a>
        </div>
    </section>"""

    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=["exercises", "lessons"]))
    out.append(site_chrome.header(REL, level_code, breadcrumb, active_top="levels"))
    out.append(page_header)
    out.append(toc)
    out.append(overview_section)
    out.append(lessons_section)
    out.append(ty_section)
    out.append(vocab_section(level_code, level_slug))
    out.append(reading_section(level_code, level_slug))
    out.append(listening_section(level_code))
    out.append(writing_speaking_section(level_code))
    out.append(site_chrome.footer(REL, extra_scripts=["exercises.js", "mastery.js"]))

    out_path = REPO_ROOT / "levels" / f"{level_slug}.html"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Built {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    for code, slug in [("Pre-A1", "pre-a1"), ("A1", "a1"), ("A2", "a2"), ("B1", "b1"), ("B2", "b2"), ("C1", "c1"), ("C2", "c2")]:
        build(code, slug)
