import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Latihan ComboBox')

        self.makanan = QComboBox()
        self.makanan.addItem('--Pilih Makanan--')
        self.makanan.addItem('Mendoan')
        self.makanan.addItem('Cireng')
        self.makanan.addItem('Gethuk')
        self.makanan.addItem('Tahu Bulat')
        self.makanan.addItem('Ketan Susu')

        self.minuman = QComboBox()
        self.minuman.addItem('--Pilih Minuman--')
        self.minuman.addItem('Es Cincau')
        self.minuman.addItem('Milkshake')
        self.minuman.addItem('Chatime')
        self.minuman.addItem('Thaitea')
        self.minuman.addItem('Kopi Hitam')

        self.getTextButton = QPushButton('Pilihan Anda')
        layout = QVBoxLayout()
        layout.addWidget(self.makanan)
        layout.addWidget(self.minuman)
        layout.addWidget(self.getTextButton)
        layout.addStretch()
        self.setLayout(layout)
        self.getTextButton.clicked.connect(self.getTextButtonClick)


    def getTextButtonClick(self):
        QMessageBox.information(self, 'Informasi',
                                'Anda memilih: ' + self.makanan.currentText()
                                + ' & ' + self.minuman.currentText())


if __name__ == '__main__':    a = QApplication(sys.argv)
form = MainForm()
form.show()
a.exec_()