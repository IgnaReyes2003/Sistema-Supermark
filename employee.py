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
        self.var_salary=StringVar()


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
        #D.O.J (date of joining) se refiere a la fecha de inicio o unión.
        lbl_doj = Label(self.root,text="F.D.I",font=("times new roman",15),bg="white").place(x=750,y=190)

        txt_name = Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob = Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_doj = Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),bg="lightyellow").place(x=850,y=190,width=180)

        #===== Fila 3 ========
        lbl_email= Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=50,y=230)
        lbl_pass= Label(self.root,text="Contraseña",font=("times new roman",15),bg="white").place(x=350,y=230)
        lbl_utype= Label(self.root,text="Rol",font=("times new roman",15),bg="white").place(x=750,y=230)

        txt_email= Entry(self.root,textvariable=self.var_email,font=("times new roman",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_pass= Entry(self.root,textvariable=self.var_pass,font=("times new roman",15),bg="lightyellow").place(x=500,y=230,width=180)
        cmb_utype =ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Empleado"),state="readonly",justify=CENTER,font=("time new roman",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)
        
        #===== Fila 4 ========
        lbl_address= Label(self.root,text="Dirección",font=("times new roman",15),bg="white").place(x=50,y=270)
        lbl_salary= Label(self.root,text="Salario",font=("times new roman",15),bg="white").place(x=500,y=270)

        self.txt_address= Text(self.root,font=("times new roman",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary= Entry(self.root,textvariable=self.var_salary,font=("times new roman",15),bg="lightyellow").place(x=600,y=270,width=180)

        #===== Botones ========
        btn_add=Button(self.root,text="Guardar",font=("times new roman",15,"bold"),bg="#2196f3",fg="black",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Actualizar",font=("times new roman",15,"bold"),bg="#4caf50",fg="black",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Eliminar",font=("times new roman",15,"bold"),bg="#f44336",fg="black",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Limpiar",font=("times new roman",15,"bold"),bg="#607d8b",fg="black",cursor="hand2").place(x=860,y=305,width=110,height=28)

        #===== Detalles del empleado ========
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrolly=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","nombre","email","género","contacto","f.d.n","f.d.i","contra","rol","dirección","salario"))
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("nombre",text="Nombre")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("género",text="Género")
        self.EmployeeTable.heading("contacto",text="Contacto")
        self.EmployeeTable.heading("f.d.n",text="F.D.N")
        self.EmployeeTable.heading("f.d.i",text="F.D.I")
        self.EmployeeTable.heading("contra",text="Contraseña")
        self.EmployeeTable.heading("rol",text="Rol")
        self.EmployeeTable.heading("dirección",text="Dirección")
        self.EmployeeTable.heading("salario",text="Salario")
        self.EmployeeTable["show"]="headings"

        
        self.EmployeeTable.pack(fill=BOTH,expand=1)

        #
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("nombre",width=90)
        self.EmployeeTable.column("email",width=90)
        self.EmployeeTable.column("género",width=90)
        self.EmployeeTable.column("contacto",width=90)
        self.EmployeeTable.column("f.d.n",width=90)
        self.EmployeeTable.column("f.d.i",width=90)
        self.EmployeeTable.column("contra",width=90)
        self.EmployeeTable.column("rol",width=90)
        self.EmployeeTable.column("dirección",width=90)
        self.EmployeeTable.column("salario",width=90)
        
        
        

if __name__=="__main__":
    root=Tk()
    obj = employeeClass(root)
    root.mainloop()

