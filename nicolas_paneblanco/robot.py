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
    def __init__(self, bateria):
        self.__bateria = bateria
        
    @property
    def bateria(self): return self.__bateria
    
    # Calcula las unidades de bateria requeridas
    def __consumo(__, metros): return metros / 10
    
    # Determina si el consumo es accesible
    def __consumoAccesible(self, unidades): 
        return self.bateria >= unidades
    
    # Metodo caminar una cantidad de metros
    def caminar(self, metros):
        """ Caminar requiere 1 unidad cada 10 metros, 
            en caso de no contar conla batería suficiente 
            arrojará una excepción."""
        unidades_requeridas = self.__consumo(metros)
        if self.__consumoAccesible(unidades_requeridas):
            self.__bateria = self.__bateria - unidades_requeridas
        else:
            raise ValueError('Bateria insuficiente.')