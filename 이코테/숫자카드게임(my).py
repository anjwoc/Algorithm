n, m = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
  item = list(map(int, input().split()))
  
  min_value = min(item)
  ans = max(ans, min_value)

print(ans)