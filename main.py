from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)  # get application setup (OS)
    # Main Window
    win = QMainWindow()
    win.setGeometry(800, 200, 600, 600)
    win.setWindowTitle("Image Classification")

    label = QtWidgets.QLabel(win)
    label.setText("label")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())


window()
