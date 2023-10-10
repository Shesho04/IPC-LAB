#Sergio José Santizo Barraza - 1018723
#Sección: 17
#Introducción a la Programación
#10 de octubre de 2023
#Objetivo: Crear funciones para convertir de una medida de longitud a otra.
#Entrada: Cantidad de una medida de longitud.
#Procesos principales: Por medio de la tasa de conversión, convertir de una medida a otra.
#Salida: Cantidad en la medida de longitud convertida.

#Conversión de cm a m
def cmAm(cm):
    total = (cm)/100
    return total

#Conversión de cm a km
def cmAkm(cm):
    total = (cm)/100000
    return total

#Conversión de cm a in
def cmAin(cm):
    total = (cm)/2.54
    return total

#Conversión de cm a ft
def cmAft(cm):
    total = (cm)/30.48
    return total