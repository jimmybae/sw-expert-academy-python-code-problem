from functools import reduce
try:
    a = list(map(int, input().split(", ")))
    b = reduce(lambda x, y: x * y, a)
    print(b)
except:
    print("에러발생")


# c = "*".join(a)
# print(c)
# print(eval(c))
