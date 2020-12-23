import sys
input = sys.stdin.readline


n = int(input())
arr = sorted(map(int, input().split()))

idx = sys.maxsize
sums = sys.maxsize

for i in range(n):
  tmp = 0
  for j in range(n):
    tmp += abs(arr[i] - arr[j])
  
  if sums > tmp:
    idx = i+1
    sums = tmp

print(arr[idx-1])