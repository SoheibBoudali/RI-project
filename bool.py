def change_bool(index_file):
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
	if requete=="":
		return False
	else:
		operator=["and","or"]
		opr_not="not"
		req=requete.split()
		if(req[len(req)-1].lower()==opr_not):
			return False
		for i in range(0,len(req)-1):
			if req[i].lower()==opr_not and req[i+1] in operator:
				return False
		req=[r for r in req if r.lower()!= opr_not]
		if len(req)%2 == 0 :
			return False
		for i in range(1,len(req),2):
			if req[i].lower() not in operator:
				return False
		for i in range(0,len(req),2):
			if req[i].lower() in operator:
				return False
		return True

def evaluate(requete , Liste_of_docs):
	pert_docs=[]
	opr_not="not"
	not_position=[]
	requete_init=requete.split()
	for i in range(0,len(requete_init)):
		if requete_init[i].lower()==opr_not:
			not_position.append(i)
	requete_init = [r for r in requete_init if r.lower()!=opr_not]
	for doc in range(0,len(Liste_of_docs)):
		req=[r for r in requete_init]
		for i in range(0,len(requete_init),2):
			for word in range(0,len(Liste_of_docs[doc])):
				if Liste_of_docs[doc][word]["word"].lower()== req[i].lower():
					req[i]=1
					break
			if req[i]!=1:
				req[i]=0
		for pos in not_position:
			req.insert(pos,opr_not)
		req_string=""
		for r in req:
			req_string+=' '+str(r)
		result = eval(req_string)
		if(result == 1):
			pert_docs.append('Documment : '+str(doc+1))
	return pert_docs

'''Liste_of_docs=change("index.txt")
requete="state and repeated or roots and not home"
if validate(requete):
	print(evaluate(requete , Liste_of_docs))
else:
	print('requete non valide')'''