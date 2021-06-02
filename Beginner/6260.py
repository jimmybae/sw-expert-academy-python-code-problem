a = input()
u = 0
l = 0
for b in a:
    if b.isupper():
        u += 1
    elif b.islower():
        l += 1
print("UPPER CASE {0}".format(u))
print("LOWER CASE {0}".format(l))