import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

ans = 0
for i in range(1, len(arr) + 1):
    ans += abs(i - arr[i - 1])

print(ans)
