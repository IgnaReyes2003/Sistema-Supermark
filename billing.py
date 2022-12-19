from tkinter import*
from PIL import Image,ImageTk #Es necesario instalar pip pillow.
from tkinter import ttk,messagebox
class BillClass:
    
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

        # ==== Marco del Producto =====
        self.var_search=StringVar()

        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="Todos los productos",font=("times new roman",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        # ======== Marco de Detalles del Producto ===========
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Buscar Producto | Por Nombre",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Nombre del Producto",font=("times new roman",15,"bold"),bg="white").place(x=3,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=190,y=47,width=110,height=22)
        btn_search=Button(ProductFrame2,text="Buscar",font=("times new roman",15,"bold"),bg="#2196f3",fg="black",cursor="hand2").place(x=308,y=45,width=80,height=25)
        btn_show_all=Button(ProductFrame2,text="Mostrar todo",font=("times new roman",15,"bold"),bg="#4cd925",fg="black",cursor="hand2").place(x=265,y=10,width=120,height=25)

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

        self.product_Table.column("pid",width=90)
        self.product_Table.column("nombre",width=100)
        self.product_Table.column("precio",width=100)
        self.product_Table.column("cant",width=100)
        self.product_Table.column("status",width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        #self.product_Table.bind("<ButtonRelease-1>",self.get_data)

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
        cartTitle=Label(cart_Frame,text="Carrito Producto Total: [0]",font=("times new roman",15,"bold"),bg="lightgray").pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","nombre","precio","cant","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("nombre",text="Nombre")
        self.CartTable.heading("precio",text="Precio")
        self.CartTable.heading("cant",text="Cant.")
        self.CartTable.heading("status",text="Estado")
        
        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("nombre",width=100)
        self.CartTable.column("precio",width=90)
        self.CartTable.column("cant",width=50)
        self.CartTable.column("status",width=90)
        self.CartTable.pack(fill=BOTH,expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)

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

        lbl_precio=Label(Add_CartWidgetsFrame,text="Precio por cantidad",font=("times new roman",15),bg="white").place(x=220,y=5)
        txt_precio=Entry(Add_CartWidgetsFrame,textvariable=self.var_nombre,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=220,y=35,width=180,height=22)

        lbl_cant=Label(Add_CartWidgetsFrame,text="Cantidad",font=("times new roman",15),bg="white").place(x=420,y=5)
        txt_cant=Entry(Add_CartWidgetsFrame,textvariable=self.var_cant,font=("times new roman",15),bg="lightyellow").place(x=420,y=35,width=110,height=22)

        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="En Stock [9999]",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Limpiar",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=145,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Añadir | Actualizar Carrito",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=305,y=70,width=235,height=30)
        
        #========== Área de facturación ==========
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=978,y=110,width=382,height=410)
        #billFrame.place(x=978,y=110,width=410,height=410)

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
        

        self.lbl_net_pay=Label(billMenuFrame,text="Salario Net.\n[0]",font=("times new roman",15),relief=RIDGE,bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=220,y=5,width=160,height=70)
        
        btn_print=Button(billMenuFrame,text="Mostrar",cursor="hand2",font=("times new roman",15),relief=RIDGE,bg="lightgreen",fg="white")
        btn_print.place(x=2,y=80,width=110,height=50)

        btn_clear_all=Button(billMenuFrame,text="Limpiar Todo",cursor="hand2",font=("times new roman",14),relief=RIDGE,bg="gray",fg="white")
        btn_clear_all.place(x=110,y=80,width=110,height=50)

        btn_generate=Button(billMenuFrame,text="Generar/Guardar",cursor="hand2",font=("times new roman",15),relief=RIDGE,bg="#009688",fg="white")
        btn_generate.place(x=220,y=80,width=160,height=50)

        # ==== El pie de la página ====
        footer=Label(self.root,text="SGS-Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1\nPara cualquier cuestión técnica, póngase en contacto con: 387xxxxx51", font=("Arial Rounded MT Bold",12),bg="#4d636d",fg="black").pack(side=BOTTOM, fill=X)


#============= Todas las Funciones ===============

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set("")

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

if __name__=="__main__":
    root=Tk()
    obj = BillClass(root)
    root.mainloop()
