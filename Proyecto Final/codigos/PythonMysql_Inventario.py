import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioInventario:
    global textBoxid_inventario
    textBoxid_inventario = None

    global textBoxid_modelo
    textBoxid_modelo = None

    global textBoxCantidad
    textBoxCantidad = None

    global textBoxFecha_entrada
    textBoxFecha_entrada = None

    global textBoxFecha_salida
    textBoxFecha_salida = None

    global textBoxEstado_producto
    textBoxEstado_producto = None



    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_Inventario(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_inventario
        global textBoxid_modelo
        global textBoxCantidad
        global textBoxFecha_entrada
        global textBoxFecha_salida
        global textBoxEstado_producto
       
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
            groupBox = LabelFrame(base,text="Datos del inventario",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_inventario = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_inventario = Entry(groupBox) #"Entry" para los datos 
            textBoxid_inventario.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelid_modelo = Label(groupBox,text="id del modelo",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxid_modelo = Entry(groupBox) #"Entry" para los datos 
            textBoxid_modelo.grid(row=1,column=1) 

            
            labelCantidad = Label(groupBox,text="Cantidad",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxCantidad = Entry(groupBox) #"Entry" para los datos 
            textBoxCantidad.grid(row=2,column=1) 

            labelFecha_entrada = Label(groupBox,text="Fecha de entrada",width=15,font=("Arial",12)).grid(row=3,column=0)
            textBoxFecha_entrada = Entry(groupBox) #"Entry" para los datos 
            textBoxFecha_entrada.grid(row=3,column=1)  

            labelFecha_salida = Label(groupBox,text="Fecha de salida",width=13,font=("Arial",12)).grid(row=4,column=0)
            textBoxFecha_salida = Entry(groupBox) #"Entry" para los datos 
            textBoxFecha_salida.grid(row=4,column=1)

            labelEstado_producto = Label(groupBox,text="Estado del producto",width=13,font=("Arial",12)).grid(row=5,column=0)
            textBoxEstado_producto = Entry(groupBox) #"Entry" para los datos 
            textBoxEstado_producto.grid(row=5,column=1)



            


            

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0,pady=15)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1,pady=15)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2,pady=15)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("id inventario","id del modelo","Cantidad","Fecha de entrada","Fecha de salida","Estado del producto"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="id inventario")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="id del modelo")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="Cantidad")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Fecha de entrada")

            tree.column("# 5",anchor=CENTER,)
            tree.heading("# 5",text="Fecha de salida")

            tree.column("# 6",anchor=CENTER,)
            tree.heading("# 6",text="Estado del producto")


          


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CInventario.mostrarInventario():
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
        global textBoxid_modelo,textBoxCantidad,textBoxFecha_entrada,textBoxFecha_salida,textBoxEstado_producto,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_modelo is None or textBoxCantidad is None or textBoxFecha_entrada is None or textBoxFecha_salida is None or textBoxEstado_producto is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            
           
           
           
            
            id_modelo = textBoxid_modelo.get()
            cantidad = textBoxCantidad.get()
            Fecha_entrada = textBoxFecha_entrada.get()
            Fecha_salida = textBoxFecha_salida.get()
            if Fecha_salida == '':
                Fecha_salida = None  
            estado_producto = textBoxEstado_producto.get()

            bandera = CInventario.IngresarInventario(id_modelo,cantidad,Fecha_entrada,Fecha_salida,estado_producto) #todo menos clave primaria
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
          datos = CInventario.mostrarInventario()

          #insertar los nuevos datos en el TreeView
          for row in CInventario.mostrarInventario():
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
               
                
               textBoxid_inventario.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_inventario.insert(0,values[0])

               textBoxid_modelo.delete(0,END)
               textBoxid_modelo.insert(0,values[1])

               textBoxCantidad.delete(0,END)
               textBoxCantidad.insert(0,values[2])

               textBoxFecha_entrada.delete(0,END)
               textBoxFecha_entrada.insert(0,values[3])

               textBoxFecha_salida.delete(0, END)
               
               if values[4] =='None':
                   textBoxFecha_salida.insert(0,'')
               
               else:
                    textBoxFecha_salida.delete(0,END)
                    textBoxFecha_salida.insert(0,values[4])
                
                

               textBoxEstado_producto.delete(0,END)
               textBoxEstado_producto.insert(0,values[5])


               


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_inventario,textBoxid_modelo,textBoxCantidad,textBoxFecha_entrada,textBoxFecha_salida,textBoxEstado_producto,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_inventario is None or textBoxid_modelo is None or textBoxCantidad is None or textBoxFecha_entrada is None or textBoxFecha_salida is None or textBoxEstado_producto is None:
                print("Los widgets no estan inicializados")
                return
            
            id_inventario = textBoxid_inventario.get()
            id_modelo = textBoxid_modelo.get()
            cantidad = textBoxCantidad.get()
            Fecha_entrada = textBoxFecha_entrada.get()
            Fecha_salida = textBoxFecha_salida.get()
            if Fecha_salida == '':
                Fecha_salida = None   
            estado_producto = textBoxEstado_producto.get()



                    #utilizar estas variables
            
            bandera = CInventario.modificarInventario(id_modelo,cantidad,Fecha_entrada,Fecha_salida,estado_producto,id_inventario)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            #limpiar campos
            textBoxid_inventario.delete(0,END)
            textBoxid_modelo.delete(0,END)
            textBoxCantidad.delete(0,END)
            textBoxFecha_entrada.delete(0,END)
            textBoxFecha_salida.delete(0,END)
            textBoxEstado_producto.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_inventario,textBoxid_modelo,textBoxCantidad,textBoxFecha_entrada,textBoxFecha_salida,textBoxEstado_producto,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_inventario is None:
                print("Los widgets no estan inicializados")
                return
            
            id_inventario=textBoxid_inventario.get()
            
           
            bandera = CInventario.eliminarInventario(id_inventario)
            if id_inventario == '':
                bandera = False
            
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            else:
                 messagebox.showinfo("Informacion","Error al eliminar un registro")
                 
            actualizarTreeView()

            #limpiar campos
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






