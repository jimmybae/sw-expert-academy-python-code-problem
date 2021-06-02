def facto(a):
    r = 1
    for i in range(1, a + 1):
        r *= i
    return r

print(facto(int(input())))