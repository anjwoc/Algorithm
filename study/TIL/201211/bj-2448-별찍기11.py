import sys
input = sys.stdin.readline

def solve(n, x, y):
  if n == 3:
    maps[y][x] = '*' # 위 삼각형
    maps[y+1][x-1] = '*' # 왼쪽 삼각형
    maps[y+1][x+1] = '*' # 오른쪽 삼각형
    for i in range(x-2, x+3, 1):
      # x의 범위가 x-2~x+2까지
      maps[y+2][i] = '*'
  else:
    solve(n//2, x, y)
    solve(n//2, x + n//2, y + n//2)
    solve(n//2, x - n//2, y + n//2)
    

n = int(input())

maps = [[' ' for _ in range(2*n)] for i in range(n)]
solve(n, n-1, 0)
for i in maps:
  # 배열의 각 행을 join함수로 공백이 없는 문자열로 변환
  print(''.join(i))

