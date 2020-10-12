import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(start):
    que = [start]
    visited = [start]
    cnt = 0
    while que:
        vertex = que.pop(0)
        for i in arr[vertex]:
            if i and i not in visited:
                visited.append(i)
                cnt += 1
                que.append(i)
    print(cnt)

bfs(1)