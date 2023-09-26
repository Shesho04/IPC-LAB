#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Laboratorio)
#Ejercicio 1 (laboratorio semana 8)
#26 de septiembre de 2023

#Objetivo: Realizar un programa que muestre un menú para que el usuario, al ingresar un número, ejecute la opción que desee. Además, se debe finalizar el programa cuando el usuario lo solicite.
#Entrada: Número de 1 al 3 y los números ingresados por el usuario para llevar a cabo el cálculo.
#Procesos principales: Tomar un número e incrementar de uno en uno.
#Salida: Mostrar en pantalla la opción solicitada por el usuario, así como el resultado del número ingresado.

# Función para calcular el factorial de un número
def calcular_factorial(numero):
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Función para generar la secuencia de Fibonacci hasta la posición n
def generar_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence

while True:
    #Mostrar el menú al usuario.
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    # Solicitar al usuario que seleccione una opción.
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        #Ejecutar la opción para calcular el factorial de un número.
        numero = int(input("Ingrese un número para calcular su factorial: "))
        factorial = calcular_factorial(numero)
        print(f"{numero} = {numero} * ... * 2 * 1")
        print(f"{numero}! = {factorial}")
    elif opcion == '2':
        #Ejecutar la opción para generar la secuencia de Fibonacci.
        numero = int(input("Ingrese un número para generar la secuencia de Fibonacci: "))
        fibonacci_sequence = generar_fibonacci(numero)
        print(", ".join(map(str, fibonacci_sequence)))
    elif opcion == '3':
        #Ejecutar la opción para salir del programa.
        print("¡Bye, bye :)!")
        break
    else:
        # Opción no válida.
        print("La opción ingresada no es válida. Por favor, seleccione una opción válida")
