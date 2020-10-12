import sys
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline


n, m = map(int, input().split())
d = [[INF]*n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    d[a-1][b-1] = 1
    d[b-1][a-1] = 1

# k = 거쳐가는 노드
for k in range(n):
    # i = 출발 노드
    for i in range(n):
        # j = 도착 노드
        for j in range(n):
            if i == j:
                d[i][j] = 0
            else:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = []
for i in d:
    ans.append(sum(i))

for i in range(n):
    if ans[i] == min(ans):
        print(i+1)
        break
