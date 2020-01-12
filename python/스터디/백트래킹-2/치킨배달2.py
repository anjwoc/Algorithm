import sys
input = sys.stdin.readline

import itertools

N, M = map(int, input().split())
house = []
chicken = []
final_chicken_distance = 99999
for i in range(1, N+1):
    info = list(map(int, input().split()))
    for j, e in enumerate(info, 1):
        if e == 1:
            house.append([i, j])
        elif e == 2:
            chicken.append([i, j])
for left_chicken in itertools.combinations(chicken, M):
  print(left_chicken)
  c_d = 0
  for h_pos in house:
      chicken_distance = 99999
      for c_pos in left_chicken:
          distance = abs(h_pos[0] - c_pos[0]) + abs(h_pos[1] - c_pos[1])
          print(distance, chicken_distance, distance < chicken_distance) 
          if distance < chicken_distance:
              chicken_distance = distance
      c_d += chicken_distance
  if c_d < final_chicken_distance:
      final_chicken_distance = c_d
print(final_chicken_distance)