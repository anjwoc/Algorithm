import sys
input = sys.stdin.readline

def solve(n, x, y):
  if n == 3:
    maps[y][x] = '*'
    maps[y+1][x-1] = '*'
    maps[y+1][x+1] = '*'
    maps[y+2][x-1] = '*'
    maps[y+2][x-2] = '*'
    maps[y+2][x] = '*'
    maps[y+2][x+1] = '*'
    maps[y+2][x+2] = '*'
  else:
    solve(n//2, x, y)
    solve(n//2, x + n//2, y + n//2)
    solve(n//2, x - n//2, y + n//2)
    

n = int(input())

maps = [[' ' for _ in range(2*n)] for i in range(n)]
solve(n, n-1, 0)
for i in maps:
  print(''.join(i))

