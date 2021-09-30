import unittest
from alien import Alien
from robot import Robot


class TestAlien(unittest.TestCase):
    # ------ setUp de la clase ------ #
    def setUp(self) -> None:
        self.alien = Alien()

    def test_elAlienIniciaConUnaVidaDe5(self):
        """ Al instanciar un alien inicia con energia en 5 unidades """
        self.assertEqual(self.alien.energia, 5)

    def test_elAlienEstaVivo(self):
        """ El alien estara vivo si su energia es mayor a 0 """
        self.assertTrue(self.alien.estaVivo())

    def test_elAlienRecibeUnDisparo(self):
        """ El alien recibe un disparo y decrementa su energia una unidad """
        self.alien.recibirDisparo()

        self.assertEqual(self.alien.energia, 4)

    def test_elAlienMuereAlQuintoDisparo(self):
        """ El alien muere cuando su energia es igual a 0 """
        self.assertEqual(self.alien.energia, 5)
        self.assertTrue(self.alien.estaVivo())

        self.alien.recibirDisparo()
        self.alien.recibirDisparo()
        self.alien.recibirDisparo()
        self.alien.recibirDisparo()
        self.alien.recibirDisparo()

        self.assertEqual(self.alien.energia, 0)
        self.assertFalse(self.alien.estaVivo())

    def test_alienSeReponeLuegoDeRecibirTresDisparos(self):
        """ El alien recibe 3 disparo y se recupera 2 unidades """
        self.alien.recibirDisparo()
        self.alien.recibirDisparo()
        self.alien.recibirDisparo()

        self.assertEqual(self.alien.energia, 2)

        self.alien.reponerse()

        self.assertEqual(self.alien.energia, 4)

    def test_laRecuperacionNoPuedeSuperarLas5unidades(self):
        """ El alien puede recuperarse sin superar las 5 unidades de energia """
        self.alien.recibirDisparo()

        self.assertEqual(self.alien.energia, 4)

        self.alien.reponerse()

        self.assertEqual(self.alien.energia, 5)
        self.assertNotEqual(self.alien.energia, 6)

    def test_alienRecibeUnDisparoDelRobot(self):
        robot = Robot(10)

        self.assertEqual(robot.bateria, 10)
        self.assertEqual(self.alien.energia, 5)

        robot.disparar(self.alien)

        self.assertEqual(robot.bateria, 9)
        self.assertEqual(self.alien.energia, 4)


if __name__ == "__main__":
    unittest.main()
