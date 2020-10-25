import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input().rstrip())
    heap = []
    print((m+1)//2)
    min_heap = []
    max_heap = []
    for i, data in enumerate(map(int, input().split())):
        idx = i+1
        if len(max_heap) == len(min_heap):
            if len(min_heap) == 0:
                heapq.heappush(max_heap, data)
            else:
                if min_heap and min_heap[0] <= data:
                    top = min_heap[0]
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, data)
                    data = top

                heapq.heappush(max_heap, data)
        else:
            if max_heap and max_heap[0] > data:
                top = max_heap[0]
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, data)
                data = top

            heapq.heappush(min_heap, data)

        if idx % 2 == 1:
            print(heapq.heappop(max_heap))
