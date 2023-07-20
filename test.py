import pdfreader
from openpyxl import load_workbook
from pdfreader import PDFDocument, SimplePDFViewer
import os
from os import listdir
from os.path import isfile, join

testdir = "C:/Users/lawre.DESKTOP-SCR7VIT/Documents/python/pdfs/NOV/3 NOV/BAYAT-ASHNA.pdf"
pdfFileObj = open(testdir, 'rb')
doc = SimplePDFViewer(pdfFileObj)

table = ["sefdsfseoj woeirjeioj jo op"]

if "lol" in table:
    print("found")
else:
    print('not found')