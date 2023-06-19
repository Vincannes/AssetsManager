
from PyQt5 import QtCore, QtGui, QtWidgets

from app.ui.mainwindow import Ui_MainWindow


class AssetManagerWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(AssetManagerWindow, self).__init__(parent=parent)

        self.setupUi(self)
        # self._refineUi()

    def _refineUi(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("NodeGraph")
