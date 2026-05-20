# Clase base
class Animal:
    def __init__(self, nombre, edad):  # Corregido: doble guion bajo
        self.nombre = nombre          # Atributo público
        self.__edad = edad            # Atributo privado (encapsulamiento)

    def hacer_sonido(self):
        return "Sonido genérico"

    def get_edad(self):              # Método para acceder al atributo privado
        return self.__edad


# Clase hija (Herencia)
class Perro(Animal):
    def hacer_sonido(self):          # Polimorfismo (sobrescritura)
        return "Guau 🐶"


# Otra clase hija
class Gato(Animal):
    def hacer_sonido(self):          # Polimorfismo (sobrescritura)
        return "Miau 🐱"


# Función que usa polimorfismo
def escuchar_animal(animal):
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")


# Programa principal
if __name__ == "__main__":
    # Instanciación de objetos
    perro = Perro("Firulais", 3)
    gato = Gato("Michi", 2)

    # Uso de polimorfismo
    escuchar_animal(perro)
    escuchar_animal(gato)

    # Acceso a través de getter
    print(f"Edad de {perro.nombre}: {perro.get_edad()} años")