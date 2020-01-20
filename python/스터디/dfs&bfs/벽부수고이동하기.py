import sys

input = lambda: sys.stdin.readline().strip()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(maps):
  global ans
  if ans == 0:
    return -1

  for i in range(4):

# 1 <= n, m <= 1000
n, m = map(int, input().split())
maps = []
ans = 0
for _ in range(0, n):
  maps.append(input())
print(maps[0][0])
print(maps[n-1][m-1])

