import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(start, next, value, visited):
  global ans
  print(value)
  if len(visited) == n:
    if travel[next][start] != 0:
      ans = min(ans, value + travel[next][start])
    return
  for i in range(n):
    if travel[next][i] != 0 and i != start and i not in visited:
      # travel[next][i]가 길이 없지 않고 출발지가 아니며 방문하지 않았으면
      visited.append(i) # 방문 표시
      dfs(start, i, value + travel[next][i], visited) # 재귀
      visited.pop()

n = int(input())
travel = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize

for i in range(n):
  dfs(i, i, 0, [i])

print(ans)

