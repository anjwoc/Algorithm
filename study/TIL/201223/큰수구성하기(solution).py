import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def dfs(x):
  global ans
  # n보다 작거나 같은 자연수에 대해서만 확인
  if x > n:
    return
  ans = max(x, ans)
  for i in arr:
    # K의 원소로만 구성된 모든 수를 탐색)
    dfs(x*10+i)

dfs(0)
print(ans)