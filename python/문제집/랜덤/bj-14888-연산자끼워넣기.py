import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(acc, idx, add, sub, mul, div):
    global arr, ans
    if idx == n:
        ans.append(acc)
        return
    else:
        if add:
            dfs(acc + arr[idx], idx+1, add-1, sub, mul, div)
        if sub:
            dfs(acc-arr[idx], idx+1, add, sub-1, mul, div)
        if mul:
            dfs(acc*arr[idx], idx+1, add, sub, mul-1, div)
        if div:
            dfs(int(acc/arr[idx]), idx+1, add, sub, mul, div-1)


n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())


ans = []
dfs(arr[0], 1, add, sub, mul, div)

min_value = min(ans)
max_value = max(ans)

print(max_value)
print(min_value)
