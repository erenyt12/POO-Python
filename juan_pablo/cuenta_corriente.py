"""
    Ejercicio 8:
        Modelar la clase CuentaCorriente:
            - un titular
            - un saldo
            - descubierto maximo
        
        y debera poder:
            - depositar un monto
            - puedeExtraer un monto
                👉🏻 un monto <= ( saldo + descubierto maximo )
            - extraer un monto
            - en el caso de querer extraer un monto superior 
              al monto disponible arrojara una 
              excepcion ValueError("Imposible realizar extracción.")

        Realizar los test necesarios que validen 
        el comportamiento.  
"""


class CuentaCorriente(object):
    """ 
    Clase cuenta corriente 
    - depositar un monto
    - puedeExtraer un monto
    👉🏻 un monto <= ( saldo + descubierto maximo )
    - extraer un monto
    
    """
    def __init__(self, titular: str, saldo: int, descubierto_maximo: int) -> None:        
        self.__titular = titular
        self.__saldo = saldo
        self.__descubierto = descubierto_maximo 

    @property
    def titular(self): return self.__titular
    @property
    def saldo(self): return self.__saldo
    @property
    def descubierto(self): return self.__descubierto
        

    def depositarUnMonto(self, un_monto: int) -> None:
        """ Deposita monto ingresado a cuenta corriente """        
        self.__saldo += un_monto
    
    def puedeExtraerUnMonto(self, un_monto:int) -> bool:
        """ Devuelve true si se puede extraer un monto """
        return un_monto <= self.saldo + self.descubierto

    def extraerUnMonto(self, un_monto: int) -> None:
        """ Extrae un monto de la cuenta corriente, en caso de que el monto
        supere el saldo y el descubierto maximo arroja una excepcion de ValueError """
        if self.puedeExtraerUnMonto(un_monto):
            self.__saldo -= un_monto
        else:
            raise ValueError("Imposible realizar extraccion.")






if __name__ == '__main__':
    cuenta = CuentaCorriente('jp', 0, 1000)

    cuenta.extraerUnMonto(500)
    cuenta.extraerUnMonto(500)
    cuenta.extraerUnMonto(1)