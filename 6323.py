def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

b = []
a = int(input())
for x in range(1, a + 1):
    b.append(fib(x))
print(b)