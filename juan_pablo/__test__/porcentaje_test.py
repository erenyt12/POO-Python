import unittest
from excepcion import CeroDivididoUnNumeroReal
from porcentaje import Porcentaje

class testPorcentaje(unittest.TestCase):
    def setUp(self) -> None:
        self.porcentaje_20 = Porcentaje(20)

    def test_SacaElPorcentajeDeUnNumero(self):
        """ El valor porcentual de mi objeto porcentaje es aplicado a un numero. """
        self.assertEqual(self.porcentaje_20.aplicarA(100), 20)

    def test_noSePuedeAplicarACero(self):
        """ Evalua la excepcion de que el porcentaje aplicado no sea 0  """
        with self.assertRaises(CeroDivididoUnNumeroReal):
            self.porcentaje_20.aplicarA(0)

