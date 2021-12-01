import psycopg2
from tkinter.constants import CENTER
import os
from tkinter import  Button, Label, PhotoImage
from tkinter import messagebox
import tkinter
from Clases.ClsUsuarios import ClsUsuario

#**************************************************************************************
#************* FUNCIONES DE VALIDACION Y PARA SALIR DEL SISTEMA
#**************************************************************************************
def ValidarUsuario():
    if (TxtNombre.get()=="") or (TxtClave.get()==""):
        messagebox.showinfo(title="Error",message="Ingrese Valores")
    else:
        ObjUsuarios = ClsUsuario()
        if (ObjUsuarios.ValidarUsuario(TxtNombre.get(),TxtClave.get())==True):
            Ventana.destroy()
            os.system("VentanaPrincipal.py")
        else:
            messagebox.showinfo(title="Error",message="Los datos ingresados no son válidos, intente nuevamente")
            TxtNombre.delete(0,tkinter.END)
            TxtClave.delete(0,tkinter.END)
            TxtNombre.focus()

def Salir():
    Opcion = messagebox.askyesno(title="Salir",message="Esta seguro que desea salir?")
    if Opcion==True:
        Ventana.destroy()


#*************  CONFIGURACION DE LA VENTANA
#**************************************************************************************
Ventana = tkinter.Tk()
# Ancho y alto de la pantalla y de la ventana para poder centrar el formulario
AnchoScreen = Ventana.winfo_screenwidth()
AltoScreen = Ventana.winfo_screenheight()
Ventana.title("VENTANA DE ACCESO")
#Medidas y centrado de la ventana
posx = AnchoScreen // 2 - 320 // 2
posy = AltoScreen // 2 - 170 // 2
centro = "340x440"+"+"+str(posx)+"+"+str(posy)
Ventana.geometry(centro)
Ventana.iconbitmap('sb.ico')
fondo=PhotoImage(file="fondo.png")
LblFondo=Label(Ventana,image=fondo).place(x=0,y=0)

#******************* Controles de nombre y password de usuario
TxtNombre = tkinter.Entry(Ventana)
TxtClave =tkinter.Entry(Ventana,show="•")
ImgUsuario = PhotoImage(file = "../Imagenes/Usuario.png")
LblImagenUsuario = tkinter.Label(Ventana,image=ImgUsuario)
ImgClave = PhotoImage(file = "../Imagenes/candado.png")
LblImagenClave = tkinter.Label(Ventana,image=ImgClave)
ImgAcademia=PhotoImage(file="../Imagenes/academia.png")
LblImagenAcademia = Label(Ventana,image=ImgAcademia)
LblTxtNombre = tkinter.Label(Ventana,text="Usuario:",font="Arial 12")
LblTxtClave = tkinter.Label(Ventana,text="Contraseña:",font="Arial 12")
#****Botones***
ImgAceptar=PhotoImage(file="../Imagenes/confirmar.png")
BtnAceptar=Button(image=ImgAceptar,command=ValidarUsuario)
ImgSalir=PhotoImage(file="../Imagenes/exit.png")
BtnSalir=Button(image=ImgSalir,command=Salir)

#******************** Ubicar controles
LblImagenAcademia.place(x=110,y=10)
LblImagenUsuario.place(x=20,y=200)
LblImagenClave.place(x=20,y=270)
LblTxtNombre.place(x=70,y=208)
LblTxtClave.place(x=70,y=278)
TxtNombre.place(x=180,y=210)
TxtClave.place(x=180,y=280)
BtnSalir.place(x=190,y=330)
BtnAceptar.place(x=90,y=330)
Ventana.mainloop()
