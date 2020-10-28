import sys
def input(): return sys.stdin.readline().strip()


gateNum = int(input())
p = int(input())
parent = [i for i in range(gateNum+1)]
rank = [0] * (gateNum+1)


def Find(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]


def Union(x, y):
    x = Find(x)
    y = Find(y)
    parent[x] = y


ans = 0
for i in range(p):
    gi = int(input())
    dock = Find(gi)
    if dock != 0:
        Union(dock, dock-1)
        ans += 1
    else:
        break

print(ans)
