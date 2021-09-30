import unittest
from robot import Robot
from mosquito import Mosquito


class TestMosquito(unittest.TestCase):
    def setUp(self) -> None:
        self.mosquito = Mosquito()

    def test_mosquitoRecibioDisparo(self):
        """ Test mosquito recibe un disparo """
        robot = Robot(10)
        self.mosquito.inicializar()

        self.assertFalse(self.mosquito.recibioDisparo())

        robot.disparar(self.mosquito)

        self.assertTrue(self.mosquito.recibioDisparo())

    def test_mosquitoInicializarVida(self):
        """ El mosquito vive una vez inicializado """
        self.assertFalse(self.mosquito.vive)

        self.mosquito.inicializar()

        self.assertTrue(self.mosquito.vive)

    def test_moquitoMuereLuegoDeRecibirUnDisparo(self):
        """ Al recibir un disparo el mosquito pierde la vida """
        self.mosquito.inicializar()
        robot = Robot(10)

        self.assertTrue(self.mosquito.vive)

        robot.disparar(self.mosquito)

        self.assertFalse(self.mosquito.vive)


if __name__ == "__main__":
    unittest.main()
