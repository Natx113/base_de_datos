import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexion import *
from Funciones import *

class FormularioDiagnosticos:
    global textBoxIdDiagnostico
    textBoxIdDiagnostico = None

    global textBoxIdMotocicleta
    textBoxIdMotocicleta = None

    global textBoxIdComponente
    textBoxIdComponente = None

    global textBoxFechaDiagnostico
    textBoxFechaDiagnostico = None

    global textBoxTipoFalla
    textBoxTipoFalla = None

    global textBoxDescripcion
    textBoxDescripcion = None

    global textBoxSolucionSugerida
    textBoxSolucionSugerida = None

    global groupBox
    groupBox = None

    global tree
    tree = None

    global base
    base = None

def Formulario_Diagnosticos():
    global textBoxIdDiagnostico
    global textBoxIdMotocicleta
    global textBoxIdComponente
    global textBoxFechaDiagnostico
    global textBoxTipoFalla
    global textBoxDescripcion
    global textBoxSolucionSugerida

    global groupBox
    global tree
    global base

    try:
        base = Tk()
        base.geometry("1600x400")
        base.title("Base de datos Diagnosticos")

        # Llenado del formulario
        groupBox = LabelFrame(base, text="Datos de los Diagnosticos", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        labelIdDiagnostico = Label(groupBox, text="Id Diagnostico", width=15, font=("Arial", 12)).grid(row=0, column=0)
        textBoxIdDiagnostico = Entry(groupBox)
        textBoxIdDiagnostico.grid(row=0, column=1)

        labelIdMotocicleta = Label(groupBox, text="Id Motocicleta", width=15, font=("Arial", 12)).grid(row=1, column=0)
        textBoxIdMotocicleta = Entry(groupBox)
        textBoxIdMotocicleta.grid(row=1, column=1)

        labelIdComponente = Label(groupBox, text="Id Componente", width=15, font=("Arial", 12)).grid(row=2, column=0)
        textBoxIdComponente = Entry(groupBox)
        textBoxIdComponente.grid(row=2, column=1)

        labelFechaDiagnostico = Label(groupBox, text="Fecha Diagnostico", width=15, font=("Arial", 12)).grid(row=3, column=0)
        textBoxFechaDiagnostico = Entry(groupBox)
        textBoxFechaDiagnostico.grid(row=3, column=1)

        labelTipoFalla = Label(groupBox, text="Tipo de Falla", width=15, font=("Arial", 12)).grid(row=4, column=0)
        textBoxTipoFalla = Entry(groupBox)
        textBoxTipoFalla.grid(row=4, column=1)

        labelDescripcion = Label(groupBox, text="Descripción", width=15, font=("Arial", 12)).grid(row=5, column=0)
        textBoxDescripcion = Entry(groupBox)
        textBoxDescripcion.grid(row=5, column=1)

        labelSolucionSugerida = Label(groupBox, text="Solución Sugerida", width=15, font=("Arial", 12)).grid(row=6, column=0)
        textBoxSolucionSugerida = Entry(groupBox)
        textBoxSolucionSugerida.grid(row=6, column=1)

        Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=7, column=0)
        Button(groupBox, text="Modificar", width=10, command=modificarRegistros).grid(row=7, column=1)
        Button(groupBox, text="Eliminar", width=10, command=eliminarRegistros).grid(row=7, column=2)

        # Lado derecho
        groupBox = LabelFrame(base, text="Lista de Diagnosticos", padx=5, pady=5)
        groupBox.grid(row=0, column=1, padx=5, pady=5)
        # Crear un TreeView
        tree = ttk.Treeview(groupBox, columns=("Id Diagnostico", "Id Motocicleta", "Id Componente", "Fecha Diagnostico", "Tipo de Falla", "Descripción", "Solución Sugerida"), show='headings', height=10)
        tree.column("# 1", anchor=CENTER, width=100)
        tree.heading("# 1", text="Id Diagnostico")

        tree.column("# 2", anchor=CENTER, width=100)
        tree.heading("# 2", text="Id Motocicleta")

        tree.column("# 3", anchor=CENTER, width=100)
        tree.heading("# 3", text="Id Componente")

        tree.column("# 4", anchor=CENTER, width=200)
        tree.heading("# 4", text="Fecha Diagnostico")

        tree.column("# 5", anchor=CENTER, width=200)
        tree.heading("# 5", text="Tipo de Falla")

        tree.column("# 6", anchor=CENTER, width=250)
        tree.heading("# 6", text="Descripción")

        tree.column("# 7", anchor=CENTER, width=250)
        tree.heading("# 7", text="Solución Sugerida")

        # Agregar los datos a la tabla
        for row in CDiagnosticos.mostrarDiagnosticos():
            tree.insert("", "end", values=row)

        # Ejecutar la función al hacer clic y mostrar el resultado en los campos
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)
        tree.pack()

        base.mainloop()

    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))

def guardarRegistros():
    global textBoxIdDiagnostico, textBoxIdMotocicleta, textBoxIdComponente, textBoxFechaDiagnostico, textBoxTipoFalla, textBoxDescripcion, textBoxSolucionSugerida, groupBox

    try:
        id_diagnostico = textBoxIdDiagnostico.get()
        id_motocicleta = textBoxIdMotocicleta.get()
        id_componente = textBoxIdComponente.get()
        fecha_diagnostico = textBoxFechaDiagnostico.get()
        tipo_falla = textBoxTipoFalla.get()
        descripcion = textBoxDescripcion.get()
        solucion_sugerida = textBoxSolucionSugerida.get()

        CDiagnosticos.IngresarDiagnosticos(id_motocicleta, id_componente, fecha_diagnostico, tipo_falla, descripcion, solucion_sugerida)
        messagebox.showinfo("Información", "Los datos fueron guardados")
        actualizarTreeView()

        # Limpiar campos
        textBoxIdDiagnostico.delete(0, END)
        textBoxIdMotocicleta.delete(0, END)
        textBoxIdComponente.delete(0, END)
        textBoxFechaDiagnostico.delete(0, END)
        textBoxTipoFalla.delete(0, END)
        textBoxDescripcion.delete(0, END)
        textBoxSolucionSugerida.delete(0, END)

    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
    global tree

    try:
        # Borrar los elementos actuales
        tree.delete(*tree.get_children())

        # Obtener los nuevos datos que deseamos mostrar
        datos = CDiagnosticos.mostrarDiagnosticos()

        # Insertar los nuevos datos en el TreeView
        for row in datos:
            tree.insert("", "end", values=row)
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))

def seleccionarRegistro(evento):
    try:
        # Obtener el id del elemento seleccionado
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            # Obtener los valores por columna
            values = tree.item(itemSeleccionado)['values']
            # Establecer los valores en los widgets entry

            textBoxIdDiagnostico.delete(0, END)
            textBoxIdDiagnostico.insert(0, values[0])

            textBoxIdMotocicleta.delete(0, END)
            textBoxIdMotocicleta.insert(0, values[1])

            textBoxIdComponente.delete(0, END)
            textBoxIdComponente.insert(0, values[2])

            textBoxFechaDiagnostico.delete(0, END)
            textBoxFechaDiagnostico.insert(0, values[3])

            textBoxTipoFalla.delete(0, END)
            textBoxTipoFalla.insert(0, values[4])

            textBoxDescripcion.delete(0, END)
            textBoxDescripcion.insert(0, values[5])

            textBoxSolucionSugerida.delete(0, END)
            textBoxSolucionSugerida.insert(0, values[6])

    except ValueError as error:
        print("Error al seleccionar registro {}".format(error))

def modificarRegistros():
    global textBoxIdDiagnostico, textBoxIdMotocicleta, textBoxIdComponente, textBoxFechaDiagnostico, textBoxTipoFalla, textBoxDescripcion, textBoxSolucionSugerida,groupBox

    try:
        id_diagnostico = textBoxIdDiagnostico.get()
        id_motocicleta = textBoxIdMotocicleta.get()
        id_componente = textBoxIdComponente.get()
        fecha_diagnostico = textBoxFechaDiagnostico.get()
        tipo_falla = textBoxTipoFalla.get()
        descripcion = textBoxDescripcion.get()
        solucion_sugerida = textBoxSolucionSugerida.get()

        bandera = CDiagnosticos.modificarDiagnosticos(id_motocicleta, id_componente, fecha_diagnostico, tipo_falla, descripcion, solucion_sugerida,id_diagnostico)
        if bandera:
            messagebox.showinfo("Información", "Los datos fueron actualizados correctamente")
        else:
            messagebox.showinfo("Información", "Los datos no fueron actualizados")

        actualizarTreeView()

        # Limpiar campos
        textBoxIdDiagnostico.delete(0, END)
        textBoxIdMotocicleta.delete(0, END)
        textBoxIdComponente.delete(0, END)
        textBoxFechaDiagnostico.delete(0, END)
        textBoxTipoFalla.delete(0, END)
        textBoxDescripcion.delete(0, END)
        textBoxSolucionSugerida.delete(0, END)

    except ValueError as error:
        print("Error al modificar los datos {}".format(error))

def eliminarRegistros():
    global textBoxIdDiagnostico

    try:
        id_diagnostico = textBoxIdDiagnostico.get()

        CDiagnosticos.eliminarDiagnosticos(id_diagnostico)
        messagebox.showinfo("Información", "Los datos fueron eliminados correctamente")
        actualizarTreeView()

        # Limpiar campos
        textBoxIdDiagnostico.delete(0, END)
        textBoxIdMotocicleta.delete(0, END)
        textBoxIdComponente.delete(0, END)
        textBoxFechaDiagnostico.delete(0, END)
        textBoxTipoFalla.delete(0, END)
        textBoxDescripcion.delete(0, END)
        textBoxSolucionSugerida.delete(0, END)

    except ValueError as error:
        print("Error al eliminar los datos {}".format(error))



