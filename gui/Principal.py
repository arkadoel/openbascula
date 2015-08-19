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
        #self.setWindowIcon(QtGui.QIcon('icono.png'))

        self.iniciar_controles()

        self.grid_fondo.addWidget(self.lblCabina, 0, 0)
        self.grid_fondo.addWidget(self.lblRemolque, 1, 0)
        self.grid_fondo.addWidget(self.lblFechaEntrada, 0, 3)
        self.grid_fondo.addWidget(self.lblProducto, 2, 0)
        self.grid_fondo.addWidget(self.lblCliente, 3, 0)
        self.grid_fondo.addWidget(self.lblProveedor, 4, 0)
        self.grid_fondo.addWidget(self.lblAgencia, 5, 0)
        self.grid_fondo.addWidget(self.lblPoseedor, 6, 0)
        self.grid_fondo.addWidget(self.lblConductor, 7, 0)

        self.grid_fondo.addWidget(self.txtCabina, 0, 1, 1, 1)
        self.grid_fondo.addWidget(self.txtRemolque, 1, 1, 1, 1)
        self.grid_fondo.addWidget(self.dtFechaEntrada, 0, 4, 1, 1)
        self.grid_fondo.addWidget(self.txtProducto, 2, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtCliente, 3, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtProveedor, 4, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtAgencia, 5, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtPoseedor, 6, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtConductor, 7, 1, 1, 5)

        self.grid_fondo.addWidget(self.btnProductos, 2, 6)

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

        self.txtCabina = QtGui.QLineEdit(self)
        self.txtCabina.setMaximumWidth(200)
        self.txtRemolque = QtGui.QLineEdit(self)
        self.txtRemolque.setMaximumWidth(200)
        self.txtProducto = QtGui.QLineEdit(self)
        self.txtCliente = QtGui.QLineEdit(self)
        self.txtProveedor = QtGui.QLineEdit(self)
        self.txtAgencia = QtGui.QLineEdit(self)
        self.txtPoseedor = QtGui.QLineEdit(self)
        self.txtConductor = QtGui.QLineEdit(self)

        self.btnProductos = QtGui.QPushButton('Buscar', self)
        self.dtFechaEntrada = QtGui.QDateTimeEdit(self)

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
                                           self.formato_matricula(
                                               control=self.txtCabina
                                           ))

        self.txtRemolque.textChanged.connect(lambda:
                                             self.formato_matricula(
                                                 control=self.txtRemolque
                                             ))

    def pulsado_enter(self, control=''):
        print('pulsado enter')

    def formato_matricula(self, control=None):
        """
        Pone en mayusculas y agrega guiones cuando se cambia entre letras y digitos
        :param control: QLineEdit que se quiere manejar
        """
        if control is not None:

            if len(control.text()) > 1:
                texto = control.text()

                print('%s __ %s' % (texto[-2], texto[-1]))
                if texto[-2].isdigit() and texto[-1].isalpha()\
                        or texto[-2].isalpha() and texto[-1].isdigit():
                    letra = texto[-1]
                    texto = texto[0:-1] + '-' + letra
                    control.setText(texto)

            #poner los espacios como guiones
            if ' ' in control.text()[-1]:
                control.setText(control.text().replace(' ', '-'))
            #poner el texto en mayusculas
            control.setText(control.text().upper())

    def poner_estilos(self):

        qss = open('gui/estilo.qss').read()
        self.setStyleSheet(qss)
