import sys
g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
plane = []
for _ in range(p):
    plane.append(int(sys.stdin.readline()))


def parent_find(x):
    if x == parent[x]:
        return x

    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]


def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y


# parent[0] = 0 까지 만들어준다. parent[x] = 0까지 만들어지는 게 핵심
parent = {i: i for i in range(g+1)}
cnt = 0
for i in plane:
    print('gi: %d' % (i))
    x = parent_find(i)
    print('docking: %d' % (x))
    if x == 0:
        break
    union(x, x-1)
    cnt += 1
print(cnt)
