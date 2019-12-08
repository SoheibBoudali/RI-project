import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow
from PySide2.QtCore import Slot, Qt
from bool import *
from vectorial import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.bool_btn.clicked.connect(self.bool)
        self.vect_btn.clicked.connect(self.vect)

    @Slot()
    def bool(self):
    	Liste_of_docs=change_bool("index.txt")
    	requete=self.bool_req.text()
    	Liste=[]
    	if validate(requete):
    		Liste=evaluate(requete , Liste_of_docs)
    		result=""
    		if(len(Liste)== 0):
    			self.bool_result.setText('no pertinant document')
    		else:
	    		for l in Liste:
	    			result+=l+'\n'
	    		self.bool_result.setText(result)
    	else:
    		self.bool_result.setText('requete non valide')
    def vect(self):
    	result=""
    	req=self.vect_req.text()
    	if req == "":
    		self.vect_result.setText('requete vide')
    	else:	
    		file=change("weights_reversed.txt")
    		if self.comboBox.currentText()=="produit_interne":
    			liste=produit_interne(file , req)
    			if liste != False:
    				for l in liste:
    					result+=l+'\n'
    				self.vect_result.setText(result)
    			else:
    				self.vect_result.setText("no pertinant document")
    		else:
    			if self.comboBox.currentText()=="Coef_de_Dice":
    				liste=Coef_de_Dice(file , req)
	    			if liste != False:
	    				for l in liste:
	    					result+=l+'\n'
	    				self.vect_result.setText(result)
	    			else:
	    				self.vect_result.setText("no pertinant document")
    			else:
    				if self.comboBox.currentText()=="Messure_de_cosinus":
    					liste=Messure_de_cosinus(file , req)
		    			if liste != False:
		    				for l in liste:
		    					result+=l+'\n'
		    				self.vect_result.setText(result)
		    			else:
		    				self.vect_result.setText("no pertinant document")
    				else:
    					liste=Mesure_de_jaccard(file , req)
		    			if liste != False:
		    				for l in liste:
		    					result+=l+'\n'
		    				self.vect_result.setText(result)
		    			else:
		    				self.vect_result.setText("no pertinant document")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
