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


class CajaDeAhorro(object):
    """ Clase CajaDeAhorro

        Atributos:
            titular: Nombre del titular de la cuenta.
            saldo: Saldo con el que se crea la caja de ahorro.
            
        Metodos:
            depositar: permite depositar unmonto en la cuenta.
            puedeExtraer: responde si es posible retirar un monto.
            extraer: extrae un monto de la cuenta, si no es posible arroja una excepción.
    """
    def __init__(self, titular: str, saldo: float):
        self.__titular = titular
        self.__saldo = saldo

    @property
    def titular(self): return self.__titular

    @property
    def saldo(self): return self.__saldo

    # -------- Metodos de la clase -------- #
    def depositar(self, un_monto: float) -> None: self.__saldo = un_monto
    
    def puedeExtraer(self, un_monto: int) -> bool:
        """ Devuelve true si se puede realizar la extracción """
        return un_monto <= self.saldo

    def extraer(self, un_monto: float):
        """ Extrae un monto de la cuenta, sino arroja la excepción: 
            -> ValueError('Imposible realizar la extracción.')"""
        if self.puedeExtraer(un_monto):
            self.__saldo -= un_monto
        else:
            raise ValueError('Imposible realizar la extracción.')


if __name__ == "__main__":
    cuenta = CajaDeAhorro('Niko', 0)

    # devuelve si posee el atributo
    print(hasattr(cuenta, 'saldo'))
