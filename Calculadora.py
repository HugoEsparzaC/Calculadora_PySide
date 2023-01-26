from PySide6.QtWidgets import QMainWindow, QLineEdit, QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(235,235)
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        self._crear_area_captura()

    def _crear_area_captura(self):
        self.linea_entrada = QLineEdit()
        self.linea_entrada.setFixedHeight(35)
        self.linea_entrada.setAlignment(Qt.AlignRight)
        self.linea_entrada.setReadOnly(True)
        self.layout_principal.addWidget(self.linea_entrada)

if __name__ == '__main__':
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()