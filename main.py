# import PyPDF2
# import glob
# pdfiles = glob.glob("rawfiles/*.pdf")
# pdfiles.sort()
# merger=PyPDF2.PdfMerger()
# for filename in pdfiles:
#     pdfFile=open(filename,'rb')
#     pdfReader=PyPDF2.PdfReader(pdfFile)
#     merger.append(pdfReader)
#     pdfFile.close()

# merger.write("merged.pdf")

# import PyPDF2
# import os

# directory = "rawfiles/"
# pdfiles = [filename for filename in os.listdir(directory) if filename.endswith(".pdf")]
# pdfiles.sort()

# match= a:
#     case='merge':
#         merger = PyPDF2.PdfMerger()
#         for filename in pdfiles:
#             filepath = os.path.join(directory, filename)
#             pdfFile = open(filepath, 'rb')
#             pdfReader = PyPDF2.PdfReader(pdfFile)
#             merger.append(pdfReader)
#             pdfFile.close()

#         merger.write("merged.pdf")


import PyPDF2
import glob

a=input('What do you want to do:')

match a:
    case'merge':
        pdfiles = glob.glob("rawfiles/*.pdf")
        pdfiles.sort()
        merger=PyPDF2.PdfMerger()
        for filename in pdfiles:
            pdfFile=open(filename,'rb')
            pdfReader=PyPDF2.PdfReader(pdfFile)
            merger.append(pdfReader)
            pdfFile.close()

        merger.write("merged.pdf")
    
    case'j':
        from PIL import Image
        import os
        imgfiles=glob.glob("rawfiles/*.jpg")
        imgfiles.sort()
        merger=PyPDF2.PdfMerger()
        i=0
        for filename in imgfiles:
            i=i+1
            imgFile=Image.open(filename)
            imgPdf=imgFile.convert("RGB") #converts the imgFile to pdf
            os.makedirs(os.path.dirname("/tempfiles"), exist_ok=True)  # Create the directory if it doesn't exist
            #savename=f"{os.path.splitext(filename[i])}.pdf"
            savename="/tempfiles/file{i}.pdf"
            imgPdf.save(savename)
            
            # merger.append(imgPdf)
        pdfiles = glob.glob("tempfiles/*.pdf")
        pdfiles.sort()
        for filename in pdfiles:
            pdfFile=open(filename,'rb')
            pdfReader=PyPDF2.PdfReader(pdfFile)
            merger.append(pdfReader)
            pdfFile.close()

        merger.write("Newpdf.pdf")





