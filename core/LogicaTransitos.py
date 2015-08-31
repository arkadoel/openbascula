
from directORM.forTransito_actuales import Transito_actual, TbTransito_actuales

class Logica_Transitos:

    def __init__(self):
        pass

    def guardar_transito(self, transito=None):
        '''
        Guarda un transito en la base de datos
        :param transito:
        '''
        if transito is not None:
            tabla = TbTransito_actuales()
            tabla.save(transito)

