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
		dic["weight"] = new_l[2]
		liste.append(dic)
	return liste
file=change("weights_reversed.txt")

