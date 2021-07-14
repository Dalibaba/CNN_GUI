from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
import sys
from PyQt5.QtGui import QPixmap


import constants


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # labels
        self.image_label = QLabel("")
        self.image_classification_label = QLabel(constants.IMAGE_CLASSIFICATION_LABEL)
        # buttons
        self.classify_image_button = QPushButton(constants.CLASSIFY_IMAGE_LABEL)
        self.choose_image_button = QPushButton(constants.CHOOSE_IMAGE_LABEL)

        self.title = "CNN_CLASSIFIER"
        self.top = 200
        self.left = 500
        self.width = constants.MAIN_SCREEN_WIDTH
        self.height = constants.MAIN_SCREEN_HEIGHT

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # alignment
        self.image_classification_label.setAlignment(Qt.AlignCenter)
        self.image_label.setAlignment(Qt.AlignCenter)
        # Create a QVBoxLayout instance
        vbox = QVBoxLayout()
        # add widgets to vbox
        vbox.addWidget(self.image_classification_label)
        vbox.addWidget(self.choose_image_button)
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.classify_image_button)

        # click events
        self.choose_image_button.clicked.connect(self.get_image)

        self.setLayout(vbox)

        self.show()

    def get_image(self):
        fileName = QFileDialog.getOpenFileName(self,
                                               "Open Image", "/home/jana", "Image Files (*.png *.jpg *.bmp)")
        imagePath = fileName[0]
        print("hi")
        pixmap = QPixmap(imagePath)
        image_height = int(constants.MAIN_SCREEN_HEIGHT * 0.5)
        image_width = int(constants.MAIN_SCREEN_WIDTH * 0.5)
        pixmap = pixmap.scaled(image_height, image_width)

        # self.image_label.setScaledContents(self, True)
        self.image_label.setPixmap(QPixmap(pixmap))
        # self.resize(image_height, image_width)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
