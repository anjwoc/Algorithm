import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, target, up, down, F):
  que = deque([(start, 0)])
  visited = set()
  visited.add(start)

  while que:
    x, cnt = que.popleft()
    if x == target:
      return cnt
    
    if x + up <= F and x + up not in visited:
      visited.add(x+up)
      que.append((x+up, cnt+1))
    if x - down >= 1 and x - down not in visited:
      visited.add(x-down)
      que.append((x-down, cnt+1))  
  return "use the stairs"

F, S, G, U, D = map(int, input().split())
print(bfs(S, G, U, D, F))