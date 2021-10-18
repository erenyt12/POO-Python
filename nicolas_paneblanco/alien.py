"""
    Ejercicio 4:
        Modelar la clase Alien con las siguientes caracteristicas:
            - Un alien posee una energia que va en el rango de 0 a 5.
            - Un alien puede:
                # estaVivo: retorna verdadero solo si su energia es mayor a 0.
                # recibirDisparo: decrementa la energia del alien en 1.
                # reponerse: aumenta la energia del alien en dos unidades. 

    Realizar los test necesarios que validen 
    el comportamiento del alien, ademas verifique que cuando el robot realice un 
    disparo al alien decremente la energia del mismo.      
"""


class Alien(object):
    """ 
        Clase Alien
        
        Atributos:
            - energia: representa la energia del objeto
            
        Metodos:
            - estaVivo: responde si la energía es mayor a 0.
            - recibirDisparo: resta una unidad de energia al Alien.
            - reponerse: recarga la energía del Alien en dos unidades.
    """
    __RECARGA = 2
    __ENERGIA_MAX = 5
    __DANIO = 1

    def __init__(self) -> None:
        self.__energia = self.__ENERGIA_MAX

    @property
    def energia(self): return self.__energia

    # ------ Metodo privado ------- #
    def __excedeEnergiaMaxima(self) -> bool:
        """ Responde True si la energía actual mas la recarga 
            excede la energia maxima de 5 unidades"""
        return self.energia + self.__RECARGA > self.__ENERGIA_MAX

    # --------- Metodos publicos --------- #
    def estaVivo(self) -> bool: return self.energia > 0

    def recibirDisparo(self) -> None: 
        """ Resta una unidad a la energia del Alien """
        self.__energia -= self.__DANIO

    def reponerse(self) -> None:
        """ Recarga dos unidades la energía del Alien sin sobrepasar 
            la energia maxima de 5 unidades"""
        if self.__excedeEnergiaMaxima():
            self.__energia = self.__ENERGIA_MAX
        else:
            self.__energia += self.__RECARGA
