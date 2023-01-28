from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Inicio de Sesión | Desarrollado por Ignacio Reyes CM1")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.otp=""

        #====== Imágenes ======
        self.phone_image=ImageTk.PhotoImage(file="images/phone1.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        #====== Marco de Inicio de Sesión =====
        self.employee_id=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Inicio de Sesión",font=("Bell MT",34,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        lbl_user=Label(login_frame,text="Empleado ID",font=("Andalus",15),bg="white",fg="#767171").place(x=46,y=100)

        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Contraseña",font=("Andalus",15),bg="white",fg="#767171").place(x=46,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show=".",font=("times new roman",15,"bold"),bg="#ECECEC").place(x=50,y=240,width=250)

        #==== Botón de login =====
        btn_login=Button(login_frame,command=self.login,text="Conectarse",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="O",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=160,y=355)
        
        btn_forget=Button(login_frame,text="Olvidaste tu contraseña?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#2438d4",bd=0,activebackground="white",activeforeground="#2438d4",cursor="hand2").place(x=85,y=390)
        
        #==== Marco 2 ======
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Ignacio Reyes | CM1 | 1000 Programadores",font=("times new roman",11,"bold"),bg="white").place(x=25,y=20)
        #lbl_reg=Label(register_frame,text="¿No tienes una cuenta?",font=("times new roman",13),bg="white").place(x=45,y=20)
        #btn_signup=Button(register_frame,text="Regístrate",font=("times new roman",13,"bold"),bg="white",fg="#72b5b8",bd=0,activebackground="white",activeforeground="#72b5b8",cursor="hand2").place(x=205,y=18)
        
        #===== Imágenes =====
        self.im4=ImageTk.PhotoImage(file="images/animacion4.png")
        self.im3=ImageTk.PhotoImage(file="images/animacion3.png")
        self.im2=ImageTk.PhotoImage(file="images/animacion2.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=337,y=145,width=241,height=430)

        self.animate()
        #self.send_email("xyz")

#=================== Todas las funciones ==================

    def animate(self):
        self.im=self.im2
        self.im2=self.im3
        self.im3=self.im4
        self.im4=self.im
        self.lbl_change_image.config(image=self.im)
        #milisec
        self.lbl_change_image.after(2000,self.animate)

    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","Todos los campos son obligatorios",parent=self.root)
            else:
                cur.execute("select rol from empleado where eid=? AND contra=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Nombre de usuario o contraseña no válidos",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:    
            if self.employee_id.get()=="":
                messagebox.showerror("Error","La ID del empleado es necesaria",parent=self.root)
            else:
                cur.execute("select email from empleado where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","La ID del empleado es inválida, inténtelo de nuevo",parent=self.root)
                else:
                    #========= Ventana Olvidar contraseña =============
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    #call send_email_function()
                    chk=self.send_email(email[0])
                    if chk=="f":
                        messagebox.showerror("Error","Conexión no establecida, inténtalo de nuevo",parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("Restablecer contraseña")
                        self.forget_win.geometry("400x350+500+100")
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text="Restablecer contraseña",font=("times new roman",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="Ingresar la clave enviada a su email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                        self.btn_reset=Button(self.forget_win,text="Enviar",command=self.validate_otp,font=("times new roman",15),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)

                        lbl_new_pass=Label(self.forget_win,text="Nueva contraseña",font=("times new roman",15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                    
                        lbl_c_pass=Label(self.forget_win,text="Confirmar contraseña",font=("times new roman",15)).place(x=20,y=225)
                        txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)
                    
                        self.btn_update=Button(self.forget_win,text="Actualizar",state=DISABLED,font=("times new roman",15),bg="lightblue")
                        self.btn_update.place(x=150,y=300,width=100,height=30)

        except Exception as ex:
            messagebox.showerror("Error",f"Error causador por: {str(ex)}",parent=self.root)

    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass:

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Clave incorrecta, inténtalo de nuevo",parent=self.forget_win)

    def send_email(self,to_):
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        
        subj="SGS-Reestablecer contraseña"
        msg=f"Dear Sir/Madamm,\n\ntu contraseña {str(self.otp)}.\n\n with regards,\nSGS Team"
        msg="Subject:{}\n\n{}".format(subj,msg)
        
        s.sendmail(email_,to_,msg.encode("utf8"))
        chk=s.ehlo()

        if chk[0]==250:
            return "s"
        else:
            return "f"

root=Tk()
obj=Login_System(root)
root.mainloop()