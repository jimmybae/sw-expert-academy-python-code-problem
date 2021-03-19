def maxx(c):
    a = c.split(", ")
    b = list(map(int, a))
    print("max({0}) => {1}".format(c, max(b)))

maxx("3, 5, 4, 1, 8, 10, 2")