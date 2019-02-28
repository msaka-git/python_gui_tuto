from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere():
    app=QApplication(sys.argv)
    window = QWidget()
    yazi=QLabel(window)
    alan=QLineEdit(window)
    yazi.setText("Bu arayüzdeki bir yazıdır.")
    yazi.move(50,100)
    alan.move(50,150)
    window.setWindowTitle("MErhaba Arayüz Tasarımı")
    window.setGeometry(200,200,300,300)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
