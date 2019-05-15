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
        self.setWindowTitle(' ')


        self.Check = QCheckBox()
        self.Check.setText('Show Titlle')

        layout = QVBoxLayout()
        layout.addWidget(self.Check)
        self.setLayout(layout)

        self.Check.stateChanged.connect(self.tampil)

    def tampil(self):
        if self.Check.isChecked(): self.setWindowTitle('Contoh QCheckBox')
        else: self.setWindowTitle(' ')

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()