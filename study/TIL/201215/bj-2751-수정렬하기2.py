import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
for i in arr:
  print(i)
