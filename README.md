# FAST — Méthode FAST

Repository for the French presentation on the FAST functional-analysis method.

## Contents
- `fast_generate.py`: reproducible PowerPoint editing script.
- `Presentation_Methode_FAST.pptx`: original source deck, to be added alongside the generated final deck.
- `FAST_Presentation_Methode_FAST.pptx`: generated output filename.

## Presentation context
- University: Université Sultan Moulay Slimane (USMS)
- Faculty: Faculté des Sciences Appliquées, Béni Mellal (FSA)
- Field: Master Data Science et Sécurité des Systèmes d’Information

## Generate the updated deck
Install the dependency:

```bash
python3 -m pip install python-pptx
```

Run:

```bash
python3 fast_generate.py Presentation_Methode_FAST.pptx
```

The script preserves the existing slide order and shapes, sets all slide backgrounds to white, and adds the institutional heading and study-field label on slide 1. It uses genuine logo image files if supplied at `assets/usms_logo.png` and `assets/fsabm_logo.png`; otherwise it deliberately uses editable text labels rather than fabricated official logos.

## Status
The original PowerPoint was located in the ChatGPT Library. The final edited binary and genuine official logo image files still need to be added to this repository. No official logo asset is fabricated or represented as authentic.
