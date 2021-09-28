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

    #------------ Metodos privados ---------- #

    def __consumo(__, metros):
        """ Calcula las unidades de bateria requeridas para recorrer una distancia """
        return metros / 10

    def __consumoAccesible(self, unidades):
        """ Determina si el consumo es accesible """
        return self.bateria >= unidades

    def __cargaExcedeElMaximo(self, unidades):
        """ Determina si la carga mas la bateria existente excede la carga maxima"""
        return self.bateria + unidades > 100

    # ---------- Metodos publicos ----------- #

    def caminar(self, metros):
        """ Caminar requiere 1 unidad cada 10 metros, 
            en caso de no contar conla batería suficiente 
            arrojará una excepción."""
        unidades_requeridas = self.__consumo(metros)

        if self.__consumoAccesible(unidades_requeridas):
            self.__bateria = self.bateria - unidades_requeridas
        else:
            raise ValueError('Bateria insuficiente.')

    def cargarBateria(self, unidades):
        """ Carga la bateria con la cantidad recibida por parametro """
        if self.__cargaExcedeElMaximo(unidades):
            self.__bateria = 100
        else:
            self.__bateria = self.bateria + unidades

    def disparar(self, objetivo):
        """ Disparar a un objetivo le consume el 10% de la batería """
        quita = self.bateria * 0.1
        self.__bateria = self.bateria - quita
