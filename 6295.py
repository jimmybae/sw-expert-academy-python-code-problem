b, c = map(int, input().split(", "))

d = [[x * y for y in range(0, c)] for x in range(0, b)]
print(d)