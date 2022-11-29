import PyPDF2
import sys
inputs=sys.argv[1:]
def pdf_combiner(pdf_list):
    merger=PyPDF2.PdfFileMerger() #PdfFileMerger is method used to merger pdf files
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf) # to append pdf files
    merger.write('Combined.pdf') # creates a new merged pdf file
pdf_combiner(inputs)