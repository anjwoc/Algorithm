import sys
input = sys.stdin.readline

'''
4n-3개의 칸들로 테두리가 이루어짐.
'''

n = int(input())
maps = [[' ' for _ in range(4*n-3)] for _ in range(4*n-3)]
def solve(n, idx):
  if n == 1:
    maps[idx][idx] = '*'
    return
  
  length = 4*n-3
  for i in range(idx, length+idx):
    maps[idx][i] = '*' # 윗줄
    maps[idx+length-1][i] = '*' # 아랫줄

    maps[i][idx] = '*' # 왼쪽
    maps[i][idx+length-1] = '*' # 오른쪽
  return solve(n-1, idx+2)

solve(n, 0)

l = 4*n-3
for i in range(l):
  for j in range(l):
    print(maps[i][j], end='')
  print()