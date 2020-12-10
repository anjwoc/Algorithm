import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
dx,dy = [-1,1,0,0], [0,0,1,-1]
q = deque()
board = ['0'*(m+2)]
dist = [[[[0 for _ in range(m+2)] for _ in range(n+2)] for _ in range(m+2)] for _ in range(n+2)]
# for i in range(n):
#     tmp = list(sys.stdin.readline().strip())
#     board.append(tmp)

def init():
    for _ in range(n):
        board.append(list('0' + input().strip() + '0'))
    board.append(list('0'*(m+2)))
    x, y = -1, -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] == 'o':
                if x == -1:
                    x, y = i, j
                else:
                    q.append((x, y, i, j))
                    return

def escape(x, y):
    return x < 1 or x > n or y < 1 or y > m

def wall(x, y):
    return board[x][y] == '#'

def bfs():
    while q:
        x, y, a, b = q.popleft()
        if dist[x][y][a][b] > 10:
            break
        if escape(x, y) ^ escape(a, b):
            print(dist[x][y][a][b])
            return
        for i in range(4):
            nx, ny, na, nb = x+dx[i], y+dy[i], a+dx[i], b+dy[i]
            if escape(nx, ny) and escape(na, nb):
                continue
            if wall(nx, ny) and wall(na, nb):
                continue
            if wall(nx, ny):
                nx, ny = x, y
            elif wall(na, nb):
                na, nb = a, b
            if not dist[nx][ny][na][nb]:
                q.append((nx, ny, na, nb))
                dist[nx][ny][na][nb] = dist[x][y][a][b]+1
    print(-1)

init()
bfs()