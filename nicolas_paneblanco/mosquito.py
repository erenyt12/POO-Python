"""
    Ejercicio 5:
        Modelar la clase Mosquito para que el siguiente test se ejecute exitosamente:

        def test_mosquitoRecibioDisparo(self):
            robot  = Robot()
            mosquito = Mosquito()
            mosquito.inicializar()

            self.assertFalse(mosquito.recibioDisparo())

            robot.disparar(mosquito)

            self.assertTrue(mosquito.recibioDisparo())
            

    Pasos sugeridos:
        1. Identifique los mensajes que debe entender el objeto “mosquito”.
        2. Implemente dichos mensajes y escriba los tests que prueben su correcto funcionamiento.
        3. Implemente el test planteado originalmente y verifique que se ejecute correctamente.
"""
