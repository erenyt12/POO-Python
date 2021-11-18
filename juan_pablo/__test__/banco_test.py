import unittest
from banco import Banco
from caja_de_ahorros import CajaDeAhorro as Caja

class TestBanco(unittest.TestCase):
    def test_puedeTransferirUnMontoDeUnaCuentaAOtra(self):
        """ Se tranfiere un monto de manera exitosa """
        # setup
        banco = Banco()   
        caja1 = Caja('Axel', 1200, 2)
        caja2 = Caja('Juampi', 0, 2)

        # precondición
        self.assertEqual(caja1.saldo, 1200)
        self.assertEqual(caja2.saldo, 0)

        # ejercitación del comportamiento
        banco.transferir(1200, caja1, caja2)

        # poscondición - objetivo
        self.assertEqual(caja1.saldo, 0)
        self.assertEqual(caja2.saldo, 1200)

    def test_imposibleRealizarTransferencia(self):
        """ Falla en la transferencia"""
        # setup
        banco = Banco()   
        caja1 = Caja('Axel', 1200,2)
        caja2 = Caja('Juampi', 0, 2)

        # precondición
        self.assertEqual(caja1.saldo, 1200)
        self.assertEqual(caja2.saldo, 0)

        # ejercitación del comportamiento
        with self.assertRaisesRegex(ValueError, 'Imposible realizar transacción'):
            banco.transferir(2000, caja1, caja2)

        # poscondición - objetivo
        self.assertEqual(caja1.saldo, 1200)
        self.assertEqual(caja2.saldo, 0)
    





if __name__ == '__main__':
    unittest.main()