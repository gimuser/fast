# FAST — Méthode FAST

Repository for the French presentation on the FAST functional-analysis method.

## Files
- `Presentation_Methode_FAST.pptx`: source presentation committed at the repository root.
- `fast_generate.py`: reproducible Python editing/generation script.
- `FAST_Presentation_Methode_FAST.pptx`: generated presentation output.
- `logo.png`: real logo asset reserved for a later update; it is intentionally not inserted yet.

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

## Current status
The generator now places one neutral `LOGO — À INSÉRER` placeholder on the title slide. The actual `logo.png` file is deliberately deferred until a later update. The generator preserves the source slide order, dimensions, backgrounds, and existing content. It also corrects title-slide contrast and restores readable text contrast on the summary slide (slide 11). The generated PowerPoint has been built, validated as a 12-slide 16:9 deck, and visually checked.

Do not fabricate or imitate an official logo. Preserve the French content, original slide order, core FAST-method material, 16:9 format, and white-background design. Avoid covering existing titles, diagrams, or content.
