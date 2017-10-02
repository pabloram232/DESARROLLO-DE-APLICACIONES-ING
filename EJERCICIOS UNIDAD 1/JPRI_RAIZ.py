"""Calcular​ ​raiz​ ​cuadrada​ ​de​ ​un​ ​lista​ ​de​ ​10​ ​digitos​ ​tecleados​ ​por​ ​el​ ​usuario."""
"Juan Pablo Ramirez"

import math
def raiz():

    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    c = int(input("Tercer numero: "))
    d = int(input("Cuarto numero: "))
    e = int(input("Quinto numero: "))
    f = int(input("Sexto numero: "))
    g = int(input("Septimo numero: "))
    h = int(input("Octavo numero: "))
    i = int(input("Noveno numero: "))
    j = int(input("Decimo numero: "))

    sumar= (a+b+c+d+e+f+g+h+i+j)
    raiz=math.sqrt(sumar)
    return raiz
