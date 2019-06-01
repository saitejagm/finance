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
			begin = int(content[at+2:at+5])
			# iterate till next number
			i,end = 7,0
			while True:
				if content[at+i].isdigit():
					while(content[at+i : at+end+i+1].isdigit()):
						end+=1
					end = int(content[at+i:at+end+i+1])
					break
				i+=1
			return begin, end