import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow
from PySide2.QtCore import Slot, Qt
from bool import *
from vectorial import *
from evaluation import *
import pickle

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
        pkl_file = open('index_dic.pkl', 'rb')
        index = pickle.load(pkl_file)
        pkl_file.close()
        requete=self.bool_req.text()
        Liste=[]
        if validate(requete):
            Liste=evaluate(requete , index)
            result=""
            if(len(Liste)== 0):
                self.bool_result.setText('no pertinant document')
            else:
                for l in Liste:
                    result+=l+'\n'
                self.bool_result.setText(result)
        else:
            self.bool_result.setText('non valide request')
    def vect(self):
        pkl_file = open('reversed_weights.pkl', 'rb')
        reversed_weights_liste = pickle.load(pkl_file)
        pkl_file.close()
        result=""
        req=self.vect_req.text()
        if req == "":
            self.vect_result.setText('empty request')
        else:	
            if self.comboBox.currentText()=="produit_interne":
                liste=produit_interne(reversed_weights_liste , req)
                if len(liste) != 0:
                    liste.sort(reverse=True)
                    for l in liste:
                        result+="document: "+str(l[1])+" similarity "+str(l[0])+'\n'
                    self.vect_result.setText(result)
                else:
                    self.vect_result.setText("no pertinant document")
            else:
                if self.comboBox.currentText()=="Coef_de_Dice":
                    liste=Coef_de_Dice(reversed_weights_liste , req)
                    if len(liste) != 0:
                        liste.sort(reverse=True)
                        for l in liste:
                            result+="document: "+str(l[1])+" similarity "+str(l[0])+'\n'
                        self.vect_result.setText(result)
                    else:
                        self.vect_result.setText("no pertinant document")
                else:
                    if self.comboBox.currentText()=="Messure_de_cosinus":
                        liste=Mesure_de_cosinus(reversed_weights_liste, req)
                        if len(liste) != 0:
                            liste.sort(reverse=True)
                            for l in liste:
                                result+="document: "+str(l[1])+" similarity "+str(l[0])+'\n'
                            self.vect_result.setText(result)
                        else:
                            self.vect_result.setText("no pertinant document")
                    else:
                        liste=Mesure_de_jaccard(reversed_weights_liste , req)
                        if len(liste) != 0:
                            liste.sort(reverse=True)
                            for l in liste:
                                result+="document: "+str(l[1])+" similarity "+str(l[0])+'\n'
                            self.vect_result.setText(result)
                        else:
                            self.vect_result.setText("no pertinant document")
    def query_selector(self,row,column):
        self.selected_query.setText(self.tableWidget.item(row, 0).text())
        self.index.setText(str(row+1))
        self.Evaluate.setEnabled(True)
    def evaluation(self):
        req=self.selected_query.text()
        file=change_vect("weights_reversed.txt")
        PI=produit_interne(file , req)
        #CD=Coef_de_Dice(file , req)
        #MC=Mesure_de_cosinus(file , req)
        #MJ=Mesure_de_jaccard(file , req)
        self.Systeme.setRowCount(len(PI))
        i=0
        for j in range(0,len(PI)):
            self.Systeme.setItem(i, 0, QtWidgets.QTableWidgetItem(str(PI[j][0])))
            self.Systeme.setItem(i, 1, QtWidgets.QTableWidgetItem(str(PI[j][1])))
            #self.Systeme.setItem(i, 2, QtWidgets.QTableWidgetItem(str(CD[j][1])))
            #self.Systeme.setItem(i, 3, QtWidgets.QTableWidgetItem(str(MC[j][1])))
            #self.Systeme.setItem(i, 4, QtWidgets.QTableWidgetItem(str(MJ[j][1])))
            i+=1        
        index=self.index.text()
        req_docs_dict=req_docs("cacm/qrels.text")
        self.Supposed.setRowCount(len(req_docs_dict[int(index)]))
        i=0
        for doc in req_docs_dict[int(index)]:
            self.Supposed.setItem(i, 0, QtWidgets.QTableWidgetItem(doc))
            i+=1
        supo_docs=req_docs_dict[int(index)]
        print(supo_docs)
        sys_docs=[str(doc[0]) for doc in PI]
        print(sys_docs)
        self.rappel.setText(str(rappel(sys_docs,supo_docs)))
        self.precision.setText(str(precision(sys_docs,supo_docs)))
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
