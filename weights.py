import math

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
		dic["freq"] = new_l[2]
		liste.append(dic)
	return liste

def maxi(dict , doc):
	return max([dict[i]["freq"] for i in range(0,len(dict)) if int(dict[i]["dic"])==doc])

def Nbr(dict):
	return len(set([dict[i]["dic"] for i in range(0,len(dict))]))

def ni(dict , word):
	liste=[int(dict[i]["dic"]) for i in range(0,len(dict)) if word== dict[i]["word"]]
	return len(liste)

def weights(dictio):
	file=open("weights_reversed.txt" , "w+" , encoding="utf-8")
	N=Nbr(dictio)
	for line in range(0,len(dictio)):
		poid_string=""
		#poids(ti, dj)=(freq(ti,dj)/Max(freq(dj))*Log((N/ni) +1)
		poid=int(dictio[line]["freq"])/int(maxi(dictio,int(dictio[line]["dic"])))*math.log10(N/ni(dictio,dictio[line]["word"])) + 1
		#poid_string="poids("+str(dictio[line]["word"])+','+str(dictio[line]["dic"])+")="+str(poid)+'\n'
		poid_string="("+str(dictio[line]["word"])+','+str(dictio[line]["dic"])+")->"+str(poid)+'\n'
		file.write(poid_string)

Dict=change("reversed.txt")

weights(Dict)
