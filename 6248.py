a = input()
b = [v for i, v in enumerate(a) if (i + 1) % 2 == 0]
print(*b, sep="")