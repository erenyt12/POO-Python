"""
    Modelar: un auto 

        atributos: 
            - una velocidad, al iniciar esta parado

        puede:
            - puede ver su velocidad
            - puede acelerar una determinada velocidad
            - puede detenerse 
            - pude saber si esta en movimiento
"""

class Auto(object):
    """ 
        Clase Auto
        
        Metodos:
            ✅ velocidad: representa la velocidad que tiene el auto.
            ✅ acelerar: se puede acelerar el auto.
            ✅ detenerse: detiene el auto a 0km/h.
            ✅ estaEnMovimiento?: responde si el vehiculo se encuentra en movimiento.
    """
    def __init__(self) -> None:
        self.__velocidad = 0
        
    @property
    def velocidad(self): return self.__velocidad
    
    def acelerar(self, una_velocidad: int) -> None: 
        """ Acelera el vehicula la velocidad especificada """
        self.__velocidad += una_velocidad
        
    def detenerse(self) -> None:
        """ Detiene el vehiculo """
        self.__velocidad = 0
        
    def estaEnMovimiento(self) -> bool:
        """ Estara en movimiento si su velocidad es mayor a 0 """
        return self.velocidad > 0
        
        
    
if __name__ == '__main__':
    pass