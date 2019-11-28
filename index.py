import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

file = open("cacm/cacm.all","r",encoding="utf-8")
lines = file.readlines()
liste_of_documents=[]
for i in range(0,len(lines)):
	document=""
	if lines[i].startswith(".I"):
		i+=1
		while  i<len(lines) and not lines[i].startswith(".I"):
			if lines[i].startswith(".T"):
				i+=1
				while i<len(lines) and not (lines[i].startswith(".I") or lines[i].startswith(".W") or lines[i].startswith(".A") or lines[i].startswith(".N") or lines[i].startswith(".B") or lines[i].startswith(".X")):
					document+=lines[i]
					i+=1
			if i<len(lines) and lines[i].startswith(".W"):
				i+=1
				while i<len(lines) and not (lines[i].startswith(".I") or lines[i].startswith(".T") or lines[i].startswith(".A") or lines[i].startswith(".N") or lines[i].startswith(".B") or lines[i].startswith(".X")):
					document+=lines[i]
					i+=1
			i+=1
		liste_of_documents.append(document)

stopWords = stopwords.words('english')
punctuation=string.punctuation
tokens=[]
for doc in liste_of_documents:
	doc_punc=""
	for c in doc:
		if c not in punctuation:
			doc_punc+=c
	new_doc=""
	for word in doc_punc.split():
		if word.lower() not in stopWords:
			new_doc+=" "+word
	tokens.append(new_doc) 
for doc in tokens:
	print(doc.split())
	print("\n")

