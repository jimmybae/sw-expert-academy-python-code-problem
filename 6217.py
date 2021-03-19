class Student:
    def __init__(self, name):
        self.name = name

    def tostring(self):
        print("이름: {0}".format(self.name))

class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
    def tostring(self):
        print("이름: {0}, 전공: {1}".format(self.name, self.major))

s = Student("홍길동")
s.tostring()

g = GraduateStudent("이순신", "국어")
g.tostring()