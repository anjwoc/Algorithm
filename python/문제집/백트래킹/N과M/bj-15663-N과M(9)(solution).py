import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
check = [False] * (n+1)
ans = []


def solve(cnt, start):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return

    overlap = 0
    for i in range(n):
        if not check[i] and overlap != arr[i]:
            check[i] = True
            ans.append(arr[i])
            overlap = arr[i]
            solve(cnt+1, start)
            ans.pop()
            check[i] = False

        start += 1


solve(0, 0)
