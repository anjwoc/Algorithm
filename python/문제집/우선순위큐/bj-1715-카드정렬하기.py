import sys
import heapq
input = sys.stdin.readline
heap = []
n = int(input())
for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

ans = 0
i = 0
while heap:
    if i == n-1:
        break
    cmp1 = heapq.heappop(heap)
    cmp2 = heapq.heappop(heap)
    tmp = cmp1 + cmp2
    ans += tmp
    heapq.heappush(heap, tmp)
    i += 1

print(ans)
