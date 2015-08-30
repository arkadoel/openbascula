from PyQt4 import QtGui, QtCore
import core.Fechas
import Constantes as const
from gui import Util

class V_Principal(QtGui.QMainWindow):
    """
    Clase que se ocupa de la ventana principal de la aplicacion
    """
    def __init__(self):
        super(V_Principal, self).__init__(parent=None)
        self.setGeometry(30, 40, 1000, 650)
        self.setWindowTitle(const.APP_NAME + " " + const.APP_VERSION)
        #self.setWindowIcon(QtGui.QIcon('icono.png'))

        self.iniciar_controles()

        self.grid_fondo.addWidget(self.btnNuevo, 0, 0)
        self.grid_fondo.addWidget(self.lblCabina, 1, 0)
        self.grid_fondo.addWidget(self.lblRemolque, 1, 3)
        self.grid_fondo.addWidget(self.lblFechaEntrada, 2, 3)
        self.grid_fondo.addWidget(self.lblProducto, 3, 0)
        self.grid_fondo.addWidget(self.lblCliente, 4, 0)
        self.grid_fondo.addWidget(self.lblProveedor, 5, 0)
        self.grid_fondo.addWidget(self.lblAgencia, 6, 0)
        self.grid_fondo.addWidget(self.lblPoseedor, 7, 0)
        self.grid_fondo.addWidget(self.lblConductor, 8, 0)
        self.grid_fondo.addWidget(self.lblPesoEntrada, 9, 0)
        self.grid_fondo.addWidget(self.lblPesoSalida, 10, 0)
        self.grid_fondo.addWidget(self.lblNeto, 11, 0)

        self.grid_fondo.addWidget(self.txtCabina, 1, 1, 1, 3)
        self.grid_fondo.addWidget(self.txtRemolque, 1, 4, 1, 1)
        self.grid_fondo.addWidget(self.dtFechaEntrada, 2, 4, 1, 1)
        self.grid_fondo.addWidget(self.txtProducto, 3, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtCliente, 4, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtProveedor, 5, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtAgencia, 6, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtPoseedor, 7, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtConductor, 8, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtPesoEntrada, 9, 1)
        self.grid_fondo.addWidget(self.txtPesoSalida, 10, 1)
        self.grid_fondo.addWidget(self.txtNeto, 11, 1)

        self.grid_fondo.addWidget(self.btnProductos, 3, 6, 1, 1)
        self.grid_fondo.addWidget(self.btnCliente, 4, 6, 1, 1)
        self.grid_fondo.addWidget(self.btnProveedor, 5, 6, 1, 1)
        self.grid_fondo.addWidget(self.btnAgencia, 6, 6, 1, 1)
        self.grid_fondo.addWidget(self.btnPoseedor, 7, 6, 1, 1)
        self.grid_fondo.addWidget(self.btnConductor, 8, 6, 1, 1)

        self.vbox_fondo.addLayout(self.grid_fondo)
        self.vbox_fondo.addStretch(0)
        self.frame.setLayout(self.vbox_fondo)

        self.setCentralWidget(self.frame)

    def iniciar_controles(self):
        """
        Zona para iniciar todos los controles
        """
        self.frame = QtGui.QFrame(parent=self)
        self.frame.setObjectName('myFrame')

        self.lblCabina = QtGui.QLabel('CABINA', self)
        self.lblRemolque = QtGui.QLabel('REMOLQUE', self)
        self.lblFechaEntrada = QtGui.QLabel('ENTRADA', self)
        self.lblProducto = QtGui.QLabel('PRODUCTO', self)
        self.lblCliente = QtGui.QLabel('CLIENTE', self)
        self.lblProveedor = QtGui.QLabel('PROVEEDOR', self)
        self.lblAgencia = QtGui.QLabel('AGENCIA', self)
        self.lblPoseedor = QtGui.QLabel('POSEEDOR', self)
        self.lblConductor = QtGui.QLabel('CONDUCTOR', self)
        self.lblPesoEntrada = QtGui.QLabel('Kg. ENTRADA', self)
        self.lblPesoSalida = QtGui.QLabel('Kg. SALIDA', self)
        self.lblNeto = QtGui.QLabel('NETO', self)

        self.txtCabina = QtGui.QLineEdit(self)
        self.txtCabina.setObjectName('txtCabina')
        self.txtCabina.setMaximumWidth(200)
        self.txtRemolque = QtGui.QLineEdit(self)
        self.txtRemolque.setObjectName('txtRemolque')
        self.txtRemolque.setMaximumWidth(200)
        self.txtProducto = QtGui.QLineEdit(self)
        self.txtCliente = QtGui.QLineEdit(self)
        self.txtProveedor = QtGui.QLineEdit(self)
        self.txtAgencia = QtGui.QLineEdit(self)
        self.txtPoseedor = QtGui.QLineEdit(self)
        self.txtConductor = QtGui.QLineEdit(self)
        self.txtPesoEntrada = QtGui.QLineEdit(self)
        self.txtPesoEntrada.setMaximumWidth(200)
        self.txtPesoSalida = QtGui.QLineEdit(self)
        self.txtPesoSalida.setMaximumWidth(200)
        self.txtNeto = QtGui.QLineEdit(self)
        self.txtNeto.setMaximumWidth(200)

        self.btnProductos = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnCliente = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnProveedor = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnAgencia = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnPoseedor = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnConductor = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnNuevo = QtGui.QPushButton(const.NUEVO, self)
        self.dtFechaEntrada = QtGui.QDateTimeEdit(self)

        self.habilitar_controles(habilitar=False)

        self.poner_estilos()
        self.iniciar_eventos()
        self.vbox_fondo = QtGui.QVBoxLayout()
        self.grid_fondo = QtGui.QGridLayout()

    def iniciar_eventos(self):
        self.txtCabina.returnPressed.connect(lambda:
                                             self.pulsado_enter(
                                                 control='txtcabina'
                                             ))
        self.txtCabina.textChanged.connect(lambda:
                                           Util.formato_matricula(
                                               control=self.txtCabina
                                           ))

        self.txtRemolque.textChanged.connect(lambda:
                                             Util.formato_matricula(
                                                 control=self.txtRemolque
                                             ))

        self.txtPoseedor.textChanged.connect(lambda:
                                             Util.formato_mayuscula(
                                                 control=self.txtPoseedor
                                             ))
        self.txtProducto.textChanged.connect(lambda:
                                             Util.formato_mayuscula(
                                                 control=self.txtProducto
                                             ))
        self.txtConductor.textChanged.connect(lambda:
                                             Util.formato_mayuscula(
                                                 control=self.txtConductor
                                             ))
        self.txtAgencia.textChanged.connect(lambda:
                                             Util.formato_mayuscula(
                                                 control=self.txtAgencia
                                             ))
        self.txtCliente.textChanged.connect(lambda:
                                             Util.formato_mayuscula(
                                                 control=self.txtCliente
                                             ))
        self.txtProveedor.textChanged.connect(lambda:
                                             Util.formato_mayuscula(
                                                 control=self.txtProveedor
                                             ))
        self.txtNeto.textChanged.connect(lambda:
                                             Util.formato_numerico(
                                                 control=self.txtNeto
                                             ))
        self.txtPesoEntrada.textChanged.connect(lambda:
                                             Util.formato_numerico(
                                                 control=self.txtPesoEntrada
                                             ))
        self.txtPesoSalida.textChanged.connect(lambda:
                                             Util.formato_numerico(
                                                 control=self.txtPesoSalida
                                             ))
        self.btnNuevo.clicked.connect(lambda: self.clickAction('Nuevo/guardar'))
        self.btnProductos.clicked.connect(lambda: self.clickAction('Buscar: Productos'))
        self.btnCliente.clicked.connect(lambda: self.clickAction('Buscar: Clientes'))
        self.btnProveedor.clicked.connect(lambda: self.clickAction('Buscar: Proveedor'))
        self.btnAgencia.clicked.connect(lambda: self.clickAction('Buscar: Agencia'))
        self.btnPoseedor.clicked.connect(lambda: self.clickAction('Buscar: Poseedor'))
        self.btnConductor.clicked.connect(lambda: self.clickAction('Buscar: Conductor'))

    def clickAction(self, accion=''):

        if accion != '':
            if 'Nuevo/guardar' in accion:
                if const.NUEVO in self.btnNuevo.text():
                    self.habilitar_controles(habilitar=True)

                elif const.GUARDAR in self.btnNuevo.text():
                    self.habilitar_controles(habilitar=False)
            elif 'Buscar: ' in accion:
                lugar = accion.replace('Buscar: ', '')
                print(lugar)


    def habilitar_controles(self, habilitar=False):

        self.txtCabina.setEnabled(habilitar)
        self.txtRemolque.setEnabled(habilitar)
        self.txtCliente.setEnabled(habilitar)
        self.txtAgencia.setEnabled(habilitar)
        self.txtProveedor.setEnabled(habilitar)
        self.txtConductor.setEnabled(habilitar)
        self.txtPoseedor.setEnabled(habilitar)
        self.txtProducto.setEnabled(habilitar)
        self.dtFechaEntrada.setEnabled(habilitar)

        if habilitar is False:
            #limpiamos los controles
            self.txtCabina.setText('')
            self.txtRemolque.setText('')
            self.txtCliente.setText('')
            self.txtAgencia.setText('')
            self.txtProveedor.setText('')
            self.txtConductor.setText('')
            self.txtPoseedor.setText('')
            self.txtProducto.setText('')

            #cambiar color a gris
            self.txtCabina.setStyleSheet('background-color: gainsboro;')
            self.txtRemolque.setStyleSheet('background-color: gainsboro;')
            self.txtCliente.setStyleSheet('background-color: gainsboro;')
            self.txtAgencia.setStyleSheet('background-color: gainsboro;')
            self.txtProveedor.setStyleSheet('background-color: gainsboro;')
            self.txtConductor.setStyleSheet('background-color: gainsboro;')
            self.txtPoseedor.setStyleSheet('background-color: gainsboro;')
            self.txtProducto.setStyleSheet('background-color: gainsboro;')
            self.dtFechaEntrada.setStyleSheet('background-color: gainsboro;')
            self.txtPesoEntrada.setStyleSheet('background-color: gainsboro;')
            self.txtPesoSalida.setStyleSheet('background-color: gainsboro;')
            self.txtNeto.setStyleSheet('background-color: gainsboro;')
            self.btnNuevo.setText(const.NUEVO)
        else:
            self.txtCabina.setStyleSheet('background-color: white;')
            self.txtRemolque.setStyleSheet('background-color: white;')
            self.txtCliente.setStyleSheet('background-color: white;')
            self.txtAgencia.setStyleSheet('background-color: white;')
            self.txtProveedor.setStyleSheet('background-color: white;')
            self.txtConductor.setStyleSheet('background-color: white;')
            self.txtPoseedor.setStyleSheet('background-color: white;')
            self.txtProducto.setStyleSheet('background-color: white;')
            self.dtFechaEntrada.setStyleSheet('background-color: white;')
            self.txtPesoSalida.setStyleSheet('background-color: white;')
            self.txtPesoEntrada.setStyleSheet('background-color: white;')
            self.txtNeto.setStyleSheet('background-color: white;')
            self.btnNuevo.setText(const.GUARDAR)
            self.txtCabina.setFocus()
            self.dtFechaEntrada.setDateTime(QtCore.QDateTime.currentDateTime())



    def pulsado_enter(self, control=''):
        print('pulsado enter en ' + control)

        if control != '':
            if 'txtCabina' in control:
                self.txtRemolque.setFocus()


    def poner_estilos(self):

        qss = open('gui/estilo.qss').read()
        self.setStyleSheet(qss)
