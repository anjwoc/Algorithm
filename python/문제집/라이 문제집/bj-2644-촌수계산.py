import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(v, target):
    cnt = 0
    q = deque([[v, cnt]])
    while q:
        value = q.popleft()
        v = value[0]
        cnt = value[1]
        if v == target:
            return cnt
        
        if not visited[v]:
            cnt += 1
            visited[v] = True
            for e in arr[v]:
                if not visited[e]:
                    q.append([e, cnt])
    return -1

print(bfs(p1, p2))