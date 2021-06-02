import datetime
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
m, d = map(int, input().split())
result = days[datetime.date(2016, m, d).weekday()]
print(result)
