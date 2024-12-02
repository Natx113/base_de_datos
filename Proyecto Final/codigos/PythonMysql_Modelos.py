import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioModelos:
    global textBoxid_modelo
    textBoxid_modelo = None

    global textBoxNombre_modelo
    textBoxNombre_modelo = None

    global textBoxDescripcion
    textBoxDescripcion = None

    global textBoxPrecio
    textBoxPrecio = None

    global textBoxFecha_lanzamiento
    textBoxFecha_lanzamiento = None


    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_Modelos(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_modelo
        global textBoxNombre_modelo
        global textBoxDescripcion
        global textBoxPrecio
        global textBoxFecha_lanzamiento
       
        global groupBox 
        global tree
        global base
        
        
        try: #la interfaz se programa dentro del try
            base = Tk () #creando un objeto de tipo interfaz para la ventana
            base.geometry("1650x370")#dimenciones de la ventana
            base.title("Base de datos")#titulo


            #llenado del formulario------------------------------------------------------------------
            #lado izquierdo ------------------------------------------------------------------------------------------          --------------------------------------------------
            #pad es el espaciado tanto en x como en y
            groupBox = LabelFrame(base,text="Datos de los modelos",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_modelo = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_modelo = Entry(groupBox) #"Entry" para los datos 
            textBoxid_modelo.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelNombre_modelo = Label(groupBox,text="Nombre del modelo",width=20,font=("Arial",12)).grid(row=1,column=0)
            textBoxNombre_modelo = Entry(groupBox) #"Entry" para los datos 
            textBoxNombre_modelo.grid(row=1,column=1) 

            
            label_Descripcion = Label(groupBox,text="Descripcion",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxDescripcion = Entry(groupBox) #"Entry" para los datos 
            textBoxDescripcion.grid(row=2,column=1) 

            labelPrecio = Label(groupBox,text="Precio",width=13,font=("Arial",12)).grid(row=3,column=0)
            textBoxPrecio = Entry(groupBox) #"Entry" para los datos 
            textBoxPrecio.grid(row=3,column=1)

            labelFecha_lanzamiento = Label(groupBox,text="Fecha de lanzamiento",width=20,font=("Arial",12)).grid(row=4,column=0)
            textBoxFecha_lanzamiento = Entry(groupBox) #"Entry" para los datos 
            textBoxFecha_lanzamiento.grid(row=4,column=1)  

            


            

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0,pady=15)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1,pady=15)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2,pady=15)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("Id modelo","Nombre del modelo","Descripcion","Precio","Fecha de lanzamiento"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="Id modelo")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="Nombre del modelo")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="Descripcion")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Precio")

            tree.column("# 5",anchor=CENTER,width=400)
            tree.heading("# 5",text="Fecha de lanzamiento")


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CModelos.mostrarModelos():
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
        global textBoxNombre_modelo,textBoxDescripcion,textBoxPrecio,textBoxFecha_lanzamiento,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxNombre_modelo is None or textBoxDescripcion is None or textBoxPrecio is None or textBoxFecha_lanzamiento is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            
           
           
            nombre_modelo = textBoxNombre_modelo.get()
            descripcion = textBoxDescripcion.get()
            precio = textBoxPrecio.get()
            fecha_lanzamiento = textBoxFecha_lanzamiento.get()

            bandera = CModelos.IngresarModelos(nombre_modelo,descripcion,precio,fecha_lanzamiento) #todo menos clave primaria
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron guardados")
                actualizarTreeView()
            else: 
                 messagebox.showinfo("Error","Error al guardar los datos")

            #limpiar campos
            
            textBoxid_modelo.delete(0,END)
            textBoxNombre_modelo.delete(0,END)
            textBoxDescripcion.delete(0,END)
            textBoxPrecio.delete(0,END)
            textBoxFecha_lanzamiento.delete(0,END)
            
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree

     try:
          #borrar los elementos actuales
          tree.delete(*tree.get_children())#cabeceras padres, registros hijos

          #obtner los nuevos datos que deseamos mostrar
          datos = CModelos.mostrarModelos()

          #insertar los nuevos datos en el TreeView
          for row in CModelos.mostrarModelos():
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

               textBoxid_modelo.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_modelo.insert(0,values[0])

               textBoxNombre_modelo.delete(0,END)
               textBoxNombre_modelo.insert(0,values[1])

               textBoxDescripcion.delete(0,END)
               textBoxDescripcion.insert(0,values[2])

               textBoxPrecio.delete(0,END)
               textBoxPrecio.insert(0,values[3])

               textBoxFecha_lanzamiento.delete(0,END)
               textBoxFecha_lanzamiento.insert(0,values[4])

               


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_modelo,textBoxNombre_modelo,textBoxDescripcion,textBoxPrecio,textBoxFecha_lanzamiento,groupBox
        
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_modelo is None or textBoxNombre_modelo is None or textBoxDescripcion is None or textBoxPrecio is None or textBoxFecha_lanzamiento is None or textBoxid_modelo is None:
                print("Los widgets no estan inicializados")
                return
            
            id_modelo = textBoxid_modelo.get()
            nombre_modelo = textBoxNombre_modelo.get()
            descripcion = textBoxDescripcion.get()
            precio = textBoxPrecio.get()
            fecha_lanzamiento = textBoxFecha_lanzamiento.get()



                    #utilizar estas variables
            
            bandera = CModelos.modificarModelos(nombre_modelo,descripcion,precio,fecha_lanzamiento,id_modelo)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            #limpiar campos
            textBoxid_modelo.delete(0,END)
            textBoxNombre_modelo.delete(0,END)
            textBoxDescripcion.delete(0,END)
            textBoxPrecio.delete(0,END)
            textBoxFecha_lanzamiento.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_modelo,textBoxNombre_modelo,textBoxDescripcion,textBoxPrecio,textBoxFecha_lanzamiento,groupBox   #utiliza clave primaria

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxid_modelo is None:
                print("Los widgets no estan inicializados")
                return
            
            id_modelo=textBoxid_modelo.get()
           
            CModelos.eliminarModelos(id_modelo)
            messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            actualizarTreeView()

           
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






