import argparse
import pandas as pd
from collections import Counter
import PyPDF2
import rmgarbage
from rmgarbage import Rmgarbage


#txt = input("Enter the name of the OCR input you want to check for anomalous text.\n")
class improvingOCR:

    def __init__(self):
        pass

    def garbageDetector(filepath):

        #parser = argparse.ArgumentParser(description='Process OCR Output')
        #parser.add_argument('ocrFile')
        #args = parser.parse_args()
        #fileName = (args.ocrFile).rsplit('/', 1)[-1]
        fileName = (filepath).rsplit('/', 1)[-1]

        #with open(args.ocrFile) as file:
        with open(filepath) as file:

            content = file.read()
            #print(content)
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
                #if (not word.isspace()):
                    isGarbage = garbage.is_garbage(word)
                    #print(word, end = ' ')
                    wordcount += 1
                    if isGarbage != False:
                        garbageWords.append(word)
                        garbagecount += 1

            #print()
            #print(page.extractText())


        frequency = Counter(garbageWords)
        '''
        df = pd.DataFrame.from_records(frequency.most_common(), columns=['page','count'])
        df.to_excel("output.xlsx", engine="xlsxwriter")
        '''
        writer = pd.ExcelWriter('filename.xlsx', engine='xlsxwriter', options={'strings_to_formulas': False})
        df = pd.DataFrame.from_records(frequency.most_common(), columns=['page','count'])
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.save()

        ratio = 0

        #account for divide by 0 error
        if wordcount == 0:
            ratio = 100

        else:
            ratio = 100 - ((garbagecount/wordcount) * 100)
            ratio = int(ratio)

        summary = [[fileName, wordcount, garbagecount, ratio]]
        summaryTable = pd.DataFrame(summary, columns = ["File Name", "Number of Words", "Number of Garbage Words", "Score"])
        print(summaryTable)
        print()

        """"
        print("File: " + fileName)
        print("Number of words: " + str(wordcount))
        print("Number of garbage words: " + str(garbagecount))
        print("Score: " + str(ratio))
        print()
        """

