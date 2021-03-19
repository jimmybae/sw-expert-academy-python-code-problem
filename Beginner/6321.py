def check(a):
    b = []
    for i in range(1, a + 1):
        if a % i == 0:
            b.append(i)
    return len(b) == 2

a = int(input())

if check(a):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
