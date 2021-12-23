from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
import sqlite3


font_list=["Times-Roman","Courier","Courier-Bold","Courier-BoldOblique","Courier-Oblique",
"Helvetica","Helvetica-Bold","Times-BoldItalic","Times-Bold","Helvetica-Oblique","Symbol"]

def prototype():
    #prototype
    file_="myPdf.pdf"
    can=Canvas(file_,pagesize=A4)
    posX,posY=2*cm,28*cm
    text="Bill"
    can.setFont(font_list[2],35)
    can.drawString(posX,posY,text.encode("utf-8"))
    #x line
    can.line(1*cm,27*cm,20*cm,27*cm)
    can.line(4*cm,24.5*cm,17*cm,24.5*cm)
    #y line
    can.line(8.33*cm,26*cm,8.33*cm,2.5*cm)
    can.line(12.33*cm,26*cm,12.33*cm,2.5*cm)

    can.setFont(font_list[2],30)
    can.drawString(12.33*cm,1*cm,"Total: ")
    can.setFont(font_list[2],20)


    can.drawString(4.40*cm,25*cm,"Name ")
    can.drawString(8.70*cm,25*cm,"Number")
    can.drawString(12.70*cm,25*cm,"Price")
    can.save()

class buy():
    def __init__(self):
        self.item_sold=[]
        self.number=[]
        #self.item_price=0
    def add_item(self,id,number=1):
        self.item_sold.append(id)
        self.number.append(number)
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        stock_in_dataBase=cr.execute(f"select stock from Item where id={id};").fetchone()[0]-number
        cr.execute(f"UPDATE Item SET stock={stock_in_dataBase} WHERE id={id};")
        db.commit()
        db.close()
    def calcul_the_price(self):
        result=0
        index=0
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        for i in self.item_sold:
            result=result+int(cr.execute(f"select price from Item where id={i}").fetchone()[0])*self.number[index]
            index=index+1

        return result
    def showDataOn_pdf(self):
            #prototype
        file_="myPdf.pdf"
        can=Canvas(file_,pagesize=A4)
        posX,posY=2*cm,28*cm
        text="Bill"
        can.setFont(font_list[2],35)
        can.drawString(posX,posY,text.encode("utf-8"))
        #x line
        can.line(1*cm,27*cm,20*cm,27*cm)
        can.line(4*cm,24.5*cm,17*cm,24.5*cm)
        #y line
        can.line(8.33*cm,26*cm,8.33*cm,2.5*cm)
        can.line(12.33*cm,26*cm,12.33*cm,2.5*cm)

        can.setFont(font_list[2],30)
        can.drawString(12.33*cm,0.5*cm,"Total: ")
        can.setFont(font_list[2],20)


        can.drawString(4.40*cm,25*cm,"Name ")
        can.drawString(8.70*cm,25*cm,"Number")
        can.drawString(12.70*cm,25*cm,"Price")
        can.setFont(font_list[2],15)
        for i in range(0,len(self.item_sold)):
            db=sqlite3.connect("pro.db")
            cr=db.cursor()
            name=cr.execute(f"select name from Item where id={self.item_sold[i]}").fetchone()
            price=cr.execute(f"select price from Item where id={self.item_sold[i]}").fetchone()
            #print(name[0])
            can.drawString(4.20*cm,(24-i/2)*cm,name[0])
            can.drawString(8.60*cm,(24-i/2)*cm,str(self.number[i]))
            can.drawString(12.60*cm,(24-i/2)*cm,str(price[0]))


        can.setFont(font_list[8],28)
        can.drawString(16.2*cm,0.5*cm,str(self.calcul_the_price())+" Da")


        can.save()


if __name__ == "__main__":
    obj=buy()
    obj.add_item(1,3)
    obj.add_item(2,2)
    
    obj.showDataOn_pdf()
    print(obj.calcul_the_price(),cm)

