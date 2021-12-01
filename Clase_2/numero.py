""" la clase Numero: 
   - (==, <, <=, >=, >)
   - esta entre "un_numero" y "otro_numero" """
from magnitud_lineal import MagnitudLineal

# class Numero(MagnitudLineal):


class Numero(MagnitudLineal):

    def __init__(self, numero) -> None:
        self.__numero = numero

    @property
    def numero(self): return self.__numero

    # overloading del operador "=="
    def __eq__(self, numero) -> bool: return self.numero == numero.numero

    # overloading del operador "<"
    def __lt__(self, numero) -> bool: return self.numero < numero.numero

    def entreDosNumeros(self, numero_1, numero_2) -> bool:
        return super().entre(numero_1, numero_2)


if __name__ == '__main__':
    numero_6 = Numero(6)
    numero_1 = Numero(1)

    
    print(numero_1 == numero_6)
