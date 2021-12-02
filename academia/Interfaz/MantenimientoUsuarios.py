from tkinter import Button, Label, PhotoImage
import tkinter
from tkinter import messagebox
from Clases.ClsUsuarios import ClsUsuario

def registrar_usuario():
    #messagebox.showinfo(title="Prueba", message="Accediendo a la función")
    datosUsuarios= {"DniUsuario":TxtDniUsuario.get(),"APaUsuario":TxtApePaUsuario.get(),"AMaUsuario":TxtApeMaUsuario.get(),"NomUsuario":TxtNomUsuario.get(),"ClaAcceso": TxtClaAcceso.get(),"NomAcceso":TxtNomAcceso.get()}
    objusuario=ClsUsuario()
    if objusuario.registrarUsuario(datosUsuarios)==True:
        messagebox.showinfo(title="Registro usuario", message="Se registró el usuario con éxito")
    else:
        messagebox.showinfo(title="Registro usuario", message="No se ha podido registrar al usuario")

def eliminar_usuario():
    objusuario = ClsUsuario()
    if objusuario.borrarUsuario(TxtDniUsuario.get()) == True:
        messagebox.showinfo(title="Eliminar usuario", message="Se eliminó el usuario con éxito")
        TxtDniUsuario.delete(" ")
        TxtNomUsuario.delete(0, "end")
        TxtApePaUsuario.delete(0, "end")
        TxtApeMaUsuario.delete(0, "end")
        TxtNomAcceso.delete(0, "end")
        TxtClaAcceso.delete(0, "end")
    else:
        messagebox.showinfo(title="Borrar usuario", message="No se ha podido borrar al usuario")

'''def limpiar_usuario():
    #TxtUsuario = ClsUsuario()
    OpcionBorrar = messagebox.askyesno(title="Borrar", message="¿Esta seguro que desea Borrar los campos?")
    if OpcionBorrar == True:
        TxtDniUsuario==print()
        TxtNomUsuario.insert(" ")
        TxtApePaUsuario.insert(" ")
        TxtApeMaUsuario.insert(" ")
        TxtNomAcceso.insert(" ")
        TxtClaAcceso.insert(" ")'''

def Salir():
    Opcion = messagebox.askyesno(title="Salir", message="Esta seguro que desea salir?")
    if Opcion == True:
        VentanaUsuarios.destroy()

    #******************VENTANA PRINCIPAL DEL MANTENIMIENTO DE USUARIOS ************
VentanaUsuarios = tkinter.Tk()
VentanaUsuarios.title("Mantenimiento de Usuarios")
AnchoScreen = VentanaUsuarios.winfo_screenwidth()
AltoScreen = VentanaUsuarios.winfo_screenheight()
#Medidas y centrado de la ventana
posx = AnchoScreen // 2 - 370 // 2
posy = AltoScreen // 2 - 300 // 2
centro = "520x520"+"+"+str(posx)+"+"+str(posy)
VentanaUsuarios.geometry(centro)
VentanaUsuarios.iconbitmap("sb.ico")
fondo=PhotoImage(file="../Imagenes/fondo.png")
LblFondo=Label(VentanaUsuarios,image=fondo).place(x=0,y=0)

#****************** CONTROLES DE LA VENTANA ***********************************************
LblDniUsuario = tkinter.Label(VentanaUsuarios,text="Dni del usuario:")
LblNomUsuario = tkinter.Label(VentanaUsuarios,text="Nombres del usuario:")
LblApePaUsuario =  tkinter.Label(VentanaUsuarios,text="Apellido Paterno del usuario:")
LblApeMaUsuario =  tkinter.Label(VentanaUsuarios,text="Apellido Materno del usuario:")
LblClaAcceso = tkinter.Label(VentanaUsuarios,text="Clave de acceso:")
LblNomAcceso = tkinter.Label(VentanaUsuarios,text="Nombre de acceso:")
TxtDniUsuario = tkinter.Entry(VentanaUsuarios)
TxtNomUsuario = tkinter.Entry(VentanaUsuarios)
TxtApePaUsuario = tkinter.Entry(VentanaUsuarios)
TxtApeMaUsuario = tkinter.Entry(VentanaUsuarios)
TxtNomAcceso = tkinter.Entry(VentanaUsuarios)
TxtClaAcceso = tkinter.Entry(VentanaUsuarios)
ImgNuevo = PhotoImage(file = "../Imagenes/Nuevo.png")
BtnNuevo = tkinter.Button(VentanaUsuarios,image=ImgNuevo)
ImgGuardar = PhotoImage(file = "../Imagenes/Guardar.png")
BtnGuardar = tkinter.Button(VentanaUsuarios,image=ImgGuardar,command=registrar_usuario)
ImgModificar = PhotoImage(file = "../Imagenes/Modificar.png")
BtnModificar = tkinter.Button(VentanaUsuarios,image=ImgModificar)
ImgBorrar = PhotoImage(file = "../Imagenes/Borrar.png")
BtnBorrar = tkinter.Button(VentanaUsuarios,image=ImgBorrar,command=eliminar_usuario)
ImgCancelar = PhotoImage(file = "../Imagenes/Cancelar.png")
BtnCancelar = tkinter.Button(VentanaUsuarios,image=ImgCancelar, command=limpiar_usuario)
ImgSalir = PhotoImage(file = "../Imagenes/exit.png")
BtnSalir = tkinter.Button(VentanaUsuarios,image=ImgSalir,command=Salir)


#*******Imagenes/texto academia****
ImgLogo = PhotoImage(file = "../Imagenes/logosb.png")
LblImgLogo = Label(VentanaUsuarios,image=ImgLogo)
ImgLogo2 = PhotoImage(file = "../Imagenes/logosb.png")
LblImgLogo2 = Label(VentanaUsuarios,image=ImgLogo2)
ImgTxtAcademia = PhotoImage(file = "../Imagenes/textoa.png")
LblTxtAcademia = Label(VentanaUsuarios,image=ImgTxtAcademia)

#***************************** POSICIONANDO LOS CONTROLES EN EL GRID **********************
LblDniUsuario.place(x=120,y=110)
LblNomUsuario.place(x=120,y=170)
LblApePaUsuario.place(x=120,y=230)
LblApeMaUsuario.place(x=120,y=290)
LblNomAcceso.place(x=120,y=350)
LblClaAcceso.place(x=120,y=410)
TxtDniUsuario.place(x=310,y=110)
TxtNomUsuario.place(x=310,y=170)
TxtApePaUsuario.place(x=310,y=230)
TxtApeMaUsuario.place(x=310,y=290)
TxtNomAcceso.place(x=310,y=350)
TxtClaAcceso.place(x=310,y=410)
BtnNuevo.place(x=15,y=100)
BtnGuardar.place(x=15,y=170)
BtnModificar.place(x=15,y=240)
BtnCancelar.place(x=15,y=310)
BtnBorrar.place(x=15,y=380)
BtnSalir.place(x=450,y=450)
LblImgLogo.place(x=10,y=10)
LblImgLogo2.place(x=440,y=10)
LblTxtAcademia.place(x=105,y=10)

VentanaUsuarios.mainloop()
