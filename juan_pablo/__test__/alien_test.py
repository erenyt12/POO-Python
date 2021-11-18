import unittest
from alien import Alien

class TestAlien(unittest.TestCase):
    def setUp(self) -> None:
        self.alien = Alien()

    def test_estaVivo(self):
        """ Retorna True si el alien esta vivo  """
        self.assertTrue(self.alien.estaVivo())

    def test_alienMuere(self):
        """ Cuando la energia del alien es 0 muere """
        self.assertTrue(self.alien.estaVivo())
        for i in range(5):
            self.alien.recibirDisparo()
        self.assertFalse(self.alien.estaVivo())
    
    def test_laEnergiaBajaSiRecibeUnDisparo(self):
        """ Si recibe un disparo baja la energia del alien  """
        self.assertEqual(self.alien.energia, 5)

        self.alien.recibirDisparo()

        self.assertEqual(self.alien.energia, 4)

    def test_reponerEnergia(self):
        """ Valida si el alien repone su energia """
        for i in range(2):
            self.alien.recibirDisparo()

        self.assertEqual(self.alien.energia, 3)
        
        self.alien.reponerEnergia()

        self.assertEqual(self.alien.energia, 5)

    def test_reponerEnergiaNoPuedeSuperar5(self):
        """ No puede reponer mas de 5 unidades  """
        self.alien.recibirDisparo()
        self.assertEqual(self.alien.energia, 4)
        
        self.alien.reponerEnergia()

        self.assertEqual(self.alien.energia, 5)

    
