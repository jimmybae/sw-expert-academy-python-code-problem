def fi(x):
   if x == 1 or x == 2:
      return 1
   return fi(x-1) + fi(x-2)

r = [fi(x) for x in range(1, 11)]
print(r)