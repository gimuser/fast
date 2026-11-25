# Instructions for ChatGPT and AI coding assistants

This repository maintains the **FAST method presentation** for the user's academic work.

## Project context
- Topic: the FAST functional-analysis method.
- Language: French.
- Presentation format: PowerPoint, 16:9.
- Intended duration: approximately 15–20 minutes, presented by two people.
- University: Université Sultan Moulay Slimane (USMS).
- Faculty: Faculté des Sciences Appliquées, Béni Mellal (FSA).
- Programme: Master Data Science et Sécurité des Systèmes d’Information.

## Files and source of truth
- `fast_generate.py` is the reproducible Python editing/generation script currently stored in this repository.
- `README.md` documents the current workflow and known missing assets.
- The original PowerPoint and generated final PowerPoint are not yet committed. Check the repository contents before assuming either file exists.
- Do not claim a PowerPoint has been generated, inspected, or committed unless that operation has actually succeeded.

## Rules when editing
1. Preserve the existing presentation's French language, 16:9 format, slide order, and core FAST-method content unless the user explicitly requests a change.
2. Keep the presentation suitable for a 15–20 minute, two-person oral presentation unless asked otherwise.
3. Keep slide backgrounds white when maintaining the current design requirement.
4. Do not fabricate, redraw as authentic, or mislabel official USMS/FSA logos. Use genuine image assets supplied by the user or official sources; otherwise use editable text labels.
5. Preserve the Python source code and update it whenever the generation workflow changes.
6. Update this repository's README when setup steps, files, or project status change.
7. Before replacing an existing file, inspect its current content and preserve unrelated work.
8. Prefer a dedicated branch and pull request for substantial changes. Direct commits to `main` are acceptable only when the repository owner explicitly asks for them.
9. After editing, report exactly which files changed, what was verified, and what remains incomplete.

## Reproducing the current deck
Install the dependency:

```bash
python3 -m pip install python-pptx
```

Run from the repository root after placing the original deck there:

```bash
python3 fast_generate.py Presentation_Methode_FAST.pptx
```

The output is `FAST_Presentation_Methode_FAST.pptx`. Optional genuine logo files:
- `assets/usms_logo.png`
- `assets/fsabm_logo.png`

If those assets are absent, the script intentionally uses text labels instead.
