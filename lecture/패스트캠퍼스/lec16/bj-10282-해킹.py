import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    heap = []
    # (cost, start)
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    INF = sys.maxsize
    distance = [INF] * (n + 1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append((a, s))
    dijkstra(c)

    cnt = 0
    max_distance = 0
    for i in distance:
        if i != INF:
            cnt += 1
            if i > max_distance:
                max_distance = i
    print(cnt, max_distance)