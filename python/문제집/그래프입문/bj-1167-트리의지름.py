import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    data = data[:data.index(-1)]
    start = data[0]
    for i in data[1:]:
        if start not in tree:
            tree[start] = [(i, )]
