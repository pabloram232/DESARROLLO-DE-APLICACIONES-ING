""" SABER SI SE PUEDE ENTRAR AL CINE SEGUN LA EDAD Y LA CLASIFICACION"""
"""JUAN PABLO RAMIREZ IBARRA"""
def entra_cine(clasificacion, edad):
    
        if clasificacion == 'AA' :
            print('Entra')
        if clasificacion == 'A' and edad >= 1 :
            print('Entra')
        if clasificacion == 'A' and edad < 1 :
            print('No entra')
        if clasificacion == 'B' and edad < 12 :
            print('No entra')
        if clasificacion == 'B' and edad >= 12 :
            print('Entra')
        if clasificacion == 'B15' and edad >= 15 :
            print('Entra')
        if clasificacion == 'B15' and edad < 15 :
            print('Entra con supervisión')
        if clasificacion == 'C' and edad >= 18 :
            print('Entra')
        if clasificacion == 'C' and edad < 18 :
            print('No entra')
        if clasificacion == 'D' and edad >= 25 :
            print('sOLO PARA ADULTOS ENTRE')
