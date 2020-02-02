import sys
import heapq
input = lambda: sys.stdin.readline().strip()

n = int(input())
max_heap = []
min_heap = []

for _ in range(n):
  num = int(input())
  if len(min_heap) == len(max_heap):
    heapq.heappush(max_heap, (-num, num))
  else:
    heapq.heappush(min_heap, (num, num))
  
  if min_heap and max_heap[0][1] > min_heap[0][1]:
    tmp_max = heapq.heappop(max_heap)[1]
    tmp_min = heapq.heappop(min_heap)[1]
    heapq.heappush(max_heap, (-tmp_min, tmp_min))
    heapq.heappush(min_heap, (tmp_max, tmp_max))
  
  print(max_heap[0][1])

    
  

