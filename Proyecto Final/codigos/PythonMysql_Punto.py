import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioPunto:
    global textBoxid_punto_venta
    textBoxid_punto_venta = None

    global textBoxNombre_punto
    textBoxNombre_punto = None

    global textBoxUbicacion
    textBoxUbicacion = None

    global textBoxContacto
    textBoxContacto = None

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




def Formulario_Punto(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_punto_venta
        global textBoxNombre_punto
        global textBoxUbicacion
        global textBoxContacto
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
            groupBox = LabelFrame(base,text="Datos de los puntos de venta",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_punto_venta = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_punto_venta = Entry(groupBox) #"Entry" para los datos 
            textBoxid_punto_venta.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelNombre_punto = Label(groupBox,text="Nombre del punto",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxNombre_punto = Entry(groupBox) #"Entry" para los datos 
            textBoxNombre_punto.grid(row=1,column=1) 

            
            label_Ubicacion = Label(groupBox,text="Ubicacion",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxUbicacion = Entry(groupBox) #"Entry" para los datos 
            textBoxUbicacion.grid(row=2,column=1) 

            labelContacto = Label(groupBox,text="Contacto",width=15,font=("Arial",12)).grid(row=3,column=0)
            textBoxContacto = Entry(groupBox) #"Entry" para los datos 
            textBoxContacto.grid(row=3,column=1)  

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

            tree = ttk.Treeview(groupBox,columns=("id Punto","Nombre del punto","Ubicacion","Contacto","Email"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="id Punto")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="Nombre del punto")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="Ubicacion")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Contacto")

            tree.column("# 5",anchor=CENTER,)
            tree.heading("# 5",text="Email")

          


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CPunto.mostrarPunto():
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
        global textBoxNombre_punto,textBoxUbicacion,textBoxContacto,textBoxEmail,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxNombre_punto is None or textBoxUbicacion is None or textBoxContacto is None or textBoxEmail is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            
           
           
           
            
            nombre_punto = textBoxNombre_punto.get()
            ubicacion = textBoxUbicacion.get()
            contacto = textBoxContacto.get()
            email = textBoxEmail.get()

            bandera = CPunto.IngresarPunto(nombre_punto,ubicacion,contacto,email) #todo menos clave primaria
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
          datos = CPunto.mostrarPunto()

          #insertar los nuevos datos en el TreeView
          for row in CPunto.mostrarPunto():
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
               


               textBoxid_punto_venta.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_punto_venta.insert(0,values[0])

               textBoxNombre_punto.delete(0,END)
               textBoxNombre_punto.insert(0,values[1])

               textBoxUbicacion.delete(0,END)
               textBoxUbicacion.insert(0,values[2])

               textBoxContacto.delete(0,END)
               textBoxContacto.insert(0,values[3])

               textBoxEmail.delete(0,END)
               textBoxEmail.insert(0,values[4])


               


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxNombre_punto,textBoxUbicacion,textBoxContacto,textBoxEmail,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_punto_venta is None or textBoxNombre_punto is None or textBoxUbicacion is None or textBoxContacto is None or textBoxEmail is None:
                print("Los widgets no estan inicializados")
                return
            
            id_punto = textBoxid_punto_venta.get()
            nombre_punto = textBoxNombre_punto.get()
            ubicacion = textBoxUbicacion.get()
            contacto = textBoxContacto.get()
            email = textBoxEmail.get()



                    #utilizar estas variables
            
            bandera = CPunto.modificarPunto(nombre_punto,ubicacion,contacto,email,id_punto)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            #limpiar campos
            textBoxid_punto_venta.delete(0,END)
            textBoxNombre_punto.delete(0,END)
            textBoxUbicacion.delete(0,END)
            textBoxContacto.delete(0,END)
            textBoxEmail.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_punto_venta,textBoxNombre_punto,textBoxUbicacion,textBoxContacto,textBoxEmail,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_punto_venta is None:
                print("Los widgets no estan inicializados")
                return
            
            id_punto_venta=textBoxid_punto_venta.get()
           
            CPunto.eliminarPunto(id_punto_venta)
            messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            actualizarTreeView()

            #limpiar campos
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






