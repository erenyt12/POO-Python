from __future__ import annotations
from typing import Union
from alien import Alien
from mosquito import Mosquito
"""
    Ejercicio 3:
        Modelar la clase Robot con las siguientes caracteristicas:
            - Un robot posee una bateria en la cual almacena su energia.
              La carga de la bateria de encuentra en el rango de 0 a 100.
            - Un robot puede:
                # caminar(metros): le consume 1 unidad cada 10 metros.
                # cargarBateria(una_carga): le agrega una determinada cantidad
                  de unidades, pero no puede superar las 100 unidades de la bateria.
                # disparar(un_objetivo): le consume el 10% de la bateria que posea. 

    Realizar los test necesarios que validen 
    el comportamiento.         
"""

"""
    Ejercicio 9:
        Extienda el modelo del Robot para que ahora pueda recibir 
        un disparo. Recibir un disparo le consume el 30% de su bateria.

        Realice los test necesarios que validen su comportamiento.
"""

class Robot(object):
    """  """

    def __init__(self, bateria: int) -> None:
        self.__bateria = bateria
        self.__CARGA_MAX = 100

    @property
    def bateria(self): return self.__bateria

    def caminar(self, diastancia: int) -> None:
        """ Consume 1 unidad de bateria cada 10 metros  """
        if diastancia < 0 :  diastancia *= -1
        unidades = diastancia / 10
            
        if self.bateria >= unidades and diastancia:
            self.__bateria -= unidades
        else:
            raise ValueError('no hay bateria suficiente')

    def cargarBateria(self, unidades: int):
        """ Le carga una determinada cantidad de unidades de bateria """
        if self.bateria + unidades <= self.__CARGA_MAX:
            self.__bateria += unidades
        else:
            self.__bateria = self.__CARGA_MAX

    def disparar(self, un_objetivo: Union[Alien,Mosquito,Robot]):
        """ Le consume el 10% de la bateria actual por disparo """        
        self.__bateria -= self.bateria *0.1
        un_objetivo.recibirDisparo()
    
    def recibirDisparo(self):
        """ Al recibir un disparo la bateria baja un 30% """
        self.__bateria -= self.bateria *0.3


    

if __name__ == '__main__':
    
   pass




