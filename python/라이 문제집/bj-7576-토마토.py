import sys
input = lambda: sys.stdin.readline().strip()

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

def zero_check(arr):
    for row in arr:
        for val in row:
            if val == 0:
                return True
    return False

def bfs(arr, tomato):
    ans = 0
    
    while len(tomato) > 0:
        new_tomato = []
        for pos in tomato:
            x, y = pos
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue

                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    new_tomato.append((nx, ny))
        ans += 1
        tomato = new_tomato
    return ans


m, n = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

tomato = [(nx, ny) for (nx, row) in enumerate(arr) for (ny, val) in enumerate(row) if val == 1]
ans = bfs(arr, tomato)

if zero_check(arr):
    print(-1)
else:
    print(ans-1)