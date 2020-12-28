import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
maps = [[0]*N for _ in range(N)]
snake = deque([[0,0]])
K = int(input())
for _ in range(K):
  x, y = map(int, input().split())
  maps[x-1][y-1] = 1 # 사과위치
  
L = int(input())
Order = [list(map(str , input().split())) for _ in range(L)]


D = [[0,1], [1,0], [0,-1], [-1,0]] # 오른쪽, 아래, 왼쪽, 위


alive = True
time = 0
direction = 0
order_number = 0

while alive:
  time += 1
  # 마지막으로 추가 된 요소가 뱀의 머리
  head = snake[-1] 
  dx = D[direction][0] + head[0]
  dy = D[direction][1] + head[1]
  
  if dx<0 or dy<0 or dx>=N or dy>=N:
    # 맵의 범위에서 벗어난 경우 break
    break
  if [dx, dy] in snake:
    # 이미 지나온 길이라면 break
    break
  
  if maps[dx][dy] == 1:
    # 사과가 있을 경우 0으로 바꿔준다.
    maps[dx][dy] = 0
  else:
    # 그렇지 않은 경우 뱀의 꼬리를 없애준다.
    snake.popleft()
  # 새로 이동한 칸을 머리로 추가
  snake.append([dx, dy])       
     
  if order_number < L and str(time) == Order[order_number][0]:
# 오더 넘버가 L보다 작으면서 시간이 현재 수행해야 할 오더의 시간과 일치하는 경우
    if Order[order_number][1] == 'D':
      # D 인 경우에 오른쪽으로 90도 회전이므로 인덱스 + 1
      direction = (direction+1)%4
    else:
      # D 인 경우에 오른쪽으로 90도 회전이므로 인덱스 - 1
      direction = (direction-1)%4
    order_number += 1
  
print(time)