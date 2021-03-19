def countdown(i):
    if(i <= 0):
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for a in range(10, 0, -1):
            print(a)

countdown(0)
countdown(10)