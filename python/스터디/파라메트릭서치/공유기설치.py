import sys
input = lambda: sys.stdin.readline().strip()

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

def maxLen(mid):
  max1, max2 = 0, 0
  for i in range(mid):
    tmp = abs(arr[mid] - arr[i])
    max1 = max(tmp, max1)
  for i in range(mid, len(arr)):
    tmp = abs(arr[mid] - arr[i])
    max2 = max(tmp, max2)
  if max1 >= max2:
    # 왼쪽 탐색해야하는 경우
    return 1
  else:
    # 오른쪽
    return -1

def BSearch(c):
  start, end = 0, max(arr)
  cArr = [arr[0], arr[-1]]
  ans = 0
  while(start <= end):  
    mid = (start + end) // 2
    if len(cArr) != c:
      cArr.append(mid)
    cArr.append(mid)
    direction = maxLen(mid)
    if direction == 1:
      end = mid - 1
    else:
      start = mid + 1
  return cArr

if c == 2:
  print(abs(arr[0] - arr[-1]))
else:
  tmp = BSearch(c)