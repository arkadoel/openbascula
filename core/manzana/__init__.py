"""
Parte del codigo encargada de la caducidad del mismo

Se establecerá un periodo de seis meses de caducidad desde su primer uso
"""
class Caducidad:

    def __init__(self):
        self.__LAST_UPDATE_FILE__ = 'updates.db'
