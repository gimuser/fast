#!/usr/bin/env python3
"""
Prepare the FAST presentation while preserving the original slide order/content.

Usage:
  python3 -m pip install python-pptx
  python3 fast_generate.py Presentation_Methode_FAST.pptx

Optional official logo files:
  assets/usms_logo.png
  assets/fsabm_logo.png

If the official logo files are absent, the script uses editable institutional
text labels instead of inventing or misrepresenting official logos.
"""
from pathlib import Path
import sys

try:
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
    from pptx.util import Inches, Pt
except ImportError:
    raise SystemExit("Missing dependency. Install it with: python3 -m pip install python-pptx")

WHITE = RGBColor(255, 255, 255)
NAVY = RGBColor(22, 54, 92)
GREY = RGBColor(90, 100, 112)
FIELD = "Master Data Science et Sécurité des Systèmes d’Information"
OUT = "FAST_Presentation_Methode_FAST.pptx"

def add_label(slide, text, x, y, w, h, size=11, color=NAVY, bold=True):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = text
    run.font.name = "Aptos"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    return box

def add_logo_or_label(slide, path, label, x, y, w, h):
    if path.exists():
        slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w), height=Inches(h))
    else:
        add_label(slide, label, x, y, w, h, size=10, color=NAVY, bold=True)

def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python3 fast_generate.py <original_pptx_path>")
    source = Path(sys.argv[1]).expanduser()
    if not source.is_file():
        raise SystemExit(f"Input PowerPoint not found: {source}")

    prs = Presentation(str(source))

    # White background on every slide; retain all existing shapes and slide order.
    for slide in prs.slides:
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = WHITE

    if prs.slides:
        slide = prs.slides[0]
        # Add a compact institutional heading without reordering or deleting content.
        # Positioning is intentionally near the top edge; adjust if the original title
        # occupies this exact area.
        add_logo_or_label(slide, Path("assets/usms_logo.png"),
                          "UNIVERSITÉ SULTAN MOULAY SLIMANE", 0.35, 0.12, 2.05, 0.62)
        add_logo_or_label(slide, Path("assets/fsabm_logo.png"),
                          "FACULTÉ DES SCIENCES APPLIQUÉES • BÉNI MELLAL",
                          9.05, 0.12, 3.55, 0.62)
        add_label(slide, FIELD, 2.35, 0.20, 6.55, 0.42, size=10, color=GREY, bold=False)

    prs.save(OUT)
    print(f"[OK] Created: {OUT}")
    print(f"[INFO] Slides preserved: {len(prs.slides)}")
    if not Path("assets/usms_logo.png").exists() or not Path("assets/fsabm_logo.png").exists():
        print("[NOTICE] Official logo assets were not found. Editable text labels were used.")
        print("Add genuine logo files at assets/usms_logo.png and assets/fsabm_logo.png, then rerun.")

if __name__ == "__main__":
    main()
