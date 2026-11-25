#!/usr/bin/env python3
"""
Prepare the FAST presentation while preserving the original slide order/content.

Usage:
  python3 -m pip install python-pptx
  python3 fast_generate.py Presentation_Methode_FAST.pptx

The title slide receives one clearly marked logo placeholder. The real logo
asset is intentionally not used yet; it can replace the placeholder later.
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
PALE_BLUE = RGBColor(244, 248, 252)
BORDER_BLUE = RGBColor(151, 174, 199)
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


def add_logo_placeholder(slide):
    """Add one neutral placeholder, not an imitation of an official logo."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.38), Inches(0.14), Inches(1.38), Inches(0.68)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = PALE_BLUE
    shape.line.color.rgb = BORDER_BLUE
    shape.line.width = Pt(1.1)

    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "LOGO"
    r.font.name = "Aptos Display"
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = NAVY

    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(0)
    r2 = p2.add_run()
    r2.text = "À INSÉRER"
    r2.font.name = "Aptos"
    r2.font.size = Pt(6.5)
    r2.font.color.rgb = GREY
    return shape


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python3 fast_generate.py <original_pptx_path>")
    source = Path(sys.argv[1]).expanduser()
    if not source.is_file():
        raise SystemExit(f"Input PowerPoint not found: {source}")

    prs = Presentation(str(source))

    # Keep the existing widescreen layout and slide sequence.
    # White backgrounds are applied consistently without changing slide content.
    for slide in prs.slides:
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = WHITE

    if prs.slides:
        slide = prs.slides[0]
        add_logo_placeholder(slide)
        add_label(slide, FIELD, 2.05, 0.20, 7.45, 0.42,
                  size=10, color=GREY, bold=False)

    prs.save(OUT)
    print(f"[OK] Created: {OUT}")
    print(f"[INFO] Slides preserved: {len(prs.slides)}")
    print("[INFO] One neutral logo placeholder was added to the title slide.")
    print("[INFO] The real logo asset is intentionally deferred.")


if __name__ == "__main__":
    main()
