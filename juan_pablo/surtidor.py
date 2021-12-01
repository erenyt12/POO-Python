"""
    Ejercicio 1:
        Estación de servicio

        Surtidor: 
            ✅ Poseen una carga inicialmente en 0
            ✅ Posee una capacidad maxima al instanciarse
            ✅ Sabe si esta vacío 
            ✅ Sabe cuanto lugar libre tiene para cargar
            ✅ Puede recibir una carga

"""

from excepctionsCustom import LaCargaNoPuedeSuperarLaCargaMax


class Surtidor(object):
    """ Clase Surtidor

        Mensajes: 
            ✅ carga 
            ✅ cargaMax

            ✅ estaVacio: responde true si esta vacio 
            ✅ cargaFaltante: carga faltante
            ✅ cargar(una_carga): carga el surtidor 
    """

    def __init__(self, carga_max: int) -> None:
        self.__carga = 0
        self.__CARGAMAX = carga_max

    @property
    def carga(self): return self.__carga
    @property
    def cargaMax(self): return self.__CARGAMAX

    def estaVacio(self) -> bool:
        """ Responde true si su carga es igual a 0  """
        return self.carga == 0

    def cargaFaltante(self) -> int:
        """ Devuelve la carga faltante """
        return self.cargaMax - self.carga

    def cargar(self, una_carga: int) -> None:
        """ Le agrega una carga al surtidor """
        if una_carga + self.carga <= self.cargaMax:
            self.__carga += una_carga
        else:
            raise LaCargaNoPuedeSuperarLaCargaMax
       
        


































if __name__ == '__main__':
    sur = Surtidor(1)

    print(sur.carga)
    print(sur.estaVacio())











