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
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(CustomerFrame,text="Datos del Cliente",font=("times new roman",15,"bold"),bg="lightgray").pack(side=TOP,fill=X)


if __name__=="__main__":
    root=Tk()
    obj = BillClass(root)
    root.mainloop()
