import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
maps= []
ans = 0
visited = [False] * 14
for _ in range(n):
  maps.append(list(map(int, input().split())))

# maps에서 치킨집(2)인 인덱스들의 배열을 구함
chickenList = [(nx+1, ny+1) for nx, row in enumerate(maps) for ny, val in enumerate(row) if val == 2]
# maps에서 집(1)인 인덱스들의 배열을 구함
homeList = [(nx+1, ny+1) for nx, row in enumerate(maps) for ny, val in enumerate(row) if val == 1]
like_chickenList = []
distance_dict = {}
print(visited)
print(homeList)

def getDistance(a, b):
  r1, c1 = a
  r2, c2 = b
  return abs(r2 - r1) + abs(c2 - c1)
