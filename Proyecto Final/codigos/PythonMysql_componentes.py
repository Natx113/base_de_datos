import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioComponentes:
    global textBoxid_componente
    textBoxid_componente = None

    global textBoxNombre_Componente
    textBoxNombre_componente = None

    global textBoxDescripcion
    textBoxDescripcion = None

    global textBoxVida_Util
    textBoxVida_Util = None

    global textBoxUnidad_Medida
    textBoxUnidad_Medida = None


    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_Componentes(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_componente
        global textBoxNombre_Componente
        global textBoxDescripcion
        global textBoxVida_Util
        global textBoxUnidad_Medida
       
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
            groupBox = LabelFrame(base,text="Datos de los componentes",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_componente = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_componente = Entry(groupBox) #"Entry" para los datos 
            textBoxid_componente.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelNombre_Componente = Label(groupBox,text="Componente",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxNombre_Componente = Entry(groupBox) #"Entry" para los datos 
            textBoxNombre_Componente.grid(row=1,column=1) 

            
            label_descripcion = Label(groupBox,text="Descripcion",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxDescripcion = Entry(groupBox) #"Entry" para los datos 
            textBoxDescripcion.grid(row=2,column=1) 

            labelVida_Util = Label(groupBox,text="Vida Util",width=13,font=("Arial",12)).grid(row=3,column=0)
            textBoxVida_Util = Entry(groupBox) #"Entry" para los datos 
            textBoxVida_Util.grid(row=3,column=1)

            labelUnidad_Medida = Label(groupBox,text="Unidad de Medida",width=15,font=("Arial",12)).grid(row=4,column=0)
            textBoxUnidad_Medida = Entry(groupBox) #"Entry" para los datos 
            textBoxUnidad_Medida.grid(row=4,column=1)  

            


            

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("id_componente","nombre_componente","descripcion","vida_util","unidad_medida"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="Id Componente")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="Nombre del componente")

            tree.column("# 3",anchor=CENTER,width=400)
            tree.heading("# 3",text="Descripcion")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Vida util")

            tree.column("# 5",anchor=CENTER,)
            tree.heading("# 5",text="Unidad de medida")


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CComponentes.mostrarComponentes():
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
        global textBoxNombre_Componente,textBoxDescripcion,textBoxVida_Util,textBoxUnidad_Medida,groupBox

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxNombre_Componente is None or textBoxDescripcion is None or textBoxVida_Util is None or textBoxUnidad_Medida is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            
            nombre_componente = textBoxNombre_Componente.get()
            descripcion_componente = textBoxDescripcion.get()
            vida_util = textBoxVida_Util.get()
            unidad_medida = textBoxUnidad_Medida.get()

            bandera = CComponentes.IngresarComponentes(nombre_componente,descripcion_componente,vida_util,unidad_medida) #todo menos clave primaria
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron guardados")
                actualizarTreeView()
            else: 
                 messagebox.showinfo("Error","Error al guardar los datos")

            #limpiar campos
            
            textBoxid_componente.delete(0,END)
            textBoxNombre_Componente.delete(0,END)
            textBoxDescripcion.delete(0,END)
            textBoxVida_Util.delete(0,END)
            textBoxUnidad_Medida.delete(0,END)
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree

     try:
          #borrar los elementos actuales
          tree.delete(*tree.get_children())#cabeceras padres, registros hijos

          #obtner los nuevos datos que deseamos mostrar
          datos = CComponentes.mostrarComponentes()

          #insertar los nuevos datos en el TreeView
          for row in CComponentes.mostrarComponentes():
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

               textBoxid_componente.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_componente.insert(0,values[0])

               textBoxNombre_Componente.delete(0,END)
               textBoxNombre_Componente.insert(0,values[1])

               textBoxDescripcion.delete(0,END)
               textBoxDescripcion.insert(0,values[2])

               textBoxVida_Util.delete(0,END)
               textBoxVida_Util.insert(0,values[3])

               textBoxUnidad_Medida.delete(0,END)
               textBoxUnidad_Medida.insert(0,values[4])

               


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_componente,textBoxNombre_Componente,textBoxDescripcion,textBoxVida_Util,textBoxUnidad_Medida,groupBox,groupBox 

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxNombre_Componente is None or textBoxDescripcion is None or textBoxVida_Util is None or textBoxUnidad_Medida is None:
                print("Los widgets no estan inicializados")
                return
            
            id_componente = textBoxid_componente.get() #         agregar clave primaria
            nombre_componente = textBoxNombre_Componente.get()
            descripcion_componente = textBoxDescripcion.get()
            vida_util = textBoxVida_Util.get()
            unidad_medida = textBoxUnidad_Medida.get()


                    #utilizar estas variables
            
            bandera = CComponentes.modificarComponentes(nombre_componente,descripcion_componente,vida_util,unidad_medida,id_componente)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            #limpiar campos
            textBoxid_componente.delete(0,END)
            textBoxNombre_Componente.delete(0,END)
            textBoxDescripcion.delete(0,END)
            textBoxVida_Util.delete(0,END)
            textBoxUnidad_Medida.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_componente,textBoxNombre_Componente,textBoxDescripcion,textBoxVida_Util,textBoxUnidad_Medida,groupBox,groupBox  #utiliza clave primaria

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxid_componente is None:
                print("Los widgets no estan inicializados")
                return
            
            id_componente=textBoxid_componente.get()
           
            CComponentes.eliminarComponentes(id_componente)
            messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            actualizarTreeView()

            #limpiar campos
            textBoxid_componente.delete(0,END)
            textBoxNombre_Componente.delete(0,END)
            textBoxDescripcion.delete(0,END)
            textBoxVida_Util.delete(0,END)
            textBoxUnidad_Medida.delete(0,END)
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






