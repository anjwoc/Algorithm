import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    que = deque([(i, j, 20)])
    visited = []
    visited.append((i, j, 20))

    while que:
        x, y, beer = que.popleft()
        if x == dest_x and y == dest_y:
            print('happy')
            return
        for nx, ny in arr:
            if (nx, ny, 20) not in visited:
                tmp = abs(nx-x) + abs(ny-y)
                if beer * 50 >= tmp:
                    que.append((nx, ny, 20))
                    visited.append((nx, ny, 20))
    print("sad")
    return

for _ in range(int(input())):
    n = int(input()) # 편의점 개수
    start_x, start_y = map(int, input().split()) # 시작 좌표
    arr = []
    for __ in range(n):
        # 편의점 좌표
        arr.append(list(map(int, input().split())))
    dest_x, dest_y = map(int, input().split())
    arr.append((dest_x, dest_y))
    bfs(start_x, start_y)
    
