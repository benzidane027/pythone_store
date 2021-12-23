import sqlite3
class item():
    def __init__(self):
        self.name=""
        self.price=None
        self.discripe=""
        self.stock=None
        self.type=None
        self.id=None
        
    def add_Item(self,name,discripe,price,type_,stock):
        self.name=name
        self.price=price
        self.discripe=discripe
        self.type=type_
        #self.id=id
        self.stock=stock
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        try:
            cr.execute(f"insert into Item(name,discripe,price,type_,stock)values('{name}','{discripe}',{price},'{type_}',{stock})")
        except:
            return 0
        db.commit()
        db.close()

    def modify_Item(self,id,name,discripe,price,type_,stock):
        self.name=name
        self.price=price
        self.discripe=discripe
        self.type=type_
        self.stock=stock
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        cr.execute(f"UPDATE Item SET name='{name}',discripe='{discripe}',price={price},type_='{type_}',stock={stock} WHERE id={id};")
        db.commit()
        db.close()

    def get_Item(self,id_):
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        result=list(cr.execute(f"select * from Item where id={id_};").fetchone())
        db.close()
        return result
    def delet_Item_byId(self,id_):
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        cr.execute(f"delete from Item where id={id_}")
        db.commit()
        db.close()
    def get_Id_byName(self,name):
        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        name_of_id=cr.execute(f"select id from Item where name='{name}'").fetchone()
        db.close()
        return name_of_id
    
    def get_id_Ofall_item(self):

        db=sqlite3.connect("pro.db")
        cr=db.cursor()
        list_of_id=cr.execute("select id from Item").fetchall()
        db.close()
        return list_of_id
if __name__ == "__main__":
    obj=item()
    obj.add_Item("sa3ida","sa3ida",120,"piece",350)
    #obj.modify_Item(3,"sabona","sabona maliha",70,"piece",100)
    print(obj.get_id_Ofall_item())
    #print(obj.get_id_Ofall_item())
