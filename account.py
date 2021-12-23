import sqlite3

def check(password,id):
    db=sqlite3.connect("pro.db")
    cr=db.cursor()
    result=cr.execute(f"select password from Log_in where id={id};").fetchone()[0]
    if (result==password):
        return True
        db.close()
    else:
        return False
        db.close()
    db.close()
def edite_myPassword(newPassword,id):
    db=sqlite3.connect("pro.db")
    cr=db.cursor()
    cr.execute(f"UPDATE Log_in SET password='{newPassword}'WHERE id={id};")
    db.commit()
    db.close()
