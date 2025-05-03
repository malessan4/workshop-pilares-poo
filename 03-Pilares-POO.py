#Pilar - Herencia
class Animal:
	def __init__(self,nombre):
		self.nombre = nombre
	
	def hacer_sonido(self):
		print('Sonido genérico')

class Perro(Animal):
	def hacer_sonido(self):
	    print('Guau!')

mi_animal = Animal('Generico')
mi_animal.hacer_sonido()
print()
mi_perro = Perro('Fido')
print(mi_perro.nombre)
mi_perro.hacer_sonido()
