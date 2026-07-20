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
| `units/gears-and-ratios.html` | **Folio 01** — ratio, π, and gear trains: rover-race fail lab, rim-unrolling π lab, drivetrain-designer assessment |
| `units/angles-that-reach.html` | **Folio 05** — trigonometry via robot-arm inverse kinematics: 3 interactive labs, 5 portrait plaques |
| `curriculum.md` | The master skeleton: every unit's robotics hook, giants, artifact formula, planned lab, plus the five design invariants |
| `assets/img/portraits/` | 22 mathematician portraits pulled from the offline Wikipedia archive |
| `assets/img/diagrams/` | edu-style diagrams + gold formula SVGs, generated locally |
| `tools/fetch_portraits.py` | CLIP-search the `wikipedia_images` index (6.8M images), extract via libzim — run with `py -3.11` |
| `tools/fetch_from_article.py` | Fallback: pull a person's infobox image straight from their Wikipedia article |
| `tools/make_diagrams.py` | Regenerate diagrams (`ultrapc.diagrams` edu style) and formula SVGs (matplotlib mathtext, no KaTeX) |

## Building the next unit

1. Add the unit's diagrams/formulas to `tools/make_diagrams.py`, run it.
2. Fetch any new giants with `tools/fetch_portraits.py` (add to `WANTED`).
3. Copy `units/angles-that-reach.html` as the template — keep the five-act
   structure (fail → history → idea → lab → payoff) and the design invariants
   listed at the bottom of `curriculum.md`.
4. Flip the unit's card in `index.html` from `planned` to `open` by giving it
   an `href` in the `STAGES` data.
