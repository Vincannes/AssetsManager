import math
from PyQt5 import QtCore, QtGui, QtWidgets


class NodeGraphSceneWidget(QtWidgets.QGraphicsScene):

    def __init__(self, scene, parent=None):
        super().__init__(parent)

        self.scene = scene

        self.grid_size = 20
        self.grid_square = 4

        self._color_bck = QtGui.QColor("#393939")
        self._color_light = QtGui.QColor("#2f2f2f")
        self._color_dark = QtGui.QColor("#292929")

        self._pen_light = QtGui.QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QtGui.QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        self.setBackgroundBrush(self._color_bck)

    def setGrScene(self, width, height):
        self.setSceneRect(
            -width // 2,
            -height // 2,
            width,
            height
        )

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # create grid
        self._create_grid(painter, rect)

    def _create_grid(self, painter, rect):
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.grid_size)
        first_top = top - (top % self.grid_size)

        line_lights, line_darks = [], []
        for x in range(first_left, right, self.grid_size):
            if x % (self.grid_size * self.grid_square) != 0:
                line_lights.append(QtCore.QLine(x, top, x, bottom))
            else:
                line_darks.append(QtCore.QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.grid_size):
            line_lights.append((QtCore.QLine(left, y, right, y)))

        painter.setPen(self._pen_light)
        painter.drawLines(*line_lights)
        painter.setPen(self._pen_dark)
        painter.drawLines(*line_darks)
