# 89, 90, 100
# 국어, 영어, 수학의 총점: 279

class student():
    def __init__(self, kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat
    
    def total(self):
        return self.kor + self.eng + self.mat

a, b, c = map(int, input().split(", "))
s = student(a, b, c)
print("국어, 영어, 수학의 총점: {0}".format(s.total()))