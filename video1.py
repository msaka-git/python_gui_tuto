from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

def pencere():
    app=QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("MErhaba Arayüz Tasarımı")
    window.setGeometry(200,200,300,300)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
