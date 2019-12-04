def change(index_file):
	special_chars="(,)"
	file = open(index_file , "r" , encoding="utf-8").read()
	file=file.split('\n')
	Liste_of_docs=[]
	for line in range(0,len(file)):
		if file[line].startswith("Doc"):
			line+=1
			words=[]
			while(line<len(file) and not file[line].startswith("Doc")):
				new_line=""
				for char in file[line]:
					if char in special_chars:
						new_line+=' '
					else:
						new_line+=char
				new_l=new_line.split()
				dic=dict()
				dic["word"]=new_l[0]
				dic["freq"]=new_l[1]
				words.append(dic)
				line+=1
			Liste_of_docs.append(words)
	return Liste_of_docs
def validate(requete):
	operator=["and","or","not"]
	req=requete.split()
	if len(req)%2 == 0 :
		return False
	for i in range(1,len(req),2):
		if req[i].lower() not in operator:
			return False
	for i in range(0,len(req),2):
		if req[i].lower() in operator:
			return False
	return True

Liste_of_docs=change("index.txt")
def evaluate(requete , Liste_of_docs):
	pert_docs=[]
	for doc in range(0,len(Liste_of_docs)):
		req=requete.split()
		for i in range(0,len(req),2):
			for word in range(0,len(Liste_of_docs[doc])):
				if(Liste_of_docs[doc][word]["word"].lower()== req[i].lower()):
					req[i]=1
					break
			if(req[i]!=1):
				req[i]=0
		req_string=""
		for r in req:
			req_string+=' '+str(r)
		result = eval(req_string)
		if(result == 1):
			pert_docs.append('Documment : '+str(doc))
	return pert_docs
requete="state and repeated or roots"
if validate(requete):
	print(evaluate(requete , Liste_of_docs))
else:
	print('requete non valide')