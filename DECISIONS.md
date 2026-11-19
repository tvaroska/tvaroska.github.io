# DECISIONS.md — Architectural Decision Log (`tvaroska.github.io`)

## ADR-001: Replace Legacy Jekyll Blog with Static Single-Page Monograph (`2026-11-19`)

- **Context:** The legacy `master` branch ran `jekyll-theme-minimal` with outdated bio copy, an empty `dev-vm-setup` page, and an unused 2019 Pelican `content` branch, while active writing moved to biweekly *No Demo Survives Production* essays on Substack and weekly Tuesday Lab Notes on LinkedIn.
- **Decision:** Replace Jekyll and multi-branch remnants with a pure static HTML5 + semantic CSS single-page Swiss Technical Monograph on `main` (`.nojekyll`, zero JS framework/npm dependencies, zero `.github/workflows/`), acting as a durable canonical index across Enterprise AI reference platforms, writing/research, embedded/robotics work, background, and personal-capacity advisory scope.
- **Consequences:** Sub-100ms page loads, zero dependency churn, zero duplicate blog maintenance, and deterministic validation via `tests/test_repo_hygiene.py`.
