import unittest
from caja_de_ahorros import CajaDeAhorro

class TestCajaDeAhorro(unittest.TestCase):
   def setUp(self) -> None:
        self.caja = CajaDeAhorro("jp", 0, 2)
   
   def test_depositarMonto(self):
      """ Se puede depositar un monto """
      self.assertEqual(self.caja.saldo, 0)

      self.caja.depositarMonto(100)

      self.assertEqual(self.caja.saldo, 100)
       
   def test_extraerUnMonto(self):
      """ extrae un monto de la caja de ahorros """
      self.caja.depositarMonto(100)
 
      self.caja.extraerUnMonto(50)
      
      self.assertEqual(self.caja.saldo, 50)

   def test_puedeExtraerUnMonto(self):
      """ Puede extraer un monto mientras no sea superior a lo que 
      tiene la caja de ahorros """
      self.caja.depositarMonto(20)

      self.assertTrue(self.caja.puedeExtraer(20))


   def test_extracionesPosiblesSuperadas(self):
      """ Cuando se superan las extraciones posibles se arroja una excepcion """
      caja = CajaDeAhorro("jp", 1000, 2)
      for _ in range(2): caja.extraerUnMonto(100)

      self.assertEqual(caja.extracionesRealizadas, 2)

      with self.assertRaises(ValueError):
         caja.extraerUnMonto(100)

      self.assertEqual(caja.extracionesRealizadas, 2)






   
    
    
    
    

if __name__ == '__main__':
    unittest.main()