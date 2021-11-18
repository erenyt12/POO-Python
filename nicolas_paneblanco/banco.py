"""
    Ejercicio 6: 
        Modelar la clase Banco:
            - Un banco puede transferir un monto de una cuenta a otra cuenta.
"""
from nicolas_paneblanco.caja_de_ahorro import CajaDeAhorro as Caja

class Banco(object): 
    """ 
        Clase Banco
        
        Metodo:
            ✅ transferirUnMonto: Transfiere un monto de una cuanta a otra cuenta
    """
    def __init__(self) -> None:
        pass
        
    def transferirUnMonto(__, un_monto: float, una_cuenta: Caja, otra_cuenta: Caja) -> None:
        """ Transfiere un monto de una cuanta a otra """
        try:
            una_cuenta.extraer(un_monto)
            otra_cuenta.depositar(un_monto)
        except ValueError:
            raise ValueError('Imposible realizar transferencia.')
        

if __name__ == '__main__':
    pass