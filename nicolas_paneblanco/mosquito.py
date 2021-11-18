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
    """ 
        Clase Mosquito
        
        Metodos:
            ✅ vida: representa la vida del mosquito
            
            ✅ inicializar: inicializa la vida del Mosquito 
            ✅ recibioDisparo: responde True si el Mosquito esta muerto
            ✅ recibirDisparo: cambia el esta de la vida del Mosquito
    """  
    def __init__(self) -> None:
        self.__vida = False
    
    @property
    def vive(self): return self.__vida
    
    # ------ Metodos publicos ---- #
    def inicializar(self): 
        """ Inicializa la vida del Mosquito """
        self.__vida = True
    
    def recibioDisparo(self): 
        """ Responde True si el mosquito esta muerto """
        return not self.vive 
    
    def recibirDisparo(self): 
        """ Cambia el estado del Mosquito """
        self.__vida = False
    