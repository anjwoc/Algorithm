import sys, collections
input = lambda: sys.stdin.readline().strip()

def solve(start):
    global visited
    que = collections.deque([start])
    visited = [start]
    cnt = 0
    while que:
        x, y = que.popleft()
        data = arr[x][y]
        if data == 0:
            continue
        for i in range(4):
            nx = i + dx[i]
            ny = i + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] == 1 and (nx, ny) not in visited:
                visited.append((nx, ny))
                que.append((nx, ny))
                cnt += 1

    return cnt

n = int(input())
arr = []
start = (0, 0)
visited = []
ans = 0

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

for _ in range(n):
    arr.append(list(map(int, list(input()))))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and (i, j) not in visited:
            print(solve((i, j)))

# print(ans)
