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
reversed_txt=open("reversed.txt","w+", encoding="utf-8")
for doc in range(0,len(reversed_file)) :
	for item in reversed_file[doc].items():
		line='('+item[0]+','+str(doc+1)+')->'+str(item[1])+'\n'
		reversed_txt.write(line)
index_txt=open("index.txt","w+", encoding="utf-8")
line=""
for doc in range(0,len(reversed_file)) :
	index_txt.write('Doc : '+str(doc+1)+'\n')
	for item in reversed_file[doc].items():
		line='('+item[0]+','+str(item[1])+')\n'
		index_txt.write(line)

#solution 2
index_dic=open("index_dic.txt","w+", encoding="utf-8")
line=""
dictionnaire=dict()		
for doc in range(0,len(reversed_file)) :
	word_dict=dict()
	for item in reversed_file[doc].items():
		word_dict[item[0]]=item[1]
	dictionnaire[doc+1]=word_dict



def word_freq_per_doc(doc , reversed_file):
	liste=[(item[0] , item[1])for item in reversed_file[doc].items()]
	return(liste)

def docs_freq_per_word(word , reversed_file):
	liste=[]
	for doc in range(0,len(reversed_file)):
		for item in reversed_file[doc].items():
			if(item[0]==word):
				liste.append((doc+1 , item[1]))
	return(liste)


