from tkinter import*
from PIL import Image,ImageTk #Es necesario instalar pip pillow.
from tkinter import ttk,messagebox
import sqlite3
import os # me permite 
class salesClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1")
        self.root.config(bg="white")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice=StringVar()

        #====== Título ========

        lbl_title=Label(self.root,text="Visualizador de facturas del cliente",font=("times new roman",30,"bold"),bg="#547ee8",fg="black",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
        
        lbl_invoice=Label(self.root,text="Factura Nro.",font=("times new roman",15,"bold"),bg="white").place(x=45,y=100)
        txt_invoice=Entry(self.root,text=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)
        
        #====== Botones ========

        btn_search=Button(self.root,text="Buscar",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="black",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Limpiar",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=490,y=100,width=120,height=28)

        #====== Lista de facturas ======
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=200,height=330)

        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_List=Listbox(sales_Frame,font=("times new roman",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH,expand=1)
        self.Sales_List.bind("<ButtonRelease-1>",self.get_data)

        #====== Área de facturación ======
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=410,height=330)

        lbl_title2=Label(bill_Frame,text="Área de facturación del cliente",font=("times new roman",15,"bold"),bg="orange").pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        #========== Imágenes =============
        self.bill_photo=Image.open("images/invoice.png")
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=700,y=140)

        self.show()
#============================================================

    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0,END)
        #print(os.listdir("../SISTEMA-SUPERMARK")) bill1.text, category.py
        for i in os.listdir("bill"):
            #print(i.split("."),i.split(".")[-1])
            if i.split(".")[-1]=="txt":
                self.Sales_List.insert(END,i)
                self.bill_list.append(i.split(".")[0])

    def get_data(self,ev):
        index_=self.Sales_List.curselection()
        file_name=self.Sales_List.get(index_)
        #print(file_name)
        self.bill_area.delete("1.0",END)
        fp=open(f"bill/{file_name}","r")
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","El nro. de factura es obligatorio",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f"bill/{self.var_invoice.get()}.txt","r")
                self.bill_area.delete("1.0",END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","El nro. de factura es incorrecto",parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete("1.0",END)

if __name__=="__main__":
    root=Tk()
    obj = salesClass(root)
    root.mainloop()
