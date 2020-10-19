import sys
input = sys.stdin.readline


def solve(start, cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    # 반복문의 시작 지점을 조정해서 최적화 가능
    for i in range(start, n+1):
        if not ans or max(ans) <= i:
            ans.append(i)
            solve(i, cnt+1)
            ans.pop()


n, m = map(int, input().split())
ans = []
check = [False] * (n+1)
solve(1, 0)
