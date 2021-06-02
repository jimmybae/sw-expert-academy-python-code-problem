a = int(input())
b = []
for i in range(1, a + 1):
    if a % i == 0:
        b.append(i)
        print("%d(은)는 %d의 약수입니다." % (i, a))
if len(b) == 2:
    print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (a, b[0], b[1]))
