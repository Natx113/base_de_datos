import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioSensores:
    global textBoxid_sensor
    textBoxid_sensor = None

    global textBoxid_componente
    textBoxid_componente = None

    global textBoxTipo
    textBoxTipo = None

    global textBoxRango_operacion
    textBoxRango_operacion = None

    global textBoxUnidad
    textBoxUnidad = None


    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_Sensores(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_sensor
        global textBoxid_componente
        global textBoxTipo
        global textBoxRango_operacion
        global textBoxUnidad
        
       
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
            groupBox = LabelFrame(base,text="Datos de los sensores",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_sensor = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_sensor = Entry(groupBox) #"Entry" para los datos 
            textBoxid_sensor.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelid_componente = Label(groupBox,text="id componente",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxid_componente = Entry(groupBox) #"Entry" para los datos 
            textBoxid_componente.grid(row=1,column=1) 

            
            labelTipo = Label(groupBox,text="Tipo",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxTipo = Entry(groupBox) #"Entry" para los datos 
            textBoxTipo.grid(row=2,column=1) 

            labelRango_operacion = Label(groupBox,text="Rango de operacion",width=15,font=("Arial",12)).grid(row=3,column=0)
            textBoxRango_operacion = Entry(groupBox) #"Entry" para los datos 
            textBoxRango_operacion.grid(row=3,column=1)  

            labelUnidad = Label(groupBox,text="Unidad",width=13,font=("Arial",12)).grid(row=4,column=0)
            textBoxUnidad = Entry(groupBox) #"Entry" para los datos 
            textBoxUnidad.grid(row=4,column=1)



            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0,pady=15)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1,pady=15)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2,pady=15)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("id sensor","id componente","Tipo","Rango de operacion","Unidad"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="id sensor")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="id componente")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="Tipo")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Rango de operacion")

            tree.column("# 5",anchor=CENTER,)
            tree.heading("# 5",text="Unidad")


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CSensores.mostrarSensores():
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
        global textBoxid_sensor,textBoxid_componente,textBoxTipo,textBoxRango_operacion,textBoxUnidad,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_componente is None or textBoxTipo is None or textBoxRango_operacion is None or textBoxUnidad is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria

            id_sensor = textBoxid_sensor.get()
            id_componente = textBoxid_componente.get()
            Tipo = textBoxTipo.get()
            Rango = textBoxRango_operacion.get()
            Unidad = textBoxUnidad.get()
     
            bandera = CSensores.IngresarSensores(id_componente,Tipo,Rango,Unidad) #todo menos clave primaria
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
          datos = CSensores.mostrarSensores()

          #insertar los nuevos datos en el TreeView
          for row in CSensores.mostrarSensores():
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

               textBoxid_sensor.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_sensor.insert(0,values[0])

               textBoxid_componente.delete(0,END)
               textBoxid_componente.insert(0,values[1])

               textBoxTipo.delete(0,END)
               textBoxTipo.insert(0,values[2])    

               textBoxRango_operacion.delete(0,END)
               textBoxRango_operacion.insert(0,values[3])

               textBoxUnidad.delete(0,END)
               textBoxUnidad.insert(0,values[4])

    
     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_sensor,textBoxid_componente,textBoxTipo,textBoxRango_operacion,textBoxUnidad,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_componente is None or textBoxTipo is None or textBoxRango_operacion is None or textBoxUnidad is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria

            id_sensor = textBoxid_sensor.get()
            id_componente = textBoxid_componente.get()
            Tipo = textBoxTipo.get()
            Rango = textBoxRango_operacion.get()
            Unidad = textBoxUnidad.get()



                    #utilizar estas variables
            
            bandera = CSensores.modificarSensores(id_componente,Tipo,Rango,Unidad,id_sensor)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            

            #limpiar campos
            textBoxid_sensor.delete(0,END)
            textBoxid_componente.delete(0,END)
            textBoxTipo.delete(0,END)
            textBoxRango_operacion.delete(0,END)
            textBoxUnidad.delete(0,END)

        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_sensor,textBoxid_componente,textBoxTipo,textBoxRango_operacion,textBoxUnidad,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_sensor is None:
                print("Los widgets no estan inicializados")
                return
            
            id_sensor=textBoxid_sensor.get()
            
           
            bandera = CSensores.eliminarSensores(id_sensor)
            if id_sensor == '':
                bandera = False
            
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            else:
                 messagebox.showinfo("Informacion","Error al eliminar un registro")
                 
            actualizarTreeView()

            #limpiar campos
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






