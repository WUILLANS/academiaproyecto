from tkinter import PhotoImage
import tkinter
from tkinter import messagebox
from Clases.ClsUsuarios import ClsUsuario

def registrar_usuario():
    #messagebox.showinfo(title="prueba", message="aacediendo a la función")
    datosUsuarios= {"DniUsuario":TxtDniUsuario.get(),"APaUsuario":TxtApePaUsuario.get(),"AMaUsuario":TxtApeMaUsuario.get(),"NomUsuario":TxtNomUsuario.get(),"ClaAcceso": TxtClaAcceso.get(),"NomAcceso":TxtNomAcceso.get()}
    objusuario=ClsUsuario()
    if objusuario.registrarUsuario(datosUsuarios)==True:
        messagebox.showinfo(title="registro usuario", message="se registro el usuario con exito")
    else:
        messagebox.showinfo(title="registro usuario", message=" no se ha podido registrar al usuario")

def limpiar_usuario():
    objusuario = ClsUsuario()
    if objusuario.borrarUsuario(TxtDniUsuario.get()) == True:
        messagebox.showinfo(title="borrar usuario", message="se borro el usuario con exito")
        TxtDniUsuario.delete(0, "end")
        TxtNomUsuario.delete(0, "end")
        TxtApePaUsuario.delete(0, "end")
        TxtApeMaUsuario.delete(0, "end")
        TxtNomAcceso.delete(0, "end")
        TxtClaAcceso.delete(0, "end")
    else:
        messagebox.showinfo(title="borrar usuario", message=" no se ha podido borrar al usuario")


    #******************VENTANA PRINCIPAL DEL MANTENIMIENTO DE USUARIOS ************
VentanaUsuarios = tkinter.Tk()
VentanaUsuarios.title("Mantenimiento de Usuarios")
AnchoScreen = VentanaUsuarios.winfo_screenwidth()
AltoScreen = VentanaUsuarios.winfo_screenheight()
#Medidas y centrado de la ventana
posx = AnchoScreen // 2 - 370 // 2
posy = AltoScreen // 2 - 300 // 2
centro = "450x400"+"+"+str(posx)+"+"+str(posy)
VentanaUsuarios.geometry(centro)

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
ImgCancelar = PhotoImage(file = "../Imagenes/Cancelar.png")
BtnCancelar = tkinter.Button(VentanaUsuarios,image=ImgCancelar,command=limpiar_usuario)
ImgSalir = PhotoImage(file = "../Imagenes/Salir.png")
BtnSalir = tkinter.Button(VentanaUsuarios,image=ImgSalir)

#***************************** POSICIONANDO LOS CONTROLES EN EL GRID **********************
LblDniUsuario.grid(row=0,column=0,padx=10,pady=10, sticky="w")
LblNomUsuario.grid(row=1,column=0,padx=10,pady=10, sticky="w")
LblApePaUsuario.grid(row=2,column=0,padx=10,pady=10, sticky="w")
LblApeMaUsuario.grid(row=3,column=0,padx=10,pady=10, sticky="w")
LblClaAcceso.grid(row=5,column=0,padx=10,pady=10, sticky="w")
LblNomAcceso.grid(row=4,column=0,padx=10,pady=10, sticky="w")
TxtDniUsuario.grid(row=0,column=1,padx=10,pady=10, sticky="w")
TxtNomUsuario.grid(row=1,column=1,padx=10,pady=10, sticky="w")
TxtApePaUsuario.grid(row=2,column=1,padx=10,pady=10, sticky="w")
TxtApeMaUsuario.grid(row=3,column=1,padx=10,pady=10, sticky="w")
TxtClaAcceso.grid(row=5,column=1,padx=10,pady=10, sticky="w")
TxtNomAcceso.grid(row=4,column=1,padx=10,pady=10, sticky="w")
BtnNuevo.grid(row=0,column=2,padx=30,pady=10, sticky="w")
BtnGuardar.grid(row=1,column=2,padx=30,pady=10, sticky="w")
BtnModificar.grid(row=2,column=2,padx=30,pady=10, sticky="w")
BtnCancelar.grid(row=3,column=2,padx=30,pady=10, sticky="w")
BtnSalir.grid(row=4,column=2,padx=30,pady=10, sticky="w")
VentanaUsuarios.mainloop()
