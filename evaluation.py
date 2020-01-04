from nltk.corpus import stopwords
import string

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
		dic[int(line_i[0])]=docs
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
	stopWords = stopwords.words('english')
	punctuation=string.punctuation
	new_liste=[]
	for doc in liste_of_documents:
		doc_punc=""
		for c in doc:
			if c not in punctuation:
				doc_punc+=c
			else :
				doc_punc+=" "
		new_doc=""
		for word in doc_punc.split():
			if word.lower() not in stopWords:
				new_doc+=" "+word.lower()
		new_liste.append(new_doc)
	i=1
	for doc in new_liste:
		dic[i]=doc
		i+=1
	return dic
#index_req("cacm/query.text")

def rappel(sys_pert_docs , supo_pert_docs):
	intersection=len([doc for doc in sys_pert_docs if doc in supo_pert_docs])
	return intersection/len(supo_pert_docs)

def precision(sys_pert_docs , supo_pert_docs):
	intersection=len([doc for doc in sys_pert_docs if doc in supo_pert_docs])
	return intersection/len(sys_pert_docs)

'''sys_pert_docs=[1,2,3,4]
supo_pert_docs=[2,4,5]
print(rappel(sys_pert_docs,supo_pert_docs))
print(precision(sys_pert_docs,supo_pert_docs))'''