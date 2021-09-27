"""
    Ejercicio 1:
        Modelar el objeto caja de ahorro:
            - un titular
            - un saldo
        
        y debera poder:
            - depositar un monto
            - extraer un monto
            - en el caso de querer extraer un monto superior 
              al monto disponiple arrojara una 
              excepcion ValueError("Imposible realizar extracción.")

        Realizar los test necesarios que validen 
        el comportamiento.  
"""

class CajaDeAhorro(object):
    def __init__(self, titular, saldo):
      self.__titular = titular
      self.__saldo = saldo
      
      
    @property
    def titular(self): return self.__titular
    
    @property
    def saldo(self): return self.__saldo
    
    # -------- Metodos de la clase -------- #
    def depositar(self, un_monto): self.__saldo = un_monto
    
    def extraer(self, un_monto): 
        if un_monto <= self.saldo:
            self.__saldo = self.__saldo - un_monto
        else:
            raise ValueError('Imposible realizar la extracción.')
        

if __name__ == "__main__":
    cuenta  = CajaDeAhorro('Niko', 0)
    
    print(hasattr(cuenta, 'saldo'))