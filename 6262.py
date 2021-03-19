# abcdefgabc
# 문자 빈도수

r = {}
a = input()
for b in a:
    c = r.get(b)
    if c == None:
        r[b] = 1
    else:
        r[b] += 1

for x in r.keys():
    print("{0},{1}".format(x, r[x]))

y = {d: 1 for d in a}
print(y)