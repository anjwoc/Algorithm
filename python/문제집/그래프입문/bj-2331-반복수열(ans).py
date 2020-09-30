import sys
input = sys.stdin.readline

a, p = map(int, input().split())
arr = [a]
link = [0] * 250000
link[a] = 1

while True:
  data = arr[-1]

  value = 0
  while data:
    value += (data % 10)**p
    data //= 10
  
  if not link[value]:
    arr.append(value)
    link[value] = 1
  else:
    print(len(arr[:arr.index(value)]))
    break
  

