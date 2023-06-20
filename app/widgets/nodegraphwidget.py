from PyQt5.QtWidgets import QGraphicsView, QGraphicsItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

from app.nodes.node_obj import Node
from app.nodes.node_scene import Scene


class NodeGraphWidget(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.zoom_in_factor = 1.25
        self.zoom_clamp = False
        self.zoom = 10
        self.zoom_step = 1
        self.zoom_range = [0, 20]

        self.scene = Scene()

        node = Node(self.scene, "Grade")

        self.setScene(self.scene.grScene)
        self.initUi()

        # rect_item = self.grScene.addRect(0, 0, 100, 100)
        # rect_item.setBrush(Qt.red)
        # rect_item.setFlag(QGraphicsItem.ItemIsMovable)

    def initUi(self):
        self.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

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

    def wheelEvent(self, event):
        zoom_out_factor = 1 / self.zoom_in_factor
        old_pos = self.mapToScene(event.pos())

        # calcul zoom
        if event.angleDelta().y() > 0:
            zoom_factor = self.zoom_in_factor
            self.zoom += self.zoom_step
        else:
            zoom_factor = zoom_out_factor
            self.zoom -= self.zoom_step

        clamp = False
        if self.zoom < self.zoom_range[0]: self.zoom, clamp = self.zoom_range[0], True
        if self.zoom > self.zoom_range[1]: self.zoom, clamp = self.zoom_range[1], True

        # set scene scale
        if not clamp:
            self.scale(zoom_factor, zoom_factor)
