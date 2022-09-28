class Vehiculo:
    numero_coche = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

        Vehiculo.numero_coche += 1
    
    def __str__(self):
        return f'{self.color},{self.ruedas},{self.puertas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

   
    def __str__(self):
      vehiculo = super().__str__() 
      return f"{vehiculo, self.velocidad, self.cilindrada}"

mazda2 = Coche("Rojo", "4 ruedas", "5 puertas", "175 km/h", "4 cilindros")

print(mazda2)

print(Vehiculo.numero_coche)


