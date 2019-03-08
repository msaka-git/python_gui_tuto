from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

# bootstrap yapmak

def pencere():
    app=QApplication(sys.argv)
    pencere=QWidget()
    pencere.setGeometry(50,50,300,300)
    h_box=QHBoxLayout()

    button1=QPushButton(pencere)
    button1.setText("Tıkla")

    button2=QPushButton(pencere)
    button2.setText("Tıkla 2")

    h_box.addWidget(button1)
    h_box.addWidget(button2)

    pencere.setLayout(h_box)

    pencere.show()
    sys.exit(app.exec())


if __name__=="__main__":
    pencere()
