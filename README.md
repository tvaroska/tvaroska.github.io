# tvaroska.github.io

Source for [https://tvaroska.github.io](https://tvaroska.github.io): single-page technical monograph covering production Enterprise AI reference architectures, *No Demo Survives Production* writing and research, embedded OTA firmware ([`fleetforge`](https://github.com/tvaroska/fleetforge)), nonprofit robotics ([`FRC-Flux-Robotics`](https://github.com/FRC-Flux-Robotics)), career background, and personal-capacity advisory scope.

## Architecture

- Pure static HTML5 + semantic CSS (`index.html`, `styles.css`, `favicon.svg`, `og-card.png`, `.nojekyll`) served directly from the `main` branch root on GitHub Pages.
- Zero JavaScript frameworks, zero npm packages, zero Jekyll plugins, and zero `.github/workflows/`.
- Supports system light/dark mode (`prefers-color-scheme: dark`) with an explicit header toggle and `prefers-reduced-motion`.

## Verification

```bash
./scripts/test.sh
```
