"""
    Ejercicio 1:
        Modelar el objeto caja de ahorro:
            - un titular
            - un saldo
        
        y debera poder:
            - depositar un monto
            - puedeExtraer un monto
            - extraer un monto
            - en el caso de querer extraer un monto superior 
              al monto disponible arrojara una 
              excepcion ValueError("Imposible realizar extracción.")

        Realizar los test necesarios que validen 
        el comportamiento.  
"""
"""
    Ejercicio 7:
        Extender la clase CajaDeAhorro para que:
            - Tenga una cantidad de extracciones fijas. 
            - Pueda restaurar la cantidad de extracciones. 
"""

class CajaDeAhorro(object):
    """ 
        Clase CajaDeAhorro
    """
    def __init__(self, titular: str, saldo: int, extracciones_posibles: int) -> None:  
        self.__titular = titular
        self.__saldo = saldo  
        self.__extraccionesPosible = extracciones_posibles
        self.__extracionesRealizadas = 0


    @property
    def titular(self): return self.__titular
    
    @property
    def saldo(self): return self.__saldo 

    @property
    def extracionesRealizadas(self): return self.__extracionesRealizadas    

    def depositarMonto(self, monto: int) -> None:
        """ Deposita monto ingresado a la caja de ahorros """        
        self.__saldo += monto

    def extraerUnMonto(self, monto: int) -> None:
        """ Extrae un monto de la caja de ahorros en caso de no poder propaga una excepción
            ValueError("Imposible realizar extracción.")"""
        if self.puedeExtraer(monto):
            self.__saldo -= monto
            self.__extracionesRealizadas += 1
        else:
            raise ValueError("Imposible realizar extracción.")

    def puedeExtraer(self, monto: int) -> bool:
        """ Responde true si se puede extraer un monto """
        return ( monto <= self.__saldo and 
                self.__extracionesRealizadas < self.__extraccionesPosible )

    def restaurarExtracciones(self) -> None:
        """ Vuelve el contador a 0  """
        self.__contador = 0


if __name__ == '__main__':
    caja = CajaDeAhorro("jp", 1000, 2)
    for _ in range(3): caja.extraerUnMonto(100)


    caja.extraerUnMonto(100)
        
        

        