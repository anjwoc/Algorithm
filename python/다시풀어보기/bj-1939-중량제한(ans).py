import sys
from collections import deque
input = sys.stdin.readline


def bfs(c):
    que = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True
    while que:
        x = que.popleft()
        for y, weight in arr[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                que.append(y)
    return visited[end_node]


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
start = 1000000000
end = 1
for _ in range(m):
    x, y, c = map(int, input().split())
    arr[x].append((y, c))
    arr[y].append((x, c))
    start = min(start, c)
    end = max(end, c)

start_node, end_node = map(int, input().split())


ans = start
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):  # 이동이 가능하면 중량 증가
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)
