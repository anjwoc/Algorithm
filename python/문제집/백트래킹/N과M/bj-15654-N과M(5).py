import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
check = [False] * (n+1)
ans = []


def solve(cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(len(arr)):
        if not check[i]:
            check[i] = True
            ans.append(arr[i])
            solve(cnt+1)
            ans.pop()
            check[i] = False


solve(0)
