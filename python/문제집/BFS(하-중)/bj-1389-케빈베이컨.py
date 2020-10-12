import sys
from collections import deque
input = sys.stdin.readline


def bfs(arr, x):
    que = deque()
    visit = [-1 for _ in range(n+1)]
    visit[x] = 0
    que.append(x)
    cnt = 0

    while que:
        v = que.popleft()
        for i in arr[v]:
            if visit[i] == -1:
                visit[i] = visit[v] + 1
                que.append(i)

    for i in range(1, n+1):
        if visit[i] != -1:
            cnt += visit[i]

    return cnt


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visit = [[0] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = []
for i in range(n+1):
    ans.append(bfs(arr, i))

result = []
min_value = min(list(filter(lambda x: x != 0, ans)))

# 가장 작은 값을 가진 인덱스를 따로 뽑아낸다.
for j in range(1, n+1):
    if ans[j] == min_value:
        result.append(j)

print(min(result))
