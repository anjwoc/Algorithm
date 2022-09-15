from collections import Counter

'''
{{4,2,3},{3},{2,3,4,1},{2,3}}을 오름차순으로 정렬하면 {{3},{2,3},{4,2,3},{2,3,4,1}}이 되고
해당 문자열을 파싱해서 원소가 들어온 순서대로 나열하면 정답이 된다.
이 부분을 이용하면 각 모든 숫자의 개수를 카운트해서 많은 순서로 나열해도 정답이 된다.
'''


def solution(s):
    ans = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)

    for i in s:
        item = i.split(',')
        for j in item:
            if int(j) not in ans:
                ans.append(int(j))

    return ans


def solution2(s):
    ans = []

    lst = s.replace('{', '').replace('}', '').split(',')
    counter = dict(Counter(lst))

    for i in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        ans.append(int(i[0]))

    return ans
