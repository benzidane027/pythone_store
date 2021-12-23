import os,sys,time,threading
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QStatusBar,QPushButton,QDialogButtonBox
from PyQt5.QtCore import QPropertyAnimation,QRect,QPoint




font_list=["Times-Roman","Courier","Courier-Bold","Courier-BoldOblique","Courier-Oblique",
"Helvetica","Helvetica-Bold","Times-BoldItalic","Times-Bold","Helvetica-Oblique","Symbol"]

print('biggen')
class gui(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,250,400,250)
        self.setWindowTitle("test")
        self.mainLable()
    def mainLable(self):
        self.lbl_1=QLabel("text 01",self)
        self.lbl_2=QLabel("text 02",self)
        self.lbl_2.move(0,40)
        self.lbl_3=QLabel("text 03",self)
        self.lbl_3.move(0,80)

        self.btn=QPushButton("click",self)
        self.btn.move(310,220)
        self.btn.clicked.connect(self.anim)
        
    def anim(self):
        lable=[self.lbl_1,self.lbl_2,self.lbl_3]
        _thread=[]
        for i in lable:
            t=threading.Thread(target=self.move,args=(i,))
            t.start()
            _thread.append(t)
    def move(self,xlable):
        self.an=QPropertyAnimation(xlable,b'geometry')
        self.an.setDuration(500)
        self.an.setEndValue(QRect(420,xlable.y(),xlable.width(),xlable.height()))
        self.an.start()


app=QApplication(sys.argv)
obj=gui()
obj.show()
app.exec_()



print("\nend")           




    

