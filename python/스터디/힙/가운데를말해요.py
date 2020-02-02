import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = []

for _ in range(n):
  x = int(input())
  arr.append(x)
  if len(arr) >= 2:
    arr.sort()
  else:
    # 1개일 때
    print(x)
    continue
  div = len(arr)//2
  if not (len(arr) % 2):
    # 짝수
    cmp_list = [arr[div-1], arr[div]]
    print(min(cmp_list))
  else:
    print(arr[div])

    
  

