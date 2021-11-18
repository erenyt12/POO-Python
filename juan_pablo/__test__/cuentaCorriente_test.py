import unittest
from cuenta_corriente import CuentaCorriente

class TestCuentaCorriente(unittest.TestCase):
    def setUp(self) -> None:
        self.cuenta = CuentaCorriente('jp',0,1000)

    def test_puedeDepositarUnMonto(self):
        """ Se puede depositar un monto en la cuenta corriente """
        self.assertAlmostEqual(self.cuenta.saldo,0)
        
        self.cuenta.depositarUnMonto(1000)

        self.assertAlmostEqual(self.cuenta.saldo,1000)


    def test_puedeExtraerUnMontoEnDescubierto(self):
        """ Extraer el maximo en descubierto """
        self.cuenta = CuentaCorriente('jp', 0, 1000)

        self.assertEqual(self.cuenta.saldo, 0)
        self.assertEqual(self.cuenta.descubierto, 1000)

        self.assertTrue(self.cuenta.puedeExtraerUnMonto(1000))

    def test_noPuedeExcederElDescubiertoMaximo(self):
        """ El monto maximo en descubierto es de 1000 """
        self.assertEqual(self.cuenta.saldo, 0)
        self.assertEqual(self.cuenta.descubierto, 1000)

        self.assertFalse(self.cuenta.puedeExtraerUnMonto(1001))
        
    
    def test_laCuentaSeInstanciaConLosValoresEnElSetup(self):
        """ La cuenta del setup se instancia con 0 de saldo y 1000 en descubierto """
        self.assertEqual(self.cuenta.saldo, 0)
        self.assertEqual(self.cuenta.descubierto, 1000)
        
        """ Se extrae un monto de la cuenta """
        self.assertEqual(self.cuenta.saldo, 0)
        
        self.cuenta.extraerUnMonto(500)
        
        self.assertEqual(self.cuenta.saldo, -500)
        
    def test_laExtraccionNoSePuedeRealizar(self):
        """ Al exceder el descubierto se propagaria la excepcion """
        self.cuenta.extraerUnMonto(1000)
        
        self.assertEqual(self.cuenta.saldo, -1000)
        self.assertEqual(self.cuenta.descubierto, 1000)
        
        with self.assertRaisesRegex(ValueError,'Imposible realizar extraccion.'):
            self.cuenta.extraerUnMonto(1)
        
        
        
        
        















if __name__ == '__main__':
    unittest.main()