import sys
import collections
input = sys.stdin.readline

dx = (1, 2, 2, 1, -1, -2, -2, -1)
dy = (2, 1, -1, -2, -2, -1, 1, 2)


def bfs(arr, x1, y1, x2, y2):
    que = collections.deque()
    que.append((x1, y1))
    visited = set()
    while que:
        x, y = que.popleft()

        if x == x2 and y == y2:
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and (nx, ny) not in visited:
                visited.add((nx, ny))
                que.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1


for _ in range(int(input())):
    l = int(input())
    arr = [[0] * l for _ in range(l)]
    x1, y1 = list(map(int, input().split()))
    x2, y2 = list(map(int, input().split()))
    bfs(arr, x1, y1, x2, y2)
    print(arr[x2][y2])
