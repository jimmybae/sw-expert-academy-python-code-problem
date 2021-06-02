#for i in range(1, 101):
#    if i % 2 != 0:
#            print(i, end =", ")


print(", ".join(str(n) for n in range(1, 101) if n % 2 != 0))

#print(*range(1, 101), sep=", ")