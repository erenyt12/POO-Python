import unittest
from robot import Robot
from alien import Alien

class TestRobot(unittest.TestCase):
   

    def test_elRobotDecrementaLaBateriaAlCaminar(self):
        """ cada 10 metros se resta una unidad de su bateria"""
        robot = Robot(100) 

        self.assertEqual(robot.bateria,100)

        robot.caminar(100)

        self.assertEqual(robot.bateria, 90)
    
    
    def test_alCaminarlasUnidadesAUtilizarNoPuedenSuperarLaBateriaDelRobot(self):
        """ pass """
        robot = Robot(10)
        robot.caminar(10)
        
        self.assertAlmostEqual(robot.bateria, 9)

        # with self.assertRaisesRegex(ValueError, 'no hay bateria suficiente'):
        #     robot.caminar(10000)
        
        # self.assertEqual(robot.bateria, 9)

    def test_elRobotPuedeCargarSuBateria(self):
        robot = Robot(0)
        
        self.assertEqual(robot.bateria, 0)

        robot.cargarBateria(50)        

        self.assertEqual(robot.bateria, 50)

    def test_elRobotNoPuedeCargarMasDe100Unidades(self):
        """ pass """

        robot = Robot(99)
        robot.caminar(10)
        

        self.assertEqual(robot.bateria, 98)

        robot.cargarBateria(2)

        self.assertEqual(robot.bateria, 100)    

    def test_dispararLeConsumeEl10PorCientoDeSuBateria(self):
        """ pass """
        alien = Alien()
        robot = Robot(100)

        self.assertEqual(alien.energia, 5)
        self.assertEqual(robot.bateria, 100)


        robot.disparar(alien)

        self.assertEqual(robot.bateria, 90)
        self.assertEqual(alien.energia, 4)


    def test_bajaLaBateriaDelRobotAlRecibirDisparo(self):
        """ Al recibir un disparo la bateria del robot baja un 30% """
        robot = Robot(100)
        robot_2 = Robot(100)
        
        self.assertEqual(robot_2.bateria, 100)
        
        robot.disparar(robot_2)

        self.assertEqual(robot_2.bateria, 70)



















if __name__ == '__main__':
    unittest.main()