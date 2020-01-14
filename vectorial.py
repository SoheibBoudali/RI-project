import pickle
from math import *
import time

pkl_file = open('reversed_weights.pkl', 'rb')
reversed_weights_liste = pickle.load(pkl_file)
pkl_file.close()

def word_weight_per_doc(doc , reversed_weights_liste):
	liste=[[item[0],item[2]] for item in reversed_weights_liste if item[1]==doc]
	return(liste)

def produit_interne(reversed_weights_liste , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	docs_zero=[]
	poids=[]
	nbrs_document=len(set([item[1] for item in reversed_weights_liste]))
	while i < nbrs_document+1:
		document=word_weight_per_doc(i,reversed_weights_liste)
		poid=0
		for word_weight in document:
			for word in requete:
				if word.lower()== word_weight[0]:
					poid+=word_weight[1]
		if poid>0:
			docs_zero.append(i)
			poids.append(poid)
			print(poid)
		i+=1
	for i in range(0,len(docs_zero)):
		pertinant_doc.append([poids[i],docs_zero[i]])
	return pertinant_doc

def Coef_de_Dice(reversed_weights_liste , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	docs_zero=[]
	poids=[]
	nbrs_document=len(set([item[1] for item in reversed_weights_liste]))
	while i < nbrs_document+1:
		document=word_weight_per_doc(i,reversed_weights_liste)
		poid=0
		top=0
		down_ti=0
		down_qi=0
		for word_weight in document:
			for word in requete:
				if word.lower()== word_weight[0]:
					top+=float(word_weight[1])
					down_ti+=top*top
					down_qi+=1
		if down_qi > 0 :
			poid=(2*top) / (down_ti + down_qi)
			if poid>0:
				docs_zero.append(i)
				poids.append(poid)
				print(poid)
		i+=1
	for i in range(0,len(docs_zero)):
		pertinant_doc.append([poids[i],docs_zero[i]])
	return pertinant_doc

def Mesure_de_cosinus(reversed_weights_liste , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	docs_zero=[]
	poids=[]
	nbrs_document=len(set([item[1] for item in reversed_weights_liste]))
	while i < nbrs_document+1:
		document=word_weight_per_doc(i,reversed_weights_liste)
		poid=0
		top=0
		down_ti=0
		down_qi=0
		for word_weight in document:
			for word in requete:
				if word.lower()== word_weight[0]:
					top+=float(word_weight[1])
					down_ti+=top*top
					down_qi+=1
		if down_qi > 0 :
			poid=top / sqrt(down_ti + down_qi)
			if poid > 0:
				docs_zero.append(i)
				poids.append(poid)
				print(poid)
		i+=1
	for i in range(0,len(docs_zero)):
		pertinant_doc.append([poids[i],docs_zero[i]])
	return pertinant_doc

def Mesure_de_jaccard(reversed_weights_liste , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	docs_zero=[]
	poids=[]
	nbrs_document=len(set([item[1] for item in reversed_weights_liste]))
	while i < nbrs_document+1:
		document=word_weight_per_doc(i,reversed_weights_liste)
		poid=0
		top=0
		down_ti=0
		down_qi=0
		for word_weight in document:
			for word in requete:
				if word.lower()== word_weight[0]:
					top+=float(word_weight[1])
					down_ti+=top*top
					down_qi+=1
		if down_qi > 0 :
			poid=top / ( down_ti + down_qi - top)
			if poid > 0:
				docs_zero.append(i)
				poids.append(poid)
				print(poid)
		i+=1
	for i in range(0,len(docs_zero)):
		pertinant_doc.append([poids[i],docs_zero[i]])
	return pertinant_doc



#test
'''requete="state home job"
start=time.time()
print(produit_interne(reversed_weights_liste , requete))
print(time.time()-start)
print(Coef_de_Dice(reversed_weights_liste , requete))
print(Mesure_de_cosinus(reversed_weights_liste , requete))
print(Mesure_de_jaccard(reversed_weights_liste , requete))'''
