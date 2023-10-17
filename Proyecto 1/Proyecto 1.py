#Sergio José Santizo Barraza - 1018723 y Diego Ignacio Sánchez López - 1249123
#Introducción a la Programación (Laboratorio)
#Proyecto No. 1 (Aserradero)
#16 de octubre de 2023
#Objetivo: Crear un programa que solicite al usuario determinados datos en dos líneas de producción y, al finalizar, compare la eficiencia de ambas.
#Entrada: Cantidad de metros cuadrados vendidos al mes, precio de venta por metro cuadrado, cantidad de empleados, cantidad de horas trabajadas y costo por hora de trabajo. 
#Procesos principales: Con los datos recabados, realizar cálculos para obtener los valores deseados.
#Salida: Ganancia total, costo total, ganancia neta, índice de eficiencia y mensaje de qué línea de producción es más eficiente.

#Título de la programación
print("Línea de producción")

#Definir la clase Producción
class Produccion:
    def __init__(self):
        #Inicializar en 0 cada variable
        self.precio_por_metro2 = 0
        self.metros_vendidos = 0
        self.empleados = []

    def ingresar_datos(self):
        #Solicitar al usuario ingresar datos importantes de la producción
        self.metros_vendidos = self.obtener_float("Indique la cantidad de metros cuadrados vendidos al mes: ")
        self.precio_por_metro2 = self.obtener_float("Indique el precio de venta por metro cuadrado: ")

        #Condicionar al usuario a ingresar un númerode empleados máximo de 20 por línea
        while True:
            num_empleados = self.obtener_entero("Cantidad de empleados por línea: ")
            if num_empleados <= 20:
                break
            else:
                print("La cantidad máxima de empleados es 20. Ingrese un número igual o menor a 20.")

        for i in range(num_empleados):
            empleado = self.ingresar_empleado(i + 1)
            self.empleados.append(empleado)

    def ingresar_empleado(self, numero_empleado):
        #Solicitar al usuario ingresar datos de los empleados
        print(f"Empleado", numero_empleado)
        horas_trabajadas = self.obtener_float("Indique la cantidad de horas trabajadas: ")
        costo_por_hora = self.obtener_float("Indique el costo por hora de trabajo: ")
        return (horas_trabajadas, costo_por_hora)

    def calcular_ganancias(self):
        #Calcular los valores solicitados
        ganancia_total = self.precio_por_metro2 * self.metros_vendidos
        costo_total = sum(horas * precio_hora for horas, precio_hora in self.empleados)
        ganancia_neta = ganancia_total - costo_total
        num_empleados = len(self.empleados)
        return ganancia_total, costo_total, ganancia_neta, num_empleados

    def obtener_entero(self, mensaje):
        #Verificación de datos, cuando es de tipo entero
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Debe ingresar un número entero válido.")

    def obtener_float(self, mensaje):
        #Verificación de datos, cuando es de tipo float
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Debe ingresar un número válido.")

#Inicio de la línea de producción 1
print("Línea de producción 1:")
linea1 = Produccion()
linea1.ingresar_datos()
ganancia_total1, costo_total1, ganancia_neta1, num_empleados1 = linea1.calcular_ganancias()

#Inicio de la línea de producción 2
print("\nLínea de producción 2:")
linea2 = Produccion()
linea2.ingresar_datos()
ganancia_total2, costo_total2, ganancia_neta2, num_empleados2 = linea2.calcular_ganancias()

#Cálculo del índice de eficiencia para la línea 1 y 2
indice_eficiencia1 = ganancia_neta1 / num_empleados1
indice_eficiencia2 = ganancia_neta2 / num_empleados2

#Mostrar en pantalla los resultados de la línea 1
print("\nResultados línea 1:")
print(f"Ganancia total de la línea 1: {ganancia_total1}")
print(f"Costo total de la línea 1 : ({' + '.join([f'{horas} * {precio_hora}' for horas, precio_hora in linea1.empleados])}) = {costo_total1}")
print(f"Ganancia neta de la línea 1: {ganancia_neta1}")
print(f"Índice de eficiencia de la línea 1: {indice_eficiencia1}")

#Mostrar en pantalla los resultados de la línea 2
print("\nResultados línea 2:")
print(f"Ganancia total de la línea 2: {ganancia_total2}")
print(f"Costo total de la línea 2 : ({' + '.join([f'{horas} * {precio_hora}' for horas, precio_hora in linea2.empleados])}) = {costo_total2}")
print(f"Ganancia neta de la línea 2: {ganancia_neta2}")
print(f"Índice de eficiencia de la línea 2: {indice_eficiencia2}")

#Comparación de índices de eficiencia y mensaje
if indice_eficiencia1 > indice_eficiencia2:
    print("La línea de producción 1 tuvo un mayor índice de eficiencia.")
elif indice_eficiencia2 > indice_eficiencia1:
    print("La línea de producción 2 tuvo un mayor índice de eficiencia.")
else:
    print("Ambas líneas de producción tuvieron el mismo índice de eficiencia.")