# Esquema de datos del currículo

Fuente única de verdad para el contenido de las lecciones. Cada lección es un
archivo JSON en `curriculum/{nivel}/{leccion-id}.json`, generado desde datos
Python escritos a mano en `scripts/curriculum_source/{nivel}.py` por
`scripts/generate_curriculum.py` — edita el Python, no el JSON directamente
(una regeneración lo sobrescribiría). `curriculum/index.json` lista las
lecciones de cada nivel en orden y también se genera, no se edita a mano.

Este es el esquema hermano del `curriculum/SCHEMA.md` del curso de inglés y
del curso de italiano, con una diferencia deliberada: los ejemplos son
**strings simples en español**, no objetos bilingües `{"it": ..., "en": ...}`
como en el curso de italiano. Este curso es de inmersión total — el
estudiante nunca ve una traducción como muleta dentro del contenido de la
lección; el significado se transmite con paráfrasis más simples en español,
contexto y los propios ejercicios. En esto coincide con el curso de inglés
(que también es monolingüe). Como el curso de italiano, tampoco existen
`prerequisites`/`related`/`sourceMaterial` (no hay material fuente en
docx/pdf para este curso — cada lección se escribió directamente), y todos
los niveles (incluyendo Pre-A1) pasan por el mismo pipeline — no hay
excepción de HTML escrito a mano para ningún nivel.

## Forma del JSON de una lección

```jsonc
{
  "id": "b1-presente-de-subjuntivo-formacion",  // coincide con el nombre del archivo generado
  "level": "B1",
  "unit": "1",                        // unidad de curriculum/index.json a la que pertenece (siempre "1" por ahora — una unidad por nivel)
  "order": 6,                         // posición dentro del nivel
  "skill": "grammar",                 // grammar | vocabulary | pronunciation | reading
                                       // | listening | speaking | writing | functional
  "strand": "subjuntivo",             // agrupación libre, solo informativa
  "title": "El Presente de Subjuntivo — Formación",
  "subtitle": "Cómo se forma el modo que expresa deseo, duda y emoción en español.",
  "objectives": ["...", "..."],
  "content": {
    "intro": "Un párrafo corto, junto a la tarjeta de objetivos.",
    "explanation": "<p>...</p>",      // opcional; HTML en línea (strong/em/p), se muestra tal cual (confiable)
    "rules": [ { "heading": "a) ...", "body": "<p>...</p> o <ul>...</ul>" }, ... ],  // se muestra tal cual (confiable)
    "table": "<div class=\"table-scroll\">...</div>",  // opcional, un bloque de tabla de referencia completo, tal cual
    "examples": [ "Espero que tengas un buen día.", "..." ],  // strings simples en español, con escape de HTML
    "commonMistakes": [ { "wrong": "...", "right": "...", "why": "..." }, ... ]
  },
  "exercises": [ /* objetos verbatim del esquema de assets/js/exercises.js — ver el comentario de cabecera de ese archivo para el esquema completo por tipo */ ],
  "summary": ["Una idea clave por línea", "..."]
}
```

`rules[].body`, `content.explanation` y `content.table` son HTML confiable,
sin escape (no pongas ahí nada que no hayas escrito tú mismo), siguiendo las
etiquetas que ya estilizan exercises.js/lessons.css (`<p>`, `<ul>/<li>`,
`<strong>`, `<em>`, `<div class="table-scroll"><table class="ref-table">`).
Todo lo demás (title, subtitle, objectives, examples, commonMistakes,
summary) recibe escape de HTML automáticamente en `scripts/build_lesson.py`
— usa texto plano ahí, incluyendo caracteres Unicode literales como `→` o
`—` en vez de entidades HTML como `&rarr;`/`&mdash;` (una entidad en un
campo con escape se codificaría dos veces y aparecería literalmente como
`&rarr;` en la página).

## Forma de `curriculum/index.json`

```jsonc
{
  "levels": {
    "B1": {
      "overview": "Un párrafo mostrado en la página hub de B1.",
      "units": [
        { "id": "1", "title": "Gramática B1", "lessons": [ { "id": "b1-presente-de-subjuntivo-formacion", "status": "published" }, ... ] }
      ]
    }
  }
}
```

## Esquema de los ítems de `exercises` (contrato exacto de `assets/js/exercises.js`)

Cada bloque de ejercicio: `{ "id", "type", "title", "instructions"?, "passage"?, "items": [...] }`.
`type` es uno de `multiple-choice`, `true-false`, `fill-blank`, `matching`,
`ordering`, `correction`, `typing`, `reading-comprehension`, `vocabulary`,
`writing`. La forma de cada `item` según el `type` del bloque:

- **multiple-choice / vocabulary / reading-comprehension**: `{ "id", "prompt", "options": [...], "answerIndex", "explanation" }`
- **true-false**: `{ "id", "statement", "answer": true|false, "explanation" }`
- **fill-blank**: `{ "id", "prompt" (usa `___` por cada espacio), "answers": [["resp1","resp2"], ...] (un array por espacio, con variantes aceptadas), "options"? (array de opciones por espacio, para renderizar un `<select>`), "explanation" }`
- **correction**: `{ "id", "incorrect", "answer": ["..."], "explanation" }`
- **typing**: `{ "id", "prompt", "answer"?: ["..."] (si se omite, autoevaluación sin calificar), "modelAnswer"?, "explanation" }`
- **matching**: `{ "id", "prompt"?, "pairs": [ {"left":"...", "right":"..."}, ... ], "explanation" }`
- **ordering**: `{ "id", "prompt", "words": [...] (orden correcto), "explanation" }`
- **writing**: `{ "id", "prompt" }` — autoevaluación únicamente, sin calificación automática.

`explanation` se muestra siempre después de calificar, sea la respuesta
correcta o no — escríbela como una regla o razón breve de la que el
estudiante pueda aprender, no solo "Respuesta correcta."

## Build

```bash
python3 scripts/build_all.py
```

Ejecuta el pipeline completo en orden: `generate_curriculum.py` (Python →
JSON) → `build_nav_map.py` → `build_lesson.py` (cada JSON de lección → su
página HTML, reutilizando el chrome compartido de `scripts/site_chrome.py`)
→ `build_level_pages.py` (las siete páginas hub de nivel) →
`build_test_yourself.py` (páginas de repaso mixto por nivel) →
`build_exercise_index.py` (búsqueda de ítems para repetición espaciada) →
`build_search_index.py` (búsqueda del sitio) → `build_static_pages.py`
(inicio, ejercicios, extras, diccionario, verbos irregulares, prueba de
nivel, progreso, repaso de hoy, exámenes simulados).
