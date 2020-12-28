import sys
from collections import deque
input = sys.stdin.readline

tetromino = [
  [(0,0), (0,1), (1,0), (1,1)], # ㅁ
  [(0,0), (0,1), (0,2), (0,3)], # ㅡ
  [(0,0), (1,0), (2,0), (3,0)], # ㅣ
  [(0,0), (0,1), (0,2), (1,0)], 
  [(1,0), (1,1), (1,2), (0,2)],
  [(0,0), (1,0), (1,1), (1,2)], # ㄴ
  [(0,0), (0,1), (0,2), (1,2)], # ㄱ
  [(0,0), (1,0), (2,0), (2,1)],
  [(2,0), (2,1), (1,1), (0,1)],
  [(0,0), (0,1), (1,0), (2,0)], 
  [(0,0), (0,1), (1,1), (2,1)],
  [(0,0), (0,1), (0,2), (1,1)], # ㅜ
  [(1,0), (1,1), (1,2), (0,1)], # ㅗ
  [(0,0), (1,0), (2,0), (1,1)], # ㅏ
  [(1,0), (0,1), (1,1), (2,1)], # ㅓ
  [(1,0), (2,0), (0,1), (1,1)],
  [(0,0), (1,0), (1,1), (2,1)],
  [(1,0), (0,1), (1,1), (0,2)],
  [(0,0), (0,1), (1,1), (1,2)]
]


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# def solve(x, y):
#   global ans
#   for i in range(19):
#     tmp = 0
#     for dx, dy in tetromino[i]:
#       nx, ny = x+dx, y+dy
#       if nx < 0 or ny < 0 or nx >= n or ny >= m:
#         break
#       tmp += maps[nx][ny]
#     ans = max(ans, tmp)

def bfs(a, b):
  global ans
  que = deque([(a, b)])

  while que:
    x, y = que.popleft()
    for shape in tetromino:
      tmp = 0
      for dx, dy in shape:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
          break        
        tmp += maps[nx][ny]
      
      ans = max(ans, tmp)

for i in range(n):
  for j in range(m):
    solve(i, j)

print(ans)
