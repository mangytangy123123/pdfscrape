import pdfreader
from openpyxl import load_workbook
from pdfreader import SimplePDFViewer

fd = open("C:/Users/lawrence/projects/pdfScraper/test folder/2022/OCT/3 OCT/AHMADIAN-AZIMI.pdf", 'rb')

viewer = SimplePDFViewer(fd)
viewer.navigate(2); viewer.render()
print(viewer.canvas.text_content)
