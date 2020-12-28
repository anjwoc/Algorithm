import sys
input = sys.stdin.readline

'''
1. NxM의 맵을 만든다.
2. 해당 보드의 숫자를 매핑한다.
3. 명령을 입력 받는다.
4. 명령을 순서대로 순회하며 동작을 수행한다.
  - 주사위가 바깥으로 이동하면 안된다(바깥으로 이동할 시 해당 명령 무시, 출력X)
  - 주사위가 이동했을 때마다 상단에 적혀있는 값 출력
  - 이동한 칸이 0 이면 주사위의 바닥칸 수가 복사되고
  - 0이 아니면 바닥칸 수가 주사위의 바닥에 복사된다.

1: 동쪽(0, 1)
2: 서쪽(0 ,-1)
3: 북쪽(-1, 0)
4: 남쪽(1, 0)
'''
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

swap_map = {
  0: [(0, 2, 3, 5), (3, 0, 5, 2)],
  1: [(0, 2, 3, 5), (2, 5, 0, 3)],
  2: [(0, 1, 4, 5), (4, 0, 5, 1)],
  3: [(0, 1, 4, 5), (1, 5, 0, 4)]
}

def swap(origin, target):
  global dice
  x1, x2, x3, x4 = origin
  y1, y2, y3, y4 = target
  dice[x1], dice[x2], dice[x3], dice[x4] = dice[y1], dice[y2], dice[y3], dice[y4]
  

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0 for _ in range(6)]

for i in range(k):
  d = order[i] - 1
  nx, ny = x+dx[d], y+dy[d]
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    continue
  swap(*swap_map[d])

  if maps[nx][ny] == 0:
    maps[nx][ny] = dice[5]
  else:
    dice[5] = maps[nx][ny]
    maps[nx][ny] = 0
  x, y = nx, ny
  print(dice[0])
