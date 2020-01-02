def req_docs(file_name):
	file=open(file_name,"r",encoding="utf-8").readlines()
	req_docs_liste=[]
	i=0
	'''	while i < len(file): 
		line_i=file[i].split()
		liste=[]
		docs=[]
		liste.append(line_i[0])
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
		liste.append(docs)
		req_docs_liste.append(liste)'''
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

print(req_docs("cacm/qrels.text"))