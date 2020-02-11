import sys
input = lambda: sys.stdin.readline().strip()
INF = 1e9
n, m = map(int, input().split()) # n은 도시의 개수, m은 버스 노선의 개수
graph = [list(map(int, input().split())) for _ in range(m)]
bf = [INF] * (n+1)
def solve():
  bf[1] = 0
  negativeCycle = False
  for i in range(n):
    for j in range(m):
      v = graph[j][0] # 현 노드
      nv = graph[j][1] # 이웃 노드
      w = graph[j][2] # 가중치
      if bf[v] != INF and bf[nv] > bf[v] + w:
        bf[nv] = bf[v] + w
        if i == n-1:
          negativeCycle = True
  if negativeCycle:
    print(-1)
  else:
    for i in range(2, n+1):
      if bf[i] == INF:
        print(-1)
      else:
        print(bf[i])

solve()





