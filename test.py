import pickle
pkl_file = open('req_docs_dict.pkl', 'rb')
req_docs_dict=pickle.load(pkl_file)
pkl_file.close()

for i in req_docs_dict:
	print(i)