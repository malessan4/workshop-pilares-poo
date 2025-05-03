#Pilar - Encapsulamiento
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def get_edad(self):
        return self.__edad
    
persona1 = Persona("Ana", 30)
print(persona1.get_nombre())
nuevo_nombre = input("Ingrese el nuevo nombre: ")
persona1.set_nombre(nuevo_nombre)
print(persona1.get_nombre())
print(persona1.get_edad())