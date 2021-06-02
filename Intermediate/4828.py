inp = []
for t in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    inp.append(lst)

for i in range(len(inp)):
    print("#{} {}".format(i + 1, max(inp[i]) - min(inp[i])))