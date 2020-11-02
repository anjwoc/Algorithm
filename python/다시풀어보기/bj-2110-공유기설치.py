import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
start = arr[1] - arr[0]  # 최소 거리
end = arr[-1] - arr[0]  # 최대 거리
ans = 0

while start <= end:
    # mid는 gap을 의미하고 설치 가능한 공유기의 개수
    gap = (start + end) // 2
    value = arr[0]
    cnt = 1  # 설치한 공유기 개수
    for i in range(1, len(arr)):
        if arr[i] >= value + gap:
            # 공유기 설치
            value = arr[i]
            cnt += 1
    if cnt >= c:
        # 설치 가능한 공유기의 개수가 C개 이상일때
        start = gap + 1
        ans = gap
    else:
        # 설치한 공유기가 c 보다 작으면 gap을 감소시킨다.
        end = gap - 1

print(ans)
