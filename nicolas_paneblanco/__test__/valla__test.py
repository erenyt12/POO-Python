import unittest
from valla import Valla

class TestValla(unittest.TestCase):
    def setUp(self) -> None:
        self.valla = Valla()
    
    def test_laVallaEstaAlta(self):
        """ La valla esta alta """        
        self.assertTrue(self.valla.alta)
        
    def test_laVallaPuedeBajarse(self):
        """ La valla puede cambiar su estado """
        self.assertTrue(self.valla.alta)
        
        self.valla.cambiarEstado()
        
        
    def test_laVallaPuedeSubirse(self):
        """ La valla puede ser subirse """
        self.valla.cambiarEstado()
        
        self.assertFalse(self.valla.alta)
        
        self.valla.cambiarEstado()
        
        self.assertTrue(self.valla.alta)
        
if __name__ == '__main__':
    unittest.main()