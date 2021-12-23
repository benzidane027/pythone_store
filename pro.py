import os,sys,time
import sqlite3
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QStatusBar,QPushButton
from PyQt5.QtGui import QPalette
print('**************begin*************')

class LOGIN_Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,340,448,280)
        self.setWindowTitle("WelCome")
        self.pp=QPalette()
        self.setPalette(self.pp)



#ittend
        self.mainLable()
        self.lables__()
        self.buttons__()
        self.lineEdit__()
#buttin_connect
        self.button_connect.clicked.connect(self.on_click_button_conect)
        self.button_singUp.clicked.connect(self.on_click_button_singUp)
        self.button_save.clicked.connect(self.on_click_button_save)
    def mainLable(self):
        self.lb0=QLabel(self)
        self.lb0.resize(448,280)
        self.lb0.setPixmap(QtGui.QPixmap("shopImg.jpg").scaled(448,280))
    def lables__(self):
        #lable 0
        self.label_LogIn=QLabel("Log In   ",self)
        self.label_LogIn.move(30,25)
        self.label_LogIn.setFont(QtGui.QFont("",30))
        self.label_LogIn.setStyleSheet("color:#ed6663;")

        #lable 1
        self.label_user=QLabel("user",self)
        self.label_user.move(40,90)
        self.label_user.setFont(QtGui.QFont("",20))
        self.label_user.setStyleSheet("color:#f5f1da;")

        #lable 2
        self.label_pass=QLabel("pass",self)
        self.label_pass.move(40,140)
        self.label_pass.setFont(QtGui.QFont("",20))
        self.label_pass.setStyleSheet("color:#f5f1da;")

        #lable 3
        self.label_error=QLabel("no error message",self)
        self.label_error.move(10,260)
        self.label_error.setFont(QtGui.QFont("",12))
        self.label_error.resize(200,20)
        #self.label_error.setStyleSheet("color:red")

    def buttons__(self):
        self.button_connect=QPushButton("connect",self)
        self.button_connect.move(260,248)

        self.button_singUp=QPushButton("sing Up",self)
        self.button_singUp.move(350,248)

        self.button_save=QPushButton("  save ",self)
        self.button_save.move(350,247)
        self.button_save.hide()
        
    def lineEdit__(self):
        #line_edit 0
        self.line_edit_user=QLineEdit(self)
        self.line_edit_user.move(35,120)
        
        #line_edit 1
        self.line_edit_pass=QLineEdit(self)
        self.line_edit_pass.move(35,175)
        self.line_edit_pass.setEchoMode(2)

    def on_click_button_conect(self):
        self.label_LogIn.setText("Log In   ")
        self.button_save.hide()
        self.button_singUp.show()
        self.line_edit_pass.setEchoMode(2)
        

        username,password=self.line_edit_user.text(),self.line_edit_pass.text()
        if username.__len__()==0 or password.__len__()==0:
            self.label_error.setText("error one field is empty")
        else:
            if username.__len__()<6 or password.__len__()<6:
                self.label_error.setText("error field less than 6 char")
            else:
                if username.isalpha() and password.isalnum():
                    if connect_to_dateBase_ForLogIn(username,password):
                        self.label_error.setText("****** welcom ******")
                        time.sleep(1)

                    else:
                        self.label_error.setText("error user not found")
                else:
                    self.label_error.setText("error bad charcter entred")

    def on_click_button_singUp(self):
        self.label_LogIn.setText("Sing Up")
        self.button_singUp.hide()
        self.button_save.show()
        self.line_edit_pass.setText("")
        self.line_edit_user.setText("")
        self.line_edit_pass.setEchoMode(0)
    def on_click_button_save(self):
        #print(self.line_edit_pass.text(),self.line_edit_user.text())
        username,password=self.line_edit_user.text(),self.line_edit_pass.text()
        if username.__len__()==0 or password.__len__()==0:
            self.label_error.setText("error one field is empty")
        else:
            if username.__len__()<6 or password.__len__()<6:
                self.label_error.setText("error field less than 6 char")
            else:
                if username.isalpha() and password.isalnum():
                    if connect_to_dateBase_ForSingUp(username,password):
                        self.label_error.setText("Done registred succesfuly")
                        self.line_edit_pass.setText("")
                        self.line_edit_user.setText("")
                    else:
                        self.label_error.setText("error username used before")
                else:
                    self.label_error.setText("error bad charcter entred")


def connect_to_dateBase_ForLogIn(usernamen,password):
    db=sqlite3.connect("pro.db")
    cr=db.cursor()
    cr__=cr.execute("select username,password from Log_in;")
    if (usernamen,password) in cr__.fetchall():
        return True
    else:
        return False
def connect_to_dateBase_ForSingUp(username,password):
    print(username,"\n",password)
    db=sqlite3.connect("pro.db")
    cr=db.cursor()
    cr__=cr.execute("select id from Log_in;")
    current_id=len(cr__.fetchall())
    cr__=cr.execute("select username from Log_in;")
    
    if (username,) in cr__.fetchall(): return False
    cr.execute(f"insert into Log_in (id,username,password)values('{current_id+1}','{username}','{password}')")
    db.commit()
    db.close()
    return True
if __name__ == "__main__":   
    app=QApplication(sys.argv)
    win=LOGIN_Gui()
    win.show()
    app.exec_()

print('\n**************end***************')
