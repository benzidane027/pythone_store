import os
os.system("pyuic5 -x item.ui -o test1.py")
from test import *
from test1 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication,QHeaderView,QTableWidgetItem
from PyQt5.QtCore import QEvent,QSize,QPoint
import sys,datetime,time,threading
import Item

class myform(QMainWindow):
    toggel_button_=True
    ismaximuz=False
    icon_maximuz = QtGui.QIcon()
    i=0
    
    def __init__(self):
        super().__init__()
        self.move(200,200)
        self.ui=Ui_MainWindow()
        self.myItem={}
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window |QtCore.Qt.CustomizeWindowHint) 
        self.ui.close_button.clicked.connect(lambda : sys.exit())
        self.ui.min_button.clicked.connect(lambda : self.showMinimized())
        self.ui.max_button.clicked.connect(lambda : self.maximuz())
        self.ui.toggel_button.clicked.connect(lambda : self.menu_exapand())

        # the 3 button 
        self.ui.button_remove.clicked.connect(self.delet_item)
        self.ui.button_add.clicked.connect(self.adding)
        self.ui.button_edit.clicked.connect(self.editting)

        self.ui.button_remove.setEnabled(False)
        self.ui.button_edit.setEnabled(False)

        #print(self.size())
        def moveWindow(e):
            if self.isMaximized() == False: #Not maximized
                if e.buttons() ==QtCore.Qt.LeftButton:  
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.frame_3.mouseMoveEvent=moveWindow

        #table
        self.ui.mytable.horizontalHeader().setStretchLastSection(True) 
        self.ui.mytable.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
        self.insetItem()
        self.ui.mytable.cellClicked.connect(self.number_of_select)
        


        #self.ui.button_cart.clicked.connect(self.number_of_select)
    def menu_exapand(self):
        #ui.left_fram.setMaximumWidth(100)
        if myform.toggel_button_:
            self.ui.left_fram.setMaximumWidth(135)
            self.ui.frame_2.setMaximumWidth(135)
            self.ui.frame_5.setMaximumWidth(135)
            self.ui.button_product.setText("  product  ")
            self.ui.bottun_account.setText("  account  ")
            self.ui.button_cart.setText(" cart  ")
            self.ui.button_file.setText(" file  ")
            self.ui.button_support.setText(" about  ")
            self.ui.button_add.setText("  add")
            self.ui.button_remove.setText("remove")
            self.ui.button_edit.setText("edit")
            myform.toggel_button_=False
        else:
            self.ui.left_fram.setMaximumWidth(55)
            self.ui.frame_2.setMaximumWidth(55)
            self.ui.frame_5.setMaximumWidth(55)
            self.ui.button_product.setText("")
            self.ui.bottun_account.setText("")
            self.ui.button_cart.setText("")
            self.ui.button_file.setText("")
            self.ui.button_support.setText("")
            self.ui.button_add.setText("")
            self.ui.button_remove.setText("")
            self.ui.button_edit.setText("")
            myform.toggel_button_=True
            
    def maximuz(self):
        if myform.ismaximuz==True:
            self.showNormal()
            myform.ismaximuz=False
            myform.icon_maximuz.addPixmap(QtGui.QPixmap("cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.max_button.setIcon(myform.icon_maximuz)
            #print(myform.ismaximuz)
        elif myform.ismaximuz==False:
            self.showMaximized()
            myform.ismaximuz=True
            myform.icon_maximuz.addPixmap(QtGui.QPixmap("cil-window-restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.max_button.setIcon(myform.icon_maximuz)
            #print(myform.ismaximuz)
    def mousePressEvent(self,ev):
        self.clickPosition=ev.globalPos()


    def insetItem(self):
        obj=Item.item()

        id_s=obj.get_id_Ofall_item()
        self.ui.mytable.setRowCount(len(id_s))

        for i,index in enumerate(id_s):
            d=obj.get_Item(index[0])
            for j in range(1,6):
                if j!=1:
                    k=QTableWidgetItem(str(d[j]).title())
                    k.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
                    self.ui.mytable.setItem(i,j-1,k)
                else:
                    k=QTableWidgetItem(str(d[j]).title())
                    k.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate|QtCore.Qt.ItemIsSelectable)
                    k.setCheckState(QtCore.Qt.Unchecked)
                    self.ui.mytable.setItem(i,j-1,k)
                    self.myItem[d[j]]=k
        self.ui.label_2.setText(str(len(self.myItem)))
                    #print(k.checkState())
    def selcted_item(self):
        result=[]
        for key in self.myItem:
            if self.myItem[key].checkState()==2:
                result.append(key)
        return result
    def number_of_select(self):
        self.ui.label_8.setText(str((len(self.selcted_item()))))
        if len(self.selcted_item()):
            self.ui.button_remove.setEnabled(True)
            self.ui.button_edit.setEnabled(True)
        else:
            self.ui.button_remove.setEnabled(False)
            self.ui.button_edit.setEnabled(False)

    # the 3 button
    def delet_item(self):
        obj=Item.item()
        if len(self.selcted_item())==1:
            for key in self.myItem:
                if self.myItem[key].checkState()==2:
                    obj.delet_Item_byId(int(obj.get_Id_byName(key)[0]))
                    self.myItem={}
                    self.insetItem()
                    break
        else:
            self.ui.label_6.setText("selct only one")


    def adding(self):
        d.setWindowFlags(QtCore.Qt.Window |QtCore.Qt.CustomizeWindowHint) 
        d.move(self.pos()+QPoint(200,100))
        d.show()
    def editting(self):
        pass
        

        



    
                    
if __name__ == "__main__":
    
    app=QApplication(sys.argv)
    obj=myform()
    obj.show()
    d=QWidget()
    obj=Ui_Form()
    obj.setupUi(d)
    app.exec_()

import sys 
from PyQt5.QtWidgets import * 
                    
   
