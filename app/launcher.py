import os
from PyQt5 import QtWidgets

from ressources.style import style
from app.nodes.main_window import AssetManagerWindow

SCRIPT_PATH = os.path.dirname(__file__)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    style.dark(app)
    win = AssetManagerWindow()
    win.show()
    app.exec_()

