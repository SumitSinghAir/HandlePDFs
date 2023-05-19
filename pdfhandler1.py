#can convert alll formats of images to pdf
import PyPDF2
import glob
from PIL import Image
import os
from datetime import datetime

try:
    while True:
        a = input('What do you want to do:')

        if a == 'pdfmerge':
            pdfiles = glob.glob("rawfiles/*.pdf")
            pdfiles.sort()
            merger = PyPDF2.PdfMerger()
            for filename in pdfiles:
                with open(filename, 'rb') as pdfFile:
                    pdfReader = PyPDF2.PdfReader(pdfFile)
                    merger.append(pdfReader)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            merged_filename = f"merged_{timestamp}.pdf"
            with open(merged_filename, 'wb') as mergedFile:
                merger.write(mergedFile)

        elif a == 'imgtopdf':
            imgfiles = glob.glob("rawfiles/*.jpg")+ glob.glob("rawfiles/*.png") + glob.glob("rawfiles/*.gif")
            imgfiles.sort()
            merger = PyPDF2.PdfMerger()
            i = 0
            for filename in imgfiles:
                i += 1
                imgFile = Image.open(filename)
                imgPdf = imgFile.convert("RGB")  # Convert the imgFile to PDF
                os.makedirs(os.path.dirname("tempfiles/"), exist_ok=True)  # Create the directory if it doesn't exist
                savename = f"tempfiles/file{i}.pdf"
                imgPdf.save(savename)
                with open(savename, 'rb') as pdfFile:
                    pdfReader = PyPDF2.PdfReader(pdfFile)
                    merger.append(pdfReader)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            converted_filename = f"converted_{timestamp}.pdf"
            with open(converted_filename, 'wb') as mergedFile:
                merger.write(mergedFile)
            # Delete the files in the tempfiles directory
            tempfiles = glob.glob("tempfiles/*.pdf")
            for temp_file in tempfiles:
                os.remove(temp_file)
        
        elif a=='q' or a=='Q':
            break

except Exception as e:
    print("Some error occurred: ",e)

