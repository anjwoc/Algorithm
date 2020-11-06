import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    data = int(input())
    heapq.heappush(arr, data)

cnt = 0
acc = 0
ans = 0
while arr:
    num = heapq.heappop(arr)
    cnt += 1
    acc += num
    if cnt == 2:
        arr.append(acc)
        ans += acc
        acc = 0
        cnt = 0
print(ans)
