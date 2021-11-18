"""
    Ejercicio 6: 
        Modelar la clase Banco:
            - Un banco puede transferir un monto de una cuenta a otra cuenta.
"""
from caja_de_ahorros import CajaDeAhorro as Caja

class Banco(object):
    """
        Clase Banco

        Mensajes:
            ✅ transferir(un_monto, una_cuenta, otra_cuenta): transferir un monto de una cuenta a otra 
    """
    def __init__(self) -> None:
        super().__init__()

    def transferir(__, un_monto: float, una_cuenta: Caja, otra_cuenta: Caja) -> None:
        """ Tranfiere un monto de una cuenta a otra """
        try:
            una_cuenta.extraerUnMonto(un_monto)
            otra_cuenta.depositarMonto(un_monto)
        except ValueError:
            raise ValueError('Imposible realizar transacción')



if __name__ == '__main__':
    pass