import math
import copy

class vector:
    def __init__(self, elements):
        self.n = len(elements)
        self.elements = elements

    def addToVector(self, v2):
        if(self.n != v2.n):
            return []
        elements = []
        for i in range(len(self.elements)):
            e1 = self.elements[i]
            e2 = v2.elements[i]
            elements.append(e1 + e2)
        return vector(elements)

    def computeWithScalar(self, scalar, operation):
        elements = copy.deepcopy(self.elements)
        if(operation == '*'):
            for i in range(len(self.elements)):
                e1 = elements[i]
                elements[i] = e1 * scalar
        elif(operation == '/'):
            for i in range(len(self.elements)):
                e1 = elements[i]
                elements[i] = e1 / scalar
        return vector(elements)
    
    def computeWithMatrix(self, matrix):
        n = len(matrix)
        if(n == 0):
            raise ValueError('Cannot compute with empty matrix.')
        m = len(matrix[0])

        if(self.n != n):
            raise ValueError('Dimensions of matrix and vector do not match.')
        
        newVectorVals = []
        for i in range(m):
            rowVal = 0
            for j in range(n):
                rowVal += matrix[j][i] * self.elements[j]
            newVectorVals.append(rowVal)
        #self.elements = newVectorVals
        return vector(newVectorVals)
    
    def rotate(self, rate):
        phi = math.radians(rate)
        rotationMatrix = [[math.cos(phi), math.sin(phi)], [-math.sin(phi), math.cos(phi)]]
        return self.computeWithMatrix(rotationMatrix)
            