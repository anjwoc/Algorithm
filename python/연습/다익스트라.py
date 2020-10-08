import sys


def dijkstart(k, v, graph):
    INF = sys.maxsize
    # s는 해당 노드를 방문 했는지 여부를 저장하는 변수
    visited = [False] * v
    # d는 memoization을 위한 배열
    # d[i]는 정점 k에서 i까지 가는 최소한의 거리가 저장되어 있다.

    d = [INF] * v
    d[k - 1] = 0

    while True:
        m = INF
        N = -1

        # 방문하지 않은 노드 중 d값이 가장 작은 값을 선택해 그 노드의 번호를 N에 저장한다.
        # 즉, 방문하지 않은 노드 중 K 정점과 가장 가까운 노드를 선택한다.
        for i in range(v):
            if not visited[i] and m > d[i]:
                m = d[i]
                N = i

        # 방문하지 않은 노드 중 현재 K 정점과 가장 가까운 노드와의 거리가 INF 라는 뜻은
        # 방문하지 않은 남아있는 모든 노드가 A에서 도달할 수 없는 노드라는 의미이므로 반복문을 빠져나간다.

        if m == INF:
            break

        # N번 노드를 방문한다.
        # 방문한다는 의미는 모든 노드를 탐색하며 N번 노드를 통해서 가면 더 빨리 갈 수 있는지 확인하고,
        # 더 빨리 갈 수 있다면 해당 노드(노드의 번호가 i라고 하면) d[i]를 업데이트 해준다.
        visited[N] = True

        for i in range(v):
            if visited[i]:
                continue
            via = d[N] + graph[N][i]
            if d[i] > via:
                d[i] = via

    return d


if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input())
    INF = sys.maxsize
    graph = [[INF] * v for _ in range(v)]

    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u - 1][v - 1] = w

    for d in dijkstart(k, v, graph):
        print(d if d != INF else "INF")
