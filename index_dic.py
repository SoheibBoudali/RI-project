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

index_freqdist=[]
from nltk import FreqDist
for doc in tokens:
	freqdist= FreqDist(doc.split())
	index_freqdist.append(freqdist)
from operator import itemgetter

index_dic=open("index_dic.txt","w+", encoding="utf-8")
line=""
dictionnaire=dict()		
for doc in range(0,len(index_freqdist)) :
	word_dict=dict()
	for item in index_freqdist[doc].items():
		word_dict[item[0]]=item[1]
	dictionnaire[doc+1]=word_dict

index_dic.write(str(dictionnaire))

import pickle

# write python dict to a file
output = open('index_dic.pkl', 'wb')
pickle.dump(dictionnaire, output)
output.close()

'''# read python dict back from the file
pkl_file = open('index_dic.pkl', 'rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()

print( mydict2)'''
som=0
print(len(dictionnaire[1]))
for i in range(1,len(dictionnaire)+1):
	som+=len(dictionnaire[i])
print(som)
end_time=time.time()
print(end_time - start_time)