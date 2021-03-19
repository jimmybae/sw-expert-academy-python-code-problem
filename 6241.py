a = input()
x = a.find("://")
p = a[0:x]
print("protocol: {0}".format(p))

y = a.find("/", x + 3)
h = a[x + 3:y]
print("host: {0}".format(h))

o = a[y + 1:]
print("others: {0}".format(o))