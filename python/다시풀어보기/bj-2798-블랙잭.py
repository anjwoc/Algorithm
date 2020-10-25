import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = arr[i]+arr[j]+arr[k]
            if tmp <= m:
                ans = max(ans, tmp)

print(ans)
