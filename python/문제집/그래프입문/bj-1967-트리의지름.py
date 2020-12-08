import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [[] for _ in range(n + 1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    arr[parent].append((child, weight))
    arr[child].append((parent, weight))

first = [0 for _ in range(n+1)]


def dfs(start, graph, result):
    for v, dist in graph[start]:
        if not result[v]:
            result[v] = result[start] + dist
            dfs(v, graph, result)

dfs(1, arr, first)

x = max(first)
idx = first.index(x)

second = [0 for _ in range(n+1)]
dfs(idx, arr, second)

print(max(second))