# DECISIONS.md — Architectural Decision Log (`tvaroska.github.io`)

## ADR-001: Replace Legacy Jekyll Blog with Static GitHub Pages Site (`2026-11-19`)

- **Context:** The legacy `master` branch ran `jekyll-theme-minimal` with outdated bio copy, an empty `dev-vm-setup` page, and an unused 2019 Pelican `content` branch, while active writing moved to biweekly *No Demo Survives Production* essays on Substack and weekly Tuesday Lab Notes on LinkedIn.
- **Decision:** Replace Jekyll and multi-branch remnants with static HTML5 + CSS on `main` (`.nojekyll`, zero npm dependencies, zero `.github/workflows/`), verified via `tests/test_repo_hygiene.py`.

## ADR-002: Adopt One-Screen Plain Directory Over Multi-Card Monograph (`2026-11-19`)

- **Context:** The initial multi-section monograph (`01 / ARCHITECTURE` monospace eyebrows, 4-cell KPI strip, 2x2 white cards on `#f8f9fa`, pill buttons, and `~700` words) read like an AI-generated SaaS landing page rather than a real Principal Architect's homepage.
- **Decision:** Switch to **Option 3 (One-Screen Directory)**: single column (`<= 260` words, zero JavaScript, `< 160` lines of CSS), zero cards/pills/badges/icons, fitting completely inside a `1440x900` laptop viewport without scrolling.
- **Consequences:** Eliminates generated-portfolio visual clichés and treats GitHub and LinkedIn as the detail layers rather than duplicating them on the landing page.
