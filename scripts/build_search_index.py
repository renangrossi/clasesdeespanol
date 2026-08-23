#!/usr/bin/env python3
"""
Build assets/data/search-index.json: the flat array assets/js/search.js
fetches once and filters entirely client-side. Entry shape:
{ type, level, title, desc, url, keywords[] } — see search.js's
TYPE_LABEL map for valid `type` values (level, lesson, grammar, exercise,
mock, extra).

Usage:
    python3 scripts/build_search_index.py
"""
import json
import glob
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

LEVEL_ENTRIES = [
    ("Pre-A1", "pre-a1", "Supervivencia", "El alfabeto y los sonidos, saludos, números, vocabulario esencial de supervivencia."),
    ("A1", "a1", "Principiante", "Ser y estar, género y artículos, presente de indicativo, saludos cotidianos."),
    ("A2", "a2", "Elemental", "Pretérito indefinido e imperfecto, verbos con cambio de raíz, pronombres de objeto directo."),
    ("B1", "b1", "Intermedio", "Presente de subjuntivo, pronombres combinados, futuro, condicional, imperativo."),
    ("B2", "b2", "Intermedio alto", "Imperfecto de subjuntivo, condicionales con si, voz pasiva, estilo indirecto."),
    ("C1", "c1", "Avanzado", "Pluscuamperfecto de subjuntivo, condicionales complejas, matices del subjuntivo, registro formal."),
    ("C2", "c2", "Maestría", "Sintaxis compleja, registro literario, matices léxicos, cohesión del discurso."),
]

STATIC_ENTRIES = [
    {"type": "extra", "level": "", "title": "Ejercicios", "desc": "Práctica extra de lectura y vocabulario, independiente del nivel.",
     "url": "exercises.html", "keywords": ["lectura", "practica", "vocabulario"]},
    {"type": "mock", "level": "", "title": "Exámenes Simulados", "desc": "Secciones de examen simulado al estilo DELE/SIELE, con hoja de respuestas.",
     "url": "simulated-exams.html", "keywords": ["dele", "siele", "examen", "prueba"]},
    {"type": "extra", "level": "", "title": "Extras", "desc": "Cultura hispanohablante, expresiones cotidianas, y uso formal frente a informal.",
     "url": "extras.html", "keywords": ["cultura", "expresiones", "tu", "usted", "vos", "formal", "informal"]},
    {"type": "grammar", "level": "", "title": "Diccionario y Referencia", "desc": "Busca cualquier palabra en español en varios diccionarios monolingües.",
     "url": "dictionary.html", "keywords": ["rae", "dle", "wikcionario", "fundeu"]},
    {"type": "grammar", "level": "", "title": "Verbos Irregulares", "desc": "Tabla de referencia de los verbos irregulares más comunes del español.",
     "url": "irregular-verbs.html", "keywords": ["ser", "estar", "ir", "tener", "conjugacion"]},
    {"type": "extra", "level": "", "title": "Prueba de Nivel", "desc": "Una prueba corta para descubrir en qué nivel del MCER empezar.",
     "url": "placement-test.html", "keywords": ["prueba de nivel", "cual es mi nivel"]},
    {"type": "extra", "level": "", "title": "Repaso de Hoy", "desc": "Repaso de repetición espaciada de los ítems que has fallado antes.",
     "url": "today-review.html", "keywords": ["repeticion espaciada", "repaso", "dominio"]},
]


def main():
    entries = []
    for code, slug, name, desc in LEVEL_ENTRIES:
        entries.append({
            "type": "level", "level": code, "title": f"{code} — {name}",
            "desc": desc, "url": f"levels/{slug}.html", "keywords": [name.lower()],
        })
        entries.append({
            "type": "grammar", "level": code, "title": f"Ponte a Prueba: {code}",
            "desc": f"Repaso mixto de todos los temas de gramática de {code}, con retroalimentación instantánea.",
            "url": f"levels/{slug}/test-yourself.html", "keywords": ["repaso", "prueba"],
        })

    files = sorted(glob.glob(str(REPO_ROOT / "curriculum" / "*" / "*.json")))
    for fpath in files:
        lesson = json.loads(Path(fpath).read_text(encoding="utf-8"))
        level = lesson.get("level", "")
        slug = level.lower()
        prefix = slug + "-"
        lesson_id = lesson.get("id", "")
        file_slug = lesson_id[len(prefix):] if lesson_id.startswith(prefix) else lesson_id
        entries.append({
            "type": "lesson",
            "level": level,
            "title": lesson.get("title", ""),
            "desc": lesson.get("subtitle", ""),
            "url": f"levels/{slug}/{file_slug}.html",
            "keywords": [lesson.get("strand", ""), lesson.get("skill", "")],
        })

    entries.extend(STATIC_ENTRIES)

    out_path = REPO_ROOT / "assets" / "data" / "search-index.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Wrote {len(entries)} search entries -> {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
