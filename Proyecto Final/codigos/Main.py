import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Funciones import *  # Mantén tu lógica para manejar usuarios aquí.
from conexion import *

#archivos de cada tabla-------------------------------------------------------
from PyrhonMysql import *
from PythonMysql_Motocicletas import *
from PythonMysql_componentes import *
from PythonMysql_diagnosticos import *
from PythonMysql_Historial import *
from PythonMysql_Modelos import *
from PythonMysql_Ventas import *
from PythonMysql_Punto import *
from PythonMysql_Inventario import *
from PythonMysql_Trabajadores import *
from PythonMysql_Proveedores import *
from PythonMysql_Sensores import *
from PythonMysql_Motocicleta_Componentes import *


# Función para mostrar el formulario dependiendo de la tabla seleccionada
def mostrar_formulario(tabla_seleccionada):
    
    
   
    if tabla_seleccionada == "Usuarios":
        Formulario()
      
    elif tabla_seleccionada == "Motocicletas":
        Formulario_Motocicleta()
      
    elif tabla_seleccionada == "Componentes":
       Formulario_Componentes()
       
    elif tabla_seleccionada == "Diagnosticos":
      Formulario_Diagnosticos()

    elif tabla_seleccionada == "Historial de mantenimiento":
      Formulario_Historial()

    elif tabla_seleccionada == "Modelos":
      Formulario_Modelos()

    elif tabla_seleccionada == "Ventas":
      Formulario_Ventas()
    
    elif tabla_seleccionada == "Punto de venta":
      Formulario_Punto()

    elif tabla_seleccionada == "Inventario":
      Formulario_Inventario()

    elif tabla_seleccionada == "Trabajadores":
      Formulario_Trabajadores()

    elif tabla_seleccionada == "Proveedores":
      Formulario_Proveedores()
    
    elif tabla_seleccionada == "Sensores":
      Formulario_Sensores()

    elif tabla_seleccionada == "Motocicleta Componentes":
      Formulario_M_C()
       
    else:
        messagebox.showerror("Error", f"Formulario para {tabla_seleccionada} no implementado")
    
    
    
    

# Función para mostrar el menú inicial
def menu_inicial():
    ventana_menu = Tk()
    ventana_menu.geometry("300x800")
    ventana_menu.title("Menú de Selección de Tabla")
    
    Label(ventana_menu, text="Selecciona la tabla a modificar", font=("Arial", 14)).pack(pady=20)
    
    # Lista de tablas
    tablas = ["Usuarios", "Motocicletas", "Componentes", "Diagnosticos","Historial de mantenimiento","Modelos","Ventas","Punto de venta","Inventario","Trabajadores","Proveedores","Sensores","Motocicleta Componentes"]  #aqui van todas las tablas 
    
    for tabla in tablas:
        Button(ventana_menu, text=tabla, width=20, height=2, 
               command=lambda t=tabla: [mostrar_formulario(t)]).pack(pady=5)
    
    ventana_menu.mainloop()

# Ejecución inicial
menu_inicial()
