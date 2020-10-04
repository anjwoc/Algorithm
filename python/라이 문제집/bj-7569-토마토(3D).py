import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
dx = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

tomato = deque([
    (nx, ny, nz)
    for (nx, row) in enumerate(arr)
    for (ny, col) in enumerate(row)
    for (nz, val) in enumerate(col) 
        if val == 1
])

def bfs(arr, tomato):
    while len(tomato) > 0:
        x, y, z = tomato.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nx>=h or ny>=n or nz<0 or nz>=m:
                continue
            if arr[nx][ny][nz]:
                continue
            tomato.append((nx, ny, nz)) 
            arr[nx][ny][nz] = arr[x][y][z] + 1
        
ans = 0
bfs(arr, tomato)
for i in range(h):
    for j in range(n):
        if 0 in arr[i][j]:
            print(-1)
            exit(0)
        ans = max(ans, max(arr[i][j]))

print(ans-1)
