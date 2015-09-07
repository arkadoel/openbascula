from PyQt4 import QtGui, QtCore

import core.Fechas
from core import Constantes as const
from gui import Util
from gui.Dialogo_buscar import Ventana_buscar
from directORM.forTransito_actuales import Transito_actual
from core.LogicaTransitos import Logica_Transitos
from gui.Dialogo_impresion import Ventana_Imprimir


class V_Principal(QtGui.QMainWindow):
    """
    Clase que se ocupa de la ventana principal de la aplicacion
    """
    def __init__(self):
        super(V_Principal, self).__init__(parent=None)
        self.setGeometry(30, 40, 1000, 650)
        self.setWindowTitle(const.APP_NAME + " " + const.APP_VERSION)
        self.setWindowIcon(QtGui.QIcon(const.ICONO.LOGO))

        self.iniciar_controles()
        self.maquetar()

        self.transito_actual = None

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
        self.lblOrigen = QtGui.QLabel('ORIGEN', self)
        self.lblDestino = QtGui.QLabel('DESTINO', self)

        self.txtCabina = QtGui.QLineEdit(self)
        self.txtCabina.setObjectName('txtCabina')
        self.txtCabina.setMaximumWidth(200)
        self.txtRemolque = QtGui.QLineEdit(self)
        self.txtRemolque.setObjectName('txtRemolque')
        self.txtRemolque.setMaximumWidth(200)
        self.txtProducto = QtGui.QLineEdit(self)
        self.txtProducto.setReadOnly(True)
        self.txtCliente = QtGui.QLineEdit(self)
        self.txtCliente.setReadOnly(True)
        self.txtProveedor = QtGui.QLineEdit(self)
        self.txtProveedor.setReadOnly(True)
        self.txtAgencia = QtGui.QLineEdit(self)
        self.txtAgencia.setReadOnly(True)
        self.txtPoseedor = QtGui.QLineEdit(self)
        self.txtPoseedor.setReadOnly(True)
        self.txtConductor = QtGui.QLineEdit(self)
        self.txtConductor.setReadOnly(True)
        self.txtPesoEntrada = QtGui.QLineEdit(self)
        self.txtPesoEntrada.setObjectName('txtPesoEntrada')
        self.txtPesoEntrada.setMaximumWidth(200)
        self.txtPesoSalida = QtGui.QLineEdit(self)
        self.txtPesoSalida.setObjectName('txtPesoSalida')
        self.txtPesoSalida.setMaximumWidth(200)
        self.txtNeto = QtGui.QLineEdit(self)
        self.txtNeto.setObjectName('txtNeto')
        self.txtNeto.setMaximumWidth(200)
        self.txtOrigen = QtGui.QLineEdit(self)
        self.txtDestino = QtGui.QLineEdit(self)

        self.btnProductos = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnCliente = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnProveedor = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnAgencia = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnPoseedor = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnConductor = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)
        self.btnNuevo = QtGui.QPushButton(const.NUEVO, self)
        self.btnTransito = QtGui.QPushButton('EN TRANSITO', self)
        self.dtFechaEntrada = QtGui.QDateTimeEdit(self)

        self.habilitar_controles(habilitar=False)

        self.poner_estilos()
        self.iniciar_eventos()
        self.vbox_fondo = QtGui.QVBoxLayout()
        self.grid_fondo = QtGui.QGridLayout()

    def maquetar(self):
        self.grid_fondo.addWidget(self.btnNuevo, 0, 0)
        self.grid_fondo.addWidget(self.btnTransito, 0, 1)
        self.grid_fondo.addWidget(self.lblCabina, 1, 0)
        self.grid_fondo.addWidget(self.lblRemolque, 1, 3)
        self.grid_fondo.addWidget(self.lblFechaEntrada, 2, 3)
        self.grid_fondo.addWidget(self.lblProducto, 3, 0)
        self.grid_fondo.addWidget(self.lblCliente, 4, 0)
        self.grid_fondo.addWidget(self.lblProveedor, 5, 0)
        self.grid_fondo.addWidget(self.lblAgencia, 6, 0)
        self.grid_fondo.addWidget(self.lblPoseedor, 7, 0)
        self.grid_fondo.addWidget(self.lblConductor, 8, 0)
        self.grid_fondo.addWidget(self.lblOrigen, 9, 0)
        self.grid_fondo.addWidget(self.lblDestino, 10, 0)
        self.grid_fondo.addWidget(self.lblPesoEntrada, 11, 0)
        self.grid_fondo.addWidget(self.lblPesoSalida, 12, 0)
        self.grid_fondo.addWidget(self.lblNeto, 13, 0)

        self.grid_fondo.addWidget(self.txtCabina, 1, 1, 1, 3)
        self.grid_fondo.addWidget(self.txtRemolque, 1, 4, 1, 1)
        self.grid_fondo.addWidget(self.dtFechaEntrada, 2, 4, 1, 1)
        self.grid_fondo.addWidget(self.txtProducto, 3, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtCliente, 4, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtProveedor, 5, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtAgencia, 6, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtPoseedor, 7, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtConductor, 8, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtOrigen, 9, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtDestino, 10, 1, 1, 5)
        self.grid_fondo.addWidget(self.txtPesoEntrada, 11, 1)
        self.grid_fondo.addWidget(self.txtPesoSalida, 12, 1)
        self.grid_fondo.addWidget(self.txtNeto, 13, 1)

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


    def iniciar_eventos(self):
        self.txtCabina.returnPressed.connect(lambda:
                                             self.pulsado_enter(
                                                 control='txtcabina'
                                             ))
        self.txtPesoEntrada.returnPressed.connect(lambda:
                                             self.pulsado_enter(
                                                 control='txtPesoEntrada'
                                             ))
        self.txtPesoSalida.returnPressed.connect(lambda:
                                             self.pulsado_enter(
                                                 control='txtPesoSalida'
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
        self.txtOrigen.textChanged.connect(lambda:
                                             Util.formato_mayuscula(
                                                 control=self.txtOrigen
                                             ))
        self.txtDestino.textChanged.connect(lambda:
                                             Util.formato_mayuscula(
                                                 control=self.txtDestino
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
        self.btnTransito.clicked.connect(lambda: self.clickAction('Buscar: Transito'))

    def clickAction(self, accion=''):

        if accion != '':
            if 'Nuevo/guardar' in accion:
                if const.NUEVO in self.btnNuevo.text():
                    self.habilitar_controles(habilitar=True)
                    self.transito_actual = Transito_actual()

                elif const.GUARDAR in self.btnNuevo.text():
                    if self.txtPesoEntrada.text().isdigit() is True \
                        and self.txtPesoSalida.text().isdigit() is True \
                        and self.txtNeto.text().isdigit() is True:
                        '''se ha pesado ya para salir, guardar en historico
                        e imprimir
                        '''
                        self.transito_actual.fecha_salida = core.Fechas.get_fecha_salida_str()
                        self.pasar_datos_a_transito()
                        historico = Logica_Transitos().guardar_a_historico(id=self.transito_actual.id_transito)
                        if historico is not None:
                            v_imprimir = Ventana_Imprimir(parent=self, datos=historico)
                            v_imprimir.show()
                    else:
                        ''' guardar transito en la base de datos
                        '''
                        self.pasar_datos_a_transito()


                    self.habilitar_controles(habilitar=False)

            elif 'Buscar: ' in accion:
                lugar = accion.replace('Buscar: ', '')
                dialogo = Ventana_buscar(parent=self, buscar=lugar)
                dialogo.show()


    def cargar_datos_desde_db(self, id=None):
        transito = Logica_Transitos().get_transito(id)
        if transito is not None:
            self.transito_actual = transito
            #self.transito_actual = Transito_actual()
            self.habilitar_controles(True)

            self.txtCabina.setText(self.transito_actual.mat_cabina)
            self.txtRemolque.setText(self.transito_actual.mat_remolque)
            self.dtFechaEntrada.setDateTime(
                QtCore.QDateTime.fromString(
                    self.transito_actual.fecha_entrada
                )
            )
            self.txtOrigen.setText(self.transito_actual.origen)
            self.txtDestino.setText(self.transito_actual.destino)
            self.txtPesoEntrada.setText(self.transito_actual.bruto.__str__())
            self.txtPesoSalida.setText(self.transito_actual.tara.__str__())
            self.txtNeto.setText(self.transito_actual.neto.__str__())

            producto, \
            poseedor, \
            proveedor, \
            cliente, \
            agencia, \
            conductor = Logica_Transitos().nombres_desde_db(transito=self.transito_actual)

            self.txtProducto.setText(producto)
            self.txtPoseedor.setText(poseedor)
            self.txtProveedor.setText(proveedor)
            self.txtCliente.setText(cliente)
            self.txtAgencia.setText(agencia)
            self.txtConductor.setText(conductor)

    def pasar_datos_a_transito(self):
        ''' Pasa los datos al objeto transito_actual para despues
        poder guardarlos si se desea
        '''
        #self.transito_actual = Transito_actual()
        self.transito_actual.mat_cabina = self.txtCabina.text()
        self.transito_actual.mat_remolque = self.txtRemolque.text()
        self.transito_actual.fecha_entrada = self.dtFechaEntrada.text()
        self.transito_actual.bruto = self.txtPesoEntrada.text()
        self.transito_actual.tara = self.txtPesoSalida.text()
        self.transito_actual.neto = self.txtNeto.text()
        self.transito_actual.origen = self.txtOrigen.text()
        self.transito_actual.destino = self.txtDestino.text()

        #lo guardamos en la DB
        Logica_Transitos().guardar_transito(self.transito_actual)
        print(self.transito_actual)

    def calcula_neto(self):
        n1 = int(self.txtPesoEntrada.text())
        n2 = int(self.txtPesoSalida.text())
        neto = 0

        if n2 > n1:
            neto = n2 -n1
        elif n1 > n2:
            neto = n1 -n2

        self.txtNeto.setText("%s" % neto)
        return neto

    def habilitar_controles(self, habilitar=False):

        self.txtCabina.setEnabled(habilitar)
        self.txtRemolque.setEnabled(habilitar)
        self.txtCliente.setEnabled(habilitar)
        self.txtAgencia.setEnabled(habilitar)
        self.txtProveedor.setEnabled(habilitar)
        self.txtConductor.setEnabled(habilitar)
        self.txtPoseedor.setEnabled(habilitar)
        self.txtProducto.setEnabled(habilitar)
        self.txtOrigen.setEnabled(habilitar)
        self.txtDestino.setEnabled(habilitar)
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
            self.txtOrigen.setText('')
            self.txtDestino.setText('')

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
            self.txtOrigen.setStyleSheet('background-color: gainsboro;')
            self.txtDestino.setStyleSheet('background-color: gainsboro;')
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
            self.txtOrigen.setStyleSheet('background-color: white;')
            self.txtDestino.setStyleSheet('background-color: white;')
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
            elif 'txtPesoEntrada' in control:
                self.txtPesoSalida.setFocus()
            elif 'txtPesoSalida' in control:
                self.calcula_neto()


    def poner_estilos(self):

        qss = open('gui/estilo.qss').read()
        self.setStyleSheet(qss)
        QtGui.qApp.setStyle('Cleanlooks')