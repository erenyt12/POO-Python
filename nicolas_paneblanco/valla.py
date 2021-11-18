"""
    Modelar: una valla

        atributos: 
            - estado por defecto esta levantada

        puede:
            - ver su estado
            - cambiar su estado
"""

class Valla(object):
    """ 
        Clase Valla
        
        Metodos:
            ✅ alta: devuelve True si la valla se encuentra arriba
            ✅ cambiarEstado: invierte el estado de la valla.
    """
    
    def __init__(self) -> None:
        self.__alta = True
        
    @property
    def alta(self): return self.__alta
    
    def cambiarEstado(self) -> None:
        """ Invierte el estado de la valla """
        self.__alta = not self.alta
        

if __name__ == '__main__':
    pass