class Shape:
    def __init__(self, l):
        self.l = l
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return self.l * self.l

a = Square(3)
print("정사각형의 면적: {0}".format(a.area()))