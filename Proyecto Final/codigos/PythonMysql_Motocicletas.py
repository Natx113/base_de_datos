import tkinter as tk #libreria para crear interfaces graficas

#Importar los modules restantes de tinter para la interfaz grafica

from tkinter import *
from tkinter import ttk ## de tkinter importa ttk
from tkinter import messagebox #mensaje que nos indica si se realizo el registro

#otros archivos de python 
from conexion import *
from Funciones import *


class FormularioMotocicletas:
    global textBoxId 
    textBoxId_motocicleta = None

    global textBoxid_usuario
    textBoxid_usuario = None

    global textBoxEmail
    textBoxEmail = None

    global textBoxTelefono
    textBoxTelefono = None

    global textBoxFecha_Registro
    textBoxFecha_Registro = None

    global groupBox 
    groupBox = None

    global tree
    tree = None

    global combo
    combo = None

    global base
    base = None




def Formulario_Motocicleta(): #funncion para crear formlario de usuarios-clientes
        global textBoxid_usuario
        global textBoxid_motocicleta
        global textBoxMarca
        global textBoxModelo
        global textBoxAnio
        global textBoxNumero_serie
        global textBoxCilindrada
        global textBoxColor

        global groupBox 
        global tree
        global base
        
        
        try: #la interfaz se programa dentro del try
            base = Tk () #creando un objeto de tipo interfaz para la ventana
            base.geometry("1160x300")#dimenciones de la ventana
            base.title("Base de datos")#titulo


            #llenado del formulario------------------------------------------------------------------
            #lado izquierdo ------------------------------------------------------------------------------------------          --------------------------------------------------
            #pad es el espaciado tanto en x como en y
            groupBox = LabelFrame(base,text="Datos de las Motocicletas",padx=5,pady=5) #panel izquierdo 
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelid = Label(groupBox,text="id",width=13,font=("Arial",12)).grid(row=0,column=0)
            textBoxid_motocicleta = Entry(groupBox) #"Entry" para los datos 
            textBoxid_motocicleta.grid(row=0,column=1) 

            #elementos de la seccion izquierda
            labelid_usuario = Label(groupBox,text="Id usuario",width=13,font=("Arial",12)).grid(row=1,column=0)
            textBoxid_usuario = Entry(groupBox) #"Entry" para los datos 
            textBoxid_usuario.grid(row=1,column=1) 

            
            labelMarca = Label(groupBox,text="Marca",width=13,font=("Arial",12)).grid(row=2,column=0)
            textBoxMarca = Entry(groupBox) #"Entry" para los datos 
            textBoxMarca.grid(row=2,column=1) 

            labelModelo = Label(groupBox,text="Modelo",width=13,font=("Arial",12)).grid(row=3,column=0)
            textBoxModelo = Entry(groupBox) #"Entry" para los datos 
            textBoxModelo.grid(row=3,column=1)

            labelAnio = Label(groupBox,text="Anio",width=15,font=("Arial",12)).grid(row=4,column=0)
            textBoxAnio = Entry(groupBox) #"Entry" para los datos 
            textBoxAnio.grid(row=4,column=1)  

            labelNumero_serie = Label(groupBox,text="Numero de serie",width=15,font=("Arial",12)).grid(row=5,column=0)
            textBoxNumero_serie = Entry(groupBox) #"Entry" para los datos 
            textBoxNumero_serie.grid(row=5,column=1) 

            labelCilindrada = Label(groupBox,text="Cilindrada",width=15,font=("Arial",12)).grid(row=6,column=0)
            textBoxCilindrada = Entry(groupBox) #"Entry" para los datos 
            textBoxCilindrada.grid(row=6,column=1) 

            labelColor = Label(groupBox,text="Color",width=15,font=("Arial",12)).grid(row=7,column=0)
            textBoxColor = Entry(groupBox) #"Entry" para los datos 
            textBoxColor.grid(row=7,column=1) 


            

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=8,column=0)

            Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=8,column=1)
            
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=8,column=2)
            #fin lado izquierdo ------------------------------------------------------------------------------------------          -----------------------------------------------------




            #lado derecho ------------------------------------------------------------------------------------------          --------------------------------------------------------------
            groupBox = LabelFrame(base,tex="Lista Obtenida",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            #Crearundo un TreeView

            #configurando columnas

            tree = ttk.Treeview(groupBox,columns=("Id","id Motocicleta","Marca","Modelo","año","Numero de serie","Cilindrada","color"),show='headings',height=5,)
            tree.column("# 1",anchor=CENTER,width=100)
            tree.heading("# 1",text="Id Motocicleta")

            tree.column("# 2",anchor=CENTER,width=100)
            tree.heading("# 2",text="id Usuario")

            tree.column("# 3",anchor=CENTER,width=100)
            tree.heading("# 3",text="Marca")

            tree.column("# 4",anchor=CENTER,width=100)
            tree.heading("# 4",text="Modelo")

            tree.column("# 5",anchor=CENTER,width=100)
            tree.heading("# 5",text="año")

            tree.column("# 6",anchor=CENTER,width=120)
            tree.heading("# 6",text="Numero de serie")

            tree.column("# 7",anchor=CENTER,width=70)
            tree.heading("# 7",text="Cilindrada")

            tree.column("# 8",anchor=CENTER,width=70)
            tree.heading("# 8",text="color")


            #agregar los datos a la tabla, solo visualizar
            #Mostrar la tabla

            for row in CMotocicletas.mostrarMotocicletas():
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
        global textBoxid_usuario,textBoxid_motocicleta,textBoxMarca,textBoxModelo,textBoxAnio,textBoxNumero_serie,textBoxCilindrada,textBoxColor,groupBox

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxid_usuario is None or textBoxid_motocicleta is None or textBoxMarca is None or textBoxModelo is None or textBoxAnio is None or textBoxNumero_serie is None or textBoxCilindrada is None or textBoxColor is None:
                print("Los widgets no estan inicializados")
                return
            
            
            id_usuario = textBoxid_usuario.get()
            marca = textBoxMarca.get()
            modelo = textBoxModelo.get()
            anio = textBoxAnio.get()
            numero_serie = textBoxNumero_serie.get()
            cilindrada = textBoxCilindrada.get()
            color = textBoxColor.get()

            CMotocicletas.IngresarMotocicletas(id_usuario,marca,modelo,anio,numero_serie,cilindrada,color)
            messagebox.showinfo("Informacion","Los datos fueron guardados")
            actualizarTreeView()

            #limpiar campos
            textBoxid_motocicleta.delete(0,END)
            textBoxid_usuario.delete(0,END)
            textBoxMarca.delete(0,END)
            textBoxModelo.delete(0,END)
            textBoxAnio.delete(0,END)
            textBoxNumero_serie.delete(0,END)
            textBoxCilindrada.delete(0,END)
            textBoxColor.delete(0,END)
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree

     try:
          #borrar los elementos actuales
          tree.delete(*tree.get_children())#cabeceras padres, registros hijos

          #obtner los nuevos datos que deseamos mostrar
          datos = CMotocicletas.mostrarMotocicletas()

          #insertar los nuevos datos en el TreeView
          for row in CMotocicletas.mostrarMotocicletas():
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

               textBoxid_motocicleta.delete(0,END)
               textBoxid_motocicleta.insert(0,values[0])

               textBoxid_usuario.delete(0,END)
               textBoxid_usuario.insert(0,values[1])

               textBoxMarca.delete(0,END)
               textBoxMarca.insert(0,values[2])

               textBoxModelo.delete(0,END)
               textBoxModelo.insert(0,values[3])

               textBoxAnio.delete(0,END)
               textBoxAnio.insert(0,values[4])

               textBoxNumero_serie.delete(0,END)
               textBoxNumero_serie.insert(0,values[5])

               textBoxCilindrada.delete(0,END)
               textBoxCilindrada.insert(0,values[6])

               textBoxColor.delete(0,END)
               textBoxColor.insert(0,values[7])


     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))

def modificarRegistros():
        global textBoxid_usuario,textBoxid_motocicleta,textBoxMarca,textBoxModelo,textBoxAnio,textBoxNumero_serie,textBoxCilindrada,textBoxColor,groupBox

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxid_usuario is None or textBoxid_motocicleta is None or textBoxMarca is None or textBoxModelo is None or textBoxAnio is None or textBoxNumero_serie is None or textBoxCilindrada is None or textBoxColor is None:
                print("Los widgets no estan inicializados")
                return
            
            id_motocicleta = textBoxid_motocicleta.get()
            id_usuario = textBoxid_usuario.get()
            marca = textBoxMarca.get()
            modelo = textBoxModelo.get()
            anio = textBoxAnio.get()
            numero_serie = textBoxNumero_serie.get()
            cilindrada = textBoxCilindrada.get()
            color = textBoxColor.get()

            
            bandera = CMotocicletas.modificarMotocicletas(id_usuario,marca,modelo,anio,numero_serie,cilindrada,color,id_motocicleta)
            if bandera:
                messagebox.showinfo("Informacion","Los datos fueron actulizados correctamente")
            else:
                messagebox.showinfo("Informacion","Los datos no fueron actualizados")
        

            actualizarTreeView()

            #limpiar campos
            textBoxid_motocicleta.delete(0,END)
            textBoxid_usuario.delete(0,END)
            textBoxMarca.delete(0,END)
            textBoxModelo.delete(0,END)
            textBoxAnio.delete(0,END)
            textBoxNumero_serie.delete(0,END)
            textBoxCilindrada.delete(0,END)
            textBoxColor.delete(0,END)
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
 

def eliminarRegistros():
        global textBoxid_usuario,textBoxid_motocicleta,textBoxMarca,textBoxModelo,textBoxAnio,textBoxNumero_serie,textBoxCilindrada,textBoxColor,groupBox

        try:
            #verificando si los elementos de la interfaz estan inicializados, es decir los widgets
            if textBoxid_motocicleta is None:
                print("Los widgets no estan inicializados")
                return
            
            id_motocicleta=textBoxid_motocicleta.get()
           
            CMotocicletas.eliminarMotocicletas(id_motocicleta)
            messagebox.showinfo("Informacion","Los datos fueron eliminados correctamente")
            actualizarTreeView()

            #limpiar campos
            textBoxid_motocicleta.delete(0,END)
            textBoxid_usuario.delete(0,END)
            textBoxMarca.delete(0,END)
            textBoxModelo.delete(0,END)
            textBoxAnio.delete(0,END)
            textBoxNumero_serie.delete(0,END)
            textBoxCilindrada.delete(0,END)
            textBoxColor.delete(0,END)
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))






