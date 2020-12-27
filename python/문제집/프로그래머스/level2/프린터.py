import heapq
from collections import deque


def solution(P, L):
    ans = 0
    alpha = list(map(str, range(1, len(P)+1)))

    targetIdx = L
    items = zip(list(map(lambda x: -x, P)), alpha)
    print(items)
    que = deque([*items])
    print(que)
    target = que[L][1]
    print(target)
    maps = list(que)
    heapq.heapify(maps)
    print(maps)

    cur = 1
    cnt = 1
    while que:
        x, char = que.popleft()
        x2, prior = heapq.heappop(maps)
        print(x, char, x2, prior, cnt)
        if char == prior:
            if char == target:
                ans = cnt
                break
            else:
                cnt += 1
                continue
        else:
            que.append((x, char))
            heapq.heappush(maps, (x2, prior))

    return ans


items = [
    [[2, 1, 3, 2],	2],
    [[1, 1, 9, 1, 1, 1], 0]
]

for P, L in items:
    print(solution(P, L))
