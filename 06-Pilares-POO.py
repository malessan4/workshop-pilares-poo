"""

Ejercicio: 
Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas. 
Cada clase hija debe tener un método propio sobrescrito que imprima información 
diferente. Crea una función que reciba un vehículo y llame a ese método.


"""

class Vehiculo:
    def __init__(self, ruedas, velocidad_maxima, color):
        self.ruedas = ruedas
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        
    def acelerar(self):
        print(f"El vehiculo de color {self.color} con {self.ruedas} ruedas esta acelerando y llego a una velocidad maxima de: {self.velocidad_maxima} Km/h")


    def probar_aceleracion(vehiculo):
        vehiculo.acelerar()     

class Moto(Vehiculo):
    def acelerar(self):
        print(f"La moto de color {self.color} con {self.ruedas} ruedas esta acelerando y llego a una velocidad maxima de {self.velocidad_maxima} Km/h ")
        
class Auto(Vehiculo):
    def acelerar(self):
        print(f"El auto de color {self.color} con {self.ruedas} ruedas esta acelerando y llego a una velocidad maxima de {self.velocidad_maxima} Km/h")

       
moto1 = Moto(2, 80, "Roja")
vehiculo1 = Vehiculo(8, 140, "Negro")
auto1 = Auto(4, 120, "Azul")

moto1.probar_aceleracion()
vehiculo1.probar_aceleracion()
auto1.probar_aceleracion()