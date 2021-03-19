a = [1, 2, 3, 4, 3, 2, 1]
# [1, 2, 3, 4]
def check(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b

print(a)
print(check(a))