#!/usr/bin/env python3
"""Capture the Oxen.ai documentation as markdown, one file per page.

Source of truth is the site's own llms.txt index: every line names the page and
the .md twin Mintlify serves. Output mirrors the URL path so a diff between two
captures is readable.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = "https://docs.oxen.ai/llms.txt"
UA = "engine-oxen-docs/0.1 (documentation capture)"


def fetch(url: str, attempts: int = 3) -> str:
    last = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(request, timeout=45) as response:
                return response.read().decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"{url}: {last}")


def pages(index_text: str) -> list[tuple[str, str]]:
    """(title, url) for every documentation page in the index, in index order."""
    found: list[tuple[str, str]] = []
    seen: set[str] = set()
    for line in index_text.splitlines():
        match = re.match(r"^- \[(.+?)\]\((https://docs\.oxen\.ai/[^)]+?)(?:\.md)?\)", line)
        if not match:
            continue
        title, url = match.group(1), match.group(2)
        if url.rstrip("/") in seen:
            continue
        seen.add(url.rstrip("/"))
        found.append((title, url))
    return found


def destination(url: str) -> Path:
    path = url.removeprefix("https://docs.oxen.ai/").strip("/")
    return ROOT / (path + ".md")


def main() -> int:
    index_text = fetch(INDEX)
    (ROOT / "llms.txt").write_text(index_text, encoding="utf-8")
    entries = pages(index_text)
    print(f"{len(entries)} pages in the index")
    manifest = []
    failures = []
    for number, (title, url) in enumerate(entries, 1):
        target = destination(url)
        source = url if url.endswith(".md") else url.rstrip("/") + ".md"
        try:
            text = fetch(source)
        except RuntimeError as exc:
            failures.append({"url": url, "error": str(exc)})
            print(f"  FAIL {url}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        header = f"---\ntitle: {json.dumps(title)}\nsource: {url}\n---\n\n"
        target.write_text(header + text, encoding="utf-8")
        manifest.append({"title": title, "url": url, "path": str(target.relative_to(ROOT)),
                         "bytes": len(text)})
        if number % 20 == 0:
            print(f"  {number}/{len(entries)}")
    (ROOT / "manifest.json").write_text(
        json.dumps({"source": INDEX, "pages": manifest, "failures": failures}, indent=1),
        encoding="utf-8")
    print(f"wrote {len(manifest)} pages, {len(failures)} failures")
    for failure in failures:
        print("  failed:", failure["url"], failure["error"])
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
