#!/usr/bin/env bash
# Canonical verification gate for tvaroska.github.io.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

export PYTHONDONTWRITEBYTECODE=1
exec python3 -m unittest discover -s tests -v "$@"
