import math
a = map(float, input().split(", "))
print(*[round(b * 2 * math.pi, 2) for b in a], sep = ", ")