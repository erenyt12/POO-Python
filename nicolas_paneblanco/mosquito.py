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
class Mosquito(object):    
    def __init__(self) -> None:
        self.__vive = False
    
    @property
    def vive(self): return self.__vive
    
    # ------ Metodos publicos ---- #
    def inicializar(self): self.__vive = True
    
    def recibioDisparo(self): return self.vive == False
    
    def recibirDisparo(self): self.__vive = False
    