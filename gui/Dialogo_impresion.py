
from PyQt4 import QtGui
from PyQt4 import QtWebKit
from PyQt4.QtCore import QUrl, Qt
from PyQt4.QtGui import QPrinter


class Ventana_Imprimir(QtGui.QDialog):

    def __init__(self, parent=None):


        self.parent = parent

        super(Ventana_Imprimir, self).__init__(parent=self.parent)
        self.setGeometry(30, 40, 800, 500)
        self.setWindowTitle("Imprimir albaran")


        self.init_controles()

        self.navegador.setUrl(QUrl('http://www.google.es'))

        self.navegador.loadFinished.connect(lambda: self.LoadEnd())

    def printPreview(self):

        dialog = QtGui.QPrintPreviewDialog(self.printer)
        dialog.setWindowState(Qt.WindowMaximized)
        #dialog.paintRequested.connect(self.print_)
        dialog.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint | Qt.WindowContextHelpButtonHint)
        dialog.exec()

    def LoadEnd(self):
        print('Prepandando impresion')

        self.printer = QPrinter();
        self.printer.setPageSize(QPrinter.A4);
        self.printer.setOrientation(QPrinter.Portrait);
        self.printer.setPageMargins(10,10,10,10,QPrinter.Millimeter);

        #self.printer = QPrinter( QPrinter.HighResolution )
        #self.printer.setOutputFormat( QPrinter.PdfFormat )
        #self.printer.setOutputFileName( "out.pdf" )
        #self.printPreview()
        self.navegador.print_( self.printer )

    def init_controles(self):
        vbox = QtGui.QVBoxLayout()
        self.navegador = QtWebKit.QWebView(self)
        vbox.addWidget(self.navegador)

        self.setLayout(vbox)
