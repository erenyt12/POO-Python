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
              al monto disponiple arrojara una 
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
    """ Clase CajaDeAhorro

        Atributos:
            titular: Nombre del titular de la cuenta.
            saldo: Saldo con el que se crea la caja de ahorro.
            extracciones: cantidad de extracciones mensuales permitidas.
            
        Metodos:
            depositar: permite depositar unmonto en la cuenta.
            puedeExtraer: responde si es posible retirar un monto.
            extraer: extrae un monto de la cuenta, si no es posible arroja una excepción.
            reastaurarEtracciones: restaura la cantidad de extracciones mensuales.
    """
    def __init__(self, titular: str, saldo: float, extracciones_posibles: int) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self.__extraccionesPosibles = extracciones_posibles
        self.__extraccionesRealizadas = 0

    @property
    def titular(self): return self.__titular

    @property
    def saldo(self): return self.__saldo
    
    @property
    def extraccionesPosibles(self): return self.__extraccionesPosibles
    @property
    def extraccionesRealizadas(self): return self.__extraccionesRealizadas

    # -------- Metodos de la clase -------- #
    def depositar(self, un_monto: float) -> None: self.__saldo = un_monto
    
    def puedeExtraer(self, un_monto: int) -> bool:
        """ Devuelve true si se puede realizar la extracción """
        return (
            un_monto <= self.saldo 
            and 
            self.extraccionesRealizadas < self.extraccionesPosibles
            )

    def extraer(self, un_monto: float):
        """ Extrae un monto de la cuenta, sino arroja la excepción: 
            -> ValueError('Imposible realizar la extracción.')"""
        if self.puedeExtraer(un_monto):
            self.__saldo -= un_monto
            self.__extraccionesRealizadas += 1
        else:
            raise ValueError('Imposible realizar la extracción.')
        
    def restaurarExtraciones(self) -> None:
        """ Reataura la cantidad de extraciones """
        self.__extraccionesRealizadas = 0

if __name__ == "__main__":
    cuenta = CajaDeAhorro('Niko', 0)

    # devuelve si posee el atributo
    print(hasattr(cuenta, 'saldo'))
