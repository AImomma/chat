# My Codex Project

This repository is for working with Codex.

## Goal
Build and organize my project step by step.

## Tasks
- Add project files
- Ask Codex to improve or generate code
- Review Codex pull requests

## Royalti Studios — Prompt Packs

Released packs live in their audience-line folder; the generator, catalog and
changelog live in `_generator/`.

- `Adult Fiction Line/` — released pack PDFs
- `_generator/pack_builder.py` — branded PDF builder (requires `reportlab`)
- `_generator/*_pack_data.py` — per-pack content files
- `_generator/pack_catalog.md` — roadmap and release status
- `_generator/CHANGELOG.md` — release and amendment log
- `_generator/versions/` — archived PDFs and data snapshots

Rebuild a pack:

```
cd _generator
python pack_builder.py <pack>_pack_data "../<Line>/<Name>_v<VERSION>.pdf"
```
