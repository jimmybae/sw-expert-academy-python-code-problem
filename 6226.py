
a = []
for i in range(200):
    if (i + 1) % 7 == 0 and (i + 1) % 5 != 0:
        a.append(str(i + 1))
print(",".join(a))