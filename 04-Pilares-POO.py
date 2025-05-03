# Pilar - Polimorfismo

class Animal:
	def __init__(self,nombre):
		self.nombre = nombre
	
	def hacer_sonido(self):
		print('Sonido genérico')

class Perro(Animal):
	def hacer_sonido(self):
	    print('Guau!')

class Gato(Animal):
	def hacer_sonido(self):
		print('Miau')

def escuchar_sonido(animal):
	animal.hacer_sonido()

mis_animales = [Perro('Fido'), Gato('Michi'), Animal('Generico')]
for animal in mis_animales:
	escuchar_sonido(animal)
