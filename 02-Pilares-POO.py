# Pilar - Abstracción
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"{self.marca} {self.modelo} esta acelerando")


mi_coche = Coche("Fiat", "Mobi")
mi_coche.acelerar()