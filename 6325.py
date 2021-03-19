b = [2, 4, 6, 8, 10]
def check(a):
    return b.count(a) > 0

print(b)
print("{0} => {1}".format(5, check(5)))
print("{0} => {1}".format(10, check(10)))