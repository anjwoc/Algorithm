import sys
from collections import Counter
input = sys.stdin.readline

def make_land(height):
  sec = 0
  for key in land:
    if key < height:
      sec += (height - key) * land[key]
    elif key > height:
      sec += (key - height) * 2 * land[key]
  return sec

n, m, B = map(int, input().split())

land = []
for _ in range(n):
  land += map(int, input().split())

_sum, length = sum(land), n*m
land = dict(Counter(land))
height, min_sec = 0, 100000000000000

for h in range(257):
  if length * h <= _sum + B:
    sec = make_land(h)
    if sec <= min_sec:
      min_sec = sec
      height = h

print(min_sec, height)
