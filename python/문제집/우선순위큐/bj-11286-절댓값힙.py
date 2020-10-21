import heapq
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    data = int(input())
    if data != 0:
        heapq.heappush(heap, (abs(data), data))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
