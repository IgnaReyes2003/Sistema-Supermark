from tkinter import*
from PIL import Image,ImageTk #Es necesario instalar pip pillow.
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1")
        self.root.config(bg="white")

        # ==== Título ====
        self.icon_title=PhotoImage(file="images/cart.png")  
        title=Label(self.root, text="Sistema de Gestión Supermark",image=self.icon_title,compound=LEFT, font=("Arial Rounded MT Bold",40,"bold"),bg="#014070",fg="black",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70) 

        # ==== Botón de cierre de sesión ====

        btn_logout=Button(self.root,text="Cerrar sesión",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1070,y=10,height=50,width=150)
        
        # ==== Reloj ====
        self.lbl_clock=Label(self.root, text="¡Bienvenido al sistema de gestión Supermark!\t\t Fecha: DD-MM-YYYY\t\t Tiempo: HH:MM:SS", font=("Arial Rounded MT Bold",15),bg="#4d636d",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        # ==== Menú de la izquierda ==== 
        self.MenuLogo=Image.open("images/inventory.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/arrow.png") 
        lbl_menu=Label(LeftMenu,text="Menú",font=("calisto mt",20,"bold"),bg="#3a7d9c").pack(side=TOP,fill=X)

        #===== Botones ===============

        btn_employee=Button(LeftMenu,text="Empleado",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("calisto mt",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Proveedor",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("calisto mt",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Categoría",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("calisto mt",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Productos",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("calisto mt",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Ventas",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("calisto mt",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Salir",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("calisto mt",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #===== Contenido ==============
        #\n
        self.lbl_employee=Label(self.root,text="Empleados Total\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Proveedores Total\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Categorías Total\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Productos Total\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Ventas Total\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        # ==== El pie de la página ====
        lbl_footer=Label(self.root, text="SGS-Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1\nPara cualquier cuestión técnica, póngase en contacto con: 387xxxxx51", font=("Arial Rounded MT Bold",12),bg="#4d636d",fg="black").pack(side=BOTTOM, fill=X)
        self.update_content()

#==========================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from producto")
            producto=cur.fetchall()
            self.lbl_product.config(text=f"Productos Total\n[ {str(len(producto))} ]")

            cur.execute("select * from proveedor")
            proveedor=cur.fetchall()
            self.lbl_supplier.config(text=f"Proveedores Total\n[ {str(len(proveedor))} ]")

            cur.execute("select * from categoria")
            categoria=cur.fetchall()
            self.lbl_category.config(text=f"Categorías Total\n[ {str(len(categoria))} ]")

            cur.execute("select * from empleado")
            empleado=cur.fetchall()
            self.lbl_employee.config(text=f"Empleados Total\n[ {str(len(empleado))} ]")

            bill=len(os.listdir("bill"))
            self.lbl_sales.config(text=f"Ventas Total [ {str(bill)} ]")

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"¡Bienvenido al sistema de gestión Supermark!\t\t Fecha: {str(date_)}\t\t Tiempo: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj = IMS(root)
    root.mainloop()
