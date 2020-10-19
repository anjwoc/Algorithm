import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []


def solve(cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
    else:
        for i in range(n):
            ans.append(arr[i])
            solve(cnt+1)
            ans.pop()


solve(0)
