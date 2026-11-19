"""Repository hygiene, air-gap, anti-slop, and one-screen restraint tests for tvaroska.github.io."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parent.parent

EXCLUDED_DIRS = {".git", "__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache", ".venv"}
TEXT_SUFFIXES = {".html", ".css", ".svg", ".md", ".txt", ".xml", ".sh", ".py"}
TEXT_NAMES = {".gitignore", ".nojekyll"}

FORBIDDEN_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("Hardcoded workstation path", re.compile(r"/usr/local/" + r"google/home|\.c\.googlers\.com")),
    ("File URI scheme", re.compile(r"file:///")),
    ("Internal Buganizer ID", re.compile(r"\bb/\d{6,}\b")),
    ("Internal shortlink", re.compile(r"\bgo/(?!mod\b|sum\b|work\b|version\b|test\b|build\b|run\b)[a-zA-Z0-9_-]{3,}")),
    ("Internal monorepo path", re.compile(r"//depot/" + r"google3|\bgoogle3\b")),
    ("Cross-workspace tilde path", re.compile(r"~/" + r"customers|~/notes|~/ideas|~/robotics|~/projects")),
    ("Private cluster subdomain", re.compile(r"\b(?:boris|drill|update|download)\.tvaroska\.sk\b")),
    ("Cookie-gated GCS URL", re.compile(r"https://storage\.cloud\.google\.com/")),
]

BANNED_BUZZWORDS_RE = re.compile(
    r"\b(?:delve|leverage|utilize|orchestrate|paradigm|synergy|ecosystem|landscape|seamless|holistic|pivotal|crucial|seam|seams)\b",
    re.IGNORECASE,
)


class _PageInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1_count = 0
        self.script_count = 0
        self.title_text = ""
        self.body_chunks: list[str] = []
        self._in_title = False
        self._in_body = False
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.meta_names: set[str] = set()
        self.meta_props: set[str] = set()
        self.has_favicon = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {k: (v or "") for k, v in attrs}
        if "id" in attr_map and attr_map["id"]:
            self.ids.add(attr_map["id"])
        if tag == "h1":
            self.h1_count += 1
        elif tag == "body":
            self._in_body = True
        elif tag == "script":
            self.script_count += 1
        elif tag == "title":
            self._in_title = True
        elif tag == "a" and "href" in attr_map:
            self.links.append(attr_map["href"])
        elif tag == "link":
            rel = attr_map.get("rel", "")
            href = attr_map.get("href", "")
            if "icon" in rel and href:
                self.has_favicon = True
            if href:
                self.links.append(href)
        elif tag == "meta":
            if attr_map.get("name"):
                self.meta_names.add(attr_map["name"])
            if attr_map.get("property"):
                self.meta_props.add(attr_map["property"])

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "body":
            self._in_body = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_text += data
        elif self._in_body:
            self.body_chunks.append(data)


def _iter_repo_text_files() -> list[Path]:
    out: list[Path] = []
    for p in sorted(REPO_ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel_parts = p.relative_to(REPO_ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if rel_parts == ("tests", "test_repo_hygiene.py"):
            continue
        if p.name in TEXT_NAMES or p.suffix.lower() in TEXT_SUFFIXES:
            out.append(p)
    return out


class RepoHygieneTests(unittest.TestCase):
    def test_governance_spine_and_static_pages_invariants(self) -> None:
        self.assertFalse((REPO_ROOT / ".github" / "workflows").exists(), "Zero .github/workflows/ allowed")
        self.assertFalse((REPO_ROOT / "_config.yml").exists(), "Legacy Jekyll _config.yml must stay removed")
        self.assertTrue((REPO_ROOT / ".nojekyll").is_file(), ".nojekyll required for pure static GitHub Pages")
        self.assertTrue((REPO_ROOT / ".stitch" / "DESIGN.md").is_file(), ".stitch/DESIGN.md required")
        self.assertTrue((REPO_ROOT / "og-card.png").is_file(), "og-card.png required for social link previews")

        agents = REPO_ROOT / "AGENTS.md"
        claude = REPO_ROOT / "CLAUDE.md"
        critical = REPO_ROOT / "CRITICAL.md"
        decisions = REPO_ROOT / "DECISIONS.md"
        self.assertTrue(agents.is_file() and agents.stat().st_size < 24_000)
        self.assertTrue(claude.is_symlink() and claude.readlink() == Path("AGENTS.md"))
        self.assertTrue(critical.is_file() and critical.stat().st_size <= 10_000)
        self.assertTrue(decisions.is_file() and decisions.stat().st_size <= 25_000)

    def test_airgap_and_portability_cleanliness(self) -> None:
        files = _iter_repo_text_files()
        self.assertGreaterEqual(len(files), 8)
        for path in files:
            content = path.read_text(encoding="utf-8")
            for label, pat in FORBIDDEN_PATTERNS:
                match = pat.search(content)
                self.assertIsNone(
                    match,
                    f"{label} leak in {path.relative_to(REPO_ROOT)}: {match.group(0) if match else ''}",
                )

    def test_index_html_one_screen_restraint_and_anti_slop(self) -> None:
        html_text = (REPO_ROOT / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("\u2014", html_text, "Unicode em-dash prohibited on public surface")
        self.assertNotIn("->", html_text, "ASCII arrow token prohibited on public surface")
        self.assertNotIn("\u2192", html_text, "Unicode right-arrow prohibited on public surface")
        self.assertNotIn("`", html_text, "Raw Markdown backtick prohibited in HTML")

        buzz = BANNED_BUZZWORDS_RE.search(html_text)
        self.assertIsNone(buzz, f"Banned buzzword in index.html: {buzz.group(0) if buzz else ''}")

        inspector = _PageInspector()
        inspector.feed(html_text)
        self.assertEqual(inspector.h1_count, 1, "Page must contain exactly one <h1>")
        self.assertEqual(inspector.script_count, 0, "Zero JavaScript needed on one-screen directory")
        self.assertIn("Boris Tvaroska", inspector.title_text)
        self.assertNotIn("&", inspector.title_text)
        self.assertTrue(inspector.has_favicon, "High-contrast favicon link required")
        self.assertIn("description", inspector.meta_names)
        for og in ("og:title", "og:description", "og:image", "og:url"):
            self.assertIn(og, inspector.meta_props)

        visible_words = " ".join(inspector.body_chunks).split()
        self.assertLessEqual(
            len(visible_words),
            260,
            f"One-screen directory exceeded 260-word budget ({len(visible_words)} words)",
        )

        for href in inspector.links:
            if href.startswith("#"):
                target_id = href[1:]
                self.assertIn(target_id, inspector.ids, f"Broken anchor href #{target_id}")
            elif not href.startswith(("https://", "mailto:")):
                self.assertFalse(href.startswith("http://"), f"Insecure http:// link: {href}")
                local_target = REPO_ROOT / href.split("#", 1)[0]
                self.assertTrue(local_target.is_file(), f"Missing local asset {href}")

    def test_xml_and_svg_assets_parse_cleanly(self) -> None:
        for xml_name in ("favicon.svg", "og-card.svg", "sitemap.xml"):
            ET.parse(REPO_ROOT / xml_name)

    def test_css_minimalism_and_calm_ux_rules(self) -> None:
        css = (REPO_ROOT / "styles.css").read_text(encoding="utf-8")
        self.assertLessEqual(len(css.splitlines()), 160, "Keep CSS compact (<160 lines) to prevent component bloat")
        for required_token in (
            "--surface:",
            "--surface-container:",
            "--on-surface:",
            "--primary:",
            "prefers-color-scheme: dark",
            "prefers-reduced-motion: reduce",
            "tabular-nums",
        ):
            self.assertIn(required_token, css)


if __name__ == "__main__":
    unittest.main()
