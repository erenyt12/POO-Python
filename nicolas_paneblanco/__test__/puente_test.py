import unittest
from nicolas_paneblanco.auto import Auto
from nicolas_paneblanco.puente import Puente

class TestPuente(unittest.TestCase):
    def setUp(self) -> None:
        self.puente = Puente(33)
        
    def test_alCrearUnPuenteSuVallaEstaAlta(self):
        """ La valla del puente esta alta """
        self.assertTrue(self.puente.vallaAlta())


    def test_elPuenteBajaLaValla(self):
        """ El puente puede bajar la valla """
        self.assertTrue(self.puente.vallaAlta())

        self.puente.bajarValla()
        
        self.assertFalse(self.puente.vallaAlta())
        
        
    def test_elPuenteSubeLaValla(self):
        """ El puente puede subir la valla """
        self.puente.bajarValla()
        
        self.assertFalse(self.puente.vallaAlta())

        self.puente.subirValla()

        self.assertTrue(self.puente.vallaAlta())


    def test_subirLaVallaCuandoEstaAlta(self):
        """ Al subir la valla estando alta su estado no se altera """
        self.assertTrue(self.puente.vallaAlta())
        
        self.puente.subirValla()

        self.assertTrue(self.puente.vallaAlta())


    def test_bajarLaVallaCuandoEstaBaja(self):
        """ Al bajar la valla estando baja su estado no se altera """
        self.puente.bajarValla()
        
        self.assertFalse(self.puente.vallaAlta())
        
        self.puente.bajarValla()

        self.assertFalse(self.puente.vallaAlta())


    def test_elPuenteRecibeUnAutoConLaVallaAlta(self):
        """ El puente recibe un auto con la valla alta y lo hace circular a 40km/h """
        auto = Auto()
        
        self.assertEqual(auto.velocidad, 0)
        self.assertTrue(self.puente.vallaAlta())
        
        self.puente.recibirAuto(auto)
        
        self.assertEqual(auto.velocidad, 40)
    
    
    def test_elPuenteRecibeUnAutoConLaVallaBaja(self):
        """ El puente recibe un auto con la valla alta y lo hace circular a 40km/h """
        auto = Auto()
        auto.acelerar(100)
        self.puente.bajarValla()
        
        self.assertEqual(auto.velocidad, 100)
        self.assertFalse(self.puente.vallaAlta())
        
        self.puente.recibirAuto(auto)
        
        self.assertEqual(auto.velocidad, 0)
        

if __name__ == '__main__':
    unittest.main()