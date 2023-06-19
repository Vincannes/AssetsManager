from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import *

from app.widgets.nodegraphscenewidget import NodeGraphSceneWidget


class NodeGraphWidget(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        scene = NodeGraphSceneWidget(self)
        self.setScene(scene)

        self.initUi()

        rect_item = scene.addRect(0, 0, 100, 100)
        rect_item.setBrush(Qt.red)
        rect_item.setFlag(QGraphicsItem.ItemIsMovable)

    def initUi(self):
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)

    def middleMouseButtonPress(self, event):
        return super().mousePressEvent(event)
    def middleMouseButtonRelease(self, event):
        return super().mousePressEvent(event)

    def leftMouseButtonPress(self, event):
        if self.dragMode() == QGraphicsView.NoDrag:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
        else:
            self.setDragMode(QGraphicsView.NoDrag)
        return super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event):
        if self.dragMode() == QGraphicsView.ScrollHandDrag:
            self.setDragMode(QGraphicsView.NoDrag)
        return super().mousePressEvent(event)

    def rightMouseButtonPress(self, event):
        return super().mousePressEvent(event)

    def rightMouseButtonRelease(self, event):
        return super().mousePressEvent(event)
