import sys
input = sys.stdin.readline

def solve(n, x, y):
  if n==1:
    maps[y][x] = '*'
    return
  row = 2**(n+1) - 3
  col = 2**(n) - 1

  if n%2 == 0:
    for i in range(x, row+x):
      maps[y][i] = '*' # 상단 가로 줄
    for i in range(col):
      maps[y+i][x+i] = '*'# 왼쪽 대각선
      maps[y+i][x+row-1-i] = '*'# 오른쪽 대각선
    solve(n-1, 2**(n-1)+x, y+1)
  else:
    for i in range(x, row+x): # 하단 가로 줄
      maps[y+col-1][i] = '*'
    for i in range(col):
      # x+row//2로 정중앙으로 옮기고 i칸씩 왼쪽 오른쪽
      maps[y+i][x+row//2-i] = '*' # 왼쪽
      maps[y+i][x+row//2+i] = '*' # 오른쪽

    solve(n-1, 2**(n-1)+x, y+col//2)
n = int(input())
row = 2**(n+1) - 3
col = 2**(n) - 1
maps = [[' '] * row for _ in range(col)]
solve(n, 0, 0)

if n % 2 == 0:
  for i in range(col):
    for j in range(row-i):
      print(maps[i][j], end="")
    print()
else:
  for i in range(col):
    for j in range(row-col+i+1):
      print(maps[i][j], end="")
    print()