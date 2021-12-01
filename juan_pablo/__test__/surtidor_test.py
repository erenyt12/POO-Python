import unittest
from excepctionsCustom import LaCargaNoPuedeSuperarLaCargaMax
from surtidor import Surtidor 


class TestSurtidor(unittest.TestCase):
    def setUp(self) -> None:
        self.surtidor = Surtidor(100)

    def test_alCrearUnSurtidorSuCargaInicializaEnCero(self):
        """ Los surtidores se instancian con una carga inicial de 0 """
        self.assertEqual(self.surtidor.carga, 0)

    def test_unSurtidorPuedeSaberSiEstaVacio(self):
        """ El surtidor se encuentra vacio """
        self.assertTrue(self.surtidor.estaVacio())

    def test_unSurtidorNoEstaVacio(self):
        """ El surtidor responde no estar vacio """
        self.assertTrue(self.surtidor.estaVacio())

        self.surtidor.cargar(50)

        self.assertFalse(self.surtidor.estaVacio())
        
    def test_unSurtidorPuedeSaberSuCargaFaltante(self):
        """ Un surtidor puede saber su carga faltante """        
        self.assertEqual(self.surtidor.cargaFaltante(), 100)

    def test_unSurtidorVacioPuedeSerCargado(self):
        """ Se le agrega una carga al surtidor """
        self.assertEqual(self.surtidor.carga, 0)

        self.surtidor.cargar(50)
        
        self.assertEqual(self.surtidor.carga, 50)

    def test_laCargaDelSurtidorSeSumaASuCargaActual(self):
        """ Al cargar el surtidor dicha se incrementa """
        self.surtidor.cargar(50)

        self.assertEqual(self.surtidor.carga, 50)

        self.surtidor.cargar(50)
        
        self.assertEqual(self.surtidor.carga, 100)

    def test_elSurtidorNoPuedeSuperarLaCargaMaxima(self):
        """ La carga no puede superar el maximo de carga admitido """
        self.assertEqual(self.surtidor.carga, 0)
        self.assertEqual(self.surtidor.cargaMax, 100)

        with self.assertRaises(LaCargaNoPuedeSuperarLaCargaMax):
            self.surtidor.cargar(101)

    def test_elSurtidorNoPuedeCargarsePorEncimaDeSuCapacidad(self):
        """ La carga no puede superar el maximo de carga admitido """
        self.surtidor.cargar(100)

        self.assertEqual(self.surtidor.carga, 100)
        self.assertEqual(self.surtidor.cargaMax, 100)

        with self.assertRaises(LaCargaNoPuedeSuperarLaCargaMax):
            self.surtidor.cargar(100)
        self.assertEqual(self.surtidor.carga, 100)



if __name__ == '__main__':
    unittest.main()