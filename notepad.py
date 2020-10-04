from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QTextEdit
import sys
import time


class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.ebby()

    def ebby(self):
        self.yazi = QLabel("Hoşgeldin")
        self.kaydet = QPushButton("Kaydet")
        self.temizle = QPushButton("Temizle")
        self.isim = QLineEdit("Başlık")
        self.parag = QTextEdit()
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addStretch()
        hbox.addWidget(self.yazi)
        hbox.addStretch()

        vbox.addLayout(hbox)
        vbox.addWidget(self.isim)
        vbox.addWidget(self.parag)
        vbox.addWidget(self.kaydet)
        vbox.addWidget(self.temizle)
        

        self.kaydet.clicked.connect(self.save)
        self.temizle.clicked.connect(self.temizlik)
        
        
        self.setLayout(vbox)
        self.setWindowTitle("root@ebby:~#")
        self.show()

    def save(self):
        try:
            self.yazi.setText("Kaydediliyor...")
            with open("{}.txt".format(self.isim.text()),"w",encoding="UTF-8") as file:
                file.write(str(self.parag.toPlainText()))
            self.yazi.setText("{} Adında Kaydedildi ! ".format(self.isim.text()))
        except:
            self.yazi.setText("Kaydedilemedi :((")
    
    def temizlik(self):
        self.isim.clear()
        self.parag.clear()
        self.yazi.setText("Temizlendi !!!")



app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())