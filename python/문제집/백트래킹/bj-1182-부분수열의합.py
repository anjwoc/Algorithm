import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
check = [False] * (n+1)
ans = 0


def solve(idx, acc):
    global ans
    print(idx, acc)
    if idx >= n:
        if acc == m:
            ans += 1
        return
    solve(idx+1, acc+arr[idx])
    solve(idx+1, acc)


solve(0, 0)
print(ans if m else ans-1)
