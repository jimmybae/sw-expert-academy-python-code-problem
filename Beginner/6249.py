# 11
# 0 1 2 3 4 5 6 7 8 9
# 0 2 0 0 0 0 0 0 0 0
re = []
a = input()
for i in range(10):
    r = 0
    print(i, end=" ")
    for b in a:
        if int(b) == i:
            r += 1
    re.append(str(r))
print("")
print(" ".join(re))