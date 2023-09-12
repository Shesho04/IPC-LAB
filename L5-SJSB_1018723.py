#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Laboratorio)
#Ejercicio 1 (laboratorio semana 6)
#12 de septiembre de 2023

#Objetivo: Dado un número entero, como dato, determinar si el mismo es positivo, negativo o cero.
#Entrada: Número entero.
#Procesos principales

#Solicitar un número entero al usuario
print("Ejercicio 1")
Número = int(input("Ingresar un número entero"))

#Evaluar si el dato es positivo, negativo o cero.
if Número > 0:
    print("El número ingresado es positivo")
elif Número < 0:
    print("El número ingresado es un negativo")
else:
    print("El número ingresado es cero")