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
    __RECARGA = 2
    __ENERGIA_MAX = 5
    __DANIO = 1

    def __init__(self) -> None:
        self.__energia = self.__ENERGIA_MAX

    @property
    def energia(self): return self.__energia

    # ------ Metodo privado ------- #
    def __excedeEnergiaMaxima(self):
        return self.energia + self.__RECARGA > self.__ENERGIA_MAX

    # --------- Metodos publicos --------- #
    def estaVivo(self): return self.energia > 0

    def recibirDisparo(self): self.__energia -= self.__DANIO

    def reponerse(self):
        if self.__excedeEnergiaMaxima():
            self.__energia = self.__ENERGIA_MAX
        else:
            self.__energia += self.__RECARGA
