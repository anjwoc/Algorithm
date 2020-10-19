import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []
check = [False] * n


def solve(cnt, idx):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return

    tmp = 0
    for i in range(idx, n):
        if not check[i] and tmp != arr[i]:
            ans.append(arr[i])
            check[i] = True
            tmp = arr[i]
            solve(cnt+1, i+1)
            ans.pop()
            check[i] = False


solve(0, 0)
