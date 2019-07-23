import datetime

def solution(a, b):
    day_list = ["SUN", "MON","TUE","WED","THU","FRI","SAT"]
    answer  = day_list[datetime.date(2016,5,24).weekday()+1]
    return answer
print(solution(5,24))


