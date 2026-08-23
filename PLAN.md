# Plan — Clases de Español (sitio hermano de englishclasses / lezionidiitaliano)

Status: architecture scaffold in progress. This document is the working
plan; it will be trimmed down to a normal README once the site is live.

## 1. Repository / folder structure

Identical shape to `course-italian` (which is itself the proven fork of
`curso-ingles`'s structure), so the build pipeline needs no structural
changes — only content and copy:

```
couse-spanish/
├── index.html, dictionary.html, exercises.html, extras.html,
│   irregular-verbs.html, placement-test.html, progress.html,
│   simulated-exams.html, today-review.html      (generated, not hand-edited)
├── levels/
│   ├── pre-a1.html, a1.html, a2.html, b1.html, b2.html, c1.html, c2.html
│   └── {level}/{lesson-id}.html + {level}/test-yourself.html  (generated)
├── curriculum/
│   ├── SCHEMA.md
│   ├── index.json                                (generated)
│   └── {level}/{lesson-id}.json                  (generated)
├── scripts/
│   ├── curriculum_source/{level}.py               (hand-authored — edit here)
│   ├── generate_curriculum.py   (Python → JSON)
│   ├── build_nav_map.py, build_lesson.py, build_level_pages.py,
│   │   build_test_yourself.py, build_exercise_index.py,
│   │   build_search_index.py, build_static_pages.py
│   ├── build_all.py              (runs the full pipeline in order)
│   └── site_chrome.py            (shared header/footer/nav/search overlay)
├── assets/
│   ├── css/ (tokens, base, layout, components, lessons, exercises, search, dark-mode)
│   ├── js/  (main, exercises, mastery, progress, search, dictionary,
│   │         dict-widget, irregular-verbs, today-review)
│   ├── img/ (favicon, badges)
│   └── data/ (search-index.json, exercise-items-index.json — generated)
├── worker/           (AI Teacher backend — Cloudflare Worker, deployed
│                       separately, NOT part of the static Pages site)
├── docs/             (gamification.md, this PLAN.md, etc.)
├── .nojekyll, .gitignore
└── PLAN.md
```

Repo: **`clasesdeespanol`** (public, under `github.com/renangrossi`) — `ñ`
is not a legal character in a GitHub repository name, so the fallback you
gave is what's actually in use. Already created and pushed:
`https://github.com/renangrossi/clasesdeespanol`. GitHub Pages is enabled
on `main` / root: `https://renangrossi.github.io/clasesdeespanol/`.

## 2. Shared vs. forked vs. duplicated from the English/Italian codebase

- **Reused verbatim (structure/logic, no content coupling):** the whole
  build pipeline (`generate_curriculum.py`, `build_lesson.py`,
  `build_level_pages.py`, `build_nav_map.py`, `build_test_yourself.py`,
  `build_exercise_index.py`, `build_search_index.py`,
  `build_static_pages.py`, `build_all.py`), the exercise engine
  (`assets/js/exercises.js` — its item schema is language-agnostic),
  progress/gamification (`progress.js`, `mastery.js` — pure
  localStorage, no hardcoded language strings beyond a couple of
  translatable copy strings), search (`search.js`), and the CSS
  architecture (`tokens.css` → `base.css` → `layout.css` →
  `components.css` → `lessons.css`/`exercises.css`/`search.css` →
  `dark-mode.css`). These were copied from `course-italian` (closer
  precedent: no docx/pdf worksheets, single generation pipeline for
  every level including the first) and are being adapted in place.
- **Forked and rewritten (same shape, new content):** `site_chrome.py`
  (header/footer/nav text → Spanish), `tokens.css` (new color values —
  done, see §4), user-facing strings inside the JS files (toasts, aria
  labels, button text), `curriculum/SCHEMA.md` (monolingual `examples`
  like the English course, not the Italian course's bilingual
  `{it, en}` pairs — see §5 for why), `dictionary.html` (new card set,
  see §6), `worker/worker.js` + `course-catalog.json` (new system
  prompt and catalog, see §8).
- **Duplicated with zero reuse (genuinely new):** every lesson's
  pedagogical content (`scripts/curriculum_source/{level}.py`) — Spanish
  grammar has a different shape than English or Italian (ser/estar,
  the preterite/imperfect contrast, a much larger subjunctive system,
  clitic pronoun clusters, voseo) and has to be authored from scratch,
  not translated from either sibling site.
- **Not carried over:** the `cefr/*.docx`/`.pdf` worksheet tree and
  `worker/.wrangler` local state — English-only legacy/local artifacts.

## 3. Full CEFR curriculum outline (Pre-A1 → C2)

78 lessons across 7 levels, prioritized by what's actually distinctive
about Spanish (ser/estar, preterite-vs-imperfect, the subjunctive, clitic
pronouns, voseo/regional variation) rather than a mechanical translation
of the English or Italian syllabus:

**Pre-A1 — Supervivencia (8):** El alfabeto y los sonidos (ñ, rr,
acentuación) · Saludos y presentaciones · Números, hora y fecha ·
Vocabulario de clase y estudio · Personas y objetos cotidianos · Verbos
básicos: ser, tener, querer, gustar · Pronombres de sujeto y primer
contacto con ser/estar · Lectura y escucha de supervivencia.

**A1 — Principiante (14):** El abecedario y la pronunciación (ampliado)
· Género y número de los sustantivos · Artículos definidos e indefinidos
· Ser y estar (introducción) · Pronombres personales de sujeto ·
Presente — verbos regulares (-ar/-er/-ir) · Presente — irregulares
comunes (ir, tener, hacer...) · Adjetivos y concordancia · Posesivos ·
Demostrativos · Hay / estar (existencia y ubicación) · Preposiciones
simples · Interrogativos y preguntas · Gustar y verbos similares.

**A2 — Elemental (12):** Pretérito perfecto compuesto · Pretérito
indefinido — regulares · Pretérito indefinido — irregulares · Pretérito
imperfecto · Indefinido vs. imperfecto · Futuro simple e ir + a +
infinitivo · Comparativos y superlativos · Verbos con cambio de raíz
(e>ie, o>ue, e>i) · Pronombres de objeto directo · Pronombres de objeto
indirecto · Imperativo afirmativo (tú/usted) · Adverbios de frecuencia y
conectores básicos.

**B1 — Intermedio (14):** Perfecto vs. indefinido (matices) ·
Pluscuamperfecto · Futuro compuesto y condicional simple · Condicional
para cortesía e hipótesis · Imperativo negativo y pronombres con el
imperativo · Presente de subjuntivo — formación · Presente de subjuntivo
— deseo, duda, emoción · Voz pasiva con ser y pasiva refleja con se ·
Estilo indirecto (presente) · Pronombres combinados (se lo, me lo...) ·
Por y para · Oraciones relativas (que, quien, donde) · El voseo argentino
y otras variedades del español · Conectores y marcadores del discurso.

**B2 — Intermedio alto (12):** Imperfecto de subjuntivo · Condicionales
con si + subjuntivo · Subjuntivo vs. indicativo (sustantivas) ·
Subjuntivo en relativas y adverbiales · Perífrasis verbales · Ser y estar
— usos avanzados · Pasiva avanzada y construcciones con se · Estilo
indirecto (todos los tiempos) · Conectores argumentativos avanzados ·
Colocaciones y expresiones idiomáticas · Registro formal e informal ·
Futuro de subjuntivo (usos jurídicos/arcaizantes, breve).

**C1 — Avanzado (10):** Pluscuamperfecto de subjuntivo · Condicionales
complejas (los cuatro tipos) · Matices del subjuntivo · Construcciones
enfáticas (lo que..., es que...) · Nominalización y estilo académico ·
Conectores textuales avanzados · Perífrasis verbales avanzadas · Voseo,
ustedeo y variación dialectal hispanoamericana · Ironía, atenuación y
cortesía lingüística · Español académico/profesional.

**C2 — Maestría (8):** Sintaxis compleja y subordinación múltiple ·
Registro literario y recursos estilísticos · Matices léxicos y falsos
amigos avanzados · Variación regional (España, México, Argentina,
Caribe...) · Cohesión textual en discurso extenso · Modalidad y
atenuación en discurso formal · Estructuras arcaicas o literarias ·
Dominio del registro y transformación estilística.

## 4. Color system — Spain + Argentina

Same token *names* as the English/Italian `tokens.css` (so
`components.css`/`layout.css`/`dark-mode.css` need zero structural
change), new values (**done** — see `assets/css/tokens.css`):

| Role | Source | Light value |
|---|---|---|
| `--navy-*` → `--color-primary` | Argentina's celeste, deepened for header/text contrast | `#0e3252` |
| `--burgundy-*` → `--color-accent` | Spain's flag red | `#aa151b` |
| `--forest-*` → `--color-secondary-accent` | Argentina's lighter celeste | `#2f6f9e` |
| `--gold-*` → `--color-gold` / focus ring | Sol de Mayo — the symbol both flags share in spirit | `#b8860e` |
| `--cotto-red` → rule lines/dividers | vivid flag red, distinct from the button accent | `#c1272d` |
| `--parchment-*`/`--ink-*` | warm paper + ink neutrals (unchanged role from the sibling sites) | — |

Dark mode's independent accent overrides were retuned from the Italian
terracotta/olive pair to a red/celeste pair (`#e2555c` / `#7ec2f0`) so
the same red-and-blue identity survives the theme switch.

## 5. Making the entire UI Spanish-only

- **`site_chrome.py`** (shared header, footer, nav, search overlay,
  mobile menu, skip link, meta tags) gets a full rewrite pass — every
  string in it is currently Italian and needs to become Spanish (next
  step, not yet done).
- **JS user-facing strings** — `progress.js` (XP/streak toasts, badge
  names), `exercises.js` (button labels, feedback), `search.js` ("no
  results"), `dict-widget.js` ("Buscar…"), `today-review.js` — copied
  as-is from Italian for now (their *logic* is language-agnostic) but
  every hardcoded string inside them still needs a translation pass
  before launch. Code comments stay in English (matching this repo's
  own convention) — only learner-facing text is in scope.
- **Curriculum schema decision:** unlike the Italian course (which
  glosses every example in English, `{"it": ..., "en": ...}`, because
  it teaches Italian *to English speakers*), this course follows the
  **English course's monolingual shape** — plain-string examples, no
  gloss language at all — because Spanish immersion means a Spanish
  learner never sees a translation crutch in the lesson content itself.
  Meaning is carried by simpler Spanish paraphrase, visual/contextual
  cues, and the exercises — not by translation. See the rewritten
  `curriculum/SCHEMA.md` (to be written) for the exact shape.
- **AI Teacher** replies only in Spanish (see §8) — no code-switching
  fallback to English or Portuguese, unlike the English course's
  Portuguese-support system prompt.
- A grep-based lint pass (`scripts/check_no_english.py`, to be added)
  will scan every generated HTML page for a denylist of common English
  function words in visible text nodes, as a last-mile safety net
  before each deploy.

## 6. Dictionary — Spanish–Spanish

Both sibling sites' "dictionary" is actually a **link-out hub**:
`dict-widget.js` rewrites a set of card links to `{word}`-templated URLs
of real external dictionaries as the user types — there's no
self-hosted definition database to fork. The Spanish version keeps that
same mechanism but swaps every card for a **monolingual Spanish** source
so no English ever appears, even one click away:

- **RAE — Diccionario de la lengua española** (`dle.rae.es`) — the
  canonical monolingual reference.
- **Wikcionario en español** (`es.wiktionary.org`)
- **Fundéu BBVA** (`fundeu.es`) — usage, style, common-error guidance.
- **Diccionario de sinónimos y antónimos** (WordReference's Spanish
  monolingual thesaurus, or `sinonimosonline.com`).
- **Conjugador de verbos en español** (e.g. `conjugacion.es` or
  SpanishDict's conjugator, which is monolingual for the tables
  themselves).
- **Forvo** (pronunciation audio, `forvo.com/word/{word}/#es`) — kept
  from the sibling sites, language-neutral by nature.

This is the one open design call worth flagging: WordReference,
SpanishDict and Linguee (used by both sibling sites) are hugely popular
learner tools but are bilingual (ES↔EN) by design — see the question
below.

## 7. Content to be created from scratch

- All 78 lesson bodies (objectives, explanation, rules, examples, common
  mistakes, exercises, summary) per §3.
- Spanish-specific pronunciation content: the alphabet, `ñ`, the
  tap/trill `r`/`rr` distinction, diphthongs, word stress and written
  accents (`tilde`), syllabification.
- The Spanish–Spanish dictionary page (§6).
- Listening/speaking material as dialogue/monologue transcripts (like
  the Italian course — no recorded audio in this phase; Forvo covers
  single-word pronunciation).
- A fully Spanish placement test and per-level "Ponte a prueba" review
  pages.
- `worker/course-catalog.json` (real lesson URLs) and the Spanish AI
  Teacher system prompt.
- Badge/achievement copy for the gamification system (`docs/gamification.md`
  equivalent).

## 8. AI Teacher — adapted for a Spanish-only environment

Forked from `curso-ingles/worker/worker.js`, same architecture
(Cloudflare Worker, Groq free tier, KV-based per-anon daily quota + per-IP
burst limit, deterministic keyword-matched course-catalog grounding so
the model can only ever link to a real page):

- System prompt rewritten entirely in Spanish, teaching persona "el
  asistente de IA de Clases de Español."
- **No bilingual fallback** — the English course's whole
  "reply in Portuguese if the student writes Portuguese" branch is
  dropped. This tutor answers in Spanish, always, regardless of what
  language the student writes in — gently redirecting ("Puedes
  escribirme en español, ¡así practicas más!") rather than
  code-switching, which is the one deliberate behavioral difference
  from the English course's design (worth confirming — see the
  question below, since a true beginner literally cannot ask a
  question in Spanish yet).
- Level-awareness, beginner-mode simplification, progressive teaching,
  exercise generation, and the "never invent a URL" grounding rule are
  all kept as-is — they're pedagogy patterns, not English-specific.
- $0 to deploy (Groq free tier + Cloudflare Workers free tier), but the
  Worker itself is **not part of the static GitHub Pages site** — like
  both sibling sites, it has to be deployed separately with your own
  Groq API key (`worker/README.md`, adapted, will carry the same
  step-by-step). I'll scaffold the code now; you deploy it when ready.

## 9. Naming, branding, domain/path strategy

- **Site name:** "Renan el Profesor — Academia de Español" (mirrors
  "Renan the Teacher — English Course" / "— Italian Language Academy").
- **Repo:** `clasesdeespanol` (created).
- **URL for now:** `https://renangrossi.github.io/clasesdeespanol/`
  (GitHub Pages, enabled). A custom domain is a zero-cost-compatible
  later step (a `CNAME` file + DNS you control) — not needed for
  launch.
- **Favicon/mark:** same SVG monogram mechanism as the sibling sites,
  recolored to the new palette (pending).

## 10. Recommended implementation order

1. ~~Scaffold repo structure, copy adaptable pipeline/CSS/JS, create +
   push GitHub repo, enable Pages~~ — **done, this commit.**
2. ~~Recolor `tokens.css` + `dark-mode.css` to the Spain/Argentina
   palette~~ — **done.**
3. ~~Full Spanish rewrite of `site_chrome.py` (nav, footer, meta, search
   overlay), `build_lesson.py`, `build_static_pages.py`, and a
   translation pass on JS user-facing strings (`main.js`,
   `search.js`)~~ — **done.**
4. ~~Write `curriculum/SCHEMA.md` (monolingual shape) and author
   `scripts/curriculum_source/pre-a1.py` + `a1.py` in full depth~~ —
   **done**, and extended straight to full depth on every level (see
   step 8) rather than stopping at a two-level proof-of-concept.
5. ~~Build `dictionary.html` (monolingual sources: RAE, Wikcionario,
   Fundéu BBVA, sinónimos, conjugador, Forvo), `placement-test.html`,
   `progress.html`, `today-review.html`, `simulated-exams.html`,
   homepage copy~~ — **done.**
6. Scaffold `worker/` (Spanish system prompt + catalog) — `worker/`
   currently only has `wrangler.toml` and a reference README copied
   from the English course; the Spanish system prompt and
   `course-catalog.json` still need to be written. Code only —
   deployment is left to you (needs your own Groq API key and
   Cloudflare account).
7. Push. `main` is 7 commits ahead of `origin/main` as of this pass —
   push and confirm the live Pages site end-to-end (not yet done in
   this session; ask before pushing, since it publishes the live URL).
8. ~~Author A2 → C2 (56 lessons)~~ — **done.** All 7 levels
   (Pre-A1 → C2, 78 lessons total) are now hand-authored at full depth
   and committed as separate per-level checkpoints. Along the way,
   `scripts/build_level_pages.py` — the level hub page generator — was
   found never to have been adapted from the Italian course at all (it
   still produced English UI strings, Italian vocabulary/reading/
   listening content, and silently dropped Pre-A1 from its hardcoded
   6-level loop, so `levels/pre-a1.html` never built even though the
   homepage linked to it). It's now fully rewritten in Spanish with
   original vocabulary/reading/listening/writing/speaking content for
   all 7 levels. `python3 scripts/build_all.py` now runs end-to-end
   with no errors and no broken internal links.
9. `check_no_english.py` lint pass (script itself still needs to be
   written — see §5's original description) + a final read-through for
   tone/CEFR accuracy before calling it "launched."

## 11. Risks and decisions needing your confirmation

- **Content depth for this pass** — 78 full lessons at sibling-site
  quality is a large authoring effort. See the question below for how
  much to complete now vs. stage as a visible roadmap.
- **Dictionary purity** (§6) — strictly monolingual-only sources, or
  keep 1–2 bilingual ES↔EN tools (WordReference, SpanishDict) as
  secondary cards the way both sibling sites do, since they're genuinely
  the most-used learner tools despite showing English.
- **AI Teacher language policy** (§8) — always reply in Spanish even to
  a true Pre-A1 beginner who can't yet write Spanish, or allow a
  narrow "explain in [any language] only for a first-contact question,
  then push back to Spanish" exception, closer to how the English
  course handles Portuguese.
- **AI Teacher deployment** — the Worker needs *your* Groq API key and
  Cloudflare account (steps in `worker/README.md`); I can't deploy it
  for you without those credentials, matching how the Italian course
  left it as a deliberate follow-up.
- **GitHub Pages is public** — `clasesdeespanol` is a public repo (Pages
  requires that on the free tier), same as both sibling sites.
- **No docx/pdf worksheets** — following the Italian course's cleaner,
  simpler pattern (every lesson authored directly, one pipeline, no
  hand-authored HTML exception) rather than the English course's
  legacy `cefr/*.docx` tree. Flag if you specifically want downloadable
  worksheets later — that's an additive feature, not a blocker.
