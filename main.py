import os
import readpdf
import writeToExcel

def main():
    wb = writeToExcel.ExcelWB()
    for year in os.listdir("C:/Users/argex/python scripts/pdfSscaper/pdfs/"):
        for month in os.listdir("C:/Users/argex/python scripts/pdfSscaper/pdfs/" + year):
            wb.getSheet(month, year)
            row = 2 # because first row is already used by format
            for day in os.listdir("C:/Users/argex/python scripts/pdfSscaper/pdfs/" + year + '/' + month):
                for file in os.listdir("C:/Users/argex/python scripts/pdfSscaper/pdfs/" + year + '/' + month + '/' + day):
                    dir = "C:/Users/argex/python scripts/pdfSscaper/pdfs/" + year + '/' + month + '/' + day + '/' + file
                    row+=1
                    
                    pdf = readpdf.createPDFobj(dir)
                    #pdf.navigate(1); pdf.render(); print(pdf.canvas.strings)
                    strings = readpdf.getPagesText(pdf,dir)
                    data = readpdf.extractText(strings, pdf,dir)
                    wb.write(data,row)
    wb.save("test1")
main()