import sys
from math import inf
input = sys.stdin.readline

n, m = int(input()), int(input())

# 이동 최소비용을 저장할 2차원 배열
cost = [[inf for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)


for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for row in cost:
    for i in range(n):
        if row[i] == inf:
            row[i] = 0
        print(row[i], end=' ')
    print()
