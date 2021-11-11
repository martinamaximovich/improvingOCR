from collections import Counter
import PyPDF2
import rmgarbage
from rmgarbage import Rmgarbage


txt = input("Enter the name of the PDF file you wa
pdfFile = open(txt, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

numberOfPages = pdfReader.numPages
garbageWords = []
garbage = Rmgarbage()
garbage.__init__()

for x in range(numberOfPages):
    print()
    print()
    print()
    print('Page ' + str(x + 1))
    page = pdfReader.getPage(x)
    allWords = page.extractText()
    words = allWords.split()

    for word in words:
        isGarbage = garbage.is_garbage(word)
        if isGarbage != False:
            garbageWords.append(word)

    print()
    print(page.extractText())

frequency = Counter(garbageWords)
print()
print(frequency)

pdfFile.close()
~                                                 
