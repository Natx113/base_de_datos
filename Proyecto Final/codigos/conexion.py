import mysql.connector 

class CConexion:#clase conexion
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user="root",
                                               password="admin",
                                               host="127.0.0.1",
                                               database="diagnosticador_multisensorial",
                                               port="3306")
            
            print("Conexion Establecida")

            return conexion #dvuelce mi variable conexion para abrir o cerrar conexion para realizar mis consultas
        



        except mysql.connector.Error as error:
            print("Error al conectarte a la base de daots {}".format(error))
            return conexion

    ConexionBaseDeDatos()