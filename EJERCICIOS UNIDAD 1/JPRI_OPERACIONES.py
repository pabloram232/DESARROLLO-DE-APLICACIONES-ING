"""Operaciones"""
"Juan Pablo Ramirez"

print('1= suma')
print('2= resta')
print('3= multiplicacion')
print('4= division')
opcion= int(input('elije una opcion: '))



if opcion == 1:
    num1= int(input("Ingresa el primer numero: "))
    num2= int(input("Ingresa el segundo numero: "))

    print("El resultado es: ",num1+num2)

if opcion ==  2:
    num1= int(input("Ingresa el primer numero: "))
    num2= int(input("Ingresa el segundo numero: "))
    print("El resultado es: ",num1-num2)

if opcion ==  3:
    num1= int(input("Ingresa el primer numero: "))
    num2= int(input("Ingresa el segundo numero: "))
    print("El resultado es: ",num1*num2)

if opcion == 4:
    num1= int(input("Ingresa el primer numero: "))
    num2= int(input("Ingresa el segundo numero: "))
    print("El resultado es: ",num1/num2)
