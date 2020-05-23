import csv
from modulo_libro import Libro
from modulo_capitulo import Capitulo

class ManejadordeLibros:
    __libros=[]
    
    def __init__(self):
        self.__libros=[]
        
    def cargarLibros(self):
        archilibros= open("Libros.csv")
        reader= csv.reader(archilibros, delimiter=',')       
        op= 0
        aux= -1
        for fila in reader:
            if op == 0:
                self.__libros.append(Libro(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5])))
                op= int(fila[5])
                aux += 1
            else:
                self.__libros[aux].agregarCapitulo(fila[0], int(fila[1]))
                op -= 1
            
                
    def mostrarLibros(self):
        for i in self.__libros:
            print (i)
            print("\n")
            
            
    def buscarID(self):
        id_a_buscar= int(input("Ingrese ID a buscar: "))
        
        print(f"Título del libro: {self.__libros[id_a_buscar-10001].get_titulo_libro()}")
        print("----------\nCapítulos\n")
        self.__libros[id_a_buscar-10001].listarNombresCapitulos()
        print(f"Cantidad de Páginas: {self.__libros[id_a_buscar-10001].sumarPaginas()}")
        
    def buscarPalabra(self):
        palabra_buscar= input("Ingrese la palabra a buscar: ")
        
        ### EN LIBROS ###
        for i in range(len(self.__libros)):
            res= int(self.__libros[i].buscarPalabraEnLibros(palabra_buscar))
            if (res != -1):
                print(f"{self.__libros[i].get_titulo_libro()}")
        
        ### EN CAPITULOS ###        
        for i in range(len(self.__libros)):
            self.__libros[i].buscarPalabraEnCapitulos(palabra_buscar)

             