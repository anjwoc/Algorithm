import sys
import math
input = lambda: sys.stdin.readline().strip()

def distance(cod1, cod2):
  x1 ,y1 = cod1
  x2, y2 = cod2
  a = x2 - x1
  b = y2 - y1
  
  return math.sqrt((a*a) + (b*b))

n = int(input())
cod = []
ans = 0
for _ in range(n):
  x, y = map(int, input().split())
  cod.append((x, y))

tmp = sorted(cod, key=lambda x : x[1])
print(tmp)

print(int(distance(cod[0], cod[1])**2))