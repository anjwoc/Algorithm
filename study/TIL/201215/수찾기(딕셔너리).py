import sys
input = sys.stdin.readline

n = int(input())
A = {}
for i in map(int, input().split()):
  A[i] = 1

m = int(input())
for i in map(int, input().split()):
  try:
    print(A[i])
  except:
    print(0)

