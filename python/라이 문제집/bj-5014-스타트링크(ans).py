import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

def bfs(start, target, up, down, F):
    visited = set()
    que = deque()
    que.append((0, start))
    visited.add(start)

    while que:
        cnt, stairs = que.popleft()
        if stairs == target:
            return cnt
        if stairs + up <= F and stairs + up not in visited:
            visited.add(stairs + up)
            que.append((cnt+1, stairs+up))
        if stairs - down >= 1 and stairs - down not in visited:
            visited.add(stairs - down)
            que.append((cnt+1, stairs-down))

    return "use the stairs"
print(bfs(S, G, U, D, F))
