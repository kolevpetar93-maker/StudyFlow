"""Check starter files and local documentation links without extra packages."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "pubspec.yaml", "pubspec.lock", "lib/main.dart", "test/app_test.dart",
    ".github/workflows/ci.yml", "dokumentacija/README.md",
    "dokumentacija/01-projekt.md", "dokumentacija/02-tehnicna-zasnova.md",
    "dokumentacija/03-nacrt-dela.md", "dokumentacija/04-razvoj-in-github.md",
    "dokumentacija/DPU/README.md", "dokumentacija/mockupi/README.md",
    "dokumentacija/mockupi/index.html", "dokumentacija/mockupi/pregled.svg",
    "dokumentacija/mockupi/pregled.png",
] + [f"dokumentacija/mockupi/slike/{name}.svg" for name in (
    "01-domov", "02-predmeti", "03-nacrt", "04-nova-naloga", "05-fokus", "06-napredek",
)]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.targets.append(value)


def main():
    errors = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file() or not path.stat().st_size:
            errors.append(f"Missing or empty file: {name}")
    for name in ("screens", "models", "services", "providers", "widgets"):
        if not (ROOT / "lib" / name).is_dir():
            errors.append(f"Missing folder: lib/{name}")

    # Inspect only project documentation, not generated SDK/build files.
    files = [ROOT / "README.md", *(ROOT / "dokumentacija").rglob("*")]
    for path in files:
        if not path.is_file() or path.suffix not in {".md", ".html", ".svg"}:
            continue
        label = path.relative_to(ROOT).as_posix()
        try:
            content = path.read_text(encoding="utf-8")
            targets = []
            if path.suffix == ".md":
                prose = re.sub(r"```.*?```|`[^`]+`", "", content, flags=re.S)
                targets = re.findall(r"\]\(([^)]+)\)", prose)
            elif path.suffix == ".html":
                parser = Links()
                parser.feed(content)
                targets = parser.targets
            else:
                if ET.fromstring(content).tag != "{http://www.w3.org/2000/svg}svg":
                    errors.append(f"{label}: invalid SVG root")
            for link in targets:
                url = urlsplit(link)
                if url.scheme in {"https", "http", "mailto", "data"}:
                    continue
                destination = (path.parent / unquote(url.path)).resolve() if url.path else path
                if url.scheme or url.netloc or not destination.is_relative_to(ROOT):
                    errors.append(f"{label}: unsupported target {link}")
                elif not destination.exists():
                    errors.append(f"{label}: missing target {link}")
        except (UnicodeError, ValueError, ET.ParseError) as error:
            errors.append(f"{label}: {error}")
    if errors:
        print("FAILED\n" + "\n".join(errors))
        return 1
    print("PASS: starter structure, local documentation links and SVG mockups.")
    print("Team DPU, GitHub publication, assignments and hosted CI remain separate steps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
