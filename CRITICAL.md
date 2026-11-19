# CRITICAL.md — Protected Invariants (`tvaroska.github.io`)

1. **Public Front-Door Air Gap & Privacy (`ADR-005`):**
   - Everything in this repository is served publicly at `https://tvaroska.github.io`.
   - Never commit corporate customer names, engagement details, internal shortlinks/codenames, workstation filesystem paths, private personal cluster hostnames, or family/teen personal details.
2. **Employer Conflict-of-Interest Clarity:**
   - Keep external peer-exchange, nonprofit board, and independent advisory descriptions strictly scoped to **personal capacity** and explicitly outside competing cloud/AI vendor products and covered Financial Services accounts.
3. **Static Branch Publishing Only:**
   - GitHub Pages publishes directly from `/` on `main` with `.nojekyll`. Never reintroduce Jekyll (`_config.yml`) or `.github/workflows/`.
4. **Design & Copy Integrity:**
   - Obey [`.stitch/DESIGN.md`](.stitch/DESIGN.md): preserve `<link rel="icon">`, `og:image` (`og-card.png`), `tabular-nums`, `prefers-color-scheme: dark`, `prefers-reduced-motion`, and zero em-dashes, arrow tokens, or buzzwords.
