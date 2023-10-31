#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Laboratorio)
#Tarea Laboratorio Semana 13
#31 de octubre de 2023
#Objetivo: Crear un programa que, a través de clases, permita almacacenar datos.
#Entrada: Nombres, apellidos, apellido de casada, fecha de nacimiento. 
#Procesos principales: 
#Salida: Contactos actualizados y ordenados alfabéticamente de forma descendente. Así mismo, debe mostrar la lista original.

class Persona:
    def __init__(self, nombres, apellidos, apellido_casada, fecha_nacimiento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.apellido_casada = apellido_casada
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombre_completo(self):
        nombre_completo = self.nombres + " " + self.apellidos
        if self.apellido_casada:
            nombre_completo += " de " + self.apellido_casada
        return nombre_completo

    def calcular_edad(self):
        import datetime
        fecha_actual = datetime.date.today()
        fecha_nacimiento = datetime.datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y").date()
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad

nombres = input("Ingrese los nombres: ")
apellidos = input("Ingrese los apellidos: ")
apellido_casada = input("Ingrese el apellido de casada (o presione Enter si no aplica): ")
fecha_nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/YYYY): ")

persona1 = Persona(nombres, apellidos, apellido_casada, fecha_nacimiento)

print("Nombres: ", persona1.nombres)
print("Apellidos: ", persona1.apellidos)
if persona1.apellido_casada:
    print("Apellido de casada: de", persona1.apellido_casada)
print("Fecha de nacimiento: ", persona1.fecha_nacimiento)
print("Edad: ", persona1.calcular_edad())
print("Nombre completo: ", persona1.obtener_nombre_completo())
