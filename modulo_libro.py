from modulo_capitulo import Capitulo

class Libro:
    __idLibro= 0
    __titulo= ''
    __autor= ''
    __editorial= ''
    __isbn= 0
    __cantidadCapitulos= 0
    __capitulo= []
    
    def __init__(self,idLibro,titulo,autor,editorial,isbn,cantidadCapitulos):
        self.__idLibro= idLibro
        self.__titulo= titulo
        self.__autor= autor
        self.__editorial= editorial
        self.__isbn= isbn
        self.__cantidadCapitulos= cantidadCapitulos
        
        self.__capitulo= []
    
    def __str__(self):
        cadenaLibro = 'ID Libro: ' + str(self.__idLibro)
        cadenaLibro += '\nTitulo: ' + self.__titulo
        cadenaLibro += '\nAutor: ' + self.__autor
        cadenaLibro += '\nEditorial: ' + self.__editorial
        cadenaLibro += '\nISBN: ' + str(self.__isbn)
        cadenaLibro += '\ncantidadCapitulos: ' + str(self.__cantidadCapitulos)
        return (cadenaLibro)

    def agregarCapitulo(self,titulo_cap,cant_pag_cap):
        self.__capitulo.append(Capitulo(titulo_cap,cant_pag_cap))

    def cantidadPaginasLibro(self):
        cont_paginas= 0
        for i in range(len(self.__capitulos)):
            cont_paginas += self.__capitulo[i].getCantPag()
            
        return int(cont_paginas)
    
    def getID(self):
        return int(self.__idLibro)
    
    def get_titulo_libro(self):
        return str(self.__titulo)
    
    def listarNombresCapitulos(self):
        for i in range(self.__cantidadCapitulos):
            print (f"Titulo Capitulo {i+1}: {self.__capitulo[i].getTitulo()}")
    
    def sumarPaginas(self):
        totalPaginas= 0
        for i in range(self.__cantidadCapitulos):
            totalPaginas += self.__capitulo[i].getCantPag()
        
        return totalPaginas
    
    def buscarPalabraEnLibros(self,p):
        return self.__titulo.find(p)
        
    def buscarPalabraEnCapitulos(self,p):
        for i in range(self.__cantidadCapitulos):
            if (self.__capitulo[i].getTitulo().find(p) != -1):
                print(f"{self.__capitulo[i].getTitulo()}")
                
        
        
        
        
        