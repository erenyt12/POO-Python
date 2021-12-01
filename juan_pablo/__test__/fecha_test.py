import unittest
from juan_pablo.fecha import Fecha

class TestFecha(unittest.TestCase):
    def setUp(self) -> None:
        self._1_2_2001 = Fecha(1, 2, 2001)
        
        
    def test_unaFechaEsIgualAOtraFecha(self):
        """ igualacion de fecha """
        
        self.assertTrue(self._1_2_2001.esIgual(Fecha(1, 2, 2001)))


    def test_lasFechasNoSonIguales(self):
        """ Las fechas ingresadas no son iguales """
        _1_3_2001_bis = Fecha(1, 3, 2001)

        self.assertFalse(self._1_2_2001.esIgual(_1_3_2001_bis))
        
    def test_unaFechaEsMenorAOtra(self):
        """ La fecha ingresada es menor a otra fecha """
        _1_3_2002 = Fecha(1, 3, 2002)

        self.assertTrue(self._1_2_2001.esMenor(_1_3_2002))
    
    def test_unaFechaNoEsMenorAOtra(self):
        """ Una fecha no es menor a otra """
        _1_3_2000 = Fecha(1, 3, 2000)

        self.assertFalse(self._1_2_2001.esMenor(_1_3_2000))

    def test_unaFechaEsMayorAotra(self):
        """ pass """
        _1_3_2000 = Fecha(1, 3, 2000)

        self.assertTrue(self._1_2_2001.esMayor(_1_3_2000))


    





if __name__ == '__main__':
    unittest.main()