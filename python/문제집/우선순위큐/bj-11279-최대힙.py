import heapq
import sys
input = sys.stdin.readline

n = int(input())
que = []
for _ in range(n):
    data = int(input())
    if data != 0:
        heapq.heappush(que, (-data, data))
    else:
        try:
            print(heapq.heappop(que)[1])
        except:
            print(0)
