# Lucent DS

Lucent is a design system: one set of design tokens and a glass-over-neumorphic surface language, built to hold up in a web app, a mobile or tablet surface, a document or presentation, and a spatial panel. Version 0.5.0.

## What is here

- `project/tokens.json` is the single source for every token.
- `export/` holds the generated files: `tokens.css`, light and dark token JSON, `typography.json`, `motion.json` and a manifest with checksums. Do not edit these by hand.
- `project/components/` holds the concept explorations, the locked Primary Direction, a dashboard and the site-structure components. Open any `preview.html` in a browser.
- `project/icons/` is a set of 1,383 single-ink outline icons as one SVG sprite, with a manifest and a grep-friendly index.
- `project/fonts/` holds Space Grotesk and Space Mono, each under the SIL Open Font License 1.1 (licence texts sit beside the files).
- `project/README.md` is the full brand and usage guide.

## Regenerating the export

```
python3 project/scripts/regen_tokens.py          # rebuild export/ from project/tokens.json
python3 project/scripts/regen_tokens.py --check  # fail if export/ is stale
python3 project/scripts/test_regen_tokens.py     # pipeline tests
```

## Notes

- A case study referenced by the `panel-*` tokens is not part of this release. Those tokens remain in the token set.
- No licence has been chosen for the system itself yet. Until one is added, all rights are reserved. The bundled fonts keep their own licence.
