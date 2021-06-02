a = input().split(" ")
b = list(set(a))
b.sort()
print(*b, sep=",")