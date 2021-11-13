import unittest
from nicolas_paneblanco.banco import Banco
from nicolas_paneblanco.caja_de_ahorro import CajaDeAhorro

class TestBanco(unittest.TestCase):
    
    def test_elBancoTranfiereUnMontoEntreCuentas(self):
        """ Se tranfiere un monto de una cuenta a otra """
        banco = Banco()
        cuenta_1 = CajaDeAhorro('Nicolas', 1000, 1)
        cuenta_2 = CajaDeAhorro('Martin', 0, 1)
        
        self.assertEqual(cuenta_1.saldo, 1000)
        self.assertEqual(cuenta_2.saldo, 0)
        
        banco.transferirUnMonto(200, cuenta_1, cuenta_2)
        
        self.assertEqual(cuenta_2.saldo, 200)
        self.assertEqual(cuenta_1.saldo, 800)
        
    def test_noSePuedeTransferirUnMontoEnDescubierto(self):
        """ Al intentar tranferir un monto mayor al saldo 
        se arroja una excepción """
        banco = Banco()
        cuenta_1 = CajaDeAhorro('Nicolas', 1000, 1)
        cuenta_2 = CajaDeAhorro('Martin', 0, 1)
        
        with self.assertRaisesRegex(ValueError, 'Imposible realizar transferencia.'):
            banco.transferirUnMonto(1001, cuenta_1, cuenta_2)