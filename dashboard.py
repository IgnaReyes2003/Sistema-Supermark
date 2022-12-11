from tkinter import*
class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Sistema de Gestión Supermark | Desarrollado por Ignacio Reyes CM1")

        # ====Título====  
        title=Label(self.root, text="Sistema de Gestión Supermark", font=("Nirmala UI",40,"bold")).place(x=0,y=0,relwidth=1,height=70) 

root=Tk()
obj = IMS(root)
root.mainloop()

