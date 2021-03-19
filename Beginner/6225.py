class Rectangle:
    def __init__(self, v, h):
        self.v = v
        self.h = h
    def getM(self):
        return self.v * self.h

a = Rectangle(4, 5)
print("사각형의 면적: {0}".format(a.getM()))