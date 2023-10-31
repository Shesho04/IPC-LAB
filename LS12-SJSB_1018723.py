#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Laboratorio)
#Tarea Laboratorio Semana 12
#30 de octubre de 2023
#Objetivo: Crear un programa que administre una lista de contactos.
#Entrada: Nombres, números telefónicos, posiciones. 
#Procesos principales: Con los datos obtenidos, solicitar al usuario que ingrese el nombre del contacto que desea eliminar de la lista, actualizar la lista, ordenarla afabéticamente y colocar los contactos según las posiciones que el usuario indica.
#Salida: Contactos actualizados y ordenados alfabéticamente de forma descendente. Así mismo, debe mostrar la lista original.

contactos = []

cantidad_contactos = int(input("Ingrese la cantidad de contactos que desea ingresar: "))

for i in range(cantidad_contactos):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono del contacto: ")
    contactos.append([nombre, numero])

print("Lista de contactos:")
for contacto in contactos:
    print(contacto)

nombre_eliminar = input("Ingrese el nombre de un contacto existente para eliminarlo: ")

i = 0
while i < len(contactos):
    if contactos[i][0] == nombre_eliminar:
        contactos.pop(i)
    else:
        i += 1

print("Lista de contactos actualizada:")
for contacto in contactos:
    print(contacto)

contactos.sort(key=lambda x: x[0])

print("Lista ordenada alfabéticamente:")
for contacto in contactos:
    print(contacto)

nuevo_contacto = input("Ingrese un nuevo contacto en mayúsculas: ").upper()
nuevo_numero = input("Ingrese el número de teléfono del nuevo contacto: ")
contactos.append([nuevo_contacto, nuevo_numero])

print("Lista de contactos completa después de agregar el nuevo contacto:")
for contacto in contactos:
    print(contacto)

posicion = int(input("Ingrese la posición donde desea guardar el nuevo contacto: "))
nuevo_contacto = input("Ingrese el nombre del nuevo contacto en mayúsculas: ").upper()
nuevo_numero = input("Ingrese el número de teléfono del nuevo contacto: ")
contactos.insert(posicion, [nuevo_contacto, nuevo_numero])

print("Lista de contactos completa después de agregar el nuevo contacto en la posición específica:")
for contacto in contactos:
    print(contacto)

contactos_ordenados = sorted(contactos, key=lambda x: x[0], reverse=True)  # Ordena alfabéticamente de forma descendente según el nombre

print("Lista ordenada alfabéticamente de forma descendente:")
for contacto in contactos_ordenados:
    print(contacto)

print("Lista original de contactos para confirmar que no ha cambiado:")
for contacto in contactos:
    print(contacto)