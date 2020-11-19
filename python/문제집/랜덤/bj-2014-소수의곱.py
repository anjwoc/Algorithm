import sys
import heapq
import copy
input = sys.stdin.readline

'''
heap을 사용하는 문제

'''

k, n = map(int, input().split())
primes = list(map(int, input().split()))
heap, check = copy.deepcopy(primes), set()
# arr = []
# list를 heap으로 바꿈
heapq.heapify(heap)
ith = 0

while ith < n:
    # 힙의 가장 꼭대기 값을 추출한다.
    min_value = heapq.heappop(heap)
    # 추출한 값이 check set에 이미 들어있는 중복된 값이라면
    # 2x3x2, 2x2x3 처럼 중복되는 경우
    if min_value in check:
        continue
    ith += 1
    # 아직 나오지 않은 수면 check에 저장한다.
    check.add(min_value)
    # arr.append(min_value)
    for i in primes:
        if min_value * i < 2 ** 32:
            heapq.heappush(heap, min_value*i)

print(arr)
print(min_value)
