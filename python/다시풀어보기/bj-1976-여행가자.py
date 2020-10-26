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


n = int(input())
m = int(input())
arr = []
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if j+1 > i+1 and arr[i][j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))
    
check = True
u = find(plan[0])
for i in range(1, len(plan)):
    if u != find(plan[i]):
        check = False
        break

ans = check is True and "YES" or "NO"

print(ans)
