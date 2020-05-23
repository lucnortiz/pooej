from modulo_maneja_libro import ManejadordeLibros
from modulo_capitulo import Capitulo
from menu import Menu

if __name__ == '__main__':
    
    libro= ManejadordeLibros()
    libro.cargarLibros()
    
    menu = Menu()
    salir = False
    
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n0. Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, libro)
        salir = op == 0