from app.widgets.node_graphics import QGraphicNode


class Node(object):

    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene
        self.title = title

        self.grNode = QGraphicNode(self, self.title)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = []
        self.outputs = []
