#!/usr/bin/env python3
"""Generate the edited FAST presentation from the committed source deck."""
from pathlib import Path
import sys

try:
    from pptx import Presentation
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE, MSO_SHAPE_TYPE
    from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
    from pptx.util import Inches, Pt
except ImportError:
    raise SystemExit("Install dependency: python3 -m pip install python-pptx")

NAVY = RGBColor(22, 54, 92)
GREY = RGBColor(90, 100, 112)
PALE_BLUE = RGBColor(244, 248, 252)
BORDER_BLUE = RGBColor(151, 174, 199)
OUT = "FAST_Presentation_Methode_FAST.pptx"


def remove_shape(shape):
    element = shape._element
    element.getparent().remove(element)


def add_logo_placeholder(slide):
    """Reserve a clean logo area without inventing an institutional logo."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(0.35), Inches(0.12), Inches(1.45), Inches(0.62)
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


def recolor_textbox(shape, color):
    if not getattr(shape, "has_text_frame", False):
        return
    for paragraph in shape.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.color.rgb = color


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python3 fast_generate.py <original_pptx_path>")
    source = Path(sys.argv[1]).expanduser()
    if not source.is_file():
        raise SystemExit(f"Input PowerPoint not found: {source}")

    prs = Presentation(str(source))
    if len(prs.slides) < 11:
        raise SystemExit("Unexpected source deck: expected at least 11 slides.")

    # Slide 1: replace the university-name text in the reserved logo area,
    # and remove the duplicate programme label added by the first draft.
    first = prs.slides[0]
    for shape in list(first.shapes):
        txt = getattr(shape, "text", "").strip()
        if txt == "UNIVERSITÉ SULTAN MOULAY SLIMANE":
            remove_shape(shape)
        elif txt == "Master Data Science et Sécurité des Systèmes d’Information" and shape.left / 914400 < 2.2:
            remove_shape(shape)

    add_logo_placeholder(first)

    # Improve contrast on the title slide while preserving its layout.
    for shape in first.shapes:
        txt = getattr(shape, "text", "").strip()
        if txt.startswith("LA MÉTHODE"):
            recolor_textbox(shape, NAVY)
        elif txt in ("Function Analysis System Technique",
                     "De l’expression du besoin à l’analyse des fonctions"):
            recolor_textbox(shape, GREY)

    # Slide 11: the source used white text on a white background for the
    # summary title and three key messages. Restore readable contrast.
    summary = prs.slides[10]
    for shape in summary.shapes:
        txt = getattr(shape, "text", "").strip()
        if not txt:
            continue
        if txt in ("À retenir",
                   "FAST transforme un besoin en fonctions organisées.",
                   "Les questions Pourquoi ? et Comment ? structurent le diagramme.",
                   "Les solutions techniques sont choisies après l’analyse des fonctions."):
            recolor_textbox(shape, NAVY)
        elif txt.startswith("Question à la classe"):
            recolor_textbox(shape, GREY)

    prs.save(OUT)
    print(f"[OK] Created: {OUT}")
    print(f"[INFO] Slides preserved: {len(prs.slides)}")
    print("[INFO] Original slide dimensions, backgrounds, order and content preserved.")
    print("[INFO] Logo placeholder added; real logo intentionally deferred.")
    print("[INFO] Title and summary slide contrast corrected.")


if __name__ == "__main__":
    main()
