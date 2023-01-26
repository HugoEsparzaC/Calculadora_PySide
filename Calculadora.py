from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QGridLayout, QApplication, QWidget, QVBoxLayout
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
        self._crear_botones()

    def _crear_area_captura(self):
        self.linea_entrada = QLineEdit()
        self.linea_entrada.setFixedHeight(35)
        self.linea_entrada.setAlignment(Qt.AlignRight)
        self.linea_entrada.setReadOnly(True)
        self.layout_principal.addWidget(self.linea_entrada)

    def _crear_botones(self):
        self.botones = {}
        layout_botones = QGridLayout()
        botones = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'C':(3,2),
            '+':(3,3),
            '=':(3,4)
        }
        for texto_boton, posicion in botones.items():
            self.botones[texto_boton] = QPushButton(texto_boton)
            self.botones[texto_boton].setFixedSize(40,40)
            layout_botones.addWidget(self.botones[texto_boton], posicion[0], posicion[1])
        self.layout_principal.addLayout(layout_botones)

if __name__ == '__main__':
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()