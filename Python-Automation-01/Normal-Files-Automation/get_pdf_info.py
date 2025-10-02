from PyPDF2 import PdfReader

pdf = PdfReader('file-01.pdf')

print("Num of pages: ", len(pdf.pages));
print("info: ", pdf.metadata)