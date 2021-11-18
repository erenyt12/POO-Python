import unittest
from mosquito import Mosquito
from robot import Robot

class TestMosquito(unittest.TestCase):
    def test_ElMosquitoRecibeDisparo(self):
        """ comprueba que el mosquito recibe el disparo. """
        robot  = Robot(100)
        mosquito = Mosquito()
        mosquito.inicializar()

        self.assertFalse(mosquito.recibioDisparo())

        robot.disparar(mosquito)

        self.assertTrue(mosquito.recibioDisparo())