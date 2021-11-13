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
from __future__ import annotations
from typing import Union
from alien import Alien
from mosquito import Mosquito

class Robot(object):
    """ Clase Robot
        
        Atributos: 
            batería: representa la batería con la que cuenta
            
        Metodos:
            caminar: consume unidades de energia, en caso de no contar 
                        con la capacidad de carga arroja una excepción.
                        
            cargarBateria: le permite agregar unidades de carga.
            
            disparar: consume unidades de energía, y envia el mensaje 
                        recibirDisparo al objeto que recibe como parametro.
    """
    def __init__(self, unidades_de_bateria: int) -> None:
        self.__bateria = unidades_de_bateria
        self.__CELDAS_MAX = 100

    @property
    def bateria(self): return self.__bateria

    # ---------- Metodos publicos ----------- #

    def caminar(self, metros: int) -> None:
        """ Caminar requiere 1 unidad cada 10 metros, en caso de no contar conla 
            batería suficiente arrojará una excepción."""
        celdas_necesarias = abs(metros) / 10
        if self.bateria >= celdas_necesarias:
            self.__bateria -= celdas_necesarias
        else:
            raise ValueError('Bateria insuficiente.')
        

    def cargarBateria(self, celdas_a_cargar: int) -> None:
        """ Carga la bateria con la cantidad recibida por parametro """
        if self.bateria + celdas_a_cargar > self.__CELDAS_MAX:
            self.__bateria = self.__CELDAS_MAX
        else:
            self.__bateria += celdas_a_cargar
            

    def disparar(self, objetivo: Union[Alien,Mosquito,Robot]) -> None:
        """ Disparar a un objetivo le consume el 10% de la batería """
        self.__bateria -= self.bateria * 0.1
        objetivo.recibirDisparo()
        

    def recibirDisparo(self) -> None:
        """ Recibir un disparo decrementa el 30% de la bateria """
        self.__bateria -= self.bateria * 0.3

if __name__ == '__main__':
    pass