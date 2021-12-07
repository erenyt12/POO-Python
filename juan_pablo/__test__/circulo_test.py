import unittest
from circulo import Circulo
from punto import Punto

class TestCirculo(unittest.TestCase):
    
    def test_unPuntoDentroDelCirculo(self):
        """  """
        circulo = Circulo(Punto(0,0), 2)
        punto = Punto(0, 1)
        
        self.assertTrue(circulo.contieneAUnPunto(punto))

    def test_unPuntoDentroDelCirculo2(self):
        """  """
        circulo = Circulo(Punto(0,0), 2)
        punto = Punto(0, 2)
        
        self.assertFalse(circulo.contieneAUnPunto(punto))

if __name__ == '__main__':
    unittest.main()