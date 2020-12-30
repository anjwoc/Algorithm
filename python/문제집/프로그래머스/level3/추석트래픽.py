from datetime import date, timedelta   

def compare(time, moment):
    start = time
    end = time + timedelta(milliseconds=999)
    
    if start >= moment[0] and start <= moment[1]:
        return True
    elif end >= moment[0] and end <= moment[1]:
        return True
    elif start <= moment[0] and end >= moment[1]:
        return True
    
    return False
    
def solution(lines):
    result = []
    for line in lines:
        temp = line.split(' ')
        full_date = str(temp[0]) + " " + str(temp[1])
        
        if '.' in temp[2]:
            delay = temp[2].split('.')
            delay[1] = delay[1][0:-1]
        else:
            delay = list(temp[2][0:-1])
            delay += ["0"]

        end = date.fromisoformat(full_date)
        start = end - timedelta(seconds=int(delay[0]), milliseconds=int(delay[1]) - 1)
        
        result.append([start, end])
        
    answers = []
    for timelist in result:
        for time in timelist:
            answer = 0
            for moment in result:
                if compare(time, moment) == True:
                    answer += 1
            answers.append(answer)        
        
    return max(answers)

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

#lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]

# lines =	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
answer = solution(lines)

print(answer)