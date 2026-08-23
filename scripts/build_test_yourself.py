#!/usr/bin/env python3
"""
Construye levels/{nivel}/test-yourself.html: todos los bloques de ejercicios
de todas las lecciones de ese nivel, agrupados bajo el título de su lección,
en una sola página — "más preguntas, mezcladas, con retroalimentación
instantánea," exactamente lo que promete el llamado a la acción "Ponte a
Prueba" de cada lección. Generado directamente desde curriculum/{nivel}/*.json
(vía lesson_nav_map.json para el orden) en vez de escrito a mano, para que
nunca se desincronice de las lecciones que repasa.

Uso:
    python3 scripts/build_test_yourself.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = "../../"
LEVELS = [
    ("Pre-A1", "pre-a1"), ("A1", "a1"), ("A2", "a2"), ("B1", "b1"),
    ("B2", "b2"), ("C1", "c1"), ("C2", "c2"),
]


def topic_section(lesson):
    blocks = "".join(
        f'<div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex, ensure_ascii=False)}</script></div>'
        for ex in lesson["exercises"]
    )
    slug = lesson["id"].split("-", 1)[1] if "-" in lesson["id"] else lesson["id"]
    return f"""<section id="{slug}" class="section section--tight ty-topic" aria-labelledby="ty-{slug}-heading">
        <div class="section__inner">
            <p class="eyebrow">{lesson['level']}</p>
            <h2 id="ty-{slug}-heading"><a href="{slug}.html">{lesson['title']}</a></h2>
            <p style="color:var(--color-text-muted);max-width:60ch;margin-bottom:var(--space-md);">{lesson['subtitle']}</p>
            {blocks}
        </div>
    </section>"""


def build(level_code, level_slug):
    nav_map = json.loads((REPO_ROOT / "scripts" / "lesson_nav_map.json").read_text(encoding="utf-8"))
    lessons_order = nav_map.get(level_slug, [])

    sections = []
    toc_links = []
    for entry in lessons_order:
        lesson_path = REPO_ROOT / "curriculum" / level_slug / f"{entry['slug']}.json"
        lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
        sections.append(topic_section(lesson))
        toc_links.append(f'<a href="#{entry["slug"]}">{lesson["title"]}</a>')

    title = f"Ponte a Prueba: {level_code} — Repaso Mixto — Renan el Profesor"
    description = f"Todos los temas de gramática de {level_code} en un repaso mixto, con retroalimentación instantánea en cada pregunta."
    breadcrumb = (
        f'<li><a href="{REL}index.html">Inicio</a></li>'
        f'<li aria-current="page">Niveles</li>'
        f'<li><a href="../{level_slug}.html">{level_code}</a></li>'
        f'<li aria-current="page">Ponte a Prueba</li>'
    )

    page_header = f"""<div class="page-header">
        {site_chrome.STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{level_code} &middot; Repaso Mixto</p>
                <h1>Ponte a Prueba: {level_code}</h1>
                <p class="page-header__lede">Todos los ejercicios de todas las lecciones de {level_code}, reunidos en una sola página. Practica tanto como quieras, en el orden que prefieras.</p>
            </div>
        </div>
    </div>"""
    toc = f'<div class="level-toc"><div class="level-toc__inner">{"".join(toc_links)}</div></div>'

    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=["exercises", "lessons"]))
    out.append(site_chrome.header(REL, level_code, breadcrumb, active_top="levels"))
    out.append(page_header)
    out.append(toc)
    out.extend(sections)
    out.append(site_chrome.footer(REL, extra_scripts=["exercises.js", "mastery.js"]))

    out_dir = REPO_ROOT / "levels" / level_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "test-yourself.html"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Built {out_path.relative_to(REPO_ROOT)} ({len(sections)} topics)")


if __name__ == "__main__":
    for code, slug in LEVELS:
        build(code, slug)
