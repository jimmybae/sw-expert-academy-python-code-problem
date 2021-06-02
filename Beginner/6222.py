a = input()
b = ord(a)

if b > 64 and b < 91:
    print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, b, chr(b + 32), b + 32))
elif b > 96 and b < 123:
    print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, b, chr(b - 32), b - 32))
else:
    print(a)