#Sergio José Santizo Barraza - 1018723
#Sección: 17
#Trabajo Supervisado de Introducción a la Programación
#Ejercicio del Uso de variables en Python (semana 7)
#21 de septiembre de 2023

#Objetivo: Realizar un programa que solicite al usuario un número en el rango de 1 a 10 y verificar que este esté correcto. Al finalizar, preguntar al usuario si desea generar la tabla de otro número y, por último, permitir que el usuario seleccione la opción salir.
#Entrada: Número de 1 a 10.
#Procesos principales
#Salida: Mostrar en la pantalla la tabla de multiplicar del número indicado por el usuario.

#Ingresar el nombre completo.
print("Mi nombre completo es Sergio José Santizo Barraza")

while True:
    # Solicitar al usuario un número en el rango de 1 a 10
    numero = int(input("Ingrese un número entre 1 y 10: "))
    
    # Verificar que el número esté en el rango correcto
    if 1 <= numero <= 10:
        # Utilizar la instrucción for para mostrar la tabla de multiplicar
        for x in range(1, 11):
            resultado = numero * x
            print(f"{numero} X {x} = {resultado}")
        
        # Preguntar al usuario si desea generar la tabla de otro número
        respuesta = input("¿Desea generar la tabla de otro número? (Salir): ").upper()
        if respuesta == "Salir":
            break
    else:
        print("El número no está en el rango correcto.")