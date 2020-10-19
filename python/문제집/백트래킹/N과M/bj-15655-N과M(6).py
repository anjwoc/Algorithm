import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
check = [False] * (n+1)
ans = []


def solve(cnt, idx):
    print(ans)
    print('idx: %d' % (idx))
    if cnt == m:
        print(' '.join(map(str, [i for i in ans if i != 0])))
        return
    for i in range(idx, n):
        if not check[i]:
            check[i] = True
            ans.append(arr[i])
            solve(cnt+1, i+1)
            ans.pop()
            check[i] = False


solve(0, 0)
