import tabula, re

def fnPDF_FindText(xFile, xString):
	import PyPDF2, re
	PageFound = -1
	pdfDoc = PyPDF2.PdfFileReader(open(xFile, "rb"))
	for i in range(0, pdfDoc.numPages):
		content = ""
		content += pdfDoc.getPage(i).extractText().strip().replace('\n','').lower()
		result = re.search(xString, content)
		print(i, result)
		if result is not None:
			PageFound = i
			content = content.replace('.','')
			at = content.index(result.group())+len(result.group())
			return int(content[at+2:at+5])


xFile = 'test1.pdf'
test = 'test1'
xString = r'summary(.{4}| )financial (?:information|statement)'
page_num = fnPDF_FindText(xFile, xString)
print(page_num)

tabula.convert_into(xFile, (test + '.csv'), output_format="csv", pages=page_num+1)
