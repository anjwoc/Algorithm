import sys

input = sys.stdin.readline
n = int(input())
maps = []
for _ in range(n):
    maps.append(tuple(map(int, input().split())))

for i in sorted(maps, key=lambda x: (x[0], x[1])):
    print(*i)
