from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere():
    app=QApplication(sys.argv)
    pencere=QDialog()

    button1=QPushButton(pencere)
    button1.setText("tıklama alanı")
    button1.move(20,30)
    button1.clicked.connect(button1tıklandı)

    button2=QPushButton(pencere)
    button2.setText("tıklama alanı 2")
    button2.move(20,100)



    pencere.setGeometry(100,100,300,300)
    pencere.show()




    sys.exit(app.exec())


def button1tıklandı():
    print("buton 1 tıklandı")


if __name__=="__main__":
    pencere()
