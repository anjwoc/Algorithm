import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
items = [list(map(int, input().split())) for _ in range(k)]

for i, j, x, y in items:
    ans = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            ans += arr[a][b]

    print(ans)
