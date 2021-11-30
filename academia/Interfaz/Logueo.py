import psycopg2
import os
from tkinter import  PhotoImage
from tkinter import messagebox
import tkinter
from Clases.ClsUsuarios import ClsUsuario

#**************************************************************************************
#************* FUNCIONES DE VALIDACION Y PARA SALIR DEL SISTEMA
#**************************************************************************************
def ValidarUsuario():
    if (TxtNombre.get()=="") or (TxtClave.get()==""):
        messagebox.showinfo(title="Mensaje",message="Debe ingresar valores")
    else:
        ObjUsuarios = ClsUsuario()
        if (ObjUsuarios.ValidarUsuario(TxtNombre.get(),TxtClave.get())==True):
            Ventana.destroy()
            os.system("VentanaPrincipal.py")
        else:
            messagebox.showinfo(title="Mensaje",message="Los datos no son válidos, intente de nuevo")
            TxtNombre.delete(0,tkinter.END)
            TxtClave.delete(0,tkinter.END)
            TxtNombre.focus()

def Salir():
    Opcion = messagebox.askyesno(title="Confirmar",message="Esta seguro de salir?")
    if Opcion==True:
        Ventana.destroy()

#**************************************************************************************
#*************  CONFIGURACION DE LA VENTANA
#**************************************************************************************
Ventana = tkinter.Tk()
# Ancho y alto de la pantalla y de la ventana para poder centrar el formulario
AnchoScreen = Ventana.winfo_screenwidth()
AltoScreen = Ventana.winfo_screenheight()
Ventana.title("Ventana de acceso")
#Medidas y centrado de la ventana
posx = AnchoScreen // 2 - 320 // 2
posy = AltoScreen // 2 - 170 // 2
centro = "320x170"+"+"+str(posx)+"+"+str(posy)
Ventana.geometry(centro)
#******************* Controles de nombre y password de usuario
TxtNombre = tkinter.Entry(Ventana)
TxtClave =tkinter.Entry(Ventana,show="*")
ImgUsuario = PhotoImage(file = "../Imagenes/Usuario.png")
LblImagenUsuario = tkinter.Label(Ventana,image=ImgUsuario)
ImgClave = PhotoImage(file = "../Imagenes/password.png")
LblImagenClave = tkinter.Label(Ventana,image=ImgClave)
LblTxtNombre = tkinter.Label(Ventana,text="Nombre:",font="Arial 12")
LblTxtClave = tkinter.Label(Ventana,text="Password:",font="Arial 12")
BtnAceptar = tkinter.Button(Ventana,text="Aceptar",font="Arial 12",command=ValidarUsuario)
BtnSalir = tkinter.Button(Ventana,text="Salir",font="Arial 12",command=Salir)
#******************** Ubicar controles
LblImagenUsuario.grid(row=0,column=0,padx=10,pady=10, sticky="w")
LblImagenClave.grid(row=1,column=0,padx=10,pady=10, sticky="w")
LblTxtNombre.grid(row=0,column=1,padx=10,pady=10, sticky="w")
LblTxtClave.grid(row=1,column=1,padx=10,pady=10, sticky="w")
TxtNombre.grid(row=0,column=2,padx=10,pady=10, sticky="w",columnspan=2)
TxtClave.grid(row=1,column=2,padx=10,pady=10,sticky="w",columnspan=2)
BtnAceptar.grid(row=2,column=2,padx=10,pady=10)
BtnSalir.grid(row=2,column=3,padx=10,pady=10)
Ventana.mainloop()
