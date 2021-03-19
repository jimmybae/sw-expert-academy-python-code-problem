a = input()
l = 0
d = 0
for b in a:
    if b.isnumeric():
        d += 1
    elif b.isalpha():
        l += 1
print("LETTERS {0}".format(l))
print("DIGITS {0}".format(d))