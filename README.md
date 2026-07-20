# Giants & Gears

A robotics-first mathematics curriculum, middle school → graduate, built as a
fully self-contained interactive site in a *da Vinci codex* style — parchment,
iron-gall ink, red chalk, hand-drawn "DaVinci Ink" diagrams, and interactive
labs where the simulation itself is the assessment.

Built by the CSUSB robotics group. Every unit obeys five invariants: the robot
fails first · history is load-bearing · one artifact formula per unit · the lab
is the assessment · everything runs without a network.

**View it:** open `index.html` in any browser (or run `serve.cmd` for a local
server). The site is static and fully offline-capable.

**Image credits:** portraits and artifact photos are drawn from Wikipedia /
Wikimedia Commons and retain their original licenses (largely public-domain
artworks; photographs may be CC-BY-SA — see the corresponding Wikipedia
articles for attribution).

## What's here

| Path | What |
|------|------|
| `index.html` | The codex map — 6 stages, 26 folios |
| `units/gears-and-ratios.html` | **Folio 01** — ratio, π, gear trains: rover-race fail, rim-unrolling π lab, drivetrain designer |
| `units/the-robots-map.html` | **Folio 02** — signed numbers & coordinates: counting-only fail, number-line road, signed dispatcher |
| `units/the-unknown.html` | **Folio 03** — linear equations & al-jabr: guessing crash, balance scale, solve-then-drive |
| `units/rigid-triangles.html` | **Folio 04** — Pythagoras & distance: eyeball fail, literal squares, fly-home-by-theorem |
| `units/angles-that-reach.html` | **Folio 05** — trigonometry via robot-arm inverse kinematics: 3 interactive labs |
| `curriculum.md` | The master skeleton: every unit's robotics hook, giants, artifact formula, planned lab, plus the five design invariants |
| `assets/img/portraits/` | mathematician portraits & artifacts pulled from the offline Wikipedia archive |
| `assets/img/diagrams/` | DaVinci Ink hand-drawn diagrams + ink formula SVGs, generated locally |
| `tools/fetch_portraits.py` | CLIP-search the `wikipedia_images` index (6.8M images), extract via libzim — run with `py -3.11` |
| `tools/fetch_from_article.py` | Fallback: pull a person's infobox image straight from their Wikipedia article |
| `tools/fetch_named_image.py` | Pull a *specific* image from an article by filename substring |
| `tools/make_diagrams.py` | Regenerate DaVinci Ink diagrams (`ultrapc.diagrams.ink_*`) and formula SVGs (matplotlib mathtext, no KaTeX) |

**Stage I — "Making a Machine Move at All" — is complete** (Folios 01–04, plus
05 from Stage II as the pilot). Folios 06–26 are mapped in `curriculum.md` and
shown "in preparation" on the codex map.

## Building the next unit

1. Add the unit's diagrams/formulas to `tools/make_diagrams.py`, run it.
2. Fetch any new giants with `tools/fetch_portraits.py` (add to `WANTED`).
3. Copy any Stage I unit (e.g. `units/the-robots-map.html`) as the template —
   keep the five-act structure (fail → history → idea → lab → payoff), the
   ink-on-parchment canvas palette, and the design invariants listed at the
   bottom of `curriculum.md`.
4. Flip the unit's card in `index.html` from `planned` to `open` by giving it
   an `href` in the `STAGES` data, and point the previous folio's "continue"
   link at it.
