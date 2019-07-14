n, m = map(int , input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
cnt , volume = 0,0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    queue = list()
    queue.append((i,j))
    volume = 1
    check[i][j] = True

    while(queue):
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx<0 or nx >= n or ny >= m or ny<0):
                continue
            if (not check[nx][ny] and arr[nx][ny]):
                queue.append((nx, ny))
                check[nx][ny] = True
                volume+=1
    return volume


for i in range(n):
    for j in range(m):
        if not check[i][j] and arr[i][j]:
            volume = max(volume, bfs(i,j))
            cnt+=1
print(cnt)
print(volume)