import pandas as pd
from collections import Counter
import PyPDF2
import rmgarbage
from rmgarbage import Rmgarbage


txt = input("Enter the name of the PDF file you want to convert to text.\n")
pdfFile = open(txt, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

numberOfPages = pdfReader.numPages
garbageWords = []
garbage = Rmgarbage()
garbage.__init__()

for x in range(numberOfPages):
    #print()
    #print()
    #print()
    #print('Page ' + str(x + 1))
    page = pdfReader.getPage(x)
    allWords = page.extractText()
    words = allWords.split()

    for word in words:
        isGarbage = garbage.is_garbage(word)
        if isGarbage != False:
            garbageWords.append(word)

    #print()
    print(page.extractText())

frequency = Counter(garbageWords)
df = pd.DataFrame.from_records(frequency.most_common(), columns=['page','count'])
df.to_excel("output.xlsx") // create output.xlsx file prior to use
print()
print(df)

pdfFile.close()                        
