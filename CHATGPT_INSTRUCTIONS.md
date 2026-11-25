# Instructions for ChatGPT and AI coding assistants

This repository maintains the FAST-method presentation for the user's academic work. Continue from the actual files on the `main` branch; do not assume earlier tasks are still pending without checking GitHub.

## Project context
- Topic: FAST functional-analysis method.
- Language: French; PowerPoint format 16:9.
- Intended duration: approximately 15–20 minutes, presented by two people.
- University: Université Sultan Moulay Slimane (USMS).
- Faculty: Faculté des Sciences Appliquées, Béni Mellal (FSA/FSABM).
- Programme: Master Data Science et Sécurité des Systèmes d’Information.

## Current repository state (verify before editing)
- `Presentation_Methode_FAST.pptx` is the source presentation committed at the repository root.
- `fast_generate.py` is the editable/reproducible Python generation script.
- `README.md` documents the workflow.
- The user requested one logo asset named exactly `logo.png` at the repository root. Check whether it has actually been committed before using it. Do not assume it exists.
- The generated output filename is `FAST_Presentation_Methode_FAST.pptx`.

## Next task requested by the user
1. Inspect the latest `Presentation_Methode_FAST.pptx` and the actual root contents of `main`.
2. If the genuine `logo.png` is present, inspect it and integrate this single logo into the presentation in an appropriate, unobtrusive position (normally the title slide). Do not add two separate institutional logos or invent any logo.
3. If `logo.png` is absent, do not fabricate or substitute an image. Ask the user to upload/push that exact file, then continue.
4. Update `fast_generate.py` so the change is reproducible and uses the root-level `logo.png` (only if it exists); keep a graceful text-only fallback if absent.
5. Preserve the French content, original slide order, core FAST-method content, 16:9 format, and white-background design. Avoid covering titles, diagrams, or existing content. Do not make unrelated redesigns.
6. Generate `FAST_Presentation_Methode_FAST.pptx`, inspect the resulting slides for placement/overlap, and commit the updated generator and final PPTX to `main` only after verification.

## Editing rules
- Never fabricate, redraw as authentic, or mislabel official logos. Use only the genuine user-supplied asset.
- Preserve unrelated work and inspect existing files before replacing them.
- Keep the Python source synchronized with every generation change.
- Update this file and `README.md` when project status or workflow changes.
- Direct commits to `main` are authorized by the repository owner for this task.
- Report exactly which files changed, what was verified, and what remains incomplete. Never claim a file was uploaded, inspected, or generated unless it actually was.

## Reproducing the current deck
Install the dependency:
```bash
python3 -m pip install python-pptx
```

Run from the repository root:
```bash
python3 fast_generate.py Presentation_Methode_FAST.pptx
```

Expected output: `FAST_Presentation_Methode_FAST.pptx`.
