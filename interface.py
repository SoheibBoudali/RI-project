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
        pkl_file = open('index_req.pkl', 'rb')
        index_req = pickle.load(pkl_file)
        pkl_file.close()
        pkl_file = open('req_docs_dict.pkl', 'rb')
        req_docs_dict=pickle.load(pkl_file)
        pkl_file.close()
        keys=[key for key in req_docs_dict]
        self.tableWidget.setRowCount(len(index_req))
        i=0
        for j in range(1,len(index_req)+1):
            if j in keys:
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(index_req[j]))
            else:
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str("no docs for this request")))               
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
        pkl_file = open('reversed_weights.pkl', 'rb')
        reversed_weights_liste = pickle.load(pkl_file)
        pkl_file.close()
        pkl_file = open('req_docs_dict.pkl', 'rb')
        req_docs_dict=pickle.load(pkl_file)
        pkl_file.close()
        keys=[key for key in req_docs_dict]
        index_q=self.index.text()
        if int(index_q) not in keys:
            print("index non valide")
        else:        
            PI=produit_interne(reversed_weights_liste , req)
            CD=Coef_de_Dice(reversed_weights_liste , req)
            MC=Mesure_de_cosinus(reversed_weights_liste , req)
            MJ=Mesure_de_jaccard(reversed_weights_liste , req)
            self.Systeme.setRowCount(len(PI))
            i=0
            for j in range(0,len(PI)):
                self.Systeme.setItem(i, 0, QtWidgets.QTableWidgetItem(str(PI[j][1])))
                self.Systeme.setItem(i, 1, QtWidgets.QTableWidgetItem(str(PI[j][0])))
                self.Systeme.setItem(i, 2, QtWidgets.QTableWidgetItem(str(CD[j][0])))
                self.Systeme.setItem(i, 3, QtWidgets.QTableWidgetItem(str(MC[j][0])))
                self.Systeme.setItem(i, 4, QtWidgets.QTableWidgetItem(str(MJ[j][0])))
                i+=1        

            self.Supposed.setRowCount(len(req_docs_dict[int(index_q)]))
            i=0
            for doc in req_docs_dict[int(index_q)]:
                self.Supposed.setItem(i, 0, QtWidgets.QTableWidgetItem(doc))
                i+=1

            supo_docs=req_docs_dict[int(index_q)]
            print(supo_docs)
            sim_pi=int(len(PI)/4)
            PI.sort(reverse=True)
            sys_docs_pi=[str(doc[1]) for doc in PI[:sim_pi]]
            print(sys_docs_pi)
            self.rappel_pi.setText(str(rappel(sys_docs_pi,supo_docs)))
            self.precision_pi.setText(str(precision(sys_docs_pi,supo_docs)))
            sim_cd=int(len(CD)/4)
            CD.sort(reverse=True)
            sys_docs_cd=[str(doc[1]) for doc in CD[:sim_cd]]
            print(sys_docs_cd)
            self.rappel_cd.setText(str(rappel(sys_docs_cd,supo_docs)))
            self.precision_cd.setText(str(precision(sys_docs_cd,supo_docs)))
            sim_mc=int(len(MC)/4)
            MC.sort(reverse=True)
            sys_docs_mc=[str(doc[1]) for doc in MC[:sim_mc]]
            print(sys_docs_mc)
            self.rappel_mc.setText(str(rappel(sys_docs_mc,supo_docs)))
            self.precision_mc.setText(str(precision(sys_docs_mc,supo_docs)))
            sim_mj=int(len(MJ)/4)
            MJ.sort(reverse=True)
            sys_docs_mj=[str(doc[1]) for doc in MJ[:sim_mj]]
            print(sys_docs_mj)
            self.rappel_mj.setText(str(rappel(sys_docs_mj,supo_docs)))
            self.precision_mj.setText(str(precision(sys_docs_mj,supo_docs)))



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
