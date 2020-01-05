import pickle
import time 
pkl_file = open('index_dic.pkl', 'rb')
index = pickle.load(pkl_file)
pkl_file.close()

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

def evaluate(requete ,index):
	pert_docs=[]
	opr_not="not"
	not_position=[]
	requete_init=requete.split()
	for i in range(0,len(requete_init)):
		if requete_init[i].lower()==opr_not:
			not_position.append(i)
	requete_init = [r for r in requete_init if r.lower()!=opr_not]
	for i in range (1,len(index)+1):
		req=[r for r in requete_init]
		for j in range(0,len(requete_init),2):
			if req[j].lower() in [key for key in index[i]]:
				req[j]=1
			if req[j]!=1:
				req[j]=0
		for pos in not_position:
			req.insert(pos,opr_not)
		req_string=""
		for r in req:
			req_string+=' '+str(r)
		result = eval(req_string)
		if(result == 1):
			pert_docs.append('Documment : '+str(i))
	return pert_docs

'''request="state or love or not preliminary and not hate"
start=time.time()
print(evaluate_dict(request ,index))
print(time.time()-start)'''
