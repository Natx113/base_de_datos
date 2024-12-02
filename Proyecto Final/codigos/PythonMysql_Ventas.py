import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioVentas:
    global textBoxid_venta
    textBoxid_venta = None

    global textBoxid_modelo
    textBoxid_modelo = None

    global textBoxFecha_venta
    textBoxFecha_venta = None

    global textBoxPrecio_venta
    textBoxPrecio_venta = None

    global textBoxid_usuario
    textBoxid_usuario = None

    global textBoxid_punto_venta
    textBoxid_punto_venta = None


    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_Ventas(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_venta
        global textBoxid_modelo
        global textBoxFecha_venta
        global textBoxPrecio_venta
        global textBoxid_usuario
        global textBoxid_punto_venta
       
        global groupBox 
        global tree
        global base
        
        
        try: #la interfaz se programa dentro del try
            base = Tk () #creando un objeto de tipo interfaz para la ventana
            base.geometry("1600x370")#dimenciones de la ventana
            base.title("Base de datos")#titulo


            #llenado del formulario------------------------------------------------------------------
            #lado izquierdo ------------------------------------------------------------------------------------------          --------------------------------------------------
            #pad es el espaciado tanto en x como en y
            groupBox = LabelFrame(base,text="Datos de las ventas",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_venta = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_venta = Entry(groupBox) #"Entry" para los datos 
            textBoxid_venta.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelid_modelo = Label(groupBox,text="Id del modelo",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxid_modelo = Entry(groupBox) #"Entry" para los datos 
            textBoxid_modelo.grid(row=1,column=1) 

            
            label_Fecha_venta = Label(groupBox,text="Fecha de la venta",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxFecha_venta = Entry(groupBox) #"Entry" para los datos 
            textBoxFecha_venta.grid(row=2,column=1) 

            labelPrecio_venta = Label(groupBox,text="Precio de la venta",width=15,font=("Arial",12)).grid(row=3,column=0)
            textBoxPrecio_venta = Entry(groupBox) #"Entry" para los datos 
            textBoxPrecio_venta.grid(row=3,column=1)  

            labelid_usuario = Label(groupBox,text="Id del usuario",width=13,font=("Arial",12)).grid(row=4,column=0)
            textBoxid_usuario = Entry(groupBox) #"Entry" para los datos 
            textBoxid_usuario.grid(row=4,column=1)

            labelid_punto_venta = Label(groupBox,text="Id Punto venta",width=15,font=("Arial",12)).grid(row=5,column=0)
            textBoxid_punto_venta = Entry(groupBox) #"Entry" para los datos 
            textBoxid_punto_venta.grid(row=5,column=1)  

            


            

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0,pady=15)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1,pady=15)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2,pady=15)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("Id venta","Id del modelo","Fecha de venta","Precio de venta","Id usuario","Id Punto de venta"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="Id venta")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="Id del modelo")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="Fecha de venta")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Precio de venta")

            tree.column("# 5",anchor=CENTER,)
            tree.heading("# 5",text="Id usuario")

            tree.column("# 6",anchor=CENTER,)
            tree.heading("# 6",text="Id Punto de venta")


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CVentas.mostrarVentas():
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
        global textBoxid_modelo,textBoxFecha_venta,textBoxPrecio_venta,textBoxid_usuario,textBoxid_punto_venta,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_modelo is None or textBoxFecha_venta is None or textBoxPrecio_venta is None or textBoxid_usuario is None or textBoxid_punto_venta is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            
           
           
           
            id_modelo = textBoxid_modelo.get()
            fecha_venta= textBoxFecha_venta.get()
            precio_venta = textBoxPrecio_venta.get()
            id_usuario = textBoxid_usuario.get()
            id_punto_venta = textBoxid_punto_venta.get()

            bandera = CVentas.IngresarVentas(id_modelo,fecha_venta,precio_venta,id_usuario,id_punto_venta) #todo menos clave primaria
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
          datos = CVentas.mostrarVentas()

          #insertar los nuevos datos en el TreeView
          for row in CVentas.mostrarVentas():
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

               textBoxid_venta.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_venta.insert(0,values[0])

               textBoxid_modelo.delete(0,END)
               textBoxid_modelo.insert(0,values[1])

               textBoxFecha_venta.delete(0,END)
               textBoxFecha_venta.insert(0,values[2])

               textBoxPrecio_venta.delete(0,END)
               textBoxPrecio_venta.insert(0,values[3])

               textBoxid_usuario.delete(0,END)
               textBoxid_usuario.insert(0,values[4])

               textBoxid_punto_venta.delete(0,END)
               textBoxid_punto_venta.insert(0,values[5])

               


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_venta,textBoxid_modelo,textBoxFecha_venta,textBoxPrecio_venta,textBoxid_usuario,textBoxid_punto_venta,groupBox
        
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_venta is None or textBoxid_modelo is None or textBoxFecha_venta is None or textBoxPrecio_venta is None or textBoxid_usuario is None or textBoxid_punto_venta is None:
                print("Los widgets no estan inicializados")
                return
            
            id_venta = textBoxid_venta.get()
            id_modelo = textBoxid_modelo.get()
            fecha_venta= textBoxFecha_venta.get()
            precio_venta = textBoxPrecio_venta.get()
            id_usuario = textBoxid_usuario.get()
            id_punto_venta = textBoxid_punto_venta.get()



                    #utilizar estas variables
            
            bandera = CVentas.modificarVentas(id_modelo,fecha_venta,precio_venta,id_usuario,id_punto_venta,id_venta)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            #limpiar campos
            textBoxid_venta.delete(0,END)
            textBoxid_modelo.delete(0,END)
            textBoxFecha_venta.delete(0,END)
            textBoxPrecio_venta.delete(0,END)
            textBoxid_usuario.delete(0,END)
            textBoxid_punto_venta.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_venta,textBoxid_modelo,textBoxFecha_venta,textBoxPrecio_venta,textBoxid_usuario,textBoxid_punto_venta,groupBox   #utiliza clave primaria

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxid_venta is None:
                print("Los widgets no estan inicializados")
                return
            
            id_venta=textBoxid_venta.get()
           
            CVentas.eliminarVentas(id_venta)
            messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            actualizarTreeView()

            #limpiar campos
            textBoxid_venta.delete(0,END)
            textBoxid_modelo.delete(0,END)
            textBoxFecha_venta.delete(0,END)
            textBoxPrecio_venta.delete(0,END)
            textBoxid_usuario.delete(0,END)
            textBoxid_punto_venta.delete(0,END)
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






