import sys
from collections import deque
input = sys.stdin.readline  

for _ in range(int(input())):
  V, E = map(int, input().split())
  adj = [[] for _ in range(V + 1)]
  color = [0] * (V + 1)
  STOP = False

  for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
  
  for i in range(1, V + 1):
    if STOP:
      break
    if color[i] > 0:
      break

    color[i] = 1
    que = deque([i])

    while que and not STOP:
      v = que.popleft()
      c = 3 - color[v]

      for x in adj[v]:
        if color[x] == 0:
          color[x] = c
          que.append(x)
        elif color[x] == color[v]:
          STOP = True
          break
  print("YES" if not STOP else "NO")

  
  
