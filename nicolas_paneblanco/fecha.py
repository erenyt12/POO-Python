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

class Fecha(object):
    def __init__(self, un_dia, un_mes, un_anio) -> None:
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
    def __eq__(self, una_fecha):
        return ( 
                    self.anio == una_fecha.anio and 
                    self.mes  == una_fecha.mes  and 
                    self.dia  == una_fecha.dia 
               )
    
    # Overloading del operador "<"
    def __lt__(self, una_fecha):
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
    def __le__(self, una_fecha):
        return ( 
                    (   self <  una_fecha ) 
                    or 
                    ( 
                        self == una_fecha
                    ) 
                )
        
    # Overloading del operador ">="
    def __ge__(self, una_fecha):
        return not self <  una_fecha 
    
    # Overloading del operador ">"
    def __gt__(self, una_fecha):
        return not  self <=  una_fecha 
    
    # Funcion de comparacion entre 
    def entreDosFechas(self, fecha_inicio, fecha_fin):
        """ Devuelve unbooleano si se encuentra entre las
            dos fechas que recibe como parametro."""
        return fecha_inicio <= self and fecha_fin >= self
        

if __name__ == "__main__":
    _1_4_2020  = Fecha(1,4,2020)
    _10_4_2020 = Fecha(10,4,2020)
    _30_4_2020 = Fecha(30,4,2020)
    
    respuesta = _1_4_2020 <= _10_4_2020
    
    print(respuesta)