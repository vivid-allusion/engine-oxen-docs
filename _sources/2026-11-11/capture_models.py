#!/usr/bin/env python3
"""Second pass: the per-model reference pages.

The llms.txt index lists one "Model API References" page; that page links every
model's own reference. Those links are the list, so this pass reads them from
the capture rather than re-deriving them.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from capture import destination, fetch

ROOT = Path(__file__).resolve().parent
INDEX_PAGE = ROOT / "inference-api/reference/model-references.md"
MANIFEST = ROOT / "manifest.json"


def main() -> int:
    text = INDEX_PAGE.read_text(encoding="utf-8")
    links = sorted(set(re.findall(r"\((https://docs\.oxen\.ai/inference-api/reference/models/[^)\s]+)\)", text)))
    print(f"{len(links)} model pages")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    known = {entry["url"] for entry in manifest["pages"]}
    added, failures = 0, []
    for url in links:
        if url in known:
            continue
        target = destination(url)
        try:
            body = fetch(url.rstrip("/") + ".md")
        except RuntimeError as exc:
            failures.append({"url": url, "error": str(exc)})
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f"---\nsource: {url}\n---\n\n" + body, encoding="utf-8")
        manifest["pages"].append({"title": "", "url": url, "path": str(target.relative_to(ROOT)),
                                  "bytes": len(body)})
        added += 1
    manifest["failures"] = manifest.get("failures", []) + failures
    MANIFEST.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print(f"added {added}, {len(failures)} failures")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
