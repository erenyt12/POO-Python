import unittest
from estacion import Estacion
from excepcion_estacion import SurtidoresLlenos
from surtidor import Surtidor

class TestEstacion(unittest.TestCase):
    def setUp(self) -> None:
        self.estacion = Estacion()
        self.surtidor1 = Surtidor(100)

    def test_agregarUnSurtidorALaEstacion(self):
        """ La estacion puede agregar surtidores. """
        self.assertEqual(self.estacion.cantidadDeSurtidores(),0)

        self.estacion.agregarSurtidor(self.surtidor1)
        
        self.assertEqual(self.estacion.cantidadDeSurtidores(),1)

    def test_saberCuantosSurtidoresTieneLaEstacion(self):
        """ La estacion sabe cuantos surtidores tiene. """
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 0 )

        for _ in range(4): self.estacion.agregarSurtidor(self.surtidor1) 
        
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 4 )

    def test_surtidoresVaciosDeLaEstacion(self):
        """ La estacion sabe cuales son sus surtidores vacios. """
        self.estacion.agregarSurtidor(self.surtidor1)

        self.assertEqual(self.surtidor1.carga, 0)
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 1)
        self.assertListEqual(self.estacion.surtidoresVacios(), [self.surtidor1])

        self.surtidor1.cargar(50)
        
        self.assertEqual(self.surtidor1.carga, 50)
        self.assertListEqual(self.estacion.surtidoresVacios(), [])

    def test_saberCuantosSurtidoresVaciosTieneLaEstacion(self):
        """ La estacion sabe cuantos surtidores vacios tiene. """
        surtidor2 = Surtidor(100)
        self.estacion.agregarSurtidor(self.surtidor1)
        self.estacion.agregarSurtidor(surtidor2)
        
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 2)
        
        surtidor2.cargar(50)
        
        self.assertEqual(self.estacion.cantidadDeSurtidoresVacios(), 1)
        
    def test_sumaDeLitrosFaltantes(self):
        """ La estacion sabe cuantos litros faltan para completar la carga de los surtidores. """
        surtidor2 = Surtidor(100)
        self.estacion.agregarSurtidor(surtidor2)
        self.estacion.agregarSurtidor(self.surtidor1)
        surtidor2.cargar(50)
        
        self.assertEqual(self.estacion.totalDeLitrosFaltantes(), 150)

    def test_costoDeLitrosFaltantesParaLaEstacionConUnSurtidorVacio(self):
        """ pass """
        self.estacion.agregarSurtidor(self.surtidor1)
        
        self.assertEqual(self.estacion.totalDeLitrosFaltantes(), 100)

        self.assertEqual(self.estacion.costoTotaDeCargaFaltante(80), 8000)

    def test_costoDeLitrosFaltantesParaLaEstacionConMasDeUnSurtidor(self):
        """ Costo total con mas de un surtidor """
        surtidor2 = Surtidor(100)
        surtidor2.cargar(50)
        self.estacion.agregarSurtidor(surtidor2)
        self.estacion.agregarSurtidor(self.surtidor1)
        
        self.assertEqual(self.estacion.totalDeLitrosFaltantes(), 150)

        self.assertEqual(self.estacion.costoTotaDeCargaFaltante(10), 1500)

    def test_elCostoEsCeroSiLaEstacionEstaLlena(self):
        """ Si el surtidor esta lleno el costo propaga una excepcion """
        self.surtidor1.cargar(100)
        self.estacion.agregarSurtidor(self.surtidor1)

        with self.assertRaises(SurtidoresLlenos):
            self.estacion.costoTotaDeCargaFaltante(50)



    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main() 
    
    
    
    
    
    
    
    