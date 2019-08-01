import sys
import queue

#정점의 개수, 간선의 개수, 시작 번호
n, m, v = map(int, sys.stdin.readline().split())

#(n+1)*(n+1) 크기의 배열
a = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    a[x][y] = 1
    a[y][x] = 1

for x in a:
    print(x)



