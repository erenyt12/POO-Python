"""
    Ejercicio 2:

        Implementar la clase Porcentaje tal que respete el siguiente protocolo:
        👉🏻 valor(unNumero). Indica el valor porcentual que va a representar el objeto.
        👉🏻 aplicarA(unNumero). Retorna el resultado de aplicar el porcentaje a un numero.

        Defina los tests de unidad que considere necesarios para esta clase.
"""
from excepcion import CeroDivididoUnNumeroReal

class Porcentaje(object):
    """ Clase porcentaje
        valor: Indica el valor porcentual que va a representar el objeto
         """

    def __init__(self, unNumero: int) -> None:
        self.__numero = unNumero

    @property
    def numero(self): return self.__numero

    def aplicarA(self, un_numero: int) -> int:
        if un_numero == 0:
            raise CeroDivididoUnNumeroReal
        else:    
            resultado = self.numero * un_numero /100
            return resultado




if __name__ == '__main__':
    porcentaje = Porcentaje(45)
    
    try:
        print(porcentaje.aplicarA(100))
    except CeroDivididoUnNumeroReal as error:
        print("error")
    