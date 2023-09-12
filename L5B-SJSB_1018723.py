#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Laboratorio)
#Ejercicio 2 (laboratorio semana 6)
#12 de septiembre de 2023

#Objetivo: Realzar un programa que indique el día de la semana correspondiente al número ingresado.
#Entrada: Número de 1 al 7.
#Procesos principales
#Mostrar el día de la semana, en base al número ingresado por el usuario.

#Solicitar al usuario que ingrese un número de día.
print("Ejercicio 2")
Número = int(input("Ingresar un número del 1 al 7: "))

#Evaluar si el dato entra en el rango definido.
if Número <= 0 or Número > 7:
    print("Error. El número a ingresar debe estar contenido entre 1 y 7")

#Determinar el día de la semana.
elif Número == 1:
    print("Lunes")
elif Número == 2:
    print("Martes")
elif Número == 3:
    print("Miércoles")
elif Número == 4:
    print("Jueves")
elif Número == 5:
    print("Viernes")
elif Número == 6:
    print("Sábado")
elif Número == 7:
    print("Domingo")