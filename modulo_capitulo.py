class Capitulo:
    __titulo= ''
    __cantidadPaginas= 0
    
    def __init__(self,titulo,cantidadPaginas):
        self.__titulo= titulo
        self.__cantidadPaginas= cantidadPaginas

    def __str__(self):
        cadenaCap= (f"Nombre Cap: {self.__titulo},Cantidad Pag: {self.__cantidadPaginas}")
        return cadenaCap
    
    def getTitulo(self):
        return self.__titulo
    
    def getCantPag(self):
        return int(self.__cantidadPaginas)