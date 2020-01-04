import time
start_time = time.time()
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
		else:
			doc_punc+=" "
	new_doc=""
	for word in doc_punc.split():
		if word.lower() not in stopWords:
			new_doc+=" "+word.lower()
	new_doc+="\n"
	tokens.append(new_doc)

reversed_file=[]
from nltk import FreqDist
for doc in tokens:
	freqdist= FreqDist(doc.split())
	reversed_file.append(freqdist)
from operator import itemgetter

reversed_liste=[]
for doc in range(0,len(reversed_file)) :
	for item in reversed_file[doc].items():
		reversed_line=[]
		reversed_line.append(item[0])
		reversed_line.append(doc+1)
		reversed_line.append(item[1])
		reversed_liste.append(reversed_line)

reversed_txt=open("reversed.txt","w+", encoding="utf-8")
for line in reversed_liste:
	reversed_line='('+line[0]+','+str(line[1])+')->'+str(line[2])+'\n'
	reversed_txt.write(reversed_line)

import pickle

# write python dict to a file
output = open('reversed.pkl', 'wb')
pickle.dump(reversed_liste, output)
output.close()

end_time=time.time()
print(end_time - start_time)

def word_freq_per_doc(doc , reversed_liste):
	liste=[[item[0],item[2]] for item in reversed_liste if item[1]==doc]
	return(liste)

def docs_freq_per_word(word , reversed_liste):
	liste=[[item[1],item[2]] for item in reversed_liste if item[0]==word]
	return(liste)


