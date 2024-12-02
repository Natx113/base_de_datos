from conexion import *

class CUsuarios: 

    def mostrarUsuarios():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from Usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))
    
    def IngresarUsarios(nombre,email,telefono,fecha_registro):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO Usuarios values(null,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (nombre,email,telefono,fecha_registro)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
            return True


        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False

    def modificarUsuarios(idUsuario,nombre,email,telefono,fecha_registro):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombre = %s, usuarios.email = %s, usuarios.telefono = %s, usuarios.fecha_registro = %s WHERE usuarios.id_usuario =%s;"
            
            valores = (nombre,email,telefono,fecha_registro,idUsuario)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))

    def eliminarUsuarios(idUsuario):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from usuarios WHERE usuarios.id_usuario=%s;"
            
            valores = (idUsuario,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))


class CMotocicletas: 

    def mostrarMotocicletas():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from motocicletas;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))
    
    def IngresarMotocicletas(id_usuario,marca,modelo,anio,numero_serie,cilindrada,color):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO motocicletas values(null,%s,%s,%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (id_usuario,marca,modelo,anio,numero_serie,cilindrada,color)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
            




        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))

    def modificarMotocicletas(id_usuario,marca,modelo,anio,numero_serie,cilindrada,color,idMotocicletas):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "UPDATE motocicletas SET motocicletas.id_usuario = %s, motocicletas.marca = %s, motocicletas.modelo = %s, motocicletas.anio = %s, motocicletas.numero_serie = %s, motocicletas.cilindrada = %s, motocicletas.color = %s WHERE motocicletas.id_motocicleta =%s;"
            

            valores = (id_usuario,marca,modelo,anio,numero_serie,cilindrada,color,idMotocicletas)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            
            
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarMotocicletas(idMotocicleta):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from motocicletas WHERE motocicletas.id_motocicleta=%s;"
            
            valores = (idMotocicleta,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))


class CComponentes: 

    def mostrarComponentes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from componentes;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarComponentes(nombre_componente,descripcion,vida_util,unidad_medida): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO componentes values(null,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (nombre_componente,descripcion,vida_util,unidad_medida)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarComponentes(nombre_componente,descripcion,vida_util,unidad_medida,id_componente): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE componentes SET componentes.nombre = %s, componentes.descripcion = %s, componentes.vida_util = %s, componentes.unidad_medida = %s WHERE componentes.id_componente=%s;"
            

            valores = (nombre_componente,descripcion,vida_util,unidad_medida,id_componente)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarComponentes(id_componente):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from componentes WHERE componentes.id_componente=%s;"
            
            valores = (id_componente,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()


class CDiagnosticos:
    def mostrarDiagnosticos():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from diagnosticos;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarDiagnosticos(id_motocicleta,id_componente,fecha_diagnostico,tipo_falla,descripcion,solucion_sugerida): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO diagnosticos values(null,%s,%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (id_motocicleta,id_componente,fecha_diagnostico,tipo_falla,descripcion,solucion_sugerida)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarDiagnosticos(id_motocicleta,id_componente,fecha_diagnostico,tipo_falla,descripcion,solucion_sugerida,id_diagnostico): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE diagnosticos SET diagnosticos.id_motocicleta = %s, diagnosticos.id_componente = %s, diagnosticos.fecha_diagnostico = %s, diagnosticos.tipo_falla = %s, diagnosticos.descripcion = %s, diagnosticos.solucion_sugerida = %s WHERE diagnosticos.id_diagnostico=%s;"
            

            valores = (id_motocicleta,id_componente,fecha_diagnostico,tipo_falla,descripcion,solucion_sugerida,id_diagnostico)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarDiagnosticos(id_diagnostico):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from diagnosticos WHERE diagnosticos.id_diagnostico=%s;"
            
            valores = (id_diagnostico,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()


class CHistorial: 

    def mostrarHistorial():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from historial_mantenimiento;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarHistorial(id_motocicleta,fecha_mantenimiento,tipo_mantenimiento,detalles): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO historial_mantenimiento values(null,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (id_motocicleta,fecha_mantenimiento,tipo_mantenimiento,detalles)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarHistorial(id_motocicleta,fecha_mantenimiento,tipo_mantenimiento,detalles,id_mantenimiento): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE historial_mantenimiento SET historial_mantenimiento.id_motocicleta = %s, historial_mantenimiento.fecha_mantenimiento = %s, historial_mantenimiento.tipo_mantenimiento = %s, historial_mantenimiento.detalles = %s WHERE historial_mantenimiento.id_mantenimiento=%s;"
            

            valores = (id_motocicleta,fecha_mantenimiento,tipo_mantenimiento,detalles,id_mantenimiento)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarHistorial(id_mantenimiento):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from historial_mantenimiento WHERE historial_mantenimiento.id_mantenimiento=%s;"
            
            valores = (id_mantenimiento,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()   

class CModelos: 

    def mostrarModelos():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from modelos;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarModelos(nombre_modelo,descripcion,precio,fecha_lanzamiento): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO modelos values(null,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (nombre_modelo,descripcion,precio,fecha_lanzamiento)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarModelos(nombre_modelo,descripcion,precio,fecha_lanzamiento,id_modelo): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE modelos SET modelos.nombre_modelo = %s, modelos.descripcion = %s, modelos.precio = %s, modelos.fecha_lanzamiento = %s WHERE modelos.id_modelo=%s;"
            

            valores = (nombre_modelo,descripcion,precio,fecha_lanzamiento,id_modelo)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarModelos(id_componente):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from modelos WHERE modelos.id_modelo=%s;"
            
            valores = (id_componente,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()
        
class CVentas: 

    def mostrarVentas():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from ventas;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarVentas(id_modelo,fecha_venta,precio_venta,id_usuario,id_punto_venta): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO ventas values(null,%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (id_modelo,fecha_venta,precio_venta,id_usuario,id_punto_venta)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarVentas(id_modelo,fecha_venta,precio_venta,id_usuario,id_punto_venta,id_venta): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE ventas SET ventas.id_modelo = %s, ventas.fecha_venta = %s, ventas.precio_venta = %s, ventas.id_usuario = %s, ventas.id_punto_venta = %s WHERE ventas.id_venta=%s;"
            

            valores = (id_modelo,fecha_venta,precio_venta,id_usuario,id_punto_venta,id_venta)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarVentas(id_venta):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from ventas WHERE ventas.id_venta=%s;"
            
            valores = (id_venta,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()

class CPunto: 

    def mostrarPunto():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from puntos_venta;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarPunto(nombre_punto,ubicacion,contacto,email): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO puntos_venta values(null,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (nombre_punto,ubicacion,contacto,email)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarPunto(nombre_punto,ubicacion,contacto,email,id_punto_venta): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE puntos_venta SET puntos_venta.nombre_punto_venta = %s, puntos_venta.ubicacion = %s, puntos_venta.contacto = %s, puntos_venta.email = %s WHERE puntos_venta.id_punto_venta=%s;"
            

            valores = (nombre_punto,ubicacion,contacto,email,id_punto_venta)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarPunto(id_punto_venta):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from puntos_venta WHERE puntos_venta.id_punto_venta=%s;"
            
            valores = (id_punto_venta,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()


class CInventario: 

    def mostrarInventario():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from inventario;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarInventario(id_modelo,cantidad,Fecha_entrada,Fecha_salida,estado_producto): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO inventario values(null,%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (id_modelo,cantidad,Fecha_entrada,Fecha_salida,estado_producto)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarInventario(id_modelo,cantidad,Fecha_entrada,Fecha_salida,estado_producto,id_inventario): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE inventario SET inventario.id_modelo = %s, inventario.cantidad_disponible = %s, inventario.fecha_entrada = %s, inventario.fecha_salida = %s, inventario.estado_producto = %s WHERE inventario.id_inventario=%s;"
            

            valores = (id_modelo,cantidad,Fecha_entrada,Fecha_salida,estado_producto,id_inventario)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarInventario(id_inventario):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from inventario WHERE inventario.id_inventario=%s;"
            
            valores = (id_inventario,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()

class CTrabajadores: 

    def mostrarTrabajadores():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from trabajadores;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarTrabajadores(nombre,puesto,Fecha_contracion,Telefono,Email,id_punto_venta): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO trabajadores values(null,%s,%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (nombre,puesto,Fecha_contracion,Telefono,Email,id_punto_venta)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarTrabajadores(nombre,puesto,Fecha_contracion,Telefono,Email,id_punto_venta,id_trabajador): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE trabajadores SET trabajadores.nombre = %s, trabajadores.puesto = %s, trabajadores.fecha_contratacion = %s, trabajadores.telefono = %s, trabajadores.email = %s, trabajadores.id_punto_venta = %s WHERE trabajadores.id_trabajador=%s;"
            

            valores = (nombre,puesto,Fecha_contracion,Telefono,Email,id_punto_venta,id_trabajador)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarTrabajadores(id_trabajador):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from trabajadores WHERE trabajadores.id_trabajador=%s;"
            
            valores = (id_trabajador,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()

class CProveedores: 

    def mostrarProveedores():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from proveedores;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarProveedores(Nombre,Direccion,Telefono,Email): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO proveedores values(null,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (Nombre,Direccion,Telefono,Email)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarProveedores(Nombre,Direccion,Telefono,Email,id_proveedores): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE proveedores SET proveedores.nombre = %s, proveedores.direccion = %s, proveedores.telefono = %s, proveedores.email = %s WHERE proveedores.id_proveedor=%s;"
            

            valores = (Nombre,Direccion,Telefono,Email,id_proveedores)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarProveedores(id_trabajador):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from proveedores WHERE proveedores.id_proveedor=%s;"
            
            valores = (id_trabajador,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()

class CSensores: 

    def mostrarSensores():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from sensores;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarSensores(Nombre,Direccion,Telefono,Email): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO sensores values(null,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (Nombre,Direccion,Telefono,Email)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarSensores(Nombre,Direccion,Telefono,Email,id_sensores): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE sensores SET sensores.id_componente = %s, sensores.tipo = %s, sensores.rango_operacion = %s, sensores.unidad = %s WHERE sensores.id_sensor=%s;"
            

            valores = (Nombre,Direccion,Telefono,Email,id_sensores)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarSensores(id_sensor):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from sensores WHERE sensores.id_sensor=%s;"
            
            valores = (id_sensor,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()

class CM_C: 

    def mostrarM_C():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from motocicleta_componentes;")
            miResultado = cursor.fetchall() #devulce todas las filas 
            cone.commit()
            cone.close()

            return miResultado



        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

   
    def IngresarM_C(id_m,id_c,cantidad): #se ingresa todo menos el id clave primaria
        
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "INSERT INTO motocicleta_componentes values(null,%s,%s,%s);"
            #La variable valores tiene que ser una tupla (tupla es un array que no se puede modificar)
            #Como minima expresion es: (valor,) con la ',' identifica que es una tupla
            #Las tuplas son listas inmutables, es decir, no se pueden modificar 

            valores = (id_m,id_c,cantidad)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            return True
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            return False
        finally:
            cone.close()


    def modificarM_C(id_m,id_c,cantidad,id_mc): #id clave primario al final porque se utiliza un where
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            #se utiliza la sintaxis de sql, por lo que tienen que ser los nombres igual que en sql, no como nombre de variable
            sql = "UPDATE motocicleta_componentes SET motocicleta_componentes.id_motocicleta = %s, motocicleta_componentes.id_componente= %s, motocicleta_componentes.cantidad = %s WHERE motocicleta_componentes.id_motocicleta_componente=%s;"
            

            valores = (id_m,id_c,cantidad,id_mc)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
        
            return True

        except mysql.connector.Error as error:
            print("Error de Actualizacion {}".format(error))
            return False
        finally:
            cone.close()

    def eliminarM_C(id_sensor):
        try:
            cone = CConexion.ConexionBaseDeDatos()

            #la variable ejecuta la funciona
            cursor = cone.cursor()
            sql = "DELETE from motocicleta_componentes WHERE motocicleta_componentes.id_motocicleta_componente=%s;"
            
            valores = (id_sensor,)#coma al final
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            return True

        except mysql.connector.Error as error:
            print("Error de Eliminacion {}".format(error))
            return False
        finally:
            cone.close()

          
    
        
