from PyQt4 import QtGui

from core import Constantes as const
from directORM.forProductos import TbProductos
from directORM.forEmpresas import TbEmpresas
from directORM.forConductores import TbConductores
from directORM.forTransito_actuales import TbTransito_actuales
import gui.Principal


class Ventana_buscar(QtGui.QDialog):
    """
    Clase encargada del dialogo de buscar
    """
    def __init__(self, parent=None, buscar=''):
        self.parent = parent

        self.lugar = buscar.upper()
        super(Ventana_buscar, self).__init__(parent=self.parent)
        self.setGeometry(30, 40, 800, 500)
        self.setWindowTitle("Busqueda de " + buscar)
        self.iniciar_controles()

        self.lista = list()
        self.cargar_segun_lugar(lugar=self.lugar)

    def iniciar_controles(self):

        self.vbox_fondo = QtGui.QVBoxLayout()

        self.txtBuscar = QtGui.QLineEdit(self)
        self.lstBuscado = QtGui.QListWidget(self)
        self.btnAceptar = QtGui.QPushButton('Aceptar', self)
        self.btnBusca = QtGui.QPushButton(QtGui.QIcon(const.ICONO.BUSCAR), '', self)

        self.btnBusca.clicked.connect(lambda: self.clickAction('BUSCAR'))
        self.btnAceptar.clicked.connect(lambda: self.clickAction('ACEPTAR'))

        self.h_box = QtGui.QHBoxLayout()
        self.h_box.addWidget(self.txtBuscar)
        self.h_box.addWidget(self.btnBusca)

        self.vbox_fondo.addLayout(self.h_box)
        self.vbox_fondo.addWidget(self.lstBuscado)
        self.vbox_fondo.addWidget(self.btnAceptar)

        self.setLayout(self.vbox_fondo)

    def cargar_segun_lugar(self, lugar='', filtro=None):
        if '' != lugar:
            if 'PRODUCTOS' in lugar:
                tabla = TbProductos()
                if filtro is not None:
                    filtro = "nombre like '%@filtro%'".replace('@filtro', filtro)
                self.lista = tabla.get_productos(filtro=filtro)

                self.lstBuscado.clear()
                for producto in self.lista:
                    self.lstBuscado.addItem(producto.nombre)

            elif 'CLIENTES' in lugar \
                    or 'PROVEEDOR' in lugar \
                    or 'POSEEDOR' in lugar \
                    or 'AGENCIA' in lugar:

                tabla = TbEmpresas()
                if filtro is not None:
                    filtro = "nombre like '%@filtro%'".replace('@filtro', filtro)
                self.lista = tabla.get_empresas(filtro=filtro)

                self.lstBuscado.clear()
                for empresa in self.lista:
                    self.lstBuscado.addItem(empresa.nombre)
            elif 'CONDUCTOR' in lugar:
                tabla = TbConductores()
                if filtro is not None:
                    filtro = "nombre || ' ' || apellidos like '%@filtro%'".replace('@filtro', filtro)
                self.lista = tabla.get_conductores(filtro=filtro)

                self.lstBuscado.clear()
                for conductor in self.lista:
                    self.lstBuscado.addItem("%s %s" % (conductor.nombre,
                                                       conductor.apellidos))
            elif 'TRANSITO' in lugar:
                tabla = TbTransito_actuales()
                if filtro is not None:
                    filtro = "mat_cabina || ' ' || mat_remolque like '%@filtro%'".replace('@filtro', filtro)
                self.lista = tabla.get_transito_actuales(filtro=filtro)

                self.lstBuscado.clear()
                for transito in self.lista:
                    self.lstBuscado.addItem("%s  %s" % (transito.mat_cabina,
                                                        transito.mat_remolque))


    def clickAction(self, accion=''):
        if 'BUSCAR' in accion:
            self.cargar_segun_lugar(
                lugar=self.lugar,
                filtro=self.txtBuscar.text()
            )
        elif 'ACEPTAR' in accion:
            seleccionado = self.lstBuscado.currentItem().text()
            index = self.lstBuscado.currentRow()

            assert isinstance(self.parent, gui.Principal.V_Principal)
            if 'PRODUCTOS' in self.lugar:
                self.parent.txtProducto.setText(seleccionado)
                id = self.lista[index].id_producto
                self.parent.transito_actual.id_producto = id
            elif 'CLIENTES' in self.lugar:
                self.parent.txtCliente.setText(seleccionado)
                id = self.lista[index].id_empresa
                self.parent.transito_actual.id_cliente = id
            elif 'PROVEEDOR' in self.lugar:
                self.parent.txtProveedor.setText(seleccionado)
                id = self.lista[index].id_empresa
                self.parent.transito_actual.id_proveedor = id
            elif 'AGENCIA' in self.lugar:
                self.parent.txtAgencia.setText(seleccionado)
                id = self.lista[index].id_empresa
                self.parent.transito_actual.id_agencia = id
            elif 'POSEEDOR' in self.lugar:
                self.parent.txtPoseedor.setText(seleccionado)
                id = self.lista[index].id_empresa
                self.parent.transito_actual.id_poseedor = id
            elif 'CONDUCTOR' in self.lugar:
                self.parent.txtConductor.setText(seleccionado)
                id = self.lista[index].id_conductor
                self.parent.transito_actual.id_conductor = id
            elif 'TRANSITO' in self.lugar:
                id = self.lista[index].id_transito
                self.parent.cargar_datos_desde_db(id=id)


            self.close()