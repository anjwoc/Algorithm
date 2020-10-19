import sys
input = sys.stdin.readline


def solve(ans):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n+1):
        if not check[i]:
            check[i] = True
            ans.append(i)
            solve(ans)
            ans.pop()
            check[i] = False


ans = []
n, m = map(int, input().split())
check = [False]*(n+1)
solve(ans)
