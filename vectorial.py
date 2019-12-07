def change(file):
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
file=change("weights_reversed.txt")

def produit_interne(file , requete):
	requete=requete.split()
	i=1
	pertinant_doc=[]
	while i < 3205:
		document=[line for line in file if int(line["dic"])==(i)]
		poid=0
		for doc in document:
			for word in requete:
				if word.lower()==doc["word"]:
					poid+=float(doc["weight"])
		if poid != 0:
			pertinant_doc.append("document: "+str(i)+" poid : "+str(poid))
		i+=1
	if len(pertinant_doc) == 0:
		return False
	else:
		return pertinant_doc

