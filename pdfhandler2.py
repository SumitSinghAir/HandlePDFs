import img2pdf
import glob
import os
from datetime import datetime

a = input('What do you want to do:')

if a == 'pdfmerge':
    pdfiles = glob.glob("rawfiles/*.pdf")
    pdfiles.sort()
    merger = PyPDF2.PdfMerger()
    for filename in pdfiles:
        with open(filename, 'rb') as pdfFile:
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            merger.append(pdfReader)
            
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    merged_filename = f"merged_{timestamp}.pdf"

    with open(merged_filename, 'wb') as mergedFile:
        merger.write(mergedFile)

elif a == 'imgtopdf':
    imgfiles = glob.glob("rawfiles/*.jpg")
    imgfiles.sort()
    pdfbytes = img2pdf.convert(imgfiles)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    converted_filename = f"converted_{timestamp}.pdf"
    with open(onverted_filename, 'wb') as pdfFile:
        pdfFile.write(pdfbytes)

