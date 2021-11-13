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
    """ 
        Clase Fecha
        
        Atributos: dia - mes - anio
        
        Metodos: 
            ✅ dia 
            ✅ mes
            ✅ anio 
            
            ✅ == : igualdad con otra Fecha
            ✅ <  : menor que otra Fecha
            ✅ <= : menor o igual que otra Fecha
            ✅ >= : mayor o igual que otra Fecha
            ✅ >  : mayor que otra Fecha
            ✅ entreDosFechas: responde True si se encuentra entre dos fechas
                            que recibe por parametro.
    """
    def __init__(self, un_dia: int, un_mes: int, un_anio: int) -> None:
        self.__dia = un_dia
        self.__mes = un_mes
        self.__anio = un_anio  
        
    @property
    def dia(self): return self.__dia
    @property
    def mes(self): return self.__mes
    @property
    def anio(self): return self.__anio
    
    # Overloading del operador "=="
    def __eq__(self, una_fecha: Fecha) -> bool:
        """ Comparación de igualdad """
        return ( 
                    self.anio == una_fecha.anio and 
                    self.mes  == una_fecha.mes  and 
                    self.dia  == una_fecha.dia 
               )
    
    # Overloading del operador "<"
    def __lt__(self, una_fecha: Fecha) -> bool:
        """ Comparación menor a otra Fecha """
        return ( 
                    (   self.anio <  una_fecha.anio ) 
                    or 
                    ( 
                        self.anio == una_fecha.anio and 
                        self.mes  <  una_fecha.mes 
                    ) 
                    or 
                    ( 
                        self.anio == una_fecha.anio and 
                        self.mes  == una_fecha.mes  and 
                        self.dia  <  una_fecha.dia 
                    )
                )
        
    # Overloading del operador "<="
    def __le__(self, una_fecha: Fecha) -> bool:
        """ Comparación menor o igual a otra Fecha """
        return ( 
                    (   self <  una_fecha ) 
                    or 
                    ( 
                        self == una_fecha
                    ) 
                )
        
    # Overloading del operador ">="
    def __ge__(self, una_fecha: Fecha) -> bool:
        """ Comparación mayor o igual a otra Fecha """
        return not self <  una_fecha 
    
    # Overloading del operador ">"
    def __gt__(self, una_fecha: Fecha) -> bool:
        """ Comparación mayor a otra Fecha """
        return not  self <=  una_fecha 
    
    # Funcion de comparacion entre 
    def entreDosFechas(self, fecha_inicio: Fecha, fecha_fin: Fecha) -> bool:
        """ Devuelve True si se encuentra entre las
            dos fechas que recibe como parametro."""
        return fecha_inicio <= self and fecha_fin >= self
        

if __name__ == "__main__":
    _1_4_2020  = Fecha(1,4,2020)
    _10_4_2020 = Fecha(10,4,2020)
    _30_4_2020 = Fecha(30,4,2020)
    
    respuesta = _1_4_2020 <= _10_4_2020
    
    print(respuesta)