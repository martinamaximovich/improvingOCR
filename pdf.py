import PyPDF2

txt = input("Enter the name of the PDF file you want to convert to text.\n")
pdfFile = open(txt, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

numberOfPages = pdfReader.numPages

for x in range(numberOfPages):
    print()
    print()
    print()
    print('Page ' + str(x + 1))
    page = pdfReader.getPage(x)
    print(page.extractText())

pdfFile.close()
