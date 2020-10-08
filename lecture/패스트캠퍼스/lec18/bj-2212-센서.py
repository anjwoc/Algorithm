import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 1e9
for i in range(n - 1):
    # print(i)
    ans = min(abs(arr[0] - arr[i]) + abs(arr[i + 1] - arr[n - 1]), ans)

print(ans)