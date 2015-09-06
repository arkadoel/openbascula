# -*- coding: utf-8 -*-
__author__ = 'https://github.com/arkadoel'
__version__ = '0.0.1'
__license__ = 'Gen Source v0.1 (compatible con GPLv3)'

import sys
import os

from PyQt4 import QtGui

from core.Constantes import *
from gui.Principal import V_Principal
from core.LogicaConfiguracion import Logica_Configuracion
from directORM import Db


def abrir_ventana():
    """
    Abrir la ventana principal
    """
    app = QtGui.QApplication(sys.argv)
    v = V_Principal()
    v.show()

    sys.exit(app.exec_())

def carga_configuraciones():
    """
    Cargar las configuraciones iniciales que sean necesarias
    """
    Db.DB_PATH = os.path.join(os.getcwd(), 'db/pesaje.db')
    Logica_Configuracion()

if __name__ == '__main__':
    print('Iniciando %s %s' % (APP_NAME, APP_VERSION))
    carga_configuraciones()
    abrir_ventana()


