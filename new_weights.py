import math
import pickle

pkl_file = open('reversed.pkl', 'rb')
reversed_liste = pickle.load(pkl_file)
pkl_file.close()

def word_freq_per_doc(doc , reversed_liste):
	liste=[[item[0],item[2]] for item in reversed_liste if item[1]==doc]
	return(liste)

def docs_freq_per_word(word , reversed_liste):
	liste=[[item[1],item[2]] for item in reversed_liste if item[0]==word]
	return(liste)

def taille(reversed_liste):
	return len(set(item[1] for item in reversed_liste))

def max_freq(doc , reversed_liste):
	liste=word_freq_per_doc(doc , reversed_liste)
	return max([item[1] for item in liste])

def ni(word , reversed_liste):
	return len(docs_freq_per_word(word , reversed_liste))

def weight(reversed_liste):
	file=open("weights_reversed.txt","w+",encoding="utf-8")
	nbr_docs=taille(reversed_liste)
	reversed_weights_liste=[]
	for line in reversed_liste:
		#poids(ti, dj)=(freq(ti,dj)/Max(freq(t,dj))*Log((N/ni) +1)
		poid=line[2]/max_freq(line[1],reversed_liste)*math.log10(nbr_docs/ni(line[0],reversed_liste))+1
		print(poid)
		file.write("("+str(line[0])+","+str(line[1])+") -> "+str(poid)+"\n")
		weight_liste=[]
		weight_liste.append(line[0])
		weight_liste.append(line[1])
		weight_liste.append(poid)
		reversed_weights_liste.append(weight_liste)
	output = open('reversed_weights.pkl', 'wb')
	pickle.dump(reversed_weights_liste, output)
	output.close()


import time
start_time = time.time()
weight(reversed_liste)
print(time.time()-start_time)