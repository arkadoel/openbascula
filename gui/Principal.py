from PyQt4 import QtGui
import Constantes as const

class V_Principal(QtGui.QMainWindow):
    """
    Clase que se ocupa de la ventana principal de la aplicacion
    """
    def __init__(self):
        super(V_Principal, self).__init__(parent=None)
        self.setGeometry(30, 40, 1000, 650)
        self.setWindowTitle(const.APP_NAME + " " + const.APP_VERSION)