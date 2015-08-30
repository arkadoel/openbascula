
from PyQt4 import QtGui
import Constantes as const

class Ventana_buscar(QtGui.QWidget):
    """
    Clase encargada del dialogo de buscar
    """
    def __init__(self, parent=None, buscar=''):
        self.parent = parent

        super(Ventana_buscar, self).__init__(parent=self.parent)
        self.setGeometry(30, 40, 1000, 650)
        self.setWindowTitle("Busqueda de ".join(buscar))

