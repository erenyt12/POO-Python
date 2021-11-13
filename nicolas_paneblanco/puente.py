"""
    Modelar: un Puente

        atributos: 
            - numero
            - valla

        puede:
            - ver su numero
            - ver si la valla esta alta
            - bajar la valla
            - levantar la valla
"""

"""
    Extender el modelo del puente para que pueda recibir un auto como 
    parametro. 
        - en caso de que la valla del puente este levantada los autos 
          pueden circular a 40km/h
        - si la valla esta baja le envia el mensaje detenerse al vehiculo
          que lo transita.
"""
from nicolas_paneblanco.valla import Valla
from nicolas_paneblanco.auto import Auto

class Puente(object):
    """ 
        Clase Puente
        
        Metodos:
            ✅ numero: muestra el numero del puente
            ✅ vallaAlta: responde si la valla esta alta
            ✅ bajarValla: baja la valla 
            ✅ subirValla: sube la valla      
    """
    def __init__(self, un_numero: int) -> None:
        self.__numero = un_numero
        self.__valla = Valla()
        
    @property
    def numero(self): return self.__numero
    
    def vallaAlta(self) -> bool:
        """ Devuelve True si la valla del puente esta alta """
        return self.__valla.alta
    
    def bajarValla(self) -> None:
        """ Baja la valla del puente """
        if self.vallaAlta(): self.__valla.cambiarEstado()
        
    def subirValla(self) -> None:
        """ Sube la valla del puente """
        if not self.vallaAlta(): self.__valla.cambiarEstado()


    def recibirAuto(self, un_auto: Auto) -> None:
        """ Recibe un auto y rige su velocidad """
        if self.vallaAlta():
            un_auto.detenerse()
            un_auto.acelerar(40)
        else: un_auto.detenerse()


if __name__ == '__main__':
    pass