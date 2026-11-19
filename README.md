# tvaroska.github.io

Source for [https://tvaroska.github.io](https://tvaroska.github.io): one-screen plain directory covering production Enterprise AI reference architectures, *No Demo Survives Production* writing and research, embedded OTA firmware ([`fleetforge`](https://github.com/tvaroska/fleetforge)), nonprofit robotics ([`FRC-Flux-Robotics`](https://github.com/FRC-Flux-Robotics)), and personal-capacity advisory scope.

## Architecture

- Pure static HTML5 + compact CSS (`index.html`, `styles.css`, `favicon.svg`, `og-card.png`, `.nojekyll`) served directly from the `main` branch root on GitHub Pages.
- Zero JavaScript, zero npm packages, zero Jekyll plugins, and zero `.github/workflows/`.
- Supports OS light/dark mode (`prefers-color-scheme: dark`) and `prefers-reduced-motion`.

## Verification

```bash
./scripts/test.sh
```
