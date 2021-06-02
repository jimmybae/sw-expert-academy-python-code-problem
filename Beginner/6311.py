a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# A-4, B-3, C-2, D-1
# map function, lambda

b = {"A": 4, "B": 3, "C": 2, "D":1}
c = list(map(lambda x: b[x], a))
print(sum(c))