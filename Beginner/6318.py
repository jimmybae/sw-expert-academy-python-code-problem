a = "abcdef"
c = {}

for i in range(0, 6):
    c[a[i]] = i
for k in c:
    print("{0}: {1}".format(k, c[k]))
