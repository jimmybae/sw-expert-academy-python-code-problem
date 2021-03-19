def long(a, b):
    if len(a) > len(b):
        return a
    else:
        return b

i = input()
c = i.split(", ")
print(long(c[0], c[1]))