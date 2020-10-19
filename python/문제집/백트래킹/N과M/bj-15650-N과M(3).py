import sys
input = sys.stdin.readline


def solve(cnt):
    if m == cnt:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, n+1):
        ans.append(i)
        solve(cnt+1)
        ans.pop()


n, m = map(int, input().split())
ans = []
solve(0)
