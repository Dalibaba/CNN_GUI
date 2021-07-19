from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit, QAction, \
    QMainWindow, QStackedWidget, QFormLayout, QHBoxLayout, QRadioButton, QLineEdit
import sys
from PyQt5.QtGui import QPixmap, QIcon

from cnn.model import Model
from constants import Window, ClassifyWidget, TrainWidget
import menubar

# path of image, which user wants to classify
IMAGE_PATH = ""
MODEL_PATH = ""


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
        self.title = Window.TITLE_LABEL
        self.width = Window.SCREEN_WIDTH
        self.height = Window.SCREEN_HEIGHT
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
        image_classification_label = QLabel(ClassifyWidget.CLASSIFICATION_LABEL)
        # buttons
        load_model_button = QPushButton(ClassifyWidget.CHOOSE_MODEL_LABEL)
        classify_image_button = QPushButton(ClassifyWidget.CLASSIFY_LABEL)
        choose_image_button = QPushButton(ClassifyWidget.CHOOSE_IMAGE_LABEL)
        # alignment
        image_classification_label.setAlignment(Qt.AlignCenter)
        self.image_label.setAlignment(Qt.AlignCenter)
        # Create a QVBoxLayout instance
        # add widgets to vbox
        vbox.addWidget(image_classification_label)
        vbox.addWidget(load_model_button)
        vbox.addWidget(choose_image_button)
        vbox.addWidget(self.image_label)
        vbox.addWidget(classify_image_button)

        # click events
        choose_image_button.clicked.connect(self.get_image)
        load_model_button.clicked.connect(self.load_model)
        classify_image_button.clicked.connect(self.load_model)
        # self.setLayout(vbox)
        self.classify_widget_stack.setLayout(vbox)

    def train_widget(self):
        train_label = QLabel(TrainWidget.TRAIN_LABEL)
        # form layout for defining parameters
        form_layout = QFormLayout()
        model_layout = QHBoxLayout()
        model_layout.addWidget(QRadioButton(TrainWidget.RESNET_LABEL))
        model_layout.addWidget(QRadioButton(TrainWidget.VGG16_LABEL))
        form_layout.addRow(train_label)
        form_layout.addRow(QLabel(TrainWidget.MODEL_TYPE), model_layout)

        self.train_widget_stack.setLayout(form_layout)

    def display_classify_widget(self):
        self.stack_widget.setCurrentIndex(Window.CLASSIFY_SCREEN_INDEX)

    def display_train_widget(self):
        self.stack_widget.setCurrentIndex(Window.TRAIN_SCREEN_INDEX)

    """functions for click events"""

    def load_model(self):
        filename = QFileDialog.getOpenFileName(self,
                                               "Open Image", "", "Image Files (*.h5)")
        MODEL_PATH = filename[0]
        print(MODEL_PATH)
        cnn = Model()
        cnn = cnn.load(MODEL_PATH)
        result = cnn.classify()

    def get_image(self):
        filename = QFileDialog.getOpenFileName(self,
                                               "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        IMAGE_PATH = filename[0]
        pixmap = QPixmap(IMAGE_PATH)
        image_height = int(Window.SCREEN_HEIGHT * 0.5)
        image_width = int(Window.SCREEN_WIDTH * 0.5)
        pixmap = pixmap.scaled(image_height, image_width)
        self.image_label.setPixmap(QPixmap(pixmap))

    def classify_image(self):
        print("classify")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())
