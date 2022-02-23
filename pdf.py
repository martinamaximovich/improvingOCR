import argparse
import pandas as pd
from collections import Counter
import PyPDF2
import rmgarbage
from rmgarbage import Rmgarbage


#txt = input("Enter the name of the OCR input you want to check for anomalous text.\n")
parser = argparse.ArgumentParser(description='Process OCR Output')
parser.add_argument('ocrFile')
args = parser.parse_args()
fileName = (args.ocrFile).rsplit('/', 1)[-1]

with open(args.ocrFile) as file:

    content = file.read()
    print(content)
#pdfReader = PyPDF2.PdfFileReader(pdfFile)

    #words = [i.split(' ') for i in file]
    words = content.split(" ")
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
    #words = words.split()

    #words = list(words)

    for word in words:
        if (len(word)):
            isGarbage = garbage.is_garbage(word)
            #print(word, end = ' ')
            wordcount += 1
            if isGarbage != False:
                garbageWords.append(word)
                garbagecount += 1

    #print()
    #print(page.extractText())

frequency = Counter(garbageWords)
df = pd.DataFrame.from_records(frequency.most_common(), columns=['page','count'])
df.to_excel("output.xlsx")
ratio = (wordcount/garbagecount)

print("File: " + fileName)
print("Number of words: " + str(wordcount))
print("Number of garbage words: " + str(garbagecount))
print("Score: " + str(ratio))
print()
