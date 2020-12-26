# P, S = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
P, S = [40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]


def solution(P, S):
    ans = []
    days = []

    for i in range(len(P)):
        if (100-P[i]) % S[i] != 0:
            days.append(((100-P[i])//S[i])+1)
        else:
            days.append(((100-P[i])//S[i]))

    print(days)
    cnt = 1
    target = days[0]
    for i in range(1, len(days)):
        if target < days[i]:
            ans.append(cnt)
            target = days[i]
            cnt = 1
        else:
            cnt += 1
    ans.append(cnt)

    return ans


print(solution(P, S))
