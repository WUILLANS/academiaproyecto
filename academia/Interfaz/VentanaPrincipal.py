from tkinter import Menu
from tkinter import messagebox
import tkinter
import os

def ManUsuarios():
    os.system("MantenimientoUsuarios.py")

def FuncionSalir():
    Opcion=messagebox.askyesno(title="Confirmar",message="Está seguro que desea salir?")
    if Opcion==True:
        Principal.destroy()

#*********** VENTANA PRINCIPAL ***************
Principal = tkinter.Tk()
Principal.title("Ventana principal del sistema")
#Principal.attributes('-fullscreen', True)
w, h = Principal.winfo_screenwidth(), Principal.winfo_screenheight()
Principal.geometry("%dx%d+0+0" % (w, h))

#******************* CREACION DE UN MENU ESTANDAR (POPUP) ****************************
# 1ro. Se crea el menu
BarraMenu = Menu(Principal)
#2do se crea las opciones de menu con sus submenus
menuProcesos = Menu(BarraMenu)
menuProcesos.add_command(label="Mantenimiento de Ciclos")
menuProcesos.add_command(label="Mantenimiento de Alumnos")
menuProcesos.add_command(label="Mantenimiento de Usuarios",command=ManUsuarios)
menuProcesos.add_separator()
menuProcesos.add_command(label="Matrículas")
menuProcesos.add_separator()
menuProcesos.add_command(label="Salir",command=FuncionSalir)
#3ro. se activa el menu
BarraMenu.add_cascade(label="Procesos", menu=menuProcesos)
#*********************************************************************************************
menuConsultas = Menu(BarraMenu)
menuConsultas.add_command(label="Consulta de matrículas")
menuConsultas.add_command(label="Consulta de ciclos")
menuConsultas.add_command(label="Consulta de alumnos")
menuConsultas.add_separator()
menuConsultas.add_command(label="Consulta de usuarios")
#3ro. se activa el menu
BarraMenu.add_cascade(label="Reportes y Consultas", menu=menuConsultas)

#4to. se establece como menu de la ventana principal
Principal.config(menu=BarraMenu)
Principal.mainloop()