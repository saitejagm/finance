 
import re, nltk, PyPDF2
from Pages import fnPDF_FindText

for k in range(3,7):
	xFile = 'samples/test'+str(k)+'.pdf'
	xString = r'our business'
	pdfDoc = PyPDF2.PdfFileReader(open(xFile, "rb"))

	article_text = ""

	begin, end = fnPDF_FindText(xFile, xString)
	print("--:",begin,end)
	for i in range(begin, end):
		article_text += pdfDoc.getPage(i).extractText().strip().replace('\n','')


	sentence_list = nltk.sent_tokenize(article_text)

	stopwords = nltk.corpus.stopwords.words('english')

	word_frequencies = {}  
	for word in nltk.word_tokenize(article_text):  
	    if word not in stopwords:
	        if word not in word_frequencies.keys():
	            word_frequencies[word] = 1
	        else:
	            word_frequencies[word] += 1


	maximum_frequncy = max(word_frequencies.values())

	for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

	sentence_scores = {}  
	for sent in sentence_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_frequencies.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in sentence_scores.keys():
	                    sentence_scores[sent] = word_frequencies[word]
	                else:
	                    sentence_scores[sent] += word_frequencies[word]


	import heapq  
	summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

	summary = ' '.join(summary_sentences)  
	print(summary) 

	with open('samples/summary'+str(k)+'.txt','a') as file:  
	    file.write(summary+'\n')


