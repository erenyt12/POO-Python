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
        
        Protocolo:
                # estaVivo: retorna verdadero solo si su energia es mayor a 0.
                # recibirDisparo: decrementa la energia del alien en 1.
                # reponerse: aumenta la energia del alien en dos unidades.
    """
    __ENERGIA_MAX = 5
    def __init__(self) -> None:
        self.__energia = self.__ENERGIA_MAX

    @property
    def energia(self): return self.__energia

    def estaVivo(self) -> bool:
        return self.energia > 0 

    def recibirDisparo(self) -> None:
        
        self.__energia -= 1


    def reponerEnergia(self) -> None:
        if self.energia + 2 <= self.__ENERGIA_MAX:
            self.__energia += 2
        else:
            self.__energia = self.__ENERGIA_MAX
            



    






if __name__ == '__main__':
    pass
        