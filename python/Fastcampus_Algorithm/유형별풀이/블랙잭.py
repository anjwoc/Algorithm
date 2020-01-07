n, m = map(int, input().split())
arr = list(map(int, input().split()))

# n(n-1)(n-2) / 3! ==> 경우
# python은 대략 1초에 2천만정도 연산을 함

ret = 0
length = len(arr)

cnt = 0

for i in range(0, length):
  for j in range(i+1, length):
    for k in range(j+1, length):
      sum_value = arr[i] + arr[j] + arr[k]
      if sum_value <= m:
        ret = max(ret, sum_value)

print(ret)

