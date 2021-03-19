a = ["가위", "바위", "보"]
m1 = input()
m2 = input()

m1n = a.index(m1)
m2n = a.index(m2)

if m1n == m2n:
    print("Result : Draw")
elif m1n - m2n == 1 or m1n - m2n == -2:
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")
