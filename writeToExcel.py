import openpyxl

class ExcelWB:
    def __init__(self) -> None:
        self.WB = openpyxl.load_workbook("C:/Users/lawrence/projects/pdfScraper/INCOMING1.xlsx")
        self.template = self.WB['template']
        self.sheet = None
    
    def getSheet(self,month, year):
        try:
            sheet = self.WB[month+'-'+year]
        except:
            sheet = self.WB.copy_worksheet(self.template)
            sheet.title = month+'-'+year
        self.sheet = sheet
    
    def write(self,data,row):
        for i,v in enumerate(data):
            self.sheet.cell(row,i+1,value=v)
    
    def save(self):
        self.WB.save("test1")

        

