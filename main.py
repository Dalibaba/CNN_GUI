from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit, QAction, \
    QMainWindow, QStackedWidget, QFormLayout, QHBoxLayout, QRadioButton, QLineEdit
import sys
from PyQt5.QtGui import QPixmap, QIcon

from constants import WINDOW, CLASSIFY_WIDGET, TRAIN_WIDGET
import menubar

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        cnn_menubar_train_action, cnn_menubar_classify_action = menubar.init_menubar(self)
        # A QMainWindow must have a central widget to display correctly
        self.central_widget = QWidget()  # define central widget
        self.setCentralWidget(self.central_widget)  # set QMainWindow.centralWidget

        # Main Window Configurations
        self.top = 200
        self.left = 500
        self.title = WINDOW.TITLE_LABEL
        self.width = WINDOW.SCREEN_WIDTH
        self.height = WINDOW.SCREEN_HEIGHT
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Initialize two pages with stacked widget
        # child widgets
        self.train_widget_stack = QWidget()
        self.classify_widget_stack = QWidget()
        self.train_widget()
        self.classify_widget()
        # add child widged to parent widget (stacked)
        self.stack_widget = QStackedWidget(self)
        self.stack_widget.addWidget(self.train_widget_stack)
        self.stack_widget.addWidget(self.classify_widget_stack)

        vbox = QVBoxLayout()
        self.centralWidget().setLayout(vbox)  # add the layout to the central widget
        # add trigger events clicking the menu bar
        cnn_menubar_train_action.triggered.connect(self.display_train_widget)
        cnn_menubar_classify_action.triggered.connect(self.display_classify_widget)
        # self.cnn_menubar.currentRowChanged.connect(self.display)

        vbox.addWidget(self.stack_widget)
        self.show()

    def classify_widget(self):
        vbox = QVBoxLayout()
        # labels
        self.image_label = QLabel("")
        image_classification_label = QLabel(CLASSIFY_WIDGET.CLASSIFICATION_LABEL)
        # buttons
        classify_image_button = QPushButton(CLASSIFY_WIDGET.CLASSIFY_LABEL)
        choose_image_button = QPushButton(CLASSIFY_WIDGET.CHOOSE_LABEL)
        # alignment
        image_classification_label.setAlignment(Qt.AlignCenter)
        self.image_label.setAlignment(Qt.AlignCenter)
        # Create a QVBoxLayout instance
        # add widgets to vbox
        vbox.addWidget(image_classification_label)
        vbox.addWidget(choose_image_button)
        vbox.addWidget(self.image_label)
        vbox.addWidget(classify_image_button)

        # click events
        choose_image_button.clicked.connect(self.get_image)

        # self.setLayout(vbox)
        self.classify_widget_stack.setLayout(vbox)

    def train_widget(self):

        train_label = QLabel(TRAIN_WIDGET.TRAIN_LABEL)
        # form layout for defining parameters
        form_layout = QFormLayout()
        model_layout = QHBoxLayout()
        model_layout.addWidget(QRadioButton(TRAIN_WIDGET.RESNET_LABEL))
        model_layout.addWidget(QRadioButton(TRAIN_WIDGET.VGG16_LABEL))
        form_layout.addRow(train_label)
        form_layout.addRow(QLabel(TRAIN_WIDGET.MODEL_TYPE), model_layout)


        self.train_widget_stack.setLayout(form_layout)

    def display_classify_widget(self):
        self.stack_widget.setCurrentIndex(WINDOW.CLASSIFY_SCREEN_INDEX)

    def display_train_widget(self):
        self.stack_widget.setCurrentIndex(WINDOW.TRAIN_SCREEN_INDEX)

    def get_image(self):
        fileName = QFileDialog.getOpenFileName(self,
                                               "Open Image", "/home/jana", "Image Files (*.png *.jpg *.bmp)")
        imagePath = fileName[0]
        pixmap = QPixmap(imagePath)
        image_height = int(WINDOW.SCREEN_HEIGHT * 0.5)
        image_width = int(WINDOW.SCREEN_WIDTH * 0.5)
        pixmap = pixmap.scaled(image_height, image_width)
        print("set image")
        self.image_label.setPixmap(QPixmap(pixmap))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())
