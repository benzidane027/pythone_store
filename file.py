import sqlite3
import sys
class files():
    def import_file_of_product(self,file_path=r"data.txt"):
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        
        try:
            #c_idinDB=current id in data base
            c_idinDB=cr.execute("SELECT id FROM Item ORDER BY Id DESC LIMIT 1;").fetchone()[0]
        except:
            c_idinDB=0
            
        file_=open(file_path,"r")
        for i in file_.readlines():
            try:
                c_idinDB+=1
                dataline=i.replace("\\n","")
                dataline=list(dataline.split(","))
                dataline[2],dataline[4]=int(dataline[2]),int(dataline[4])
                cr.execute(f"insert into Item(id,name,discripe,price,type_,stock)values({c_idinDB},'{dataline[0]}','{dataline[1]}',{dataline[2]},'{dataline[3]}',{dataline[4]})")

            except:
                return "the file shoud contien line as: name,discripe,price,type_,stock"
           # print(dataline,c_idinDB)
        db.commit()
        db.close()


    def export_file_of_product(self,file_name="myProduct.txt",file_path=r"C:\Users\myPC\Desktop"):
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        data=cr.execute("select * from Item;").fetchall()
        file_=open(file_name,"w")
        for i in data:
            dataline=i[1:6]
            dataline=','.join([str(elem) for elem in dataline])
            file_.writelines(dataline+"\n")
            
    def exit_(self):
        sys.exit()
if __name__ == "__main__":
    obj=files()
    #obj.export_file_of_product()
    obj.import_file_of_product()
