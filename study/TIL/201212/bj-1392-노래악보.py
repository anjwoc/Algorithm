import sys
input = sys.stdin.readline

n, q= map(int, input().split())
T = [int(input()) for _ in range(n)]
Q = [int(input()) for _ in range(q)]

ranges = [-1 for _ in range(n)]
for i in range(n):
  for j in range(i+1):
    ranges[i] += T[j]

for q in Q:
  for i in range(n):
    if i == 0 and q <= ranges[0]:
      print(1)
    elif i>0 and ranges[i-1] < q <= ranges[i]:
      print(i+1)
    
    
    




