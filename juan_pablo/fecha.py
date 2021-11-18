"""
    Ejercicio 2:
        Modelar el objeto fecha en donde tendra:
            - un dia 
            - un mes 
            - un anio 
        
        y debera poder compararse con otra fecha:
            - (==, <, <=, >=, >)
            - esta entre "una_fecha" y "otra_fecha"

        Realizar los test necesarios que validen 
        el comportamiento.  
"""
from __future__ import annotations

class Fecha(object):
    def __init__(self, dia: int, mes: int, anio: int) -> None:
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    @property
    def dia(self): return self.__dia
    @property
    def mes(self): return self.__mes
    @property
    def anio(self): return self.__anio

    def esIgual(self, una_fecha: Fecha) -> bool:
        """Comparar si la fecha ingresada es igual a la fecha almacenada  """
        # return verAnio() == anio  and  verMes() == mes  and  verDia() == dia
        return(
            self.anio == una_fecha.anio
            and
            self.mes == una_fecha.mes
            and
            self.dia == una_fecha.dia
        )
    
    def esMenor(self, una_fecha: Fecha) -> bool:
        """Comparar si la fecha ingresada es menor a la fecha almacenada  """
        return (
            self.anio < una_fecha.anio 
            or 
            
            (
                self.anio == una_fecha.anio and
                self.mes < una_fecha.mes
            ) 
            
            or
            
            (
                self.anio == una_fecha.anio and
                self.mes == una_fecha.mes and
                self.dia < una_fecha.dia   
            )        
        )

    def esMenorOIgual(self, una_fecha: Fecha) -> bool:
        """ Responde si es menor o igual a otra fecha """
        return self.esMenor(una_fecha) or self.esIgual(una_fecha)


    def esMayor(self, una_fecha: Fecha) -> bool:
        """ Responde si es mayor a otra fecha """
        return not self.esMenorOIgual(una_fecha)

    def esMayorOIgual(self, una_fecha: Fecha) -> bool:
        """ Responde si es mayor o igual """
        return not self.esMenor(una_fecha)

    def entreDosFechas(self, una_fecha: Fecha, otra_fecha: Fecha) -> bool:
        """ Responde si se encuentra entre dos fechas pasadas como parametro """
        return (
            self.esMayorOIgual(una_fecha)
            and 
            self.esMenorOIgual(otra_fecha)
        )



if __name__ == '__main__':
    _1_2_2001 = Fecha(1, 2, 2001)
    _1_3_2000 = Fecha(1, 3, 2000)
   
    # print(_1_2_2021.esIgual(_1_3_2000))       
    print(_1_2_2001.esMenor(_1_3_2000))       
    



















    # def __init__(self, dia:int , mes:int , anio:int  ) -> None:
    #     self.__dia = dia
    #     self.__mes = mes
    #     self.__anio = anio

    # def setearUnaFecha(self, dia:int, mes:int, anio:int ) -> None:
    #     self.dia = dia
    #     self.mes = mes
    #     self.anio = anio
    

    

    # def fechasIguales(self, fecha: 'Fecha') -> bool:
    #     return fecha == pass






















        
        



    
  





   
    

    

