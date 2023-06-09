import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
#import time

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    pdf.add_page()

    # gives 10001-2023.1.18
    filename = Path(filepath).stem
    invoice_nr,date = filename.split("-")

    # Write Invoice nr.12321424 text
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"Invoice nr.{invoice_nr}", align="L",
             ln=1, border=0)

    # Write day and creating date
    # named_tuple=time.localtime()
    # time_string=time.strftime("%Y.%m.%d")

    pdf.cell(w=0,h=12,txt=f"Date: {date}",align="L",ln=1,border=0)

    #Reading .xlsx files
    data=pd.read_excel(filepath,sheet_name="Sheet 1")

    #Adding first row as a column names
    columns=data.columns
    columns=[item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(80, 80, 80)

    # Add a header
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1,ln=1)

    for index,rows in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)

        # Cells for every row
        pdf.cell(w=30,h=8,txt=str(rows["product_id"]),border=1)
        pdf.cell(w=70,h=8,txt=str(rows["product_name"]),border=1)
        pdf.cell(w=30, h=8, txt=str(rows["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(rows["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(rows["total_price"]),border=1,ln=1)

    # Adding total price
    total_sum=data["total_price"].sum()

    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    #Writing total sum as a text
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=f"Total price is: {total_sum}", ln=1)


    pdf.output(f"PDFs/{filename}.pdf")
