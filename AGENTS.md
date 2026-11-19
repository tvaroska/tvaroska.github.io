# AGENTS.md — `tvaroska.github.io`

Personal technical and executive homepage served at `https://tvaroska.github.io` directly from the `main` branch root (`.nojekyll`, static HTML5 + CSS).

## 1. Repository Map

- [`index.html`](index.html) — Single-page Swiss Technical Monograph covering Enterprise AI reference systems, *No Demo Survives Production* writing and research, embedded firmware (`fleetforge`) and FLUX Robotics (`FRC Team 10413`), career history, and conflict-clean personal advisory scope.
- [`styles.css`](styles.css) — Semantic token stylesheet (`:root` light + `prefers-color-scheme: dark` / `[data-theme]` override, `tabular-nums`, responsive asymmetric Swiss grid).
- [`favicon.svg`](favicon.svg) & [`og-card.svg`](og-card.svg) / [`og-card.png`](og-card.png) — High-contrast tab monogram icon and `1200x630` OpenGraph preview image.
- [`.stitch/DESIGN.md`](.stitch/DESIGN.md) — Locked visual identity, semantic tokens, and negative design constraints.
- [`CRITICAL.md`](CRITICAL.md) & [`DECISIONS.md`](DECISIONS.md) — Air-gap, COI, publishing, and architectural invariants.
- [`tests/test_repo_hygiene.py`](tests/test_repo_hygiene.py) — Deterministic HTML, link, air-gap, anti-slop, and asset verification suite.

## 2. Invariants & Verification

1. **Zero Build Bloat & Zero GitHub Actions:** Serve pure static files from `main` with `.nojekyll`. Never add `.github/workflows/`, Jekyll `_config.yml`, or npm/bundler toolchains.
2. **Air Gap, Privacy & COI Guardrails:** Keep 100% free of corporate customer names, internal identifiers, private personal cluster URLs, and family/student details. All advisory copy must explicitly state personal-capacity and conflict-of-interest boundaries.
3. **Voice & Anti-Slop Discipline:** First-person Boris voice, plain systems nouns, **Ports, Adapters, and Contracts** terminology, zero Unicode em-dashes, zero arrow tokens, and zero banned AI buzzwords.
4. **Verification Gate:** Run `python3 -m unittest discover -s tests -v` (or `proj-test tvaroska.github.io`) before committing.
