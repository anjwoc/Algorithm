import sys

input = lambda: sys.stdin.readline().strip()

arr = []
ans = [0] * 10
sums = 0
for _ in range(9):
    n = int(input())
    arr.append(n)
    sums += n

arr.sort()
cnt = 0
# 총합 sum(9개의 합)에서 2개씩 더한 값을 빼서 100인걸 찾는다.
for i in range(0, 9, 1):
    for j in range(i + 1, 9, 1):
        tmp = arr[i] + arr[j]
        if sums - tmp == 100:
            for k in range(0, 9, 1):
                if k == i or k == j:
                    continue
                ans[cnt] = arr[k]
                cnt += 1

for i in ans:
    if i == 0:
        break
    print(i)
