import os
import readpdf
import writeToExcel

def main():
    currentDIR = os.curdir
    print(currentDIR)
    wb = writeToExcel.ExcelWB()
    for year in os.listdir(os.curdir +"/test folder/"):
        for month in os.listdir(os.curdir +"/test folder/" + year):
            wb.getSheet(month, year)
            row = 2 # because first row is already used by format
            for day in os.listdir(os.curdir +"/test folder/" + year + '/' + month):
                for file in os.listdir(os.curdir +"/test folder/" + year + '/' + month + '/' + day):
                    dir = os.curdir +"/test folder/" + year + '/' + month + '/' + day + '/' + file
                    row+=1
                    
                    pdf = readpdf.createPDFobj(dir)
                    #pdf.navigate(1); pdf.render(); print(pdf.canvas.strings)
                    strings = readpdf.getPagesText(pdf,dir)
                    data = readpdf.extractText(strings, pdf,dir)
                    wb.write(data,row)
    wb.save("test1")
main()