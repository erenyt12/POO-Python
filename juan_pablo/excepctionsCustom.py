""" Excepciones Personalizadas """

class LaCargaNoPuedeSuperarLaCargaMax(Exception):
    """ Imposible realizar una carga que supere 
    la carga maxima admitida """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)