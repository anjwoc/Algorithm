n, m = map(int, input().split())
dist = [[0]*m]*n
maze = [list(map(int, input().split())) for a in range(4)]
check = [[0]*m]*n
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    queue = []
    queue.append((i,j))
    while(queue):
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx < 0 or ny < 0 or nx <= n or ny <= m):
                continue
            if(not check[nx][ny] and maze[nx][ny]):
                dist[nx][ny] += 1
                check[nx][ny] = 1

for i in range(n):
    for j in range(m):
        bfs(i, j)
print(dist)    





