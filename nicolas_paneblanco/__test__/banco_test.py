import unittest
from banco import Banco
from caja_de_ahorro import CajaDeAhorro

class TestBanco(unittest.TestCase):
    
    def test_elBancoTranfiereUnMontoEntreCuentas(self):
        """ Se tranfiere un monto de una cuenta a otra """
        banco = Banco()
        cuenta_1 = CajaDeAhorro('Nicolas', 1000, 1)
        cuenta_2 = CajaDeAhorro('Martin', 0, 1)
        
        self.assertEqual(cuenta_2.saldo, 0)
        
        banco.transferirUnMonto(200, cuenta_1, cuenta_2)
        
        self.assertEqual(cuenta_2.saldo, 200)
        self.assertEqual(cuenta_1.saldo, 800)