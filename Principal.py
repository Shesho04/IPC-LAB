#Sergio José Santizo Barraza - 1018723
#Sección: 17
#Introducción a la Programación
#10 de octubre de 2023
#Objetivo: Invocar el módulo para convertir de una medida de longitud a otra.
#Entrada: Cantidad de una medida de longitud.
#Procesos principales: Haciendo uso de los módulos de conversión, convertir de una medida de longitud a otra.
#Salida: Cantidad en la medida de longitud convertida.

#Importar el código fuente del módulo indicado
import conversiones

while True:
    #Solicitar al usuario la cantidad a convertir
    cm = float(input("Ingrese la cantidad de cm que desee convertir o ingrese 0 para salir): "))
    
    #Identificar si el usuario desea salir
    if cm == 0:
        break

    #Mostrar el menú de opciones
    print("Elija la unidad a la que desea convertir:")
    print("1. Metros")
    print("2. Kilómetros")
    print("3. Pulgadas")
    print("4. Pies")

    opcion = int(input("Ingrese el número de la unidad: "))

    #Realizar la conversión y mostrar el resultado en pantalla
    if opcion == 1:
        metros = round(conversiones.cmAm(cm), 2)
        print(f"{cm} centímetros equivale a {metros} metros.")
    elif opcion == 2:
        kilometros = round(conversiones.cmAkm(cm), 2)
        print(f"{cm} centímetros equivale a {kilometros} kilómetros.")
    elif opcion == 3:
        pulgadas = round(conversiones.cmAin(cm), 2)
        print(f"{cm} centímetros equivale a {pulgadas} pulgadas.")
    elif opcion == 4:
        pies = round(conversiones.cmAft(cm), 2)
        print(f"{cm} centímetros equivale a {pies} pies.")
    else:
        print("Elija una opción válida.")

print("¡Bye, bye :)!")