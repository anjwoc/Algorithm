import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
heap = []
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1


for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    data = heapq.heappop(heap)
    ans.append(data)
    for y in arr[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in ans:
    print(i, end=' ')
