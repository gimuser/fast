# FAST — Méthode FAST

Repository for the French presentation on the FAST functional-analysis method.

## Files
- `Presentation_Methode_FAST.pptx`: source presentation committed at the repository root.
- `fast_generate.py`: reproducible Python editing/generation script.
- `FAST_Presentation_Methode_FAST.pptx`: expected generated output.
- `logo.png`: single user-requested logo asset; verify its presence on `main` before using it.

## Presentation context
- University: Université Sultan Moulay Slimane (USMS)
- Faculty: Faculté des Sciences Appliquées, Béni Mellal (FSA/FSABM)
- Field: Master Data Science et Sécurité des Systèmes d’Information
- Language and format: French, widescreen 16:9
- Oral duration: approximately 15–20 minutes, two presenters

## Generate the updated deck
Install:
```bash
python3 -m pip install python-pptx
```

Run from the repository root:
```bash
python3 fast_generate.py Presentation_Methode_FAST.pptx
```

Expected output: `FAST_Presentation_Methode_FAST.pptx`.

## Current status and next action
The source presentation `Presentation_Methode_FAST.pptx` is committed to `main`. The next requested edit is to integrate exactly one genuine image named `logo.png` into the presentation, preferably on the title slide, once that asset is confirmed present in the repository. Update `fast_generate.py`, regenerate and visually inspect the final deck, then commit the generator and generated PPTX to `main`.

Do not invent or redraw a logo. If `logo.png` is not present, ask the user to push it before proceeding. Preserve the French content, slide order, core FAST-method material, 16:9 format, and white backgrounds; avoid unrelated redesigns.
