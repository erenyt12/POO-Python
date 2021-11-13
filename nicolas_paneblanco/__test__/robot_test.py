import unittest
from robot import Robot
from alien import Alien


class TestRobot(unittest.TestCase):
    # ------- setUp de la clase Robot ----- #
    def setUp(self) -> None:
        self.robot = Robot(10)

    def test_robotConEnergiaInicialEn100Unidades(self):
        """ El robot cuenta con una energia inicial de 100 unidades  """
        self.assertEqual(self.robot.bateria, 10)

    def test_robotCamina10Metros(self):
        """ El robot camina 10 metros y pierde 1 unidad de energia """
        self.assertEqual(self.robot.bateria, 10)

        self.robot.caminar(10)

        self.assertEqual(self.robot.bateria, 9)

    def test_robotAgotaSuBateria(self):
        """ El robot camina 100 metros y agota su energia """
        self.assertEqual(self.robot.bateria, 10)

        self.robot.caminar(100)

        self.assertEqual(self.robot.bateria, 0)

    def test_bateriaInsuficiente(self):
        """ El robot propaga una excepción al exceder su bateria disponible """
        self.assertEqual(self.robot.bateria, 10)

        with self.assertRaisesRegex(ValueError, 'Bateria insuficiente.'):
            self.robot.caminar(101)

        self.assertEqual(self.robot.bateria, 10)

    def test_robotCarga10UnidadesSuBateria(self):
        """ El robot carga 10 unidades en su bateria """
        self.assertEqual(self.robot.bateria, 10)

        self.robot.cargarBateria(10)

        self.assertEqual(self.robot.bateria, 20)

    def test_laCargaExcedeElMaximoDe100Unidades(self):
        """ Al exceder la carga maxima la bateria queda en 100 unidades"""
        self.assertEqual(self.robot.bateria, 10)

        self.robot.cargarBateria(91)

        self.assertEqual(self.robot.bateria, 100)

    def test_elRobotRealizaUnDisparo(self):
        """ El robot realiza un disparo y pierde el 10% de su batería"""
        alien = Alien()

        self.assertEqual(self.robot.bateria, 10)

        self.robot.disparar(alien)

        self.assertEqual(self.robot.bateria, 9)
        
    def test_elRobotRecibeUnDisparo(self):
        """ Al recibir un disparo el robot decrementa el 30% de su bateria actual """
        robot_dos = Robot(100)
        
        self.assertEqual(robot_dos.bateria, 100)
        
        self.robot.disparar(robot_dos)

        self.assertEqual(robot_dos.bateria, 70)

if __name__ == "__main__":
    unittest.main()
