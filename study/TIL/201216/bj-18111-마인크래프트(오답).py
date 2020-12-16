import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
maps = [[0]*(M+1) for _ in range(N+1)]

min_height = 257
max_height = -1
dic = {}

for i in range(1, N+1):
  row = [0] + list(map(int, input().split()))
  for j in range(1, len(row)):
    maps[i][j] = row[j]

    min_height = min(row[j], min_height)
    max_height = max(row[j], max_height)

    if maps[i][j] not in dic:
      dic[maps[i][j]] = 1
    else:
      dic[maps[i][j]] += 1

if dic[min_height] > dic[max_height]:
  min_land = dic[max_height]
  if B >= min_land:
    target = max_height
    pass_item = min_height
  else:
    target = min_height
    pass_item = max_height
else:
  min_land = dic[min_height]
  if B >= min_land:
    target = min_height
    pass_item = max_height
  else:
    target = max_height
    pass_item = min_height
  

time = 0
height = 0

if min_land <= B:
  # 인벤토리의 개수가 더 많아서 블록을 쌓을 수 있다.
  while dic[target]:
    for i in range(1, N+1):
      for j in range(1, M+1):
        if maps[i][j] == pass_item:
          continue
        if maps[i][j] == target and pass_item < target:
          dic[maps[i][j]] -= 1
          maps[i][j] -= 1
          time += 2
          B += 1
        else:
          dic[maps[i][j]] -= 1
          maps[i][j] += 1
          time += 1
          B += 1
        height = max(height, maps[i][j])
else:
  # 인벤토리의 개수가 부족한 경우
  while dic[target]:
    for i in range(1, N+1):
      for j in range(1, M+1):
        if maps[i][j] == pass_item:
          continue
        dic[maps[i][j]] -= 1
        maps[i][j] -= 1
        height = max(height, maps[i][j])
        time += 2

print(time, height)