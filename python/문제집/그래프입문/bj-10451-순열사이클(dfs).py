import sys
input = sys.stdin.readline

def dfs(visited, v):
  visited[i] = 1

  for x in adj[v]:
    if not visited[x]:
      visited[x] = 1
      dfs(visited, x)
    

for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  adj = [[] for _ in range(n + 1)]
  visited = [0] * (n+1)
  for i in range(1, n + 1):
    adj[i].append(arr[i-1])
    adj[arr[i-1]].append(i)

  ans = 0
  for i in range(1, n + 1):
    if not visited[i]:
      ans += 1
      dfs(visited, i)
  print(ans)      


