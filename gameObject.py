from rigidBody import rigidBody

class gameObject:
    width = 0
    height = 0

    def __init__(self, width, height, rigidBody, nodes, scale):
        self.rigidBody = rigidBody
        self.width = width
        self.height = height
        self.nodes = []
        for node in nodes:
            self.nodes.append(node.computeWithScalar(scale, '*'))
        self.scale = scale

    def rotate(self, angle):
        for i in range(len(self.nodes)):
            self.nodes[i] = self.nodes[i].rotate(angle)