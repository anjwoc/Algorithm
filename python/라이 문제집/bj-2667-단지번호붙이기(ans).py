import sys, collections
input = lambda: sys.stdin.readline().strip()

def solve(arr, cnt, pos):
    r, c = pos
    if arr[r][c] == 0:
        return -1
    arr[r][c] = 0
    que = collections.deque([pos])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                que.append((nx, ny))
                cnt += 1
    return cnt

n = int(input())
arr = []
visited = []
ans = []
dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

for _ in range(n):
    arr.append(list(map(int, list(input()))))

item_list = [(nx, ny) for nx, row in enumerate(arr) for ny, val in enumerate(row) if val == 1]

cnt = 0
for x,y in item_list:
    result = solve(arr, cnt + 1, (x, y))
    if result != -1:
        ans.append(result)
    
print(len(ans))
for i in sorted(ans):
    print(i)
