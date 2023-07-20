import pdfreader
from openpyxl import load_workbook
from pdfreader import SimplePDFViewer

fd = open("C:/Users/lawrence/projects/pdfScraper/pdfs/2022/OCT/3 OCT/AHMADIAN-AZIMI.pdf", 'rb')

viewer = SimplePDFViewer(fd)
viewer.navigate(2); viewer.render()
page = viewer.canvas.strings

print(page[page.index("15. ID number:")+1])
print(page[page.index("11. Date of birth:")+1])

