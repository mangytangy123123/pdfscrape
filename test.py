import pdfreader
from openpyxl import load_workbook
from pdfreader import SimplePDFViewer

things = ['1. Full name of entity:','12. Occupation:',"13. Client's account number:",'15. ID number:',"11. Date of birth:","4. Other/initial: 3. Given name:"]
stuff = ['a','b','1. Full name of entity:']
a = ["unfilled" if x in things else x for x in stuff]
print(a)
