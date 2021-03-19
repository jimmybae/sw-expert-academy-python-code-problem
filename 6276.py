# 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수
# 제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.

# [[2, 4, 8, 10, 16], [], [4, 8, 16, 20, 32], [5, 10, 20, 25, 40], [], [], [8, 16, 32, 40, 64], []]

re = []
for a in range(2, 10):
    c = []
    for b in range(1, 10):
        d = a * b
        if d % 3 != 0 and d % 7 != 0:
            c.append(d)
    re.append(c)
print(re)


# re = [[a * b for b in range(1, 10) if b % 3 != 0 and b % 7 != 0] for a in range(2, 10) if a % 3 != 0 and a % 7 != 0]
# print(re)