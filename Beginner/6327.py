def pow(i):
    print("square({0}) => {1}".format(i, i**2))

a = input()
for b in a.split(", "):
    pow(int(b))