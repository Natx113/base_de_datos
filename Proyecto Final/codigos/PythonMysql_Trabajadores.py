import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioTrabajadores:
    global textBoxid_trabajador
    textBoxid_trabajador = None

    global textBoxNombre_trabajador
    textBoxNombre_trabajador = None

    global textBoxPuesto
    textBoxPuesto = None

    global textBoxFecha_contratacion
    textBoxFecha_contratacion = None

    global textBoxTelefono
    textBoxTelefono = None

    global textBoxEmail
    textBoxEmail = None

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




def Formulario_Trabajadores(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_trabajador
        global textBoxNombre_trabajador
        global textBoxPuesto
        global textBoxFecha_contratacion
        global textBoxTelefono
        global textBoxEmail
        global textBoxid_punto_venta
       
        global groupBox 
        global tree
        global base
        
        
        try: #la interfaz se programa dentro del try
            base = Tk () #creando un objeto de tipo interfaz para la ventana
            base.geometry("1800x370")#dimenciones de la ventana
            base.title("Base de datos")#titulo


            #llenado del formulario------------------------------------------------------------------
            #lado izquierdo ------------------------------------------------------------------------------------------          --------------------------------------------------
            #pad es el espaciado tanto en x como en y
            groupBox = LabelFrame(base,text="Datos de los trabajadores",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid_trabajador = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_trabajador = Entry(groupBox) #"Entry" para los datos 
            textBoxid_trabajador.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelNombre_trabajador = Label(groupBox,text="Nombre",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxNombre_trabajador = Entry(groupBox) #"Entry" para los datos 
            textBoxNombre_trabajador.grid(row=1,column=1) 

            
            labelPuesto = Label(groupBox,text="Puesto",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxPuesto = Entry(groupBox) #"Entry" para los datos 
            textBoxPuesto.grid(row=2,column=1) 

            labelFecha_contratacion = Label(groupBox,text="Fecha de contratacion",width=15,font=("Arial",12)).grid(row=3,column=0)
            textBoxFecha_contratacion = Entry(groupBox) #"Entry" para los datos 
            textBoxFecha_contratacion.grid(row=3,column=1)  

            labelTelefono = Label(groupBox,text="Telefono",width=13,font=("Arial",12)).grid(row=4,column=0)
            textBoxTelefono = Entry(groupBox) #"Entry" para los datos 
            textBoxTelefono.grid(row=4,column=1)

            labelEmail = Label(groupBox,text="Email",width=13,font=("Arial",12)).grid(row=5,column=0)
            textBoxEmail = Entry(groupBox) #"Entry" para los datos 
            textBoxEmail.grid(row=5,column=1)

            labelid_punto_venta = Label(groupBox,text="id punto venta",width=13,font=("Arial",12)).grid(row=6,column=0)
            textBoxid_punto_venta = Entry(groupBox) #"Entry" para los datos 
            textBoxid_punto_venta.grid(row=6,column=1)



            


            

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0,pady=15)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1,pady=15)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2,pady=15)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("id Trabajador","Nombre","Puesto","Fecha de contratacion","Telefono","Email","id punto venta"),show='headings',height=15,)
            tree.column("# 1",anchor=CENTER,)
            tree.heading("# 1",text="id Trabajador")

            tree.column("# 2",anchor=CENTER,)
            tree.heading("# 2",text="Nombre")

            tree.column("# 3",anchor=CENTER,)
            tree.heading("# 3",text="Puesto")

            tree.column("# 4",anchor=CENTER,)
            tree.heading("# 4",text="Fecha de contratacion")

            tree.column("# 5",anchor=CENTER,)
            tree.heading("# 5",text="Telefono")

            tree.column("# 6",anchor=CENTER,)
            tree.heading("# 6",text="Email")

            tree.column("# 7",anchor=CENTER,)
            tree.heading("# 7",text="id punto venta")


          


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CTrabajadores.mostrarTrabajadores():
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
        global textBoxNombre_trabajador,textBoxPuesto,textBoxFecha_contratacion,textBoxTelefono,textBoxEmail,textBoxid_punto_venta,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_trabajador is None or textBoxNombre_trabajador is None or textBoxPuesto is None or textBoxFecha_contratacion is None or textBoxTelefono is None or textBoxEmail is None or textBoxid_punto_venta is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            nombre = textBoxNombre_trabajador.get()
            puesto = textBoxPuesto.get()
            Fecha_contracion = textBoxFecha_contratacion.get()
            Telefono = textBoxTelefono.get()
            Email = textBoxEmail.get()
            id_punto_venta = textBoxid_punto_venta.get()
            if id_punto_venta == '':
                id_punto_venta = None  

            
            

            bandera = CTrabajadores.IngresarTrabajadores(nombre,puesto,Fecha_contracion,Telefono,Email,id_punto_venta) #todo menos clave primaria
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
          datos = CTrabajadores.mostrarTrabajadores()

          #insertar los nuevos datos en el TreeView
          for row in CTrabajadores.mostrarTrabajadores():
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
               
            
              

               textBoxid_trabajador.delete(0,END)  #    <-----    incluir clave primaria
               textBoxid_trabajador.insert(0,values[0])

               textBoxNombre_trabajador.delete(0,END)
               textBoxNombre_trabajador.insert(0,values[1])

               textBoxPuesto.delete(0,END)
               textBoxPuesto.insert(0,values[2])

               textBoxFecha_contratacion.delete(0,END)
               textBoxFecha_contratacion.insert(0,values[3])

               textBoxTelefono.delete(0,END)
               textBoxTelefono.insert(0,values[4])

               textBoxEmail.delete(0,END)
               textBoxEmail.insert(0,values[5])

               textBoxid_punto_venta.delete(0,END)
               if values[6] =='None':
                   
                   textBoxid_punto_venta.insert(0,'')
               else:
                    textBoxid_punto_venta.delete(0,END)
                    textBoxid_punto_venta.insert(0,values[6])
               


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros(): 
        global textBoxid_trabajador,textBoxNombre_trabajador,textBoxPuesto,textBoxFecha_contratacion,textBoxTelefono,textBoxEmail,textBoxid_punto_venta,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_trabajador is None or textBoxNombre_trabajador is None or textBoxPuesto is None or textBoxFecha_contratacion is None or textBoxTelefono is None or textBoxEmail is None or textBoxid_punto_venta is None:
                print("Los widgets no estan inicializados")
                return
            
            #agregar todos los datos menos clave primaria
            
           
           
            id_trabajador = textBoxid_trabajador.get()
            nombre = textBoxNombre_trabajador.get()
            puesto = textBoxPuesto.get()
            Fecha_contracion = textBoxFecha_contratacion.get()
            Telefono = textBoxTelefono.get()
            Email = textBoxEmail.get()
            id_punto_venta = textBoxid_punto_venta.get()
            if id_punto_venta == '':
                id_punto_venta = None



                    #utilizar estas variables
            
            bandera = CTrabajadores.modificarTrabajadores(nombre,puesto,Fecha_contracion,Telefono,Email,id_punto_venta,id_trabajador)  #agregar clave primaria al final
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            #limpiar campos
            textBoxid_trabajador.delete(0,END)
            textBoxNombre_trabajador.delete(0,END)
            textBoxPuesto.delete(0,END)
            textBoxFecha_contratacion.delete(0,END)
            textBoxTelefono.delete(0,END)
            textBoxEmail.delete(0,END)
            textBoxid_punto_venta.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_trabajador,textBoxNombre_trabajador,textBoxPuesto,textBoxFecha_contratacion,textBoxTelefono,textBoxEmail,textBoxid_punto_venta,groupBox
        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if  textBoxid_trabajador is None:
                print("Los widgets no estan inicializados")
                return
            
            id_trabajador=textBoxid_trabajador.get()
            
           
            bandera = CTrabajadores.eliminarTrabajadores(id_trabajador)
            if id_trabajador == '':
                bandera = False
            
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            else:
                 messagebox.showinfo("Informacion","Error al eliminar un registro")
                 
            actualizarTreeView()

            #limpiar campos
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






