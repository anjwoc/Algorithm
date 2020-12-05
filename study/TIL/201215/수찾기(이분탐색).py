import sys
input = sys.stdin.readline

def binary_search(start, end, target):
  while start <= end:
    mid = (start+end) // 2
    if target == A[mid]:
      return 1
    else:
      if A[mid] > target:
        end = mid - 1
      else:
        start = mid + 1
  return 0
  

n = int(input())
A = sorted(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

for i in B:
  print(binary_search(0, n-1, i))