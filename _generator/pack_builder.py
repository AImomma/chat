"""
Royalti Studios — Master Prompt Pack PDF builder (v2).

Renders a branded prompt-pack PDF from a data dict:
cover page, how-to-use, table of contents, quick reference card,
genre rules cheat sheet, phased copy-paste prompts, final words, brand footer.

Branding: Royalti Studios (royal blue / gold / purple).
Supports audience lines: adult, teen (YA), middle grade, chapter book,
picture book, and leveled readers (Lexile band + Guided Reading letter).

Usage:
    from pack_builder import build_pack
    from adventure_pack_data import DATA
    build_pack(DATA, "Adventure_Master_Prompt_Pack.pdf")

Optional data keys (all safe to omit):
    brand_name        -> defaults to "Royalti Studios"
    audience_line     -> e.g. "Young Adult Line" / "Leveled Reader Line"
    reading_level     -> e.g. "Lexile 420L-650L  |  Guided Reading Level M-P"
    cover_h2          -> defaults to "From Concept to Published Novel"
    works_with_line   -> defaults to the standard any-LLM line

Versioning (required policy):
    version           -> e.g. "2.0"  (bump on every amendment)
    version_date      -> e.g. "2026-07-02"
    Version + date print on the cover and footer. Never overwrite an old
    PDF: archive it in _generator/versions/ and log the change in
    _generator/CHANGELOG.md before releasing a new version.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)

# ---------- ROYALTI STUDIOS BRAND ----------
BRAND_NAME = "Royalti Studios"

ROYAL_PURPLE = colors.HexColor("#4B2E83")   # headers, titles
ROYAL_BLUE   = colors.HexColor("#1B3B8B")   # phase bars, structure
GOLD         = colors.HexColor("#C9A227")   # accents, rules, brand marks
BOX_FILL     = colors.HexColor("#F5F3FA")   # prompt box fill (soft lavender)
BOX_BORDER   = ROYAL_PURPLE
BLACK        = colors.HexColor("#1A1A1A")
GREY_RULE    = colors.HexColor("#CCCCCC")

styles = getSampleStyleSheet()


def make_styles():
    s = {}
    s["CoverTitle"] = ParagraphStyle("CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold",
                                     fontSize=32, leading=38, textColor=ROYAL_PURPLE, alignment=TA_CENTER, spaceAfter=10)
    s["CoverSubtitle"] = ParagraphStyle("CoverSubtitle", parent=styles["Title"], fontName="Helvetica-Bold",
                                        fontSize=18, textColor=ROYAL_BLUE, alignment=TA_CENTER, spaceAfter=10)
    s["CoverAudience"] = ParagraphStyle("CoverAudience", parent=styles["Normal"], fontName="Helvetica-Bold",
                                        fontSize=12, textColor=GOLD, alignment=TA_CENTER, spaceAfter=6)
    s["CoverLevel"] = ParagraphStyle("CoverLevel", parent=styles["Normal"], fontName="Helvetica-Bold",
                                     fontSize=11, textColor=ROYAL_BLUE, alignment=TA_CENTER, spaceAfter=10)
    s["CoverH2"] = ParagraphStyle("CoverH2", parent=styles["Normal"], fontName="Helvetica-Bold",
                                  fontSize=15, textColor=BLACK, alignment=TA_CENTER, spaceAfter=10)
    s["CoverItalic"] = ParagraphStyle("CoverItalic", parent=styles["Normal"], fontName="Helvetica-Oblique",
                                      fontSize=12, textColor=ROYAL_PURPLE, alignment=TA_CENTER, spaceAfter=14)
    s["CoverBody"] = ParagraphStyle("CoverBody", parent=styles["Normal"], fontName="Helvetica",
                                    fontSize=11, textColor=BLACK, alignment=TA_CENTER, spaceAfter=10, leading=15)
    s["CoverBold"] = ParagraphStyle("CoverBold", parent=styles["Normal"], fontName="Helvetica-Bold",
                                    fontSize=11, textColor=BLACK, alignment=TA_CENTER, spaceAfter=10, leading=15)
    s["CoverAccent"] = ParagraphStyle("CoverAccent", parent=styles["Normal"], fontName="Helvetica",
                                      fontSize=10.5, textColor=ROYAL_BLUE, alignment=TA_CENTER, spaceAfter=8)
    s["CoverBrand"] = ParagraphStyle("CoverBrand", parent=styles["Normal"], fontName="Helvetica-Bold",
                                     fontSize=13, textColor=GOLD, alignment=TA_CENTER, spaceAfter=14)

    s["H1"] = ParagraphStyle("H1", parent=styles["Heading1"], fontName="Helvetica-Bold",
                             fontSize=20, textColor=ROYAL_PURPLE, spaceAfter=14, spaceBefore=4)
    s["Body"] = ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica",
                               fontSize=10.5, textColor=BLACK, leading=15, spaceAfter=10)
    s["TOCEntry"] = ParagraphStyle("TOCEntry", parent=styles["Normal"], fontName="Helvetica",
                                   fontSize=11, textColor=BLACK, spaceAfter=6, leading=14)
    s["TOCPhase"] = ParagraphStyle("TOCPhase", parent=styles["Normal"], fontName="Helvetica-Bold",
                                   fontSize=11.5, textColor=ROYAL_BLUE, spaceAfter=4, spaceBefore=10)
    s["QRTitle"] = ParagraphStyle("QRTitle", parent=styles["Normal"], fontName="Helvetica-Bold",
                                  fontSize=11, textColor=ROYAL_BLUE, spaceAfter=8, spaceBefore=10)
    s["QRItem"] = ParagraphStyle("QRItem", parent=styles["Normal"], fontName="Courier",
                                 fontSize=9.5, textColor=colors.HexColor("#333333"), spaceAfter=2, leftIndent=14)

    s["CheatHeader"] = ParagraphStyle("CheatHeader", parent=styles["Normal"], fontName="Helvetica-Bold",
                                      fontSize=11.5, textColor=ROYAL_BLUE, spaceBefore=14, spaceAfter=6)
    s["CheatItem"] = ParagraphStyle("CheatItem", parent=styles["Normal"], fontName="Helvetica",
                                    fontSize=9.7, textColor=BLACK, leading=13.5, spaceAfter=3, leftIndent=6)
    s["CheatFormula"] = ParagraphStyle("CheatFormula", parent=styles["Normal"], fontName="Helvetica-Oblique",
                                       fontSize=9.7, textColor=colors.HexColor("#333333"), leading=14)

    s["PhaseIntro"] = ParagraphStyle("PhaseIntro", parent=styles["Normal"], fontName="Helvetica",
                                     fontSize=10.5, textColor=BLACK, leading=15, spaceAfter=10)
    s["PromptOf"] = ParagraphStyle("PromptOf", parent=styles["Normal"], fontName="Helvetica-Bold",
                                   fontSize=10.5, textColor=GOLD, spaceBefore=6, spaceAfter=6)
    s["PromptTitle"] = ParagraphStyle("PromptTitle", parent=styles["Normal"], fontName="Helvetica-Bold",
                                      fontSize=15, textColor=ROYAL_PURPLE, spaceAfter=8, leading=19)
    s["PromptDesc"] = ParagraphStyle("PromptDesc", parent=styles["Normal"], fontName="Helvetica",
                                     fontSize=10.3, textColor=BLACK, leading=14.5, spaceAfter=8)
    s["CopyLabel"] = ParagraphStyle("CopyLabel", parent=styles["Normal"], fontName="Helvetica-Bold",
                                    fontSize=10.5, textColor=ROYAL_BLUE, spaceBefore=4, spaceAfter=6)
    s["PromptBox"] = ParagraphStyle("PromptBox", parent=styles["Normal"], fontName="Courier",
                                    fontSize=8.7, textColor=colors.HexColor("#222222"), leading=12.2)
    s["ProTip"] = ParagraphStyle("ProTip", parent=styles["Normal"], fontName="Helvetica-Oblique",
                                 fontSize=9.7, textColor=ROYAL_PURPLE, leading=13.5, spaceBefore=10, spaceAfter=6)

    s["FinalWords"] = ParagraphStyle("FinalWords", parent=styles["Normal"], fontName="Helvetica",
                                     fontSize=11, textColor=BLACK, leading=16, spaceAfter=14)
    s["FooterBrand"] = ParagraphStyle("FooterBrand", parent=styles["Normal"], fontName="Helvetica-Bold",
                                      fontSize=11, textColor=GOLD, alignment=TA_CENTER, spaceBefore=8)
    s["FooterTagline"] = ParagraphStyle("FooterTagline", parent=styles["Normal"], fontName="Helvetica-Oblique",
                                        fontSize=9.5, textColor=ROYAL_PURPLE, alignment=TA_CENTER, spaceBefore=4)
    return s


def esc(text):
    """Escape reportlab-sensitive characters; strip glyphs the PDF fonts can't render (e.g. emoji)."""
    text = str(text)
    try:
        text.encode("cp1252")
    except UnicodeEncodeError:
        cleaned = text.encode("cp1252", "ignore").decode("cp1252")
        print(f"WARNING: removed unrenderable characters (emoji?) from: {text[:50]!r}")
        text = cleaned
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


REQUIRED_TOP = ["genre_title", "total_prompts", "hook_line", "subgenres_line",
                "closing_tagline", "how_to_use_intro", "phase_summaries",
                "placeholder_note", "skip_note", "cheat_sheet", "final_words", "phases"]


def validate(data):
    """Friendly errors instead of KeyError crashes."""
    missing = [k for k in REQUIRED_TOP if k not in data]
    if missing:
        raise ValueError(f"Pack data is missing top-level fields: {missing}")
    for k in ["makes", "kills", "voice", "formula"]:
        if k not in data["cheat_sheet"]:
            raise ValueError(f"cheat_sheet is missing '{k}'")
    for pi, ph in enumerate(data["phases"], 1):
        for k in ["name", "intro", "prompts"]:
            if k not in ph:
                raise ValueError(f"Phase {pi} is missing '{k}'")
        for qi, pr in enumerate(ph["prompts"], 1):
            for k in ["title", "desc", "prompt_text", "pro_tip"]:
                if k not in pr:
                    raise ValueError(f"Phase {pi}, prompt {qi} ('{pr.get('title','?')}') is missing '{k}'")


def phase_header(name, S):
    t = Table([[Paragraph(f'<font color="white"><b>{esc(name)}</b></font>', ParagraphStyle(
        "PhaseBar", fontName="Helvetica-Bold", fontSize=13, alignment=TA_CENTER, textColor=colors.white))]],
        colWidths=[6.5 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ROYAL_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    return t


def prompt_box(text, S):
    p = Paragraph(esc(text).replace("\n", "<br/>"), S["PromptBox"])
    try:
        t = Table([[p]], colWidths=[6.3 * inch], splitInRow=1)
    except TypeError:
        t = Table([[p]], colWidths=[6.3 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BOX_FILL),
        ("BOX", (0, 0), (-1, -1), 0.75, BOX_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return t


def build_pack(data, output_path):
    validate(data)
    S = make_styles()
    brand = data.get("brand_name", BRAND_NAME)
    actual = sum(len(ph["prompts"]) for ph in data["phases"])
    if data.get("total_prompts") != actual:
        print(f"WARNING: total_prompts said {data.get('total_prompts')} but {actual} prompts found — using {actual}.")
        data = dict(data)
        data["total_prompts"] = actual
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            topMargin=0.85 * inch, bottomMargin=0.75 * inch,
                            leftMargin=1.0 * inch, rightMargin=1.0 * inch)
    story = []

    # ---------- COVER ----------
    story.append(Spacer(1, 1.2 * inch))
    story.append(Paragraph(esc(data["genre_title"]), S["CoverTitle"]))
    story.append(Paragraph("MASTER PROMPT PACK", S["CoverSubtitle"]))
    if data.get("audience_line"):
        story.append(Paragraph(esc(data["audience_line"]), S["CoverAudience"]))
    if data.get("reading_level"):
        story.append(Paragraph(esc(data["reading_level"]), S["CoverLevel"]))
    if data.get("version"):
        vline = f'Version {data["version"]}'
        if data.get("version_date"):
            vline += f'  •  {data["version_date"]}'
        story.append(Paragraph(esc(vline), S["CoverAccent"]))
    story.append(HRFlowable(width="100%", thickness=1.0, color=GOLD, spaceAfter=16))
    story.append(Paragraph(esc(data.get("cover_h2", "From Concept to Published Novel")), S["CoverH2"]))
    story.append(Paragraph(f'{data["total_prompts"]} Copy-Paste Prompts for Any AI', S["CoverItalic"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph(esc(data["hook_line"]), S["CoverBody"]))
    for line in data.get("keyword_lines", []):
        story.append(Paragraph(esc(line), S["CoverBody"]))
    story.append(Paragraph(esc(data["subgenres_line"]), S["CoverBold"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(esc(data.get("works_with_line",
        "Works with ChatGPT • Claude • Gemini • Copilot • Any LLM")), S["CoverAccent"]))
    story.append(Paragraph(esc(brand), S["CoverBrand"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(esc(data["closing_tagline"]), S["CoverBody"]))
    story.append(PageBreak())

    # ---------- HOW TO USE ----------
    story.append(Paragraph("How to Use This Pack", S["H1"]))
    story.append(Paragraph(esc(data["how_to_use_intro"]), S["Body"]))
    for para in data["phase_summaries"]:
        story.append(Paragraph(esc(para), S["Body"]))
    story.append(Paragraph(esc(data["placeholder_note"]), S["Body"]))
    story.append(Paragraph(esc(data["skip_note"]), S["Body"]))
    story.append(PageBreak())

    # ---------- TABLE OF CONTENTS ----------
    story.append(Paragraph("Table of Contents", S["H1"]))
    story.append(Paragraph("How to Use This Pack", S["TOCEntry"]))
    story.append(Paragraph("Quick Reference Card", S["TOCEntry"]))
    story.append(Paragraph("Genre Rules Cheat Sheet", S["TOCEntry"]))
    story.append(Spacer(1, 8))
    counter = 1
    for phase in data["phases"]:
        story.append(Paragraph(esc(phase["name"]), S["TOCPhase"]))
        for p in phase["prompts"]:
            story.append(Paragraph(f'{counter}. {esc(p["title"])}', S["TOCEntry"]))
            counter += 1
    story.append(PageBreak())

    # ---------- QUICK REFERENCE CARD ----------
    story.append(Paragraph("Quick Reference Card", S["H1"]))
    story.append(Paragraph(f'THE {data["total_prompts"]} PROMPTS AT A GLANCE', S["QRTitle"]))
    counter = 1
    for phase in data["phases"]:
        story.append(Paragraph(esc(phase["name"]), S["QRTitle"]))
        for p in phase["prompts"]:
            story.append(Paragraph(f'&#9632; Prompt {counter}: {esc(p["title"])}', S["QRItem"]))
            counter += 1
    story.append(PageBreak())

    # ---------- CHEAT SHEET ----------
    cs = data["cheat_sheet"]
    story.append(Paragraph(f'{data["genre_title"].title()} Rules Cheat Sheet', S["H1"]))
    story.append(Paragraph(f'WHAT MAKES IT {data["genre_title"].upper()}:', S["CheatHeader"]))
    for item in cs["makes"]:
        story.append(Paragraph(f'&#10003; {esc(item)}', S["CheatItem"]))
    story.append(Paragraph(f'WHAT KILLS {data["genre_title"].upper()}:', S["CheatHeader"]))
    for item in cs["kills"]:
        story.append(Paragraph(f'&#10007; {esc(item)}', S["CheatItem"]))
    story.append(Paragraph(f'{data["genre_title"].upper()} VOICE ESSENTIALS:', S["CheatHeader"]))
    for item in cs["voice"]:
        story.append(Paragraph(f'&#10003; {esc(item)}', S["CheatItem"]))
    story.append(Paragraph(f'THE {data["genre_title"].upper()} STRUCTURE FORMULA:', S["CheatHeader"]))
    story.append(Paragraph(esc(cs["formula"]), S["CheatFormula"]))
    if cs.get("reader_expectations"):
        story.append(Paragraph("READER EXPECTATIONS:", S["CheatHeader"]))
        story.append(Paragraph(esc(cs["reader_expectations"]), S["Body"]))
    if cs.get("level_spec"):
        story.append(Paragraph("READING LEVEL SPEC:", S["CheatHeader"]))
        for item in cs["level_spec"]:
            story.append(Paragraph(f'&#9632; {esc(item)}', S["CheatItem"]))
    story.append(PageBreak())

    # ---------- PHASES / PROMPTS ----------
    counter = 1
    for phase in data["phases"]:
        story.append(phase_header(phase["name"], S))
        story.append(Spacer(1, 12))
        story.append(Paragraph(esc(phase["intro"]), S["PhaseIntro"]))
        story.append(Spacer(1, 4))
        for p in phase["prompts"]:
            story.append(Paragraph(f'PROMPT {counter} of {data["total_prompts"]}', S["PromptOf"]))
            story.append(Paragraph(esc(p["title"]), S["PromptTitle"]))
            story.append(Paragraph(esc(p["desc"]), S["PromptDesc"]))
            story.append(Paragraph('&#9986; COPY THIS PROMPT:', S["CopyLabel"]))
            story.append(prompt_box(p["prompt_text"], S))
            story.append(Paragraph(f'Pro Tip: {esc(p["pro_tip"])}', S["ProTip"]))
            story.append(HRFlowable(width="100%", thickness=0.5, color=GREY_RULE,
                                    spaceBefore=8, spaceAfter=10))
            counter += 1

    # ---------- FINAL WORDS + BRAND FOOTER ----------
    story.append(Paragraph(esc(data["final_words"]), S["FinalWords"]))
    story.append(HRFlowable(width="40%", thickness=1.0, color=GOLD, spaceBefore=10, spaceAfter=6))
    story.append(Paragraph(esc(brand), S["FooterBrand"]))
    story.append(Paragraph(esc(data["closing_tagline"]), S["FooterTagline"]))
    if data.get("version"):
        story.append(Paragraph(
            esc(f'Version {data["version"]} — {data.get("version_date", "")}'), S["FooterTagline"]))

    doc.build(story)
    return output_path


if __name__ == "__main__":
    import importlib
    import sys
    if len(sys.argv) < 3:
        print("Usage: python pack_builder.py <data_module_name> <output.pdf>")
        sys.exit(1)
    mod = importlib.import_module(sys.argv[1])
    build_pack(mod.DATA, sys.argv[2])
    print(f"Built {sys.argv[2]}")
