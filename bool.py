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

#Liste=change("index.txt")

print(validate("hello And kh AND cedric"))