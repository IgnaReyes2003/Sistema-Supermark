from tkinter import*
from PIL import Image,ImageTk #Es necesario instalar pip pillow.
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile
class BillClass:
    
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0

        # ==== Título ====
        self.icon_title=PhotoImage(file="images/cart.png")  
        title=Label(self.root, text="Sistema de Gestión Supermark",image=self.icon_title,compound=LEFT, font=("Arial Rounded MT Bold",40,"bold"),bg="#014070",fg="black",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70) 

        # ==== Botón de cierre de sesión ====

        btn_logout=Button(self.root,text="Cerrar sesión",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1070,y=10,height=50,width=150)
        
        # ==== Reloj ====
        self.lbl_clock=Label(self.root, text="¡Bienvenido al sistema de gestión Supermark!\t\t Fecha: DD-MM-YYYY\t\t Tiempo: HH:MM:SS", font=("Arial Rounded MT Bold",15),bg="#4d636d",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        # ==== Marco del Producto =====
        
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="Todos los productos",font=("times new roman",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        # ======== Marco de Búsqueda del Producto ===========
        self.var_search=StringVar()
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Buscar Producto | Por Nombre",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Nombre del Producto",font=("times new roman",15,"bold"),bg="white").place(x=3,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=190,y=47,width=110,height=22)
        btn_search=Button(ProductFrame2,text="Buscar",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="black",cursor="hand2").place(x=308,y=45,width=80,height=25)
        btn_show_all=Button(ProductFrame2,text="Mostrar todo",command=self.show,font=("times new roman",15,"bold"),bg="#4cd925",fg="black",cursor="hand2").place(x=265,y=10,width=120,height=25)

        #==========================================

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","nombre","precio","cant","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("nombre",text="Nombre")
        self.product_Table.heading("precio",text="Precio")
        self.product_Table.heading("cant",text="Cant.")
        self.product_Table.heading("status",text="Estado")
        
        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=40)
        self.product_Table.column("nombre",width=100)
        self.product_Table.column("precio",width=100)
        self.product_Table.column("cant",width=40)
        self.product_Table.column("status",width=90)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(ProductFrame1,text="Nota:'Introduzca 0 cantidad para eliminar el producto del carrito'",font=("times new roman",11),anchor="w",bg="white",fg="red").pack(side=BOTTOM,fill=X)

        # =================== Marco del cliente ===================
        self.var_name=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=555,height=70)

        cTitle=Label(CustomerFrame,text="Datos del Cliente",font=("times new roman",15,"bold"),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Nombre",font=("times new roman",15,"bold"),bg="white").place(x=5,y=34)
        txt_name=Entry(CustomerFrame,textvariable=self.var_name,font=("times new roman",13,"bold"),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(CustomerFrame,text="Contacto Nro.",font=("times new roman",15,"bold"),bg="white").place(x=270,y=34)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13,"bold"),bg="lightyellow").place(x=400,y=35,width=140)

        #=============== Marco de Cal Cart =================

        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=555,height=360)

        #============ Marco de la Calculadora ==============

        self.var_cal_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text="7",font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text="8",font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text="9",font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text="+",font=("arial",15,"bold"),command=lambda:self.get_input("+"),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text="4",font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text="5",font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text="6",font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text="-",font=("arial",15,"bold"),command=lambda:self.get_input("-"),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)

        btn_1=Button(Cal_Frame,text="1",font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text="2",font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text="3",font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text="*",font=("arial",15,"bold"),command=lambda:self.get_input("*"),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(Cal_Frame,text="0",font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        #=====c es para limpiar=====
        btn_c=Button(Cal_Frame,text="c",font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text="/",font=("arial",15,"bold"),command=lambda:self.get_input("/"),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)

        #=============== Marco del Carrito =================

        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=290,y=8,width=245,height=342)

        #=================== Carrito =======================
        self.cartTitle=Label(cart_Frame,text="Carrito Producto Total: [0]",font=("times new roman",15,"bold"),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","nombre","precio","cant"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("nombre",text="Nombre")
        self.CartTable.heading("precio",text="Precio")
        self.CartTable.heading("cant",text="Cant.")
        
        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("nombre",width=90)
        self.CartTable.column("precio",width=90)
        self.CartTable.column("cant",width=40)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)

        #============ Marco de los widgets Carrito ===============
        self.var_pid=StringVar()
        self.var_nombre=StringVar()
        self.var_precio=StringVar()
        self.var_cant=StringVar()
        self.var_stock=StringVar()

        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=555,height=110)
        
        lbl_p_name=Label(Add_CartWidgetsFrame,text="Nombre del Producto",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_nombre,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)

        lbl_precio=Label(Add_CartWidgetsFrame,text="Precio por unidad",font=("times new roman",15),bg="white").place(x=220,y=5)
        txt_precio=Entry(Add_CartWidgetsFrame,textvariable=self.var_precio,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=220,y=35,width=180,height=22)

        lbl_cant=Label(Add_CartWidgetsFrame,text="Cantidad",font=("times new roman",15),bg="white").place(x=420,y=5)
        txt_cant=Entry(Add_CartWidgetsFrame,textvariable=self.var_cant,font=("times new roman",15),bg="lightyellow").place(x=420,y=35,width=110,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="En Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Limpiar",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=145,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Añadir | Actualizar Carrito",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=305,y=70,width=235,height=30)
        
        #========== Área de facturación ==========
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=978,y=110,width=382,height=410)

        BTitle=Label(billFrame,text="Área de facturación del cliente",font=("times new roman",15),bg="red",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #========== Botones de facturación ==========
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=978,y=520,width=382,height=140)

        self.lbl_amnt=Label(billMenuFrame,text="Imp. Factura \n[0]",font=("times new roman",15),relief=RIDGE,bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=110,height=70)

        self.lbl_discount=Label(billMenuFrame,text="Descuento \n[5%]",font=("times new roman",15),relief=RIDGE,bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=110,y=5,width=110,height=70)
        

        self.lbl_net_pay=Label(billMenuFrame,text="Total a Pagar\n[0]",font=("times new roman",15),relief=RIDGE,bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=220,y=5,width=160,height=70)
        
        btn_print=Button(billMenuFrame,text="Imprimir",command=self.print_bill,cursor="hand2",font=("times new roman",15),bg="lightgreen",fg="white")
        btn_print.place(x=1,y=80,width=109,height=50)

        btn_clear_all=Button(billMenuFrame,text="Limpiar Todo",command=self.clear_all,cursor="hand2",font=("times new roman",14),bg="gray",fg="white")
        btn_clear_all.place(x=110,y=80,width=110,height=50)

        btn_generate=Button(billMenuFrame,text="Generar/Guardar",command=self.generate_bill,cursor="hand2",font=("times new roman",15),bg="#009688",fg="white")
        btn_generate.place(x=220,y=80,width=160,height=50)

        # ==== El pie de la página ====
        footer=Label(self.root,text="SGS-Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1\nPara cualquier cuestión técnica, póngase en contacto con: 387xxxxx51", font=("Arial Rounded MT Bold",12),bg="#4d636d",fg="black").pack(side=BOTTOM, fill=X)

        self.show()
        #self.bill_top()
        self.update_date_time()

#============= Todas las Funciones ===============

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set("")

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select pid,nombre,precio,cant,estado from producto where estado='Disponible'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Debe introducir los datos del producto que desea buscar",parent=self.root)
            
            else:
                cur.execute("select pid,nombre,precio,cant,estado from producto where nombre LIKE '%"+self.var_search.get()+"%' and estado='Disponible'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No se encontró ningún registro!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        #si da error probar var_name
        self.var_pid.set(row[0])
        self.var_nombre.set(row[1])
        self.var_precio.set(row[2])
        self.lbl_inStock.config(text=f"En Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_cant.set("1")

    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        #pid 0,nombre 1,precio 2,cant 3,estado 4
        self.var_pid.set(row[0])
        self.var_nombre.set(row[1])
        self.var_precio.set(row[2])
        self.var_cant.set(row[3])
        self.lbl_inStock.config(text=f"En Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        


    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Por favor, seleccione un producto de la lista",parent=self.root)
        elif self.var_cant.get()=="":
            messagebox.showerror("Error","Se requiere una cantidad",parent=self.root)
        elif int(self.var_cant.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Cantidad inválida",parent=self.root)
        else:
            #price_cal=float(int(self.var_cant.get())*float(self.var_precio.get()))
            #price_cal=float(price_cal)
            price_cal=self.var_precio.get()
            cart_data=[self.var_pid.get(),self.var_nombre.get(),price_cal,self.var_cant.get(),self.var_stock.get()]

    # ===== Actualizar carrito =======
            present="no"
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:

                    present="yes"
                    break
                index_+=1

            if present=="yes":
                op=messagebox.askyesno("Confirmar","Producto ya presente\n¿Desea Actualizarlo| Removerlo del carrito?",parent=self.root)
                if op==True:
                    if self.var_cant.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #pid 0,nombre 1,precio 2,cant 3,estado 4
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_cant.get()

            else:
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            #pid 0,nombre 1,precio 2,cant 3,stock

            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amnt.config(text=f"Imp. Factura\n{str(self.bill_amnt)}")
        self.lbl_net_pay.config(text=f"Total a Pagar\n{str(self.net_pay)}")
        self.cartTitle.config(text=f"Carrito Producto Total: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def generate_bill(self):
        if self.var_name.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error",f"Se necesitan los datos del cliente",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Por favor, añada uno o más productos al carrito!!!",parent=self.root)
        elif len(self.cart_list)>=31:
            messagebox.showerror("Error",f"El límite es 30, remueva uno o más productos de su carrito!!!",parent=self.root)
        else:
            #====Factura Parte Superior =====
            self.bill_top()
            #====Factura Zona del Medio ====
            self.bill_middle()
            #==== Factura Al Fondo ====
            self.bill_bottom()

            fp=open(f"bill/{str(self.invoice)}.txt","w")
            fp.write(self.txt_bill_area.get("1.0",END))
            fp.close()
            messagebox.showinfo("Aviso","La factura ha sido generada/guardada en el sistema",parent=self.root)
            self.chk_print=1


    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tSGS-Inventario
\tNro. Móvil 38754***** ,Ignacio-02751
{str("="*44)}
 Nombre del cliente: {self.var_name.get()}
 Cel. Nro. :{self.var_contact.get()}
 Factura Nro. {str(self.invoice)}\t\t\tFecha: {str(time.strftime("%d/%m/%Y"))}
{str("="*44)}
 N. Producto\t\t\tCant\tPrecio
{str("="*44)}
        '''
        self.txt_bill_area.delete("1.0",END)
        self.txt_bill_area.insert("1.0",bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*44)}
 Imp. Factura\t\t\t\tArs.{self.bill_amnt}
 Descuento\t\t\t\tArs.{self.discount}
 Total a pagar:\t\t\tArs.{self.net_pay}
{str("="*44)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)

    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                nombre=row[1]
                cant=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    estado="Agotado"
                if int(row[3])!=int(row[4]):
                    estado="Disponible"

                precio=float(row[2])*int(row[3])
                precio=str(precio)
                self.txt_bill_area.insert(END,"\n "+nombre+"\t\t\t"+row[3]+"\tArs."+precio)
                #====== Actualizar cantidad de productos en la tabla ======
                cur.execute("Update producto set cant=?,estado=? where pid=?",(
                    cant,
                    estado,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def clear_cart(self):
        self.var_pid.set("")
        self.var_nombre.set("")
        self.var_precio.set("")
        self.var_cant.set("")
        self.lbl_inStock.config(text=f"En Stock")
        self.var_stock.set("")
        
    def clear_all(self):
        self.chk_print=0
        del self.cart_list[:]
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_bill_area.delete("1.0",END)
        self.cartTitle.config(text=f"Carrito Producto Total: [0]")
        self.var_search.set("")
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"¡Bienvenido al sistema de gestión Supermark!\t\t Fecha: {str(date_)}\t\t Tiempo: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Mensaje","Por favor, espere mientras se imprime",parent=self.root)
            new_file=tempfile.mktemp(".txt")
            open(new_file,"w").write(self.txt_bill_area.get("1.0",END))
            os.startfile(new_file,"print")
        else:
            messagebox.showerror("Error","Por favor, realice la factura y luego podrá imprimirla",parent=self.root)
            

if __name__=="__main__":
    root=Tk()
    obj = BillClass(root)
    root.mainloop()
