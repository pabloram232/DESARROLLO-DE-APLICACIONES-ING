"""Conversion de grados"""
"Juan Pablo Ramirez"
def grados():

    print('1.- fahrenheit a Celsius')
    print('2.- Celsius a fahrenheit')
    opc= int(input('Selecciona una opcion: '))
    
    if opc == 2:
        grd=int(input('Grados: '))
        conv = grd*9/5+32
        return print(grd, ' grados Celsius equivalen a ', conv,  ' grados fahrenheit')
    elif opc == 1:
        grd=int(input('Grados: '))
        conv = (grd-32)*5/9
        return print(grd, ' grados fahrenheit equivalen a', conv, ' grados Celcius')
        

