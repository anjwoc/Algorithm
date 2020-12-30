def solution(lines):
    S, E = [], []
    length = 0

    for line in lines:
        length += 1
        d, s, t = line.split()

        t = float(t[:-1])
        hh, mm, ss = s.split(":")
        second = float(hh)*3600 + float(mm)*60 + float(ss)

        E.append(second + 1)
        S.append(second - t + 0.001)

    print(S)
    print(E)

    S.sort()

    curTraffic = 0
    maxTraffic = 0
    e_cnt = 0
    s_cnt = 0

    while ((e_cnt < length) and (s_cnt < length)):
        if S[s_cnt] < E[e_cnt]:
            curTraffic += 1
            maxTraffic = max(maxTraffic, curTraffic)
            s_cnt += 1
        else:
            curTraffic -= 1
            e_cnt += 1

    return maxTraffic


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
