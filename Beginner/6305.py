def ch(li):
    new_li = []
    for x in li:
        if x not in new_li:
            new_li.append(x)
    return new_li

a = [12,24,35,24,88,120,155,88,120,155]
print(ch(a))