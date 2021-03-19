d = {"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000}

a = dict(sorted(d.items(), key=(lambda x:x[1]), reverse=True))
for key in a.keys():
    print("{0}: {1}".format(key, a[key]))