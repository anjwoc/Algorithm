def solution(S, T):
    answer = 0
    for item in T:
        lst = list(filter(lambda x: x in S, item))

        flag = True
        for i in range(len(lst)):
            if S[i] != lst[i]:
                flag = False
        if not flag:
            continue
        answer += 1

    return answer
