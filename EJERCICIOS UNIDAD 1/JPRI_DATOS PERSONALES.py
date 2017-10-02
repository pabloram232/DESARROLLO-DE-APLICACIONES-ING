""" INSERCCION DE DATOS A DICCIONARIO"""
"""JUAN PABLO RAMIREZ IBARRA"""

import pprint
def datos_persona():
    
    nom = input("Nombre ")
    tel = input("Telefono ")
    edad = input("Edad ")
    cor = input("Correo ")
    cp = input("Codigo postal ")
    
    datos = {'Nombre':nom,'Telefono':tel,'Edad':edad,'Correo':cor,'Codigo postal':cp}
    pprint.pprint (datos)
