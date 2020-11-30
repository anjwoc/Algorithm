import sys
from collections import deque
input = sys.stdin.readline

def bfs(v,group):
  que = deque([(v, group)])
  color[v] = group
  
  while que:
    v, group = que.popleft()
    for i in adj[v]:
      if color[i] == 0:
        que.append((i, -group))
        color[i] = -group
      elif color[i] == color[v]:
        return False
  return True

for _ in range(int(input())):
  v,e=map(int,input().split())
  adj=[[] for i in range(v+1)]
  color=[0]*(v+1)

  for i in range(e):
    # 인접리스트 초기화
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

  ans=True
  for i in range(1, v + 1):
    # 각 정점을 방문하며
    if color[i] == 0:
      # 현재 정점의 체크 값이 0이라면 dfs 순회
      if bfs(i, 1) is False:
        # 결과가 False가 나온다면 이분 그래프가 아님
        ans = False
        break

  print('YES' if ans else 'NO')
  