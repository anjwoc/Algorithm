import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
check = [False] * (n+1)
ans = []
record = set()


def solve(cnt, start):
    if cnt == m:
        record.add(str(' '.join(map(str, ans))))
        return
    else:
        for i in range(start, n):
            if not check[i]:
                check[i] = True
                ans.append(arr[i])
                solve(cnt+1, start)
                ans.pop()
                check[i] = False

        start += 1


solve(0, 0)
print('\n'.join(sorted(record)))
