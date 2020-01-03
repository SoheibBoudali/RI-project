import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow
from PySide2.QtCore import Slot, Qt
from bool import *
from vectorial import *
from evaluation import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.bool_btn.clicked.connect(self.bool)
        self.vect_btn.clicked.connect(self.vect)
        dic = index_req("cacm/query.text")
        self.tableWidget.setRowCount(len(dic))
        i=0
        for j in range(1,len(dic)+1):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(dic[j]))
            i+=1
        self.tableWidget.cellClicked.connect(self.query_selector)
        self.Evaluate.clicked.connect(self.evaluation)
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
    		file=change_vect("weights_reversed.txt")
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
    def query_selector(self,row,column):
        self.selected_query.setText(self.tableWidget.item(row, 0).text())
        self.index.setText(str(row+1))
        self.Evaluate.setEnabled(True)
    def evaluation(self):
        print("hello")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
