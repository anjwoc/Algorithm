import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs(i, j, visited):
    que = deque([(i, j)])
    melting_que = deque()

    while que:
        x, y = que.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited:
                if arr[nx][ny] == 0:
                    cnt += 1
                else:
                    visited.add((nx, ny))
                    que.append((nx, ny))
        if cnt:
            melting_que.append((x, y, cnt))
    return melting_que
        

year = 0
while True:
    visited = set()
    melting_que = deque()
    cnt = 0
    
    for i in range(n-1):
        for j in range(m-1):    
            if arr[i][j] != 0 and (i, j) not in visited:
                visited.add((i,j))
                melt = bfs(i, j, visited)
                cnt += 1
                
                for x, y, val in melt:
                    arr[x][y] = max(arr[x][y] - val, 0)

    if cnt == 0:
        year = 0
        break
                
    if cnt >= 2:
        break
    year += 1

print(year)
    
       

