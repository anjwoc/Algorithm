import sys
import heapq
input: lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    m = int(input())
    heap = []
    print((m+1)//2)
    ans = ''
    min_heap = []
    max_heap = []
    cnt = 0
    n = int(m / 10)
    n = (m % 10) != 0 and n + 1 or n
    arr = []
    for i in range(n):
        arr.extend(list(map(int, input().split())))

    for idx, data in enumerate(arr):

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, data)
        else:
            heapq.heappush(min_heap, data)
        if len(min_heap) != 0:
            if max_heap[0] > min_heap[0]:
                heapq.heappush(min_heap, heapq.heappop(max_heap))
                heapq.heappush(max_heap, heapq.heappop(min_heap))

        if (i+1) % 2 == 0:
            if idx == m-1 or cnt == 9:
                # print(max_heap)
                ans += '%d\n' % (heapq.heappop(max_heap))
                cnt = 0
                # if max_heap:

            else:
                ans += '%d ' % (heapq.heappop(max_heap))
                # print(max_heap)
                # if max_heap:

        cnt += 1
