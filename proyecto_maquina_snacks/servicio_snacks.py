import os.path
from snacks import Snack 

class Servicio_snacks:

    Nombre_archivo = 'snacks.txt'

    def __init__(self):
        self.snacks = []
        
        # Revisar si existe el archivo. Si existe, obtenemos los snacks; si no, añadimos algunos snacks
        if os.path.isfile(self.Nombre_archivo):
            self.snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Papas', 70),
            Snack('Refresco', 58),
            Snack('Sandwich', 120)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.Nombre_archivo, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print('Error al guardar snacks en archivo: {e}')

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.Nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    _, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre , float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f'Error al leer el archivo de snacks: {e}')
        return snacks

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print('--- Snacks en inventario ---')
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks