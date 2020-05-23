class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            0:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, libro):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(libro)
        
    def salir(self,libro):
        print('Salir')
        
    def opcion1(self, libro):
        libro.buscarID()

    def opcion2(self, libro):
        libro.buscarPalabra()
