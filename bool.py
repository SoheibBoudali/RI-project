def change(index_file):
	special_chars="(,)"
	file = open(index_file , "r" , encoding="utf-8").read()
	file=file.split('\n')
	Liste_of_docs=[]
	for line in range(0,len(file)):
		if file[line].startswith("Doc"):
			line+=1
			while(line<len(file) and not file[line].startswith("Doc")):
				new_line=""
				for char in file[line]:
					if char in special_chars:
						new_line+=' '
					else:
						new_line+=char
				new_l=new_line.split()
				print(new_l)
				line+=1


'''def change(file):
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
'''
change("index.txt")
