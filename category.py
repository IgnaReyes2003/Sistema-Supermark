from tkinter import*
from PIL import Image,ImageTk #Es necesario instalar pip pillow.
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1")
        self.root.config(bg="white")
        self.root.focus_force()

        #====== Variables =====

        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #====== Título ========

        lbl_title=Label(self.root,text="Categoría de productos",font=("times new roman",30,"bold"),bg="#547ee8",fg="black",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
        lbl_name=Label(self.root,text="Introducir nombre de la categoría",font=("times new roman",30),bg="white").place(x=46,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",18),bg="lightyellow").place(x=50,y=160,width=300)

        #====== Botones =======

        btn_add=Button(self.root,text="Añadir",command=self.add,font=("times new roman",15),bg="#4caf50",fg="black",cursor="hand2").place(x=360,y=160,width=80,height=32)
        btn_delete=Button(self.root,text="Eliminar",command=self.delete,font=("times new roman",15),bg="#e30e31",fg="black",cursor="hand2").place(x=450,y=160,width=80,height=32)


        #===== Detalles categoría ========

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.category_table=ttk.Treeview(cat_frame,columns=("cid","nombre"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.heading("cid",text="Ctg ID")
        self.category_table.heading("nombre",text="Nombre")
        
        self.category_table["show"]="headings"

        self.category_table.column("cid",width=90)
        self.category_table.column("nombre",width=100)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        #===== Imágenes ========

        self.im1=Image.open("images/category1.png")
        self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open("images/category.png")
        self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)

        self.show()

#======= Funciones =======

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","El nombre de la categoría es obligatorio",parent=self.root)
            else:
                cur.execute("Select * from categoria where nombre=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Categoría ya presente, pruebe con otra",parent=self.root)
                else:
                    cur.execute("Insert into categoria (nombre) values(?)",(
                                                self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Éxito!","Categoría añadida correctamente",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from categoria")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        #print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Por favor, selecciona la categoría que deseas eliminar",parent=self.root)
            else:
                cur.execute("Select * from categoria where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, por favor inténtelo de nuevo",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirmar","Quieres eliminarlo?",parent=self.root)
                    if op==True:
                        cur.execute("delete from categoria where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Categoría eliminada correctamente",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj = categoryClass(root)
    root.mainloop()

