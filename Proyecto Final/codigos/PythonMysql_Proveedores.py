import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioProvedores:
    global textBoxid_proveedor
    textBoxid_proveedor = None

    global textBoxNombre
    textBoxNombre = None

    global textBoxDireccion
    textBoxDireccion = None

    global textBoxTelefono
    textBoxTelefono = None

    global textBoxEmail
    textBoxEmail = None


    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_Proveedores(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_proveedor
        global textBoxNombre
        global textBoxDireccion
        global textBoxTelefono
        global textBoxEmail
        
       
        global groupBox 
        global tree
        global base
        
        
        try: #la interfaz se programa dentro del try
            base = Tk () #creando un objeto de tipo interfaz para la ventana
            base.geometry("1400x370")#dimenciones de la ventana
            base.title("Base de datos")#titulo


            #llenado del formulario------------------------------------------------------------------
            #lado izquierdo ------------------------------------------------------------------------------------------          --------------------------------------------------
            #pad es el espaciado tanto en x como en y
            groupBox = LabelFrame(base,text="Datos de los trabajadores",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_proveedor = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_proveedor = Entry(groupBox) #"Entry" para los datos 
            textBoxid_proveedor.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelNombre = Label(groupBox,text="Nombre",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxNombre = Entry(groupBox) #"Entry" para los datos 
            textBoxNombre.grid(row=1,column=1) 

            
            labelDireccion = Label(groupBox,text="Direccion",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxDireccion = Entry(groupBox) #"Entry" para los datos 
            textBoxDireccion.grid(row=2,column=1) 

            labelTelefono = Label(groupBox,text="Telefono",width=15,font=("Arial",12)).grid(row=3,column=0)
            textBoxTelefono = Entry(groupBox) #"Entry" para los datos 
            textBoxTelefono.grid(row=3,column=1)  

            labelEmail = Label(groupBox,text="Email",width=13,font=("Arial",12)).grid(row=4,column=0)
            textBoxEmail = Entry(groupBox) #"Entry" para los datos 
            textBoxEmail.grid(row=4,column=1)



            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0,pady=15)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1,pady=15)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2,pady=15)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("id proveedor","Nombre","Direccion","Telefono","Email"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="id proveedor")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="Nombre")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="Direccion")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Telefono")

            tree.column("# 5",anchor=CENTER,)
            tree.heading("# 5",text="Email")



            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CProveedores.mostrarProveedores():
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
        global textBoxid_proveedor,textBoxNombre,textBoxDireccion,textBoxTelefono,textBoxEmail,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_proveedor is None or textBoxNombre is None or textBoxDireccion is None or textBoxTelefono is None or textBoxEmail is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            id_proveedor = textBoxid_proveedor.get()
            Nombre = textBoxNombre.get()
            Direccion = textBoxDireccion.get()
            Telefono = textBoxTelefono.get()
            Email = textBoxEmail.get()
            if Direccion == '':
                Direccion = None  
    

            bandera = CProveedores.IngresarProveedores(Nombre,Direccion,Telefono,Email) #todo menos clave primaria
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron guardados")
                actualizarTreeView()
            else: 
                 messagebox.showinfo("Error","Error al guardar los datos")

            
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree

     try:
          #borrar los elementos actuales
          tree.delete(*tree.get_children())#cabeceras padres, registros hijos

          #obtner los nuevos datos que deseamos mostrar
          datos = CProveedores.mostrarProveedores()

          #insertar los nuevos datos en el TreeView
          for row in CProveedores.mostrarProveedores():
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

               textBoxid_proveedor.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_proveedor.insert(0,values[0])

               textBoxNombre.delete(0,END)
               textBoxNombre.insert(0,values[1])

               textBoxDireccion.delete(0,END)

               if values[2] == 'None':
                    textBoxDireccion.insert(0,'')
               else:
                    textBoxDireccion.delete(0,END)
                    textBoxDireccion.insert(0,values[2])    

               textBoxTelefono.delete(0,END)
               textBoxTelefono.insert(0,values[3])

               textBoxEmail.delete(0,END)
               textBoxEmail.insert(0,values[4])

    
     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_proveedor,textBoxNombre,textBoxDireccion,textBoxTelefono,textBoxEmail,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_proveedor is None or textBoxNombre is None or textBoxDireccion is None or textBoxTelefono is None or textBoxEmail is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            id_proveedor = textBoxid_proveedor.get()
            Nombre = textBoxNombre.get()
            Direccion = textBoxDireccion.get()
            Telefono = textBoxTelefono.get()
            Email = textBoxEmail.get()
            if Direccion == '':
                Direccion = None  



                    #utilizar estas variables
            
            bandera = CProveedores.modificarProveedores(Nombre,Direccion,Telefono,Email,id_proveedor)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            

            #limpiar campos

            textBoxid_proveedor.delete(0,END)
            textBoxNombre.delete(0,END)
            textBoxDireccion.delete(0,END)
            textBoxTelefono.delete(0,END)
            textBoxEmail.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_proveedor,textBoxNombre,textBoxDireccion,textBoxTelefono,textBoxEmail,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_proveedor is None:
                print("Los widgets no estan inicializados")
                return
            
            id_proveedor=textBoxid_proveedor.get()
            
           
            bandera = CProveedores.eliminarProveedores(id_proveedor)
            if id_proveedor == '':
                bandera = False
            
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            else:
                 messagebox.showinfo("Informacion","Error al eliminar un registro")
                 
            actualizarTreeView()

            #limpiar campos
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






