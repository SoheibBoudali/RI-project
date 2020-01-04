def change_vect(file):
	special_chars="(,)->"
	File=open(file,"r",encoding="utf-8")
	lines=File.readlines()
	liste=[]
	for line in lines:
		dic= dict()
		new_line=""
		for char in line:
			if char in special_chars:
				new_line+=' '
			else:
				new_line+=char
		new_l=new_line.split()
		dic["word"] = new_l[0]
		dic["dic"] = new_l[1]
		dic["weight"] = new_l[2]
		liste.append(dic)
	return liste

def produit_interne(file , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	docs_zero=[]
	poids=[]
	while i < 3205:
		document=[line for line in file if int(line["dic"])==(i)]
		poid=0
		for doc in document:
			for word in requete:
				if word.lower()==doc["word"]:
					poid+=float(doc["weight"])
		if poid != 0:
			print(poid)
			docs_zero.append(i)
			poids.append(poid)
		i+=1
	sim=sum(poids)/len(poids)
	for i in range(0,len(docs_zero)):
		if poids[i]>sim:
			pertinant_doc.append([docs_zero[i],poids[i]])
	return pertinant_doc

def Coef_de_Dice(file , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	while i < 3205:
		document=[line for line in file if int(line["dic"])==(i)]
		top=0
		down_ti=0
		down_qi=0
		poid=0
		for doc in document:
			for word in requete:
				if word.lower()==doc["word"]:
					top+=float(doc["weight"])
					down_ti+=float(doc["weight"])*float(doc["weight"])
					down_qi+=1
		if down_qi != 0 :
			poid=(2*top) / (down_ti + down_qi)
			print("document :"+str(i)+" poid "+str(poid))
			if poid != 0:
				pertinant_doc.append([i,poid])
		i+=1
	return pertinant_doc

def Mesure_de_cosinus(file , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	while i < 3205:
		document=[line for line in file if int(line["dic"])==(i)]
		top=0
		down_ti=0
		down_qi=0
		poid=0
		for doc in document:
			for word in requete:
				if word.lower()==doc["word"]:
					top+=float(doc["weight"])
					down_ti+=float(doc["weight"])*float(doc["weight"])
					down_qi+=1
		if down_qi != 0 :
			poid=top / sqrt(down_ti + down_qi)
			print("document :"+str(i)+" poid "+str(poid))
			if poid != 0:
				pertinant_doc.append([i,poid])
		i+=1
	return pertinant_doc

def Mesure_de_jaccard(file , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	while i < 3205:
		document=[line for line in file if int(line["dic"])==(i)]
		top=0
		down_ti=0
		down_qi=0
		poid=0
		for doc in document:
			for word in requete:
				if word.lower()==doc["word"]:
					top+=float(doc["weight"])
					down_ti+=float(doc["weight"])*float(doc["weight"])
					down_qi+=1
		if down_qi != 0 :
			poid=top / ( down_ti + down_qi - top)
			print("document :"+str(i)+" poid "+str(poid))
			if poid != 0:
				pertinant_doc.append([i,poid])
		i+=1
	return pertinant_doc

from math import *
'''file=change("weights_reversed.txt")
requete="preliminary state" 
print(Mesure_de_jaccard(file , requete))'''
