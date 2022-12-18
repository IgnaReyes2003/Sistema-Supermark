from tkinter import*
from PIL import Image,ImageTk #Es necesario instalar pip pillow.
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1")
        self.root.config(bg="white")
        self.root.focus_force()

        #======== Variables =============

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()

        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        #===== Columna 1 =====

        title=Label(product_Frame,text="Gestión de productos",font=("times new roman",18,"bold"),bg="#0f4d7d",fg="black").pack(side=TOP,fill=X)
        
        lbl_category=Label(product_Frame,text="Categoria",font=("times new roman",18,"bold"),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Proveedor",font=("times new roman",18,"bold"),bg="white").place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text="Nombre",font=("times new roman",18,"bold"),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Precio",font=("times new roman",18,"bold"),bg="white").place(x=30,y=210)
        lbl_qty=Label(product_Frame,text="Cantidad",font=("times new roman",18,"bold"),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Estado",font=("times new roman",18,"bold"),bg="white").place(x=30,y=310)

        #===== Columna 2 =====

        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("time new roman",15),bg="lightyellow").place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("time new roman",15),bg="lightyellow").place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("time new roman",15),bg="lightyellow").place(x=150,y=260,width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Disponible","Agotado"),state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)

        #===== Botones ========

        btn_add=Button(product_Frame,text="Guardar",command=self.add,font=("times new roman",15,"bold"),bg="#2196f3",fg="black",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Actualizar",command=self.update,font=("times new roman",15,"bold"),bg="#84f578",fg="black",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Eliminar",command=self.delete,font=("times new roman",15,"bold"),bg="#f44336",fg="black",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Limpiar",command=self.clear,font=("times new roman",15,"bold"),bg="#607d8b",fg="black",cursor="hand2").place(x=340,y=400,width=100,height=40)

        #===== Cuadro de búsqueda =====
        SearchFrame=LabelFrame(self.root,text="Buscar Producto",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #===== Opciones =====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Seleccionar","Categoria","Proveedor","Nombre"),state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("times new roman",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Buscar",command=self.search,font=("times new roman",15,"bold"),bg="#84f578",fg="black",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #===== Los detalles del producto ========

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("pid","proveedor","categoria","nombre","precio","cant","estado"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid",text="P ID")
        self.product_table.heading("proveedor",text="Proveedor")
        self.product_table.heading("categoria",text="Categoria")
        self.product_table.heading("nombre",text="Nombre")
        self.product_table.heading("precio",text="Precio")
        self.product_table.heading("cant",text="Cant.")
        self.product_table.heading("estado",text="Estado")
        
        self.product_table["show"]="headings"

        self.product_table.column("pid",width=90)
        self.product_table.column("categoria",width=100)
        self.product_table.column("proveedor",width=100)
        self.product_table.column("nombre",width=100)
        self.product_table.column("precio",width=100)
        self.product_table.column("cant",width=100)
        self.product_table.column("estado",width=100)

        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)


        self.show()

    #========== Funciones ========================================

    def fetch_cat_sup(self):
        self.cat_list.append("Vacío")
        self.sup_list.append("Vacío")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select nombre from categoria")
            cat=cur.fetchall()

            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Seleccionar")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select nombre from proveedor")
            sup=cur.fetchall()

            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Seleccionar")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)
    

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if  self.var_cat.get()=="Seleccionar" or self.var_cat.get()=="Vacío" or self.var_sup.get()=="Seleccionar" or self.var_name.get()=="":
                messagebox.showerror("Error","Todos los campos son obligatorios",parent=self.root)
            else:
                cur.execute("Select * from producto where nombre=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Este producto ya está registrado, pruebe con otro",parent=self.root)
                else:
                    cur.execute("Insert into producto (categoria,proveedor,nombre,precio,cant,estado) values(?,?,?,?,?,?)",(
                                                self.var_cat.get(),
                                                self.var_sup.get(),
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                                                ))
                    con.commit()
                    messagebox.showinfo("Éxito!","Producto añadido satisfactoriamente",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from producto")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[2])
        self.var_sup.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Por favor, seleccione un producto de la lista",parent=self.root)
            else:
                cur.execute("Select * from producto where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Producto no válido",parent=self.root)
                else:
                    cur.execute("Update producto set categoria=?,proveedor=?,nombre=?,precio=?,cant=?,estado=? where pid=?",(
                            self.var_cat.get(),
                                                self.var_sup.get(),
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                                                self.var_pid.get()
                                                ))
                    con.commit()
                    messagebox.showinfo("Éxito!","Producto actualizado correctamente",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Por favor, seleccione un producto de la lista",parent=self.root)
            else:
                cur.execute("Select * from producto where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Producto no válido",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirmar","Realmente lo quieres eliminar?",parent=self.root)
                    if op==True:
                        cur.execute("delete from producto where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Eliminar","Producto eliminado correctamente",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_cat.set("Seleccionar")
        self.var_sup.set("Seleccionar")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Disponible")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Seleccionar")
        self.show()
        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Seleccionar":
                messagebox.showerror("Error","Seleccione la opción de búsqueda",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Debe introducir los datos del producto que desea buscar",parent=self.root)
            
            else:
                cur.execute("select * from producto where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No se encontró ningún registro!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj = productClass(root)
    root.mainloop()
