a = []
for i in range(100, 301):
    b = str(i)
    if int(b[0]) % 2 == 0 and int(b[1]) % 2 == 0 and int(b[2]) % 2 == 0:
        a.append(b)
print(",".join(a))