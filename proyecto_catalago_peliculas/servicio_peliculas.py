import os

class Servicio_Peliculas():

    def __init__(self):
        self.Nombre_archivo = 'catalago_peliculas.txt'

    def agregar_pelicula(self, pelicula):
        
        with open(self.Nombre_archivo, 'a', encoding='utf8') as archivo:
                archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
         with open(self.Nombre_archivo, 'r', encoding='utf8') as archivo:
              print('--- Listado de Películas')
              print(archivo.read())

    def eliminar_archivo_peliculas(self):
         os.remove(self.Nombre_archivo)
         print(f'Archivo {self.Nombre_archivo} eliminado')


        