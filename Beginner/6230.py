score = [88, 30, 61, 55, 96]

for idx, val in enumerate(score):
    re = "불합격"
    if val >= 60:
        re = "합격"
    print("{0}번 학생은 {1}점으로 {2}입니다.".format(idx + 1, val, re))
