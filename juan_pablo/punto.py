from __future__ import annotations
"""
    Ejercicio 3:

        Implemente la clase Punto: 
            que represente un punto en el plano de coordenadas (x,y). 
        Las instancias de dicha clase deben responder al mensaje:
        👉🏻 distanciaA(otroPunto). Que retorna la distancia entre dos puntos
                usando el teorema de Pitágoras.
        👉🏻 si es igual a otro punto.

        Pista:
            🛠 El metodo abs(un_numero) devuelve el valor absoluto de un numero
            ej: 
                abs(2)    >>> 2
                abs(-2)   >>> 2

            🛠 El metodo math.pow(un_numero, 2) eleva un numero al cuadrado
            🛠 El metodo math.sqrt(un_numero) devuelve la raiz cuadrada
             👉🏻 Para hacer uso de estos se debe importar el modulo math incluido en Python
                
            ej:
                import math

                math.pow(3, 2) >>> 9
                math.sqrt(9)   >>> 3
"""
import math
class Punto(object):
    def __init__(self, coordenadaX: int, coordenadaY : int) -> None:
        self.__x = coordenadaX
        self.__y = coordenadaY 
        
    @property
    def x(self): return self.__x
    @property
    def y(self): return self.__y
    
    def distancia(self, un_punto: Punto):
        """ Calcula la distancia entre dos puntos  """  
        delta_x = un_punto.x - self.x
        delta_y = un_punto.y - self.y
        return math.sqrt(math.pow( delta_x, 2) + math.pow(delta_y, 2))
    
    # overloading ==
    def __eq__(self, un_punto: 'Punto'):
        """ Un punto es igual a otro """
        return self.x == un_punto.x and self.y == un_punto.y
        


if __name__ == '__main__':
    pt1 = Punto(2,2)
    pt2 = Punto(3,2)

    print(pt1.distancia(pt2))

