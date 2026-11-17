"""Initial CI checks for planning files; standard library only."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
REQUIRED = [
    "README.md", "CONTRIBUTING.md", ".github/workflows/ci.yml",
    ".github/ISSUE_TEMPLATE/naloga.md", "lib/README.md",
    "assets/README.md", "test/README.md",
    "dokumentacija/00-nacrt-oddaje.md",
    "dokumentacija/01-opis-projekta.md",
    "dokumentacija/02-uporabniski-scenariji.md",
    "dokumentacija/03-podatkovni-model.md",
    "dokumentacija/04-arhitektura.md",
    "dokumentacija/05-organizacija-dela.md",
    "dokumentacija/06-prototip.md",
    "dokumentacija/07-zacetne-naloge.md",
    "dokumentacija/08-github-in-ci.md",
    "dokumentacija/diagrami/primeri-uporabe.svg",
    "dokumentacija/diagrami/primeri-uporabe.puml",
    "dokumentacija/mockupi/index.html",
    "dokumentacija/mockupi/pregled.svg",
]


def fail(path, message):
    ERRORS.append(f"{path.relative_to(ROOT).as_posix()}: {message}")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicates = set()
        self.links = []
        self.screens = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            value = attrs["id"]
            if value in self.ids:
                self.duplicates.add(value)
            self.ids.add(value)
            if tag == "section" and "screen" in attrs.get("class", "").split():
                self.screens.add(value)
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


def check_link(source, link, page=None):
    target = urlsplit(link)
    if target.scheme in {"http", "https", "mailto", "data", "tel"}:
        return
    if target.scheme or target.netloc:
        fail(source, f"unsupported link: {link}")
        return
    destination = (source.parent / unquote(target.path)).resolve() if target.path else source
    if not destination.is_relative_to(ROOT):
        fail(source, f"link leaves repository: {link}")
    elif not destination.exists():
        fail(source, f"missing link target: {link}")
    elif page and not target.path and target.fragment not in page.ids:
        fail(source, f"missing HTML id: {link}")


def main():
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file() or not path.stat().st_size:
            fail(path, "required file missing or empty")
    for folder in ("screens", "models", "services", "providers", "widgets"):
        path = ROOT / "lib" / folder
        if not path.is_dir():
            fail(path, "required Flutter folder missing")

    files = [path for path in ROOT.rglob("*") if path.is_file()
             and not any(part.startswith(".") for part in path.relative_to(ROOT).parts)]
    for path in files:
        if path.suffix not in {".md", ".svg", ".html"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
            if path.suffix == ".md":
                # Ignore examples inside code fences and inline code.
                prose = re.sub(r"```.*?```", "", content, flags=re.S)
                prose = re.sub(r"`[^`]+`", "", prose)
                for link in re.findall(r"\]\(([^)]+)\)", prose):
                    check_link(path, link)
            elif path.suffix == ".svg":
                root = ET.fromstring(content)
                if root.tag != "{http://www.w3.org/2000/svg}svg":
                    fail(path, "expected SVG root")
            else:
                page = Page()
                page.feed(content)
                for link in page.links:
                    check_link(path, link, page)
                if page.duplicates:
                    fail(path, f"duplicate HTML ids: {sorted(page.duplicates)}")
                expected = {"welcome", "today", "subjects", "new-task", "plan", "replan",
                            "focus", "progress", "settings", "material", "quiz"}
                if not expected.issubset(page.screens):
                    fail(path, f"missing prototype screens: {sorted(expected - page.screens)}")
        except (UnicodeError, ET.ParseError, ValueError) as error:
            fail(path, str(error))

    backlog = ROOT / "dokumentacija/07-zacetne-naloge.md"
    if backlog.is_file():
        sections = re.split(r"(?m)^## SF-", backlog.read_text(encoding="utf-8"))[1:]
        if len(sections) != 12:
            fail(backlog, "expected 12 initial issue drafts")
        for section in sections:
            for marker in ("**Prioriteta:** P", "**Odgovorna oseba:**", "**Merila sprejema:**", "**Odvisnosti:**"):
                if marker not in section:
                    fail(backlog, f"SF-{section[:2]} missing {marker}")

    if ERRORS:
        print("FAILED\n" + "\n".join(f"- {error}" for error in ERRORS))
        return 1
    print("PASS: required structure, local links, SVG, prototype routes and 12 issue drafts.")
    print("GitHub publication, collaborators, assignments and hosted CI need separate verification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
