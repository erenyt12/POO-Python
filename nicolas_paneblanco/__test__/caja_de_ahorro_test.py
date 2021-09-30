import unittest
from caja_de_ahorro import CajaDeAhorro


class TestCajaDeAhorro(unittest.TestCase):
    # ------ setup de la clase CajaDeAhorro ------ #
    def setUp(self) -> None:
        self.cuenta = CajaDeAhorro('Ruben', 0)

    # ----- Test la cuenta se inicializa con un monto especificado ----- #
    def test_cuentaInicializadaEn100(self):
        cuenta = CajaDeAhorro('Marcos', 100)

        self.assertEqual(cuenta.saldo, 100)

    # ----- Test depositar en una caja de ahorro ----- #
    def test_depositarEnUnaCuentaVacia(self):
        self.assertEqual(self.cuenta.saldo, 0)

        self.cuenta.depositar(1000)

        self.assertEqual(self.cuenta.saldo, 1000)

    # ----- Test extraer dinero de una cuenta ----- #

    def test_extraerDineroDeUnaCuenta(self):
        self.cuenta.depositar(1000)

        self.assertEqual(self.cuenta.saldo, 1000)

        self.cuenta.extraer(500)

        self.assertEqual(self.cuenta.saldo, 500)

    # ----- Test extraer dinero de una cuenta sin fondos ----- #
    def test_extraerDineroDeUnaCuenta(self):
        self.assertEqual(self.cuenta.saldo, 0)

        with self.assertRaisesRegex(ValueError, "Imposible realizar la extracción."):
            self.cuenta.extraer(500)

        self.assertEqual(self.cuenta.saldo, 0)


if __name__ == "__main__":
    unittest.main()
