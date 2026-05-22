class vector:
    n = 0
    elements = []

    def __init__(self, elements):
        self.n = len(elements)
        self.elements = elements

    def addToVector(self, v2):
        if(self.n != v2.n):
            return []
        for i in range(len(self.elements)):
            e1 = self.elements[i]
            e2 = v2.elements[i]
            self.elements[i] = e1 + e2
        return self

    def computeWithScalar(self, scalar, operation):
        if(operation == '*'):
            for i in range(len(self.elements)):
                e1 = self.elements[i]
                self.elements[i] = e1 * scalar
        elif(operation == '/'):
            for i in range(len(self.elements)):
                e1 = self.elements[i]
                self.elements[i] = e1 / scalar
        return self