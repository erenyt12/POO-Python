import unittest
from punto import Punto

class TestPunto(unittest.TestCase):

    def test_unPuntoEsIgualAOtroPunto(self):
        """ pass """
        punto = Punto(1, 1)

        self.assertTrue(punto == Punto(1, 1))

    # dos puntos que son distintos
        # distintos por coordenada x
        # distintos por coordenada y

    def test_distanciaEntreElPunto0x0y_y_Punto0x2y(self):
        """ Un punto puede calcular la distancia a otro punto """
        punto1 = Punto(0, 0)
        punto2 = Punto(0, 2)

        self.assertEqual(punto1.distancia(punto2), 2)


    def test_distanciaEntreElPunto0x0y_y_PuntoMenos2x2y(self):
        """ Distancia al punto -2 de X 0 de Y """
        punto1 = Punto(0, 0)
        punto2 = Punto(2, 2)

        self.assertAlmostEqual(punto1.distancia(punto2), 2.83, places=2)

    def test_distanciaEntrePuntosConLasMismasCoordenadas(self):
        """ Distancia al punto 0 de X 0 de Y """
        pass


if __name__ == '__main__':
    unittest.main()