import sys
input = sys.stdin.readline

n, arr = int(input()), {i: 1 for i in map(int, input().split())}
m = int(input())
for i in map(int, input().split()):
    print(arr.get(i, 0))
