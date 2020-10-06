import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    que = deque()
    c = []
    que.append((i, j, 20))
    c.append((i, j, 20))

    while que:
        x, y, beer = que.popleft()
        if x == dx and y == dy:
            print("happy")
            return
        for nx, ny in arr:
            if [nx, ny, 20] not in c:
                l1 = abs(nx- x) + abs(ny - y)
                if beer*50 >= l1:
                    que.append([nx, ny, 20])
                    c.append([nx, ny, 20])
    print("sad")
    return

for _ in range(int(input())):
    n = int(input())
    sx, sy = map(int, input().split())
    arr = []

    for __ in range(n):
        arr.append(list(map(int, input().split())))
    dx, dy = map(int, input().split())
    arr.append((dx, dy))
    bfs(sx, sy)
    
    

        
