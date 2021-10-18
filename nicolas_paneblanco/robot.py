"""
    Ejercicio 3:
        Modelar la clase Robot con las siguientes caracteristicas:
            - Un robot posee una bateria en la cual almacena su energia.
              La carga de la bateria de encuentra en el rango de 0 a 100.
            - Un robot puede:
                # caminar(metros): le consume 1 unidad cada 10 metros.
                # cargarBateria(una_carga): le agrega una determinada cantidad
                  de unidades, pero no puede superar las 100 unidades de la bateria.
                # disparar(un_objetivo): le consume el 10% de la bateria que posea. 

    Realizar los test necesarios que validen 
    el comportamiento.         
"""


class Robot(object):
    """ Clase Robot
        
        Atributos: 
            batería: representa la batería con la que cuenta
            
        Metodos:
            caminar: consume unidades de energia, en caso de no contar 
                        con la capacidad de carga arroja una excepción.
                        
            cargarBateria: le permite agregar unidades de carga.
            
            disparar: consume unidades de energía, y envia el mensaje 
                        recibirDisparo al objeto que recibe como parametro.
    """
    def __init__(self, unidades_de_bateria: int) -> None:
        self.__bateria = unidades_de_bateria

    @property
    def bateria(self): return self.__bateria

    # ---------- Metodos publicos ----------- #

    def caminar(self, metros: int) -> None:
        """ Caminar requiere 1 unidad cada 10 metros, en caso de no contar conla 
            batería suficiente arrojará una excepción."""
        if self.bateria >= metros / 10:
            self.__bateria -= metros / 10
        else:
            raise ValueError('Bateria insuficiente.')
        

    def cargarBateria(self, unidades: int) -> None:
        """ Carga la bateria con la cantidad recibida por parametro """
        if self.bateria + unidades > 100:
            self.__bateria = 100
        else:
            self.__bateria += unidades
            

    def disparar(self, objetivo: any) -> None:
        """ Disparar a un objetivo le consume el 10% de la batería """
        self.__bateria -= self.bateria * 0.1
        objetivo.recibirDisparo()


if __name__ == '__main__':
    robot = Robot(20)