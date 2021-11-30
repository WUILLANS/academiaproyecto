import psycopg2
import sys

class ClsUsuario():
    DniUsuario = ""
    NomUsuario = ""
    ApeUsuario = ""
    NomAcceso = ""
    ClaAcceso = ""

    def ValidarUsuario(self,NombreUsuario,ClaveUsuario):
        try:
            conexion = psycopg2.connect(host="localhost", database="academia", user="postgres", password="HONORIO")
            instruccion = conexion.cursor()
            instruccion.execute("Select count(*) from \"Usuarios\" where \"NomAcceso\"='"+NombreUsuario+"' and \"ClaAcceso\"='"+ClaveUsuario+"'")
            fila = instruccion.fetchone()
            if fila[0]==1:
                return True
            else:
                return False
        except:
            print("Error de conexión")

    def registrarUsuario(self, datosusuarios):
        try:

            conexion = psycopg2.connect(host="localhost", database="academia", user="postgres", password="HONORIO")
            instruccion = conexion.cursor()
            print("lugar1")
            query="INSERT INTO public.\"Usuarios\"(\"DniUsuario\", \"APaUsuario\", \"AMaUsuario\", \"NomUsuario\", \"ClaAcceso\", \"NomAcceso\") VALUES (%s, %s, %s, %s, %s, %s);"
            print(query)
            data=(datosusuarios["DniUsuario"],datosusuarios["APaUsuario"],datosusuarios["AMaUsuario"],datosusuarios["NomUsuario"],datosusuarios["ClaAcceso"],datosusuarios["NomAcceso"])
            print(data)
            instruccion.execute(query,data)
            conexion.commit()
            return True
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])
            return False


    def borrarUsuario(self, dniusuarios):
        try:

            conexion = psycopg2.connect(host="localhost", database="academia", user="postgres", password="HONORIO")
            instruccion = conexion.cursor()
            print("lugar1")
            query="DELETE FROM public.\"Usuarios\" WHERE  \"DniUsuario\" ='"+dniusuarios+"';"
            print(query)
            instruccion.execute(query)
            conexion.commit()
            return True
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])
            return False


