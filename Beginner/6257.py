fruit = ['   apple    ','banana','  melon']
a = {x.strip(): len(x.strip()) for x in fruit}
print(a)