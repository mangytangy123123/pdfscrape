import os
import readpdf
import writeToExcel

def main():
    for year in os.listdir('C:/Users/lawrence/projects/pdfScraper/pdfs'):
        for month in os.listdir('C:/Users/lawrence/projects/pdfScraper/pdfs/' + year):
            index = 0
            for day in os.listdir('C:/Users/lawrence/projects/pdfScraper/pdfs/' + year + '/' + month):
                for file in os.listdir('C:/Users/lawrence/projects/pdfScraper/pdfs/' + year + '/' + month + '/' + day):
                    dir = 'C:/Users/lawrence/projects/pdfScraper/pdfs/' + year + '/' + month + '/' + day + '/' + file
                    index+=1

def testmain():
    wb = writeToExcel.ExcelWB()
    for year in os.listdir('C:/Users/lawrence/projects/pdfScraper/pdfs'):
        for month in os.listdir('C:/Users/lawrence/projects/pdfScraper/pdfs/' + year):
            wb.getSheet(month, year)
            row = 2 # because first row is already used by format
            for day in os.listdir('C:/Users/lawrence/projects/pdfScraper/pdfs/' + year + '/' + month):
                for file in os.listdir('C:/Users/lawrence/projects/pdfScraper/pdfs/' + year + '/' + month + '/' + day):
                    dir = 'C:/Users/lawrence/projects/pdfScraper/pdfs/' + year + '/' + month + '/' + day + '/' + file
                    row+=1

                    pdf = readpdf.createPDFobj(dir)
                    strings = readpdf.getPagesText(pdf,dir)
                    data = readpdf.extractText(strings, pdf,dir)
                    #wb.write(data,row)
                    #wb.save()

testmain()