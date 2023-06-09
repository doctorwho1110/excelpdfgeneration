from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("exercise_doc/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:
    pdf.add_page()

    # gives cats,dogs,foxes,snakes
    filename = Path(filepath).stem
    name = filename.title()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=name, align="L",
             ln=1, border=0)

pdf.output(f"PDFs/output.pdf")
