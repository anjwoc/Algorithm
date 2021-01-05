import sys
input = sys.stdin.readline


def dfs(v, start):
    visited[v] = True

    for x in adj[v]:
        if not visited[x]:
            dfs(x, start)
        elif visited[x] and x == start:
            # 현재 방문한 정점이 최초 시작 정점과 같으면 사이클을 이룬다.
            ans.append(x)


n = int(input())
adj = [[] for _ in range(n+1)]
for i in range(n):
    adj[i+1].append(int(input()))

ans = []

for i in range(1, n+1):
    # i는 시작 정점
    visited = [False] * (n+1)
    dfs(i, i)

print(len(ans))
for i in ans:
    print(i)
