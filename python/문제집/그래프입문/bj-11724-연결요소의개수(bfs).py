import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

def bfs(A, visited, i):
  que = deque([i])
  visited[i] = 1
  while que:
    v = que.popleft()
    for i in A[v]:
      if not visited[i]:
        visited[i] = 1
        que.append(i)

for _ in range(m):
  x, y = map(int, input().split())
  arr[x].append(y)
  arr[y].append(x)

ans = 0
visited = [0] * (n + 1)
for i in range(1, n+1):
  if not visited[i]:
    bfs(arr, visited, i)
    ans += 1

print(ans)
