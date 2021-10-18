import unittest
from caja_de_ahorro import CajaDeAhorro


class TestCajaDeAhorro(unittest.TestCase):
    # ------ setup de la clase CajaDeAhorro ------ #
    def setUp(self) -> None:
        self.cuenta = CajaDeAhorro('Ruben', 0)

    
    def test_cuentaInicializaConElMontoEspecificado(self):
        """ Al crear la caja de ahorro se especifica el saldo inicial """
        cuenta = CajaDeAhorro('Marcos', 100)

        self.assertEqual(cuenta.saldo, 100)

    
    def test_depositarSaldoEnUnaCuenta(self):
        """ Se deposita un monto en una caja de ahorro """
        self.assertEqual(self.cuenta.saldo, 0)

        self.cuenta.depositar(1000)

        self.assertEqual(self.cuenta.saldo, 1000)
        
    
    def test_NoSePuedeExtreaerUnMonto(self):
        """ El monto de la extracción supera el saldo """
        self.assertFalse(self.cuenta.puedeExtraer(100))
        
        
    def test_sePuedeExtreaerUnMonto(self):
        """ El monto de la extracción es menor o igual al saldo """
        self.cuenta.depositar(150)
        
        self.assertTrue(self.cuenta.puedeExtraer(100))
  

    def test_extraerDineroDeUnaCuenta(self):
        """ Extracción de una caja de ahorro """
        self.cuenta.depositar(1000)

        self.assertEqual(self.cuenta.saldo, 1000)

        self.cuenta.extraer(500)

        self.assertEqual(self.cuenta.saldo, 500)

   
    def test_extraerDineroDeUnaCuentaVacia(self):
        """ Se intenta realizar una extracción superior al saldo """
        self.assertEqual(self.cuenta.saldo, 0)

        with self.assertRaisesRegex(ValueError, "Imposible realizar la extracción."):
            self.cuenta.extraer(500)

        self.assertEqual(self.cuenta.saldo, 0)


if __name__ == "__main__":
    unittest.main()
