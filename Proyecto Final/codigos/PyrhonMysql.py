import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioUsuarios:
    global textBoxId 
    textBoxId = None

    global textBoxNombre
    textBoxNombre = None

    global textBoxEmail
    textBoxEmail = None

    global textBoxTelefono
    textBoxTelefono = None

    global textBoxFecha_Registro
    textBoxFecha_Registro = None

    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario(): #funncion para crear formlario de usuarios-clientes
        global textBoxId 
        global textBoxNombre
        global textBoxEmail
        global textBoxTelefono
        global textBoxFecha_Registro
        global groupBox 
        global tree
        global base
        
        
        try: #la interfaz se programa dentro del try
            base = Tk () #creando un objeto de tipo interfaz para la ventana
            base.geometry("1400x300")#dimenciones de la ventana
            base.title("Base de datos")#titulo


            #llenado del formulario------------------------------------------------------------------
            #lado izquierdo ------------------------------------------------------------------------------------------          --------------------------------------------------
            #pad es el espaciado tanto en x como en y
            groupBox = LabelFrame(base,text="Datos de los Usuarios",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            #elementos de la seccion izquierda
            labelId = Label(groupBox,text="Id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxId = Entry(groupBox) #"Entry" para los datos 
            textBoxId.grid(row=0,column=1) 

            labelNombre = Label(groupBox,text="Nombre",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxNombre = Entry(groupBox) #"Entry" para los datos 
            textBoxNombre.grid(row=1,column=1) 
            
            labelEmail = Label(groupBox,text="Email",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxEmail = Entry(groupBox) #"Entry" para los datos 
            textBoxEmail.grid(row=2,column=1) 

            labelTelefono = Label(groupBox,text="Telefono",width=13,font=("Arial",12)).grid(row=3,column=0)
            textBoxTelefono = Entry(groupBox) #"Entry" para los datos 
            textBoxTelefono.grid(row=3,column=1)

            labelFecha_Registro = Label(groupBox,text="Fecha de Registro",width=15,font=("Arial",12)).grid(row=4,column=0)
            textBoxFecha_Registro = Entry(groupBox) #"Entry" para los datos 
            textBoxFecha_Registro.grid(row=4,column=1)  

            

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=6,column=0)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=6,column=1)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=6,column=2)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("Id","Nombre","Email","Telefono","Fecha De Registro"),show='headings',height=5,)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="Id")

            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="Nombre")

            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="Email")

            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4",text="Telefono")

            tree.column("# 5",anchor=CENTER)
            tree.heading("# 5",text="Fecha de Registro")


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CUsuarios.mostrarUsuarios():
                 #el resultado que me devuelca la el recorrido de la funcion me lo insertara en el tree
                 tree.insert("","end",values=row)


        
            #ejecutar la funcion al hacer click y mostrar el resultado en los campos / entry

            tree.bind("<<TreeviewSelect>>",seleccionarRegistro) #cuando se pinta de azul es, este es el evento



            tree.pack() #muestra el treeview


            #fin lado derecho ------------------------------------------------------------------------------------------          ---------------------------------------------------------------



            #fin de llenado de fomulario------------------------------------------------------------------

            base.mainloop()#va al final---------------------------------------------------------------------------------------------------------------------------

        
        except ValueError as error: #equivalete a catch guardando el error en la variable error
            print("Error al mostrar la interfa, error: {}".format(error))





def guardarRegistros():
        global textBoxNombre,textBoxEmail,textBoxTelefono,textBoxFecha_Registro,groupBox

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxNombre is None or textBoxEmail is None or textBoxTelefono is None or textBoxFecha_Registro is None:
                print("Los widgets no estan inicializados")
                return
            
            nombre = textBoxNombre.get()
            email = textBoxEmail.get()
            telefono = textBoxTelefono.get()
            fecha_registro = textBoxFecha_Registro.get()

            CUsuarios.IngresarUsarios(nombre,email,telefono,fecha_registro)
            messagebox.showinfo("Informacion","Los datos fueron guardados")
            actualizarTreeView()

            #limpiar campos
            textBoxId.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxEmail.delete(0,END)
            textBoxTelefono.delete(0,END)
            textBoxFecha_Registro.delete(0,END)
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree

     try:
          #borrar los elementos actuales
          tree.delete(*tree.get_children())#cabeceras padres, registros hijos

          #obtner los nuevos datos que deseamos mostrar
          datos = CUsuarios.mostrarUsuarios()

          #insertar los nuevos datos en el TreeView
          for row in CUsuarios.mostrarUsuarios():
               tree.insert("","end",values=row)
     except ValueError as error:
          print("Error al actualizar tabla {}".format(error))       



def seleccionarRegistro(evento): #evento al ser click el evento
     try:
          #obtner el id del eelemento seleccionado
          itemSeleccionado = tree.focus()
          if itemSeleccionado:
               #obtener lo valores por columan
               values = tree.item(itemSeleccionado)['values']
               #establecer los valores en los widgets entry

               textBoxId.delete(0,END)
               textBoxId.insert(0,values[0])

               textBoxNombre.delete(0,END)
               textBoxNombre.insert(0,values[1])

               textBoxEmail.delete(0,END)
               textBoxEmail.insert(0,values[2])

               textBoxTelefono.delete(0,END)
               textBoxTelefono.insert(0,values[3])

               textBoxFecha_Registro.delete(0,END)
               textBoxFecha_Registro.insert(0,values[4])


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros():
        global textBoxId,textBoxNombre,textBoxEmail,textBoxTelefono,textBoxFecha_Registro,groupBox

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxNombre is None or textBoxEmail is None or textBoxTelefono is None or textBoxFecha_Registro is None or textBoxId is None:
                print("Los widgets no estan inicializados")
                return
            
            idUsuario=textBoxId.get()
            nombre = textBoxNombre.get()
            email = textBoxEmail.get()
            telefono = textBoxTelefono.get()
            fecha_registro = textBoxFecha_Registro.get()

            CUsuarios.modificarUsuarios(idUsuario,nombre,email,telefono,fecha_registro)
            messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            actualizarTreeView()

            #limpiar campos
            textBoxId.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxEmail.delete(0,END)
            textBoxTelefono.delete(0,END)
            textBoxFecha_Registro.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxId,textBoxNombre,textBoxEmail,textBoxTelefono,textBoxFecha_Registro,groupBox

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxId is None:
                print("Los widgets no estan inicializados")
                return
            
            idUsuario=textBoxId.get()
           
            CUsuarios.eliminarUsuarios(idUsuario)
            messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            actualizarTreeView()

            #limpiar campos
            textBoxId.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxEmail.delete(0,END)
            textBoxTelefono.delete(0,END)
            textBoxFecha_Registro.delete(0,END)
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))




