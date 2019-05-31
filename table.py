# import tabula

def fnPDF_FindText(xFile, xString):
	import PyPDF2, re
	PageFound = -1
	pdfDoc = PyPDF2.PdfFileReader(open(xFile, "rb"))
	for i in range(0, pdfDoc.numPages):
		content = ""
		content += pdfDoc.getPage(i).extractText().strip().replace('\n','').lower()
		print(i, xString in content)
		if xString in content:
			PageFound = i
			content = content.replace('.','')
			at = content.index(xString)+len(xString)
			return int(content[at+2:at+5])


xFile = '/Users/ksreenivasareddy/Downloads/test1.pdf'
xString = 'summary of financial information'
page_num = fnPDF_FindText(xFile, xString)
print(page_num)