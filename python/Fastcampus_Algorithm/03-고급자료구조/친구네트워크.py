import sys

input = lambda: sys.stdin.readline().strip()


def getParent(parents, x):
    if parents[x] == x:
        return x

    # 재귀적으로 내가 연결하려는 노드에 부모가 있으면 해당 부모로 연결해야한다.
    p = getParent(parents, parents[x])
    parents[x] = p
    return p


def union(parents, x, y, cnt):
    a = getParent(parents, x)
    b = getParent(parents, y)
    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]


def find(x, parents):
    if parents[x] == x:
        return x
    return find(parents[x], parents)


for _ in range(int(input())):
    parents = dict()
    cnt = {}
    for _ in range(int(input())):
        f1, f2 = input().split()
        if f1 not in parents:
            parents[f1] = f1
            cnt[f1] = 1
        if f2 not in parents:
            parents[f2] = f2
            cnt[f2] = 1
        union(parents, f1, f2, cnt)
        print(cnt[find(f1, parents)])
