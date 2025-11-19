class carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        return f"{self.anio} {self.marca} {self.modelo}"
    
class motor:
    def __init__(self, tipo, caballos_de_fuerza):
        self.tipo = tipo
        self.caballos_de_fuerza = caballos_de_fuerza

    def mostrar_detalles(self):
        return f"Motor: {self.tipo}, Caballos de fuerza: {self.caballos_de_fuerza}"

carro1 = carro("Toyota", "Corolla")
carro1.anio = 2020
print(carro1.mostrar_informacion())
motor1 = motor("Gasolina", 132)
print(motor1.mostrar_detalles())