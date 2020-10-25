import sys
def input(): return sys.stdin.readline().strip()


def find(x):
    # path compression
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    # union-by-rank
    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


parent = [0]*100
rank = [0]*100
for i in range(0, 5):
    parent[i] = i
    rank[i] = i


union(1, 2)
union(2, 4)

for i in range(1, 5):
    print(find(i), end=' ')

print()
