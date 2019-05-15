import sys
from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.GridUI()


    def GridUI(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Tugas QRadioButton')

        self.label1 = QLabel('Bilangan pertama')
        self.label2 = QLabel('Bilangan kedua')
        self.radio1 = QRadioButton('Tambah')
        self.radio2 = QRadioButton('Kurang')
        self.radio3 = QRadioButton('Kali')
        self.radio4 = QRadioButton('Bagi')
        self.line1 = QLineEdit(self)
        self.line2 = QLineEdit(self)
        self.button = QPushButton('Hitung')
        self.hasil = QLabel('<b>Hasil </b>')

        #self.line1.resize(100, 20)


        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0,)
        layout.addWidget(self.line1, 0, 1, 1, 3)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.line2, 1, 1, 1, 3)
        layout.addWidget(self.radio1, 2, 0)
        layout.addWidget(self.radio2, 2, 1)
        layout.addWidget(self.radio3, 2, 2)
        layout.addWidget(self.radio4, 2, 3)
        #layout.addWidget(self.button, 5, 0, 1, 4)

        vbox = QVBoxLayout()
        vbox.addLayout(layout)
        vbox.addStretch()
        hline = QFrame();
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)
        vbox.addWidget(hline)
        vbox.addWidget(self.hasil)
        vbox.addWidget(self.button)

        self.button.clicked.connect(self.hitung)
        self.setLayout(vbox)

    def hitung(self):
        a = float(self.line1.text())
        b = float(self.line2.text())

        if self.radio1.isChecked():
            jumlah = a + b
            self.hasil.setText('<b>Hasil penjumlahan : ' + str(jumlah) + '</b>')
        elif self.radio2.isChecked():
            pengurangan = a - b
            self.hasil.setText('<b>Hasil pengurangan : ' + str(pengurangan) + '</b>')
        elif self.radio3.isChecked():
            perkalian = a * b
            self.hasil.setText('<b>Hasil perkalian : ' + str(perkalian) + '</b>')
        elif self.radio4.isChecked():
            pembagian = a / b
            self.hasil.setText('<b>Hasil pembagian : ' + str(pembagian) + '</b>')
        else:
            self.hasil.setText('<b>Pilih operasi hitung terlebih dahulu</b>')


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()