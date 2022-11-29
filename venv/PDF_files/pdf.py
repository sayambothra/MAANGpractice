import PyPDF2
#always read them as binary
with open('HRX4W.pdf', 'rb') as file:
    reader=PyPDF2.PdfFileReader(file)
    print(reader)
    print(reader.getPage(1)) #returns page Object
    page=reader.getPage(0)
    print(page.rotateCounterClockwise(180)) #rotate a page
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open ('../../tilt.pdf', 'wb') as new_file:
        writer.write(new_file)


