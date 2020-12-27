from collections import deque


def solution(P, L):
    ans = 0

    que = deque([(v, i) for i, v in enumerate(P)])

    while que:
        value, index = que.popleft()

        if que and max(que)[0] > value:
            que.append((value, index))
        else:
            ans += 1
            if index == L:
                break

    return ans
