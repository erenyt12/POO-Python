
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
    # __VIDA_MAX = 0
    def __init__(self) -> None:
        # self.__energia = self.__VIDA_MAX
        self.__vida = False

    @property
    def vive(self): return self.__vida

    def inicializar(self) -> None:
        self.__vida = True 
        
    def recibioDisparo(self) -> bool:
        return not self.vive


    def recibirDisparo(self) -> None:
        self.__vida = False
        
    



if __name__ == '__main__':
    pass