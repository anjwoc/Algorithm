import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    arr[parent].append((child, weight))
    arr[child].append((parent, weight))

def findFarthest(node, dist):
    visited[node] = True
    ans[node] = dist

    for v in arr[node]:
        if not visited[v[0]]:
            findFarthest(v[0], dist + v[1])
    # 한 번 더 탐색을 해야하므로 visited를 다시 초기화
    visited[node] = False 
    return

ans = [0] * (n+1)
findFarthest(1, 0)
dist = max(ans) # 최대값
node = ans.index(dist) # 최대값의 노드 찾기

ans = [0] * (n+1)
findFarthest(node, 0) # 최대값인 노드로 부터 다시 탐색
print(max(ans))