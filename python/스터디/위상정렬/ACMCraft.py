import sys
from collections import deque
imput = lambda: sys.stdin.readline().strip()

def topSort(graph,D,indegree,W):
  queue = deque()
  temp = {}
  for i in graph:
    temp[i] = 0

  for i in graph:
    if indegree[i] == 0:
      queue.append(i)
      temp[i] = times[i]
        
  for t in graph:
    u = queue.popleft()
    if u == W:
      return temp[u]

    for i in graph[u]:
      indegree[i] -= 1
      temp[i] = max(temp[i],temp[u]+times[i])
      if indegree[i] == 0:
        queue.append(i)

for t in range(int(input())):
  N,K = map(int,input().split())
  times = tuple(map(int,input().split()))
  graph = {}
  indegree = {}
  for i in range(N):
    graph[i] = []
    indegree[i] = 0
  for i in range(K):
    X,Y = map(int,input().split())
    graph[X-1].append(Y-1)
    indegree[Y-1] += 1
  W = int(input())
  W -= 1

  print(topSort(graph,times,indegree,W))