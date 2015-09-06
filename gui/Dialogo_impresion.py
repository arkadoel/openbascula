
from PyQt4 import QtGui
from PyQt4 import QtWebKit
from PyQt4.QtCore import QUrl, Qt
from PyQt4.QtGui import QPrinter
from core.Constantes import PLANTILLA_ALBARAN, IMPRIMIR
from core.LogicaTransitos import Logica_Transitos
from directORM.forHistoricos import Historico

class Ventana_Imprimir(QtGui.QDialog):

    def __init__(self, parent=None, datos=None):

        self.parent = parent
        self.transito = datos
        super(Ventana_Imprimir, self).__init__(parent=self.parent)
        self.setGeometry(30, 40, 800, 500)
        self.setWindowTitle("Imprimir albaran")

        self.init_controles()

        #self.navegador.setUrl(QUrl('http://www.google.es'))
        self.navegador.setHtml(self.leer_plantilla_y_poner_datos())
        #self.navegador.loadFinished.connect(lambda: self.LoadEnd())

    def leer_plantilla_y_poner_datos(self):
        html = open(PLANTILLA_ALBARAN).read()

        if self.transito is None:
            html = """
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body >
                <h1 style='color:red;'>NO HAY DATOS QUE PRESENTAR</h1>
            </body>
            </html>
            """
        else:
            #pongamos los datos
            #self.transito = Historico()
            html = html.replace("@num_albaran", str(self.transito.num_albaran))
            html = html.replace("@mat_cabina", self.transito.mat_cabina)
            html = html.replace("@mat_remolque", self.transito.mat_remolque)

            html = html.replace("@cliente", self.transito.razon_social_cliente)
            html = html.replace("@producto", self.transito.nombre_producto)
            html = html.replace("@proveedor", self.transito.razon_social_proveedor)
            html = html.replace("@poseedor", self.transito.razon_social_poseedor)
            html = html.replace("@agencia", self.transito.razon_social_agencia)
            html = html.replace("@conductor", self.transito.nombre_conductor)
            html = html.replace("@origen", self.transito.origen)
            html = html.replace("@destino", self.transito.destino)
            html = html.replace("@fech_entrada", self.transito.fecha_entrada)
            html = html.replace("@fech_salida", self.transito.fecha_salida)
            html = html.replace("@peso_entrada", str(self.transito.bruto))
            html = html.replace("@peso_salida", str(self.transito.tara))
            html = html.replace("@neto", str(self.transito.neto))

        return html

    def printPreview(self):

        dialog = QtGui.QPrintPreviewDialog(self.printer)
        dialog.setWindowState(Qt.WindowMaximized)
        #dialog.paintRequested.connect(self.print_)
        dialog.setWindowFlags(Qt.CustomizeWindowHint |
                              Qt.WindowTitleHint |
                              Qt.WindowMinMaxButtonsHint |
                              Qt.WindowCloseButtonHint |
                              Qt.WindowContextHelpButtonHint)
        dialog.exec()

    def imprimir(self):
        print('Prepandando impresion')

        self.printer = QPrinter(QPrinter.HighResolution);
        self.printer.setPageSize(QPrinter.A4);
        self.printer.setOrientation(QPrinter.Portrait);
        self.printer.setPageMargins(10, 10, 10, 10, QPrinter.Millimeter)
        self.navegador.print_(self.printer)

    def LoadEnd(self):

        #self.printer = QPrinter( QPrinter.HighResolution )
        #self.printer.setOutputFormat( QPrinter.PdfFormat )
        #self.printer.setOutputFileName( "out.pdf" )
        #self.printPreview()
        #self.navegador.print_( self.printer )
        pass

    def init_controles(self):
        vbox = QtGui.QVBoxLayout()

        self.navegador = QtWebKit.QWebView(self)
        self.btnImprimir = QtGui.QPushButton(IMPRIMIR, self)
        self.btnImprimir.clicked.connect(lambda: self.imprimir())

        vbox.addWidget(self.btnImprimir)
        vbox.addWidget(self.navegador)

        self.setLayout(vbox)
