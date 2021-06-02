a = int(input())
b = [c for c in range(1, a + 1) if a % c == 0]
print(b)