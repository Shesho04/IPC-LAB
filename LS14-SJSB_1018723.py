#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Laboratorio)
#Tarea Laboratorio Semana 14
#7 de noviembre de 2023
#Objetivo: Crear un programa que, almacene los datos en una clase y, en base a estos, printee los resultados y los cálculos necesarios.
#Entrada: Modelo, precio, marca, disponibilidad, tipo de dolar, porcentaje descuento aplicado. 
#Procesos principales: Interactuar con el usuario para que ingrese los datos sobre el automóvil, manipular la mediante la clase 'automovil' y presentar en pantalla los datos.
#Salida: Mostrar la información ingresada por el usuarip, incluyendo el cálculo del descuento y la conversión.

class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ''
        self.disponible = True
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self, estado):
        self.disponible = estado

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def Mostrarinformacion(self):
        precioDolar = self.precio / self.tipoCambioDolar
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares $ {precioDolar} . {self.MostrarDisponibilidad()}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        self.precio = self.precio - (self.precio * self.descuentoAplicado)
        self.DefinirPrecio(self.precio)

auto = Automovil()

try:
    auto.DefinirModelo(int(input("Ingrese el modelo del automóvil: ")))
    auto.DefinirPrecio(float(input("Ingrese el precio del automóvil: ")))
    auto.DefinirMarca(input("Ingrese la marca del automóvil: "))
    auto.DefinirTipoCambio(float(input("Ingrese el tipo de cambio en dólares: ")))

    disponible = input("El automóvil está disponible? (Sí/No): ").strip().lower()
    if disponible == 'si':
        auto.CambiarDisponibilidad(False)
    else:
        auto.CambiarDisponibilidad(True)

    print(auto.Mostrarinformacion())

    descuento = float(input("Ingrese el descuento a aplicar (en decimal, por ejemplo, 0.1 para 10%): "))
    auto.AplicarDescuento(descuento)
    print(auto.Mostrarinformacion())
except ValueError:
    print("Error: Ingrese un valor numérico válido para el precio, el tipo de cambio y el descuento.")