#create a fuction that read qrels file and return for each req a liste of docs
def req_docs(file_name):
	file=open(file_name,"r",encoding="utf-8").readlines()
	i=0
	dic=dict()
	while i < len(file): 
		line_i=file[i].split()
		docs=[]
		cpt=0
		j=i
		exit=0
		while (j < len(file) and not exit):
			line_j=file[j].split()
			j+=1
			if line_i[0]==line_j[0]:
				docs.append(line_j[1])
				cpt+=1
			else:
				exit=1
		i+=cpt
		dic[line_i[0]]=docs
	return dic
#print(req_docs("cacm/qrels.text"))

#create a function that read query file and return dictionnaire of req
def index_req(file_name):
	lines = open(file_name,"r",encoding="utf-8").readlines()
	dic=dict()
	liste_of_documents=[]
	for i in range(0,len(lines)):
		document=""
		if lines[i].startswith(".I"):
			i+=1
			while  i<len(lines) and not lines[i].startswith(".I"):
				if i<len(lines) and lines[i].startswith(".W"):
					i+=1
					while i<len(lines) and not (lines[i].startswith(".I") or lines[i].startswith(".A") or lines[i].startswith(".N")):
						document+=lines[i]
						i+=1
				i+=1
			liste_of_documents.append(document)
	i=1
	for doc in liste_of_documents:
		dic[i]=doc
		i+=1
	return dic
#print(index_req("cacm/query.text"))

