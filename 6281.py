a = int(input())

r = [x for x in range(1, a + 1) if a % x == 0]
print(r)