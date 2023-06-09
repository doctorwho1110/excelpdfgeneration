import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    pdf.add_page()

    # gives 10001-2023.1.18
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"Invoice nr.{invoice_nr}", align="L",
             ln=1, border=0)
    pdf.output(f"PDFs/{filename}.pdf")
