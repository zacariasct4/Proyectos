
class Snack:
    contador_snack = 0 # variable de clase para que lo tengan todas las variables creadas a partir de la clase

    def __init__(self, nombre= '', precio = 0.0):
        Snack.contador_snack += 1
        self.id_snack = Snack.contador_snack
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return (f'Snack: id_snack = {self.id_snack}, nombre = {self.nombre}, precio = {self.precio}')
    
    def escribir_snack(self):
        return f'{self.id_snack}, {self.nombre}, {self.precio}'