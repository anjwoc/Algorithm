import sys

input = lambda: sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n, idx = map(int, input().split())
    priority = [int(input()) for _ in range(n)]
