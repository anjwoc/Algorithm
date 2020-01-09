import sys
input = sys.stdin.readline

def prettyPrint(arr):
  for val in arr:
    print(val)

n = int(input())

check = [[True] * n for _ in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]
