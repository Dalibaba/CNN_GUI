from PyQt5.QtWidgets import QAction, qApp
from constants import Menubar


def init_menubar(self):
    # menu bar
    self.menubar = self.menuBar()
    exit_action = QAction(Menubar.EXIT_LABEL, self)
    exit_action.setShortcut('Ctrl+E')
    train_action = QAction(Menubar.TRAIN_LABEL, self)
    train_action.setShortcut('Ctrl+T')
    classify_action = QAction(Menubar.CLASSIFY_LABEL, self)
    classify_action.setShortcut('Ctrl+C')
    # add trigger events for clicking
    exit_action.triggered.connect(qApp.quit)
    # create filemenu
    file_menu = self.menubar.addMenu(Menubar.SCREEN_LABEL)
    # add actions to file menu
    file_menu.addAction(train_action)
    file_menu.addAction(classify_action)
    file_menu.addAction(exit_action)

    return train_action, classify_action
