from tkinter import*
from PIL import Image,ImageTk #Es necesario instalar pip pillow.
class IMS:
    
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1")

        # ====Título====
        self.icon_title=PhotoImage(file="images/cart.png")  
        title=Label(self.root, text="Sistema de Gestión Supermark",image=self.icon_title,compound=LEFT, font=("Arial Rounded MT Bold",40,"bold"),bg="#014070",fg="black",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70) 

        # ====Botón de cierre de sesión====
        btn_logout=Button(self.root,text="Cerrar sesión",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1070,y=10,height=50,width=150)
        # ====Reloj====
        self.lbl_clock=Label(self.root, text="¡Bienvenido al sistema de gestión Supermark!\t\t Fecha: DD-MM-YYYY\t\t Tiempo: HH:MM:SS", font=("Arial Rounded MT Bold",15),bg="#4d636d",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)


root=Tk()
obj = IMS(root)
root.mainloop()

