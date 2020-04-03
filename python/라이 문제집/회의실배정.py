import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
arr = sorted(arr, key=lambda arr: arr[0])
arr = sorted(arr, key=lambda arr: arr[1])
ans = 0
curtime = 0

for time in arr:
    if time[0] >= curtime:
        curtime = time[1]
        ans += 1

print(ans)
