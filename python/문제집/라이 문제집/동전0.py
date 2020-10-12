import sys

input = lambda: sys.stdin.readline().strip()
arr = []
n, k = map(int, input().split())
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

ans = 0
for i in arr:
    if k // i == 0:
        continue
    ans += k // i
    k = k % i


print(ans)
