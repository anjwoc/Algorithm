import datetime

now = datetime.datetime.now()
print(now)

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)

nowTime = now.strftime('%H:%M:%S')
print(nowTime)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDateTime)

D = datetime.date(2016,4,29)
print(D)
print(D.year)
print(D.month)
print(D.day)
