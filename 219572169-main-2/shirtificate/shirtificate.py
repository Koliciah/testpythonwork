from fpdf import FPDF

name = input("Name: ")

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", size=22)
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        self.ln(20)

pdf = PDF()
pdf.add_page(orientation="P")
pdf.image("shirtificate.png", 0, 50, 210)
pdf.set_font("helvetica", size=22)
pdf.set_text_color(255, 255, 255)
pdf.text(60, 140, text=f"{name} took cs50")
pdf.output("shirtificate.pdf")

