import sys
input = sys.stdin.readline


def solve(cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, n+1):
        if not check[i] and not ans or max(ans) < i:
            check[i] = True
            ans.append(i)
            solve(cnt+1)
            ans.pop()
            check[i] = False


n, m = map(int, input().split())
ans = []
check = [False] * (n+1)
solve(0)
