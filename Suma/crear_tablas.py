"""JUAN PABLO RAMIREZ IBARRA
GITI9072-E

CREAR TABLA PARA GUARDAR EL TOTAL DE LA SUMA DE DOS NUMEROS"""
import psycopg2

#This function do the connection into Python and postrgeSQL
def crear_tablas():
    # The script create the Table 'Resultado' in the Database 'UNIDAD_III'
    comandos = ("CREATE TABLE Resultado("
                "id SERIAL PRIMARY KEY,"
                "numero1 FLOAT NOT NULL,"
                "numero2 FLOAT NOT NULL,"
                "total VARCHAR NOT NULL)")

    conexion = None
    #Here we are going the insert the params for the connection with postgreSQL
    try:
        configuracionDB = {'host': 'localhost',
                              'user':'postgres',
                              'password':'2414',
                              'database':'UNIDAD_III',}
        conexion = psycopg2.connect(**configuracionDB)
        #Here we create the cursor for execute the commands of the Database
        cursor = conexion.cursor()
        cursor.execute(comandos)
        #Here we close the cursor
        cursor.close()
        conexion.commit()
    #Here is created the error of the Database if the params are not good
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    #Here we close the connection with the Database
    finally:
        if conexion is not None:
            conexion.close()


if __name__ == '__main__':
    crear_tablas()

