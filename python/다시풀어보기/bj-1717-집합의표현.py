import sys

input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x


n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        # union
        union(a, b)
    elif op == 1:
        # find
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
