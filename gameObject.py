from rigidBody import rigidBody

class gameObject:
    width = 0
    height = 0
    rigidBody

    def __init__(self, width, height, rigidBody):
        self.rigidBody = rigidBody
        self.width = width
        self.height = height