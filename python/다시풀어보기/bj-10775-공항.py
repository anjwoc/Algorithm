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

    parent[x] = y


g = int(input())
p = int(input())
parent = {i: i for i in range(g+1)}
ans = 0

for _ in range(p):
    gi = int(input())
    docking = find(gi)
    if docking != 0:
        union(docking, docking-1)
        ans += 1
    else:
        break
print(ans)
