"""  FUNCION CON MENSAJE DE VIENVENIDA SI LOS DATOS INGRESADOS SON CORRECTOS"""
"JUAN PABLO RAMIREZ IBARRA"""

def login():
    usuario=input('Usuario: ')
    contraseña=input('Contraseña: ')

    if usuario == 'utng' and contraseña == 'mexico' :
        print('***** BIENVENIDO *****')
