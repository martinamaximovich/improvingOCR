import argparse
import pandas as pd
from collections import Counter
import PyPDF2
import rmgarbage
from rmgarbage import Rmgarbage


#txt = input("Enter the name of the OCR input you want to check for anomalous text.\n")
parser = argparse.ArgumentParser(description='Process OCR Output')
parser.add_argument('ocrFile', type=argparse.FileType('r'))
args = parser.parse_args()

with open(args.ocrFile) as file:

#pdfReader = PyPDF2.PdfFileReader(pdfFile)

    garbagecount = 0
    wordcount = 0
    #numberOfPages = pdfReader.numPages
    garbageWords = []
    garbage = Rmgarbage()
    garbage.__init__()

#for x in range(numberOfPages):
    #print()
    #print()
    #print()
    #print('Page ' + str(x + 1))
    #page = pdfReader.getPage(x)
    #allWords = page.extractText()
    words = ocrFile.split()

    for word in words:
        isGarbage = garbage.is_garbage(word)
        wordcount += 1
        if isGarbage != False:
            garbageWords.append(word)
            garbagecount += 1

    #print()
    #print(page.extractText())

frequency = Counter(garbageWords)
df = pd.DataFrame.from_records(frequency.most_common(), columns=['page','count'])
df.to_excel("output.xlsx")
ratio = garbagecount/wordcount
print()

