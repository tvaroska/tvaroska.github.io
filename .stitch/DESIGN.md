# Visual Design Contract (`.stitch/DESIGN.md`) — `tvaroska.github.io`

## 1. Identity & Category

- **Surface:** Personal directory (`https://tvaroska.github.io`)
- **Aesthetic Direction:** **One-Screen Plain Directory** (*Mitchell Hashimoto / Russ Cox restraint*: single `660px` column, `~225` words total, zero vertical scroll on a `1440x900` laptop viewport, zero cards, zero JavaScript).
- **Stack:** Pure static HTML5 + ~95 lines of CSS (`index.html`, `styles.css`, `favicon.svg`, `og-card.png`, `.nojekyll`).

## 2. Semantic Color Tokens (`:root` Light + `prefers-color-scheme: dark`)

### Light Mode
- `--surface`: `#fcfcfb`
- `--surface-container`: `#f4f4f2`
- `--on-surface`: `#141413`
- `--on-surface-variant`: `#4a4a46`
- `--on-surface-muted`: `#73736d`
- `--outline-variant`: `#e2e2dd`
- `--primary`: `#0b57d0`

### Dark Mode (`@media (prefers-color-scheme: dark)`)
- `--surface`: `#111214`
- `--surface-container`: `#1a1c1f`
- `--on-surface`: `#e6e6e3`
- `--on-surface-variant`: `#a3a39e`
- `--on-surface-muted`: `#787873`
- `--outline-variant`: `#26292e`
- `--primary`: `#6cb6ff`

## 3. Typography & Layout Rules

- **Sans Stack:** `-apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", system-ui, sans-serif`
- **Mono Stack:** `"JetBrains Mono", "SFMono-Regular", ui-monospace, Menlo, Consolas, monospace`
- **Single-Viewport Budget:** `<= 260` visible words, `max-width: 660px`, unbordered `175px 1fr` directory rows with `tabular-nums`, fitting completely inside `1440x900` without scrolling.

## 4. Do Not Generate (Hard Negative Constraints)

- Zero bordered cards, boxes, KPI stat strips, pill buttons, status badges, or SVG social icons.
- Zero `01 / SECTION` uppercase eyebrows, top coordinate bars, navigation bars, or theme-switcher buttons.
- Zero multi-column SaaS feature grids, gradient text, or purple dark-mode accents.
- Zero Unicode em-dashes, arrow tokens (`->`), raw Markdown backticks, or AI buzzwords.
