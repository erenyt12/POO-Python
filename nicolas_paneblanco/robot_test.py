import unittest
from nicolas_paneblanco.robot import Robot

class TestRobot(unittest.TestCase):
    # ------- setUp de la clase Robot ----- #
    def setUp(self) -> None:
        self.robot = Robot(10)
        
    # ---------- Test el robot cuenta con una energia inicial de 100 unidades ------ #
    def test_robotConEnergiaInicialEn100Unidades(self):
        self.assertEqual(self.robot.bateria, 10)
    
    # ---------- Test el robot camina 10 metros y pierde 1 unidad de energia ------ #
    def test_robotCamina10Metros(self):
        self.assertEqual(self.robot.bateria, 10)
        
        self.robot.caminar(10)
        
        self.assertEqual(self.robot.bateria, 9)
    
    # ---------- Test el robot camina 100 metros y agota su energia ------ #
    def test_robotAgotaSuBateria(self):
        self.assertEqual(self.robot.bateria, 10)
        
        self.robot.caminar(100)
        
        self.assertEqual(self.robot.bateria, 0)
    
    # ---------- Test el robot propaga una excepción al exceder su bateria disponible ------ #
    def test_robotBateriaInsuficiente(self):
        self.assertEqual(self.robot.bateria, 10)
        
        with self.assertRaisesRegex(ValueError, 'Bateria insuficiente.'):
            self.robot.caminar(101)
        
        self.assertEqual(self.robot.bateria, 10)
        