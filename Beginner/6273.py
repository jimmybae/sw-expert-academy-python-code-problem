# 1번 학생의 총점은 170점이고, 평균은 85.0입니다.
a = [(90, 80), (85, 75), (90, 100)]

for idx, val in enumerate(a):
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:.1f}입니다.".format(idx + 1, sum(val), sum(val) / 2))