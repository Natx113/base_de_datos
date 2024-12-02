import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioMC:
    global textBoxid_MC
    textBoxid_MC = None

    global textBoxid_M
    textBoxid_M = None

    global textBoxid_C
    textBoxid_C = None

    global textBoxCantidad
    textBoxCantidad = None


    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_M_C(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_MC
        global textBoxid_M
        global textBoxid_C
        global textBoxCantidad
      
        
       
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
            groupBox = LabelFrame(base,text="Datos de los componentes de las motocicletas",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_MC = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_MC = Entry(groupBox) #"Entry" para los datos 
            textBoxid_MC.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelid_M = Label(groupBox,text="id de motocicleta",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxid_M = Entry(groupBox) #"Entry" para los datos 
            textBoxid_M.grid(row=1,column=1) 

            
            labelid_C = Label(groupBox,text="id de componente",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxid_C = Entry(groupBox) #"Entry" para los datos 
            textBoxid_C.grid(row=2,column=1) 

            labelCantidad = Label(groupBox,text="Cantidad",width=15,font=("Arial",12)).grid(row=3,column=0)
            textBoxCantidad = Entry(groupBox) #"Entry" para los datos 
            textBoxCantidad.grid(row=3,column=1)



            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0,pady=15)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1,pady=15)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2,pady=15)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("id","id Motocicleta","id de componente","Cantidad"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="id")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="id Motocicleta")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="id de componente")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Cantidad")

            


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CM_C.mostrarM_C():
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
        global textBoxid_MC,textBoxid_M,textBoxid_C,textBoxCantidad,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_MC is None or textBoxid_M is None or textBoxid_C is None or textBoxCantidad is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria

            id_mc = textBoxid_MC.get()
            id_m =textBoxid_M.get()
            id_c = textBoxid_C.get()
            cantidad = textBoxCantidad.get()

     
            bandera = CM_C.IngresarM_C(id_m,id_c,cantidad) #todo menos clave primaria
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
          datos = CM_C.mostrarM_C()

          #insertar los nuevos datos en el TreeView
          for row in CM_C.mostrarM_C():
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


               textBoxid_MC.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_MC.insert(0,values[0])

               textBoxid_M.delete(0,END)
               textBoxid_M.insert(0,values[1])

               textBoxid_C.delete(0,END)
               textBoxid_C.insert(0,values[2])    

               textBoxCantidad.delete(0,END)
               textBoxCantidad.insert(0,values[3])

    
     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_MC,textBoxid_M,textBoxid_C,textBoxCantidad,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_MC is None or textBoxid_M is None or textBoxid_C is None or textBoxCantidad is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria

            id_mc = textBoxid_MC.get()
            id_m =textBoxid_M.get()
            id_c = textBoxid_C.get()
            cantidad = textBoxCantidad.get()



                    #utilizar estas variables
            
            bandera = CM_C.modificarM_C(id_m,id_c,cantidad,id_mc)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            

            #limpiar campos
            textBoxid_MC.delete(0,END)
            textBoxid_M.delete(0,END)
            textBoxid_C.delete(0,END)
            textBoxCantidad.delete(0,END)

        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_MC,textBoxid_M,textBoxid_C,textBoxCantidad,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_MC is None:
                print("Los widgets no estan inicializados")
                return
            
            id_mc=textBoxid_MC.get()
            
           
            bandera = CM_C.eliminarM_C(id_mc)
            if id_mc == '':
                bandera = False
            
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            else:
                 messagebox.showinfo("Informacion","Error al eliminar un registro")
                 
            actualizarTreeView()

            #limpiar campos
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






