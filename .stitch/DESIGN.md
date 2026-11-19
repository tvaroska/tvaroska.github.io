# Visual Design Contract (`.stitch/DESIGN.md`) — `tvaroska.github.io`

## 1. Identity & Category

- **Surface:** Personal technical & executive homepage (`https://tvaroska.github.io`)
- **Aesthetic Direction:** **Swiss Technical Monograph** (crisp typographic index grid, architectural hairline borders, empirical receipt strips, zero marketing fluff)
- **Stack:** Pure static HTML5 + semantic CSS custom properties (`index.html`, `styles.css`, `favicon.svg`, `og-card.png`, `.nojekyll`) with zero JavaScript frameworks, zero npm dependencies, and zero GitHub Actions workflows.

## 2. Semantic Color Tokens (`:root` Light + `prefers-color-scheme: dark`)

### Light Mode (Default — Architectural Paper & Carbon Ink)
- `--surface`: `#f8f9fa`
- `--surface-container`: `#ffffff`
- `--surface-container-low`: `#f1f3f4`
- `--on-surface`: `#14171a`
- `--on-surface-variant`: `#4b525a`
- `--on-surface-muted`: `#69717a`
- `--outline`: `#14171a`
- `--outline-variant`: `#dadce0`
- `--primary`: `#1a73e8`
- `--primary-subtle`: `#e8f0fe`
- `--status-ok-fg`: `#137333`
- `--status-ok-bg`: `#e6f4ea`

### Dark Mode (`@media (prefers-color-scheme: dark)` / `[data-theme="dark"]` — Carbon Slate, Zero Purple)
- `--surface`: `#0d1117`
- `--surface-container`: `#151b23`
- `--surface-container-low`: `#1c232d`
- `--on-surface`: `#e6edf3`
- `--on-surface-variant`: `#9ca3af`
- `--on-surface-muted`: `#7d8590`
- `--outline`: `#e6edf3`
- `--outline-variant`: `#2a323d`
- `--primary`: `#58a6ff`
- `--primary-subtle`: `#16263b`
- `--status-ok-fg`: `#3fb950`
- `--status-ok-bg`: `#12261e`

## 3. Typography & Layout Rules

- **Sans Stack:** `"Google Sans", "Inter Variable", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif`
- **Mono Stack:** `"JetBrains Mono Variable", "JetBrains Mono", "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, monospace`
- **Numeric Discipline:** Apply `font-variant-numeric: tabular-nums` on all section numbers (`01`..`05`), metric strips, dates, and ledger rows.
- **Grid:** `1040px` max-width container with `1.5px solid var(--outline)` masthead rule and asymmetric `220px` index rail + `1fr` content column (`<= 820px` collapses cleanly to a single column).
- **Motion & Favicon:** Respect `@media (prefers-reduced-motion: reduce)` and ship high-contrast `favicon.svg` + `1200x630` `og-card.png`.

## 4. Do Not Generate (Hard Negative Constraints)

- No SaaS hero biscuit pills or pulsing status dots above `<h1>`.
- No CSS gradient text fills on headlines or keywords.
- No purple or violet accents in dark mode.
- No decorative left-edge or top-edge colored accent bars on cards.
- No icon-stuffed bento boxes or icon-in-circle KPI headers.
- No SVG noise/grain overlays (`feTurbulence`) or grid-line backgrounds.
- No Unicode em-dashes, arrow tokens (`->`), or corporate AI buzzwords (*delve, leverage, utilize, orchestrate, paradigm, synergy, ecosystem, landscape, seamless, holistic, pivotal, crucial*).
