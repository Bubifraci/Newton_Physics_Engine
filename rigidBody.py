from vector import vector
import copy

class rigidBody:
    gravity = vector([0, 9.81, 0])

    def __init__(self, allForces, mass, startTime, startPos):
        self.allForces = allForces
        self.mass = mass
        self.startTime = startTime
        self.position = startPos

        self.allImpulses = []
        self.allForces = []
        self.isGrounded = False
        self.position = vector([0, 0, 0])
        self.velocity = vector([0, 0, 0])
        self.currentTime = 0

    def compute(self):
        dT = self.currentTime - self.startTime
        totalForce = vector([0, 0, 0])
        for force in self.allForces:
            totalForce.addToVector(force)
        totalForce.addToVector(self.gravity)
        #Acceleration
        totalForce.computeWithScalar(self.mass, '/')

        #Velocity
        self.velocity.addToVector(totalForce.computeWithScalar(dT, '*'))
        for i in range(len(self.allImpulses)):
            impulse = copy.deepcopy(self.allImpulses[i])
            self.velocity.addToVector(impulse.computeWithScalar(self.mass, '/'))
        self.allImpulses.clear()

        #Position
        velocity = copy.deepcopy(self.velocity)
        self.position = self.position.addToVector(velocity.computeWithScalar(dT, "*"))

        if(self.position.elements[1] >= 550):
            self.position.elements[1] = 550
            self.velocity.elements[1] = 0
            self.isGrounded = True
        else:
            self.isGrounded = False
        

    def update(self, t):
        self.currentTime = t
        self.compute()
        self.startTime = t

    def addForce(self, f):
        self.allForces.append(f)

    def addImpulse(self, i):
        self.allImpulses.append(i)