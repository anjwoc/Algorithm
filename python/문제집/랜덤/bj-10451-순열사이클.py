import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v, start):
    global ans, visited
    visited[v] = True

    for x in adj[v]:
        if not visited[x]:
            dfs(x, start)
        elif visited[x] and x == start:
            ans += 1


for _ in range(int(input())):
    n = int(input())
    adj = [[] for _ in range(n+1)]

    arr = list(map(int, input().split()))
    for i in range(n):
        adj[i+1].append(arr[i])

    ans = 0
    visited = [False] * (n+1)
    for i in range(1, n+1):
        dfs(i, i)

    print(ans)
