import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n + 1)]

for _ in range(1, n + 1):
    path = list(map(int, input().split()))
    length = len(path)

    for i in range(1, length // 2):
        arr[path[0]].append([path[2 * i - 1], path[2 * i]])


# 첫 번째 결과
first = [0 for _ in range(n + 1)]

# 임의의 노드 x에 대해 dfs(x)에서 최장거리를 이루는 y를 구한다.


def dfs(start, graph, result):
    for v, dist in graph[start]:
        # 결과 배열이 0이면(값이 들어오지 않았다면)
        if not result[v]:
            result[v] = result[start] + dist
            dfs(v, graph, result)


dfs(1, arr, first)
# 루트 노드가 정해저 있지 않아서 초기화
first[1] = 0

ans = max(first)  # 최대값
idx = first.index(ans)  # 최장 경로 노드

# for i in range(len(first)):
#     if ans < first[i]:
#         ans = first[i]
#         idx = i

# 앞에서 구한 y를 다시 dfs(y)를 통해 최장길이를 구한다.
second = [0 for _ in range(n + 1)]
dfs(idx, arr, second)
second[idx] = 0
print(max(second))
