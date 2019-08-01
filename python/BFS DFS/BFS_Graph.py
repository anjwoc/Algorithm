import sys

n, m, v = map(int, input().split()) #정점의 개수, 간선의 개수, 시작 번호

a = [list() for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for x in a:
    print(x)