import sys, heapq
from collections import deque

input = sys.stdin.readline


def dijkstra():
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            # dropped[now][i[0]]를 체크하는 이유는 제거된 간선들을 고려하지 않기 위해
            if distance[i[0]] > cost and not dropped[now][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


def bfs():
    que = deque()
    que.append(end)
    while que:
        now = que.popleft()
        if now == start:
            continue
        for prev, cost in reverse_arr[now]:
            if distance[now] == distance[prev] + cost:
                dropped[prev][now] = True
                que.append(prev)


while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    start, end = map(int, input().split())

    # INF = sys.maxsize
    arr = [[] for _ in range(n + 1)]
    reverse_arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, time = map(int, input().split())
        arr[x].append((y, time))
        reverse_arr[y].append((x, time))
    distance = [1e9] * (n + 1)
    dropped = [[False] * (n + 1) for _ in range(n + 1)]
    dijkstra()
    bfs()
    distance = [1e9] * (n + 1)
    dijkstra()
    if distance[end] != 1e9:
        print(distance[end])
    else:
        print(-1)
