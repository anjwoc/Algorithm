import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []


def solve(cnt, start):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    else:
        for i in range(start, n):
            if not ans or max(ans) <= arr[i]:
                ans.append(arr[i])
                solve(cnt+1, start)
                ans.pop()
        start += 1


solve(0, 0)
