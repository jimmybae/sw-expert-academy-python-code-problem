# 홍길동
# 20
# 홍길동(은)는 2099년에 100세가 될 것입니다.

import datetime

x = datetime.datetime.now()
name = input()
age = int(input())

print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(name, x.year + 100 - age))