#aqui montare lo nuevo que hice del main"

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"

persona1 = Persona("Juan")
print(persona1.saludar())
