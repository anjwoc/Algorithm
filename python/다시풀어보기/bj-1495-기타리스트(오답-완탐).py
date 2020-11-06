import sys
from collections import deque
input = sys.stdin.readline


def solve(s):
    que = deque([])
    que.append((s, 0))
    ans = 0
    while que:
        p, idx = que.popleft()
        if idx == n:
            break
        for v in [p+volume[idx], p-volume[idx]]:
            if v < 0 or v > m:
                continue
            if idx == n-1:
                ans = max(ans, v)
            que.append((v, idx+1))

    if ans == 0:
        print(-1)
    else:
        print(ans)
    exit(0)


n, s, m = map(int, input().split())
volume = list(map(int, input().split()))
solve(s)
