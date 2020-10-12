import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
count = [0] * (1000001)
visited = set()

que = deque([s])
while que:
    v = que.popleft()
    if v == g:
        print(count[g])
        exit(0)
    if v + u <= f and v+u not in visited:
        idx = v + u
        visited.add(idx)
        que.append(idx)
        count[idx] = count[v] + 1
    if v - d >= 1 and v-d not in visited:
        idx = v - d
        visited.add(idx)
        que.append(idx)
        count[idx] = count[v] + 1
            
print("use the stairs")