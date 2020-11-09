import sys
from collections import deque
input = sys.stdin.readline

dx = {
    # 가로
    0: [(1, 1), (1, 1)],
    # 세로
    1: [(0, 0), (0, 1)],
    # 대각선
    2: [(1, 1), (1, 0), (1, 1)],
}

dy = {
    # 가로
    0: [(0, 0), (0, 1)],
    # 세로
    1: [(1, 1), (1, 1)],
    # 대각선
    2: [(1, 0), (1, 1), (1, 1)],
}

n = int(input())
arr = []
que = deque([])
pipe = [(0, 0, 0, 1)]
direction = 0  # 0:가로, 1: 세로, 2: 대각선
for _ in range(n):
    arr.append(list(map(int, input().split())))


def bfs(direction, start):
    que = deque(start)
    visited = {}
    ans = 0

    while que:
        x1, y1, x2, y2 = que.popleft()

        length = len(dx[direction])
        for i in range(length):
            nx1 = x1 + dx[direction][i][0]
            ny1 = y1 + dy[direction][i][0]
            nx2 = x2 + dx[direction][i][1]
            ny2 = y2 + dy[direction][i][1]
            if nx1 >= 0 and nx2 >= 0 and nx2 < n and nx1 < n and ny1 >= 0 and ny2 >= 0 and ny1 < n and ny2 < n:
                if arr[nx1][ny1] == 0 and arr[nx2][ny2] == 0:
                    if (nx2 == n-1 and ny2 == n-1) or (nx1 == n-1 and ny1 == n-1):
                        ans += 1
                    try:
                        if visited[(direction, nx1, ny1, nx2, ny2)]:
                            continue
                    except:
                        visited[(direction, nx1, ny1, nx2, ny2)] = True
                        que.append((nx1, ny1, nx2, ny2))

    print(ans)


bfs(direction, pipe)
