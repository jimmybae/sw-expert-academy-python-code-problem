a = ["가위", "바위", "보"]

def rps(m1, m2):
    m1n = a.index(m1)
    m2n = a.index(m2)

    if m1n == m2n:
        return None
    elif m1n - m2n == 1 or m1n - m2n == -2:
        return m1
    else:
        return m2

l1 = input()
l2 = input()
m1 = input()
m2 = input()

result = rps(m1, m2)
if result is not None:
    print("{0}가 이겼습니다!".format(result))