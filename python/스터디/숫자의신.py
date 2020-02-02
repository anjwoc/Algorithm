import sys
import heapq
input = lambda: sys.stdin.readline()

k, n = map(int, input().split())
arr = []
heap = []
pr = 0
# 수가 중복으로 들어올 수 있는데 중복으로 들어오면
# 들어온만큼 이용해야한다.
for _ in range(k):
  tmp = input()
  arr.append((int(tmp[0]), tmp))
  heapq.heappush(heap, (-tmp, tmp))

for _ in range(len(heap)):
  if len(heap)>=0:
    print(heapq.heappop(heap)[1], end='')
  else:
    # 숫자들을 1번 이상 사용할 경우
    print(type(arr))
    print(type(arr[1]))
    print(max(arr, key=lambda num: num[0])