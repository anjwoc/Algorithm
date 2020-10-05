import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j, visited):
    que = deque()
    melting_que = deque()
    visited[i][j] = 1
    que.append((i, j))

    print(visited)

    while que:
        x, y = que.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <= n-1 and 0<= ny <= m-1 and visited[nx][ny] == 0:
                if arr[nx][ny] != 0:
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                else:
                    cnt += 1
        if cnt:
            melting_que.append([i, j, cnt])
        # print(melting_que)
    return melting_que


year = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

while True:
    cnt = 0
    visited = [[0]*(m) for _ in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            if arr[i][j] != 0 and visited[i][j] == 0:
                cnt+=1
                melt = bfs(i, j, visited)
                while melt:
                    nx, ny, value = melt.popleft()
                    arr[nx][ny] = max(arr[nx][ny] - value, 0)
    if cnt == 0:
        year = 0
        break
    if cnt > 2:
        break
    year += 1


print(year)
    
            


        
