import sys
from collections import deque
input = sys.stdin.readline

def command(num, cmd):
  if cmd == 'D':
    num = num * 2
    if num > 9999:
      return (2*num)%10000
    return num
  elif cmd == 'S':
    return num-1
  elif cmd == 'L':
    num = str(num)
    return int(num[1:] + num[0])
  elif cmd == 'R':
    num = str(num)
    return int(num[-1] + num[:-1])

def bfs(start, target):
  global ans
  visited[start] = 1
  que = deque([(start, '')])
  
  while que:
    now, cmd = que.popleft()
    if now == target:
      ans.append(cmd)
      
    for order in ['D', 'S', 'L', 'R']:
      number = command(now, order)
      if number < 0 or number > 9999:
        continue
      if visited[number]:
        continue
      visited[number] = 1
      # cmd = order + cmd
      que.append((number, order + cmd))


# for _ in range(int(input())):
#   start, target = map(int, input().split())
#   visited = [0] * 10001
#   ans = []
#   bfs(start, target)
#   print(min(ans, key=lambda x: len(x)))
