from tkinter import*
from PIL import Image,ImageTk #Es necesario instalar pip pillow.
from tkinter import ttk
class employeeClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1")
        self.root.config(bg="white")
        self.root.focus_force()

        #==============================
        #== Todas las variables =======
        #==============================

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()

        #===== Cuadro de búsqueda =====
        SearchFrame=LabelFrame(self.root,text="Buscar Empleado",font=("times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #===== Opciones =====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Seleccionar","Email","Nombre","Contacto"),state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("times new roman",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Buscar",font=("times new roman",15,"bold"),bg="#84f578",fg="black",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #===== Title =====
        title = Label(self.root,text="Datos del empleado",font=("times new roman",15,"bold"),bg="#0f4d7d",fg="black").place(x=50,y=100,width=1000)

        #===== Contenido =====
        #===== Fila 1 ========
        lbl_empid = Label(self.root,text="Emp ID",font=("times new roman",15),bg="white").place(x=50,y=150)
        lbl_gender = Label(self.root,text="Género",font=("times new roman",15),bg="white").place(x=350,y=150)
        lbl_contact = Label(self.root,text="Contacto",font=("times new roman",15),bg="white").place(x=750,y=150)

        txt_empid = Entry(self.root,textvariable=self.var_emp_id,font=("times new roman",15),bg="lightyellow").place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Seleccionar","Hombre","Mujer","Otro"),state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=850,y=150,width=180)

        #===== Fila 2 ========

        lbl_name = Label(self.root,text="Nombre",font=("times new roman",15),bg="white").place(x=50,y=190)
        #D.O.B (date of birth) se refiere a la fecha de nacimiento. 
        lbl_dob = Label(self.root,text="F.D.N",font=("times new roman",15),bg="white").place(x=350,y=190)
        #D.O.J (date of joining) se refiere a la fecha de inscripción.
        lbl_doj = Label(self.root,text="F.D.I",font=("times new roman",15),bg="white").place(x=750,y=190)

        txt_name = Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob = Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_doj = Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),bg="lightyellow").place(x=850,y=190,width=180)


if __name__=="__main__":
    root=Tk()
    obj = employeeClass(root)
    root.mainloop()

