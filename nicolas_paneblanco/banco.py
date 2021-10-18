"""
    Ejercicio 6: 
        Modelar la clase Banco:
            - Un banco puede transferir un monto de una cuenta a otra cuenta.
"""
from caja_de_ahorro import CajaDeAhorro

class Banco(object): 
    """ 
        Clase Banco
        
        Metodo:
            - transferirUnMonto: Transfiere un monto de una cuanta a otra cuenta
    """
    def __init__(self) -> None:
        super().__init__()
        
    def transferirUnMonto(__, un_monto: float, una_cuenta: CajaDeAhorro, otra_cuenta: CajaDeAhorro) -> None:
        """ Transfiere un monto de una cuanta a otra """
        try:
            una_cuenta.extraer(un_monto)
            otra_cuenta.depositar(un_monto)
        except ValueError as error:
            print(error)
        
         