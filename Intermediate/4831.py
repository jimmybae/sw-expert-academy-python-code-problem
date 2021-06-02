for t in range(int(input())):
    k, n, m = map(int, input().split())
    num = list(map(int, input().split()))
    c = [0] * (n + 1)
    v = [0] * (n + 1)

    for i in num:
        c[i] = 1

    dis = k
    now = k

    while True:
        if now >= n:
            result = sum(v)
            break
        elif c[now] == 1:
            dis = k
            v[now] = 1
            now += k
        elif c[now] == 0:
            now -= 1
            dis -= 1
            if dis == 0:
                result = 0
                break
    
    print("#{} {}".format(t + 1, result))