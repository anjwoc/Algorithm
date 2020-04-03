import sys
input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 0 ~ n까지의 합을 구함
sums = [0] * (N + 1)
for i in range(1, N+1):
  sums[i] = sums[i-1] + A[i-1]

# 투 포인터 설정
answer = 10001
start = 0
end = 1

print(sums)
while start != N:
  if sums[end] - sums[start] >= M:
    if end - start < answer:
      answer = end - start
    start += 1
  else:
    if end != N:
      end += 1
    else:
      start += 1

if answer != 10000001:
  print(answer)
else:
  print(0)



