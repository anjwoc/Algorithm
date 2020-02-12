import sys, collections
input = lambda: sys.stdin.readline().strip()

def topological_sort():
  ans = init()
  que = collections.deque(ans[:])
  while que:
    v = que.popleft()
    for nv in adj[v]:
      degree[nv] -= 1
      if not degree[nv]:
        que.append(nv)
        ans.append(nv)
  for i in range(N+1):
    if degree[i]:
      ans.append(nv)
  return ans

def init():
  ans = []
  for i in range(1, N+1):
    if not degree[i]:
      # 진입 차수가 0이면 넣는다.
      ans.append(i)
  return ans

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
check = [False] * (N+1)
degree = [0] * (N+1)
for _ in range(M):
  a, b = map(int, input().split())
  adj[a].append(b)
  degree[b] += 1


print(*topological_sort())


