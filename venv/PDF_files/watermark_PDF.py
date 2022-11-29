import PyPDF2
template=PyPDF2.PdfFileReader(open('venv/PDF_files/HRX4W.pdf','rb')) #to open a pdf file
Watermark=PyPDF2.PdfFileReader(open('venv/PDF_files/wtr.pdf','rb')) #to open a pdf file
output=PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page=template.getPage(i)
    page.mergePage(Watermark.getPage(0)) #mergePage use to write on the same page instead of one after the other ike with PdfFileMerger
with open('venv/PDF_files/watermarked.pdf','wb') as file:
    output.write(file)
