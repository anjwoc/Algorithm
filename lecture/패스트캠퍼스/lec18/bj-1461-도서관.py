import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
positive = []
negative = []

# 가장 거리가 먼 책까지의 거리
largest = max(max(arr), -min(arr))

# 최대 힙을 위해 원소를 음수로 구성
for i in arr:
    if i > 0:
        # 양수인 경우
        heapq.heappush(positive, -i)
    else:
        # 음수인 경우
        heapq.heappush(negative, i)

ans = 0
while positive:
    # 한 번에 m개 씩 올믹ㄹ 수 있으므로 m개 씩 빼내기
    ans += heapq.heappop(positive)
    for _ in range(m - 1):
        if positive:
            heapq.heappop(positive)

while negative:
    # 한 번에 m개 씩 올믹ㄹ 수 있으므로 m개 씩 빼내기
    ans += heapq.heappop(negative)
    for _ in range(m - 1):
        if negative:
            heapq.heappop(negative)

print(-ans * 2 - largest)
