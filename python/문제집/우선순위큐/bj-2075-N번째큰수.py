import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    for num in input().split():
        data = int(num)
        heapq.heappush(arr, data)
        if len(arr) > n:
            heapq.heappop(arr)

print(arr)
