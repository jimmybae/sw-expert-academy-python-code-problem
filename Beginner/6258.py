# 5
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

a = int(input())
b = {x: x*x for x in range(1, a + 1)}
print(b)