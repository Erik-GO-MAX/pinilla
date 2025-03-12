import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class Loggin():
    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Ingrese el nombre de usuario y contraseña asignados\nEl campo nombre de usuario solo recibe letras, \nEl campo contraseña solo recibe numeros")
    
    def verCaracteres(self, event):
        if(self.bandera == False):
            self.txtpassword.config(show='')
            self.bandera = True
        else:
            self.txtpassword.config(show='*')
            self.bandera = False



    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("login")
        self.ventana.config(width=405, height=250)

        self.iconoIngresar = tk.PhotoImage(file=r"icons\door_in.png")#r es para que el programa sepa que no es una cadena de texto normal, si no una ruta
        self.icocoAyuda = tk.PhotoImage(file=r"icons\help.png")
        self.icocoVer = tk.PhotoImage(file=r"icons\eye.png")

        self.bandera = False

        self.lblTitulo = tk.Label(self.ventana, text="Inicio de Sesión")
        self.lblTitulo.place(width=150, height=25, y=30, relx=0.5, anchor="n")

        self.btnAyuda= tk.Button(self.ventana, image=self.icocoAyuda)
        self.btnAyuda.place(width=25, height=25, x=330, y=30)
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.place(width=70, height=25, x=50, y=85)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(width=150, height=25, x=150, y=85)
        #listener

        self.lblpassword = tk.Label(self.ventana, text="Contraseña*:" )
        self.lblpassword.place(width=70, height=25, x=50, y=140)

        self.txtpassword = tk.Entry(self.ventana, show="*")
        self.txtpassword.place(width=150, height=25, x=150, y=140)
        #listener
        

        self.btnVer = tk.Button(self.ventana, image=self.icocoVer)
        self.btnVer.place(width=25, height=25, x=330, y=140)
        #listener
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)
        
        

        self.btnIngresar = tk.Button(self.ventana, text= "Ingresar", image=self.iconoIngresar, compound=LEFT)
        self.btnIngresar.place(width=70, height=25, relx=0.5, y=195, anchor="n")
        #listener

        self.ventana.mainloop()

app = Loggin()