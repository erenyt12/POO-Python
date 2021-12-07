from __future__ import annotations
from punto import Punto
class Circulo():
    """ pass """
    def __init__(self,  un_centro: Punto, un_radio: int) -> None:
        self.__centro = un_centro
        self.__radio = un_radio

    @property
    def centro(self): return self.__centro
    @property
    def radio(self): return self.__radio

    def contieneAUnPunto(self, un_punto: Punto) -> bool:
        """ Devuelve true si un punto (x,y) se encuentra dentro del ciruclo """
        return Punto.distancia(self.centro, un_punto) < self.radio

        # return dis <= self.radio

    def circuloSuperPuesto(self, un_circulo: Circulo) -> bool:
        """ Devuelve true si el circulo esta superpuesto """
        return(self.centro == un_circulo.centro and self.radio == un_circulo.radio)
if __name__ == '__main__':
    pass

    