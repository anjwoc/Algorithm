import sys, heapq

input = sys.stdin.readline
n = int(input())
arr = []
que = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

for i in arr:
    a = i[0]
    heapq.heappush(que, i[1])
    # 데드라인을 초과하는 경우에 최소 원소를 제거
    if a < len(que):
        heapq.heappop(que)

print(sum(que))