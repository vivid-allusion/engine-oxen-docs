# Oxen.ai docs — capture 2026-11-11

Full English documentation from <https://docs.oxen.ai>, saved as markdown.

- **427 pages**: 208 from the site's own `llms.txt` index, plus 219 per-model
  reference pages reached from the "Model API References" page.
- Every page is the markdown twin Mintlify serves (`<url>.md`), with a small
  YAML header naming the source URL.
- `llms.txt` is kept verbatim at the root of this folder; `manifest.json` lists
  every page with its URL and byte size, and any fetch that failed.
- Files mirror the URL path, so `inference-api/reference/models/flux-2-pro.md`
  is `https://docs.oxen.ai/inference-api/reference/models/flux-2-pro`.

## Why these two passes

The index names whole sections, not the per-model pages, and the per-model
pages are where the parameter tables live — the only honest source for a
catalogue entry. The second pass reads its list from the captured
`model-references.md` rather than guessing URL patterns, so a model the site
does not link cannot appear.

## Re-run

```
python3 capture.py          # index pages
python3 capture_models.py   # per-model reference pages
```

Both are idempotent: an existing page is overwritten with today's text, and the
second pass skips URLs already in the manifest.

One model page failed to fetch on this run; it is listed under `failures` in
`manifest.json` rather than silently omitted.
