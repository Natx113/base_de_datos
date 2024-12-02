import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioHistorial:
    global textBoxid_mantenimiento
    textBoxid_componente = None

    global textBoxid_motocicleta
    textBoxNombre_componente = None

    global textBoxFecha_mantenimiento
    textBoxDescripcion = None

    global textBoxTipo_mantenimiento
    textBoxVida_Util = None

    global textBoxDetalles
    textBoxUnidad_Medida = None


    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_Historial(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_mantenimiento
        global textBoxid_motocicleta
        global textBoxFecha_mantenimiento
        global textBoxTipo_mantenimiento
        global textBoxDetalles
       
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
            groupBox = LabelFrame(base,text="Datos del Historil de mantenimiento",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_mantenimiento = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_mantenimiento = Entry(groupBox) #"Entry" para los datos 
            textBoxid_mantenimiento.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelid_motocicleta = Label(groupBox,text="Id Motocicleta",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxid_motocicleta = Entry(groupBox) #"Entry" para los datos 
            textBoxid_motocicleta.grid(row=1,column=1) 

            
            label_Fecha_mantenimiento = Label(groupBox,text="Fecha de mantenimiento",width=20,font=("Arial",12)).grid(row=2,column=0)
            textBoxFecha_mantenimiento = Entry(groupBox) #"Entry" para los datos 
            textBoxFecha_mantenimiento.grid(row=2,column=1) 

            labelTipo_mantenimiento = Label(groupBox,text="Tipo de mantenimiento",width=20,font=("Arial",12)).grid(row=3,column=0)
            textBoxTipo_mantenimiento = Entry(groupBox) #"Entry" para los datos 
            textBoxTipo_mantenimiento.grid(row=3,column=1)

            labelDetalles = Label(groupBox,text="Detalles",width=15,font=("Arial",12)).grid(row=4,column=0)
            textBoxDetalles = Entry(groupBox) #"Entry" para los datos 
            textBoxDetalles.grid(row=4,column=1)  

            


            

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0,pady=15)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1,pady=15)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2,pady=15)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("Id Mantenimiento","Id Motocicleta","Fecha de mantenimiento","Tipo de mantenimiento","Detalles"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="Id Mantenimiento")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="Id Motocicleta")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="Fecha de mantenimiento")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Tipo de mantenimiento")

            tree.column("# 5",anchor=CENTER,width=400)
            tree.heading("# 5",text="Detalles")


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CHistorial.mostrarHistorial():
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
        global textBoxid_mantenimiento,textBoxid_motocicleta,textBoxFecha_mantenimiento,textBoxTipo_mantenimiento,textBoxDetalles,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_mantenimiento is None or textBoxid_motocicleta is None or textBoxFecha_mantenimiento is None or textBoxTipo_mantenimiento is None or textBoxDetalles is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            
           
            id_motocicleta = textBoxid_motocicleta.get()
            fecha_mantenimiento = textBoxFecha_mantenimiento.get()
            tipo_mantenimiento = textBoxTipo_mantenimiento.get()
            detalles = textBoxDetalles.get()

            bandera = CHistorial.IngresarHistorial(id_motocicleta,fecha_mantenimiento,tipo_mantenimiento,detalles) #todo menos clave primaria
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron guardados")
                actualizarTreeView()
            else: 
                 messagebox.showinfo("Error","Error al guardar los datos")

            #limpiar campos
            
            textBoxid_mantenimiento.delete(0,END)
            textBoxid_motocicleta.delete(0,END)
            textBoxFecha_mantenimiento.delete(0,END)
            textBoxTipo_mantenimiento.delete(0,END)
            textBoxDetalles.delete(0,END)
            
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree

     try:
          #borrar los elementos actuales
          tree.delete(*tree.get_children())#cabeceras padres, registros hijos

          #obtner los nuevos datos que deseamos mostrar
          datos = CHistorial.mostrarHistorial()

          #insertar los nuevos datos en el TreeView
          for row in CHistorial.mostrarHistorial():
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

               textBoxid_mantenimiento.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_mantenimiento.insert(0,values[0])

               textBoxid_motocicleta.delete(0,END)
               textBoxid_motocicleta.insert(0,values[1])

               textBoxFecha_mantenimiento.delete(0,END)
               textBoxFecha_mantenimiento.insert(0,values[2])

               textBoxTipo_mantenimiento.delete(0,END)
               textBoxTipo_mantenimiento.insert(0,values[3])

               textBoxDetalles.delete(0,END)
               textBoxDetalles.insert(0,values[4])

               


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_mantenimiento,textBoxid_motocicleta,textBoxFecha_mantenimiento,textBoxTipo_mantenimiento,textBoxDetalles,groupBox 

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_mantenimiento is None or textBoxid_motocicleta is None or textBoxFecha_mantenimiento is None or textBoxTipo_mantenimiento is None or textBoxDetalles is None:
                print("Los widgets no estan inicializados")
                return
            
            id_mantenimiento = textBoxid_mantenimiento.get()
            id_motocicleta = textBoxid_motocicleta.get()
            fecha_mantenimiento = textBoxFecha_mantenimiento.get()
            tipo_mantenimiento = textBoxTipo_mantenimiento.get()
            detalles = textBoxDetalles.get()



                    #utilizar estas variables
            
            bandera = CHistorial.modificarHistorial(id_motocicleta,fecha_mantenimiento,tipo_mantenimiento,detalles,id_mantenimiento)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            #limpiar campos
            textBoxid_mantenimiento.delete(0,END)
            textBoxid_motocicleta.delete(0,END)
            textBoxFecha_mantenimiento.delete(0,END)
            textBoxTipo_mantenimiento.delete(0,END)
            textBoxDetalles.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_mantenimiento,textBoxid_motocicleta,textBoxFecha_mantenimiento,textBoxTipo_mantenimiento,textBoxDetalles,groupBox   #utiliza clave primaria

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxid_mantenimiento is None:
                print("Los widgets no estan inicializados")
                return
            
            id_mantenimiento=textBoxid_mantenimiento.get()
           
            CHistorial.eliminarHistorial(id_mantenimiento)
            messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            actualizarTreeView()

            #limpiar campos
            textBoxid_mantenimiento.delete(0,END)
            textBoxid_motocicleta.delete(0,END)
            textBoxFecha_mantenimiento.delete(0,END)
            textBoxTipo_mantenimiento.delete(0,END)
            textBoxDetalles.delete(0,END)
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






