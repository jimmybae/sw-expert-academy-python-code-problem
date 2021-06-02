a = list(range(1, 11))
# print(a)

b = list(filter(lambda x: x % 2 == 0, a))
# print(b)

c = list(map(lambda x: x ** 2, b))
print(c)
