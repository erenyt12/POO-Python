import unittest
from nicolas_paneblanco.fecha import Fecha


class TestFecha(unittest.TestCase):
    def setUp(self):
        self._2_4_2020 = Fecha(2, 4, 2020)


    def test_unaFechaEsIgualAOtraFecha(self):
        """ Una fecha es igual a otra fecha """
        self.assertTrue(self._2_4_2020 == Fecha(2, 4, 2020))


    def test_unaFechaEsMenorQueOtraFecha(self):
        self.assertTrue(Fecha(1, 4, 2020) < self._2_4_2020)


    def test_unaFechaNoEsMenorQueOtraFecha(self):
        """ Una fecha no es menor que otra fecha  """
        self.assertFalse(self._2_4_2020 < Fecha(1, 4, 2020))


    def test_unaFechaEsMenorOIgualAOtraFecha(self):
        """ Una fecha es menor o igual a otra fecha """
        self.assertTrue(Fecha(1, 4, 2020) <= self._2_4_2020)
        

    def test_unaFechaEsMenorOIgualAOtraFechaSegundoCaso(self):
        """ Una fecha es menor o igual a otra fecha segundo caso  """
        self.assertTrue(self._2_4_2020 <= Fecha(2, 4, 2020))


    def test_unaFechaEsMayorOIgualAOtraFecha(self):
        """  Una fecha es mayor o igual a otra fecha """
        self.assertTrue(self._2_4_2020 >= Fecha(1, 4, 2020))


    def test_unaFechaEsMayorOIgualAOtraFechaSegundoCaso(self):
        """ Una fecha es mayor o igual a otra fecha caso 2 """
        self.assertTrue(self._2_4_2020 >= Fecha(2, 4, 2020))


    def test_unaFechaEsMayorAOtraFecha(self):
        """ Una fecha es mayor a otra fecha """
        self.assertTrue(self._2_4_2020 > Fecha(1, 4, 2020))


    def test_unaFechaEstaEntreDosFechas(self):
        """ Una fecha se encuentra entre dos fechas """
        _10_4_2020 = Fecha(10, 4, 2020)
        _30_4_2020 = Fecha(30, 4, 2020)

        self.assertTrue(_10_4_2020.entreDosFechas(self._2_4_2020, _30_4_2020))


    def test_unaFechaNoEstaEntreDosFechas(self):
        """ Una fecha no se encuentra entre dos fecha """
        _10_4_2020 = Fecha(10, 4, 2020)
        _30_4_2020 = Fecha(30, 4, 2020)

        self.assertFalse(self._2_4_2020.entreDosFechas(_10_4_2020, _30_4_2020))


if __name__ == "__main__":
    unittest.main()
