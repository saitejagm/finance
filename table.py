import tabula, re
from Pages import fnPDF_FindText

xFile = 'test1.pdf'
test = 'test1'
xString = r'summary(.{4}| )financial (?:information|statement)'
page_num, _ = fnPDF_FindText(xFile, xString)
print(page_num)

tabula.convert_into(xFile, (test + '.csv'), output_format="csv", pages=page_num+1)
