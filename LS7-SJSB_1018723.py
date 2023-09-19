#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Laboratorio)
#Ejercicio 1 "Operaciones aritméticas"
#19 de septiembre de 2023

#Objetivo: Realzar un programa que solicite al usuario dos números y realice las operaciones básicas aritméticas y que muestre el resultado en pantalla.
#Entrada: Dos números enteros.
#Procesos principales
#Salida: Resultado de las operaciones básicas aritméticas.

#Solicitar al usuario que ingrese dos números enteros.
print("Ingrese el primer número: ")
n1 = float(input())
print("Ingrese el segundo número: ")
n2 = float(input())

#Operaciones y resultados
Suma = n1 + n2
Resta = n1 - n2
Multiplicación = n1 * n2
División = n1 / n2
Módulo = n1 % n2
Exponenciación = n1 ** n2
Cociente = n1 // n2

#Mostrar resultados
print("la suma es: {:.2f}".format(Suma))
print("la resta es: {:.2f}".format(Resta))
print("la multiplicación es: {:.2f}".format(Multiplicación))
print("la división es: {:.2f}".format(División))
print("el módulo es: {:.2f}".format(Módulo))
print("la exponenciación es: {:.2f}".format(Exponenciación))
print("el cociente es: {:.2f}".format(Cociente))