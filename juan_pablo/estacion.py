""" 
    Estacion:
            ✅ Tienen un conjunto de surtidores
            ✅ Al instanciarse no tendrá surtidores
            ✅ Podrá agregar un surtidor
            ✅ Saber cuantos surtidores tiene

            ✅ Saber cuáles son su surtidores vacios
            ✅ Saber cuantos surtidores vacios tiene 
            
            ✅ Sumar total de litros que faltan para 
                completar su capacidad total
            ✅ Obtener el costo total para completar 
                la carga faltante dado un precio por litro                
                
 """
from excepcion_estacion import SurtidoresLlenos
from surtidor import Surtidor 
from functools import reduce
class Estacion():
    """  """
    def __init__(self) -> None:
        self.__surtidores = []
        
    @property
    def surtidores(self): return self.__surtidores
    

    def agregarSurtidor(self, un_surtidor: Surtidor) -> None:
        """ Agrega un surtidor a la colección """
        self.__surtidores.append(un_surtidor)

    def cantidadDeSurtidores(self) -> int:
        """ Cuenta la cantidad de surtidores añadidos """
        return len(self.surtidores)

    def surtidoresVacios(self) -> list[Surtidor]:
        """ Retorna la lista de surtidores vacios."""
        # surtidoresVacios = lambda surtidor: surtidor.estaVacio()
        return list(filter(Surtidor.estaVacio, self.surtidores))

    def cantidadDeSurtidoresVacios(self) -> int:
        """ Retorna la cantidad de surtidores vacios """
        return len(self.surtidoresVacios())

    def totalDeLitrosFaltantes(self) -> int:
        """ Suma la cantidad de litros que faltan para completar la carga
        de los surtidores. """
        suma = lambda acumulador, surtidor: acumulador + surtidor.cargaFaltante()
        return reduce(suma, self.surtidores, 0)

    def costoTotaDeCargaFaltante(self, precio_por_litro: int) -> int:
        """ Retorna el precio de los litros faltantes """
        if self.totalDeLitrosFaltantes() > 0:
            return precio_por_litro * self.totalDeLitrosFaltantes()
        else:
            raise SurtidoresLlenos



if __name__ == '__main__':
    pass