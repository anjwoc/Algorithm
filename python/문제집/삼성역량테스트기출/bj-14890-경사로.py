import sys
input = sys.stdin.readline

def calc(i, row):
  global ans
  cnt = 1
  for j in range(N-1):
    sub = arr[i][j+1] - arr[i][j] if row else arr[j+1][i] - arr[j][i]
    if sub == 0:
      cnt += 1
    elif sub == 1 and cnt >= L:
      # 오르막
      cnt = 1
    elif sub == -1 and cnt >= 0:
      # 내리막
      cnt = -L+1
    else:
      return

  if cnt >= 0:
    ans += 1

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
  calc(i, 1)
  calc(i, 0)

print(ans)
