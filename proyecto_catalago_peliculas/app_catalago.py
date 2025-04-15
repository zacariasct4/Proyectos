from servicio_peliculas import Servicio_Peliculas
from pelicula import Pelicula
class App_catalago:

    def __init__(self):
        self.servicio_peliculas = Servicio_Peliculas()

    def mostrar_menu(self):
        print('*** App catálogo películas')

        while True: 
            try:
                print(f'''Menu
                      1. Agregar película
                      2. Listar películas
                      3. Eliminar catálogo de películas
                      4. Salir''')
                opcion = int(input('Elige tu opción: '))

                if opcion == 1:
                    nombre_pelicula = input('Dame el nombre de la película: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2: 
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('Salimos del programa')
                    break
                else:
                    print('Opción inválida')
            
            except ValueError:
                print('Error: Introduce un número válido')
            except Exception as e:
                print('Error tipo ' + e)

if __name__ == '__main__':
    app = App_catalago()
    app.mostrar_menu()
    

    