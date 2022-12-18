import sqlite3
def create_db():
    #ims se refiere a inventory management system, que en español sería sistema de gestión 
    #de inventario.
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    #en este caso, me veo obligado a fdn(fecha de nacimiento) sin puntos al igual que fdi(fecha de inscripción).
    cur.execute("CREATE TABLE IF NOT EXISTS empleado(eid INTEGER PRIMARY KEY AUTOINCREMENT,nombre text,email text,género text,contacto text,fdn text,fdi text,contra text,rol text,dirección text,salario text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS proveedor(invoice INTEGER PRIMARY KEY AUTOINCREMENT,nombre text,contacto text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS categoria(cid INTEGER PRIMARY KEY AUTOINCREMENT,nombre text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS producto(pid INTEGER PRIMARY KEY AUTOINCREMENT,proveedor text,categoria text,nombre text,precio text,cant text,estado text)")
    con.commit()

create_db()
