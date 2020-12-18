import sys
from collections import deque
input = sys.stdin.readline

'''
이 문제의 핵심은 L과 R연산에 있다.
1이란 숫자를 L과 R 연산을 했을 때 1이 나오면 안된다.
10과 1000이 된다.
1을 0001로 보고 진행해야 한다.

다음으로 L과 R연산을 수행하는데 string으로 변환하면 틀리도록 설계되어 있다.

시간 제한도 걸리지만 메모리 제한도 걸린다..
command 함수를 따로 생성해서 채점하면 메모리 초과가 발생해서 함수 없이
설계 하면 통과된다.

'''

def command(length, num, cmd):
  if cmd == 'D':
    return (2*num) % 10000
  elif cmd == 'S':
    return (num - 1) % 10000
  elif cmd == 'L':
    if length != 4:
      num *= 10
    else:
      num, d = divmod(num, 10**(length-1))
      num += (d*10)
    return num
  elif cmd == 'R':
    if length == 1:
      num = num * 1000
    else:
      num, d = divmod(num, 10)
      num += (d*1000)
    return num


def bfs(start, target):
  que = deque([(start, '')])
  visited[start] = 1

  while que:
    now, cmd = que.popleft()
    if now == target:
      return cmd
    
    length = len(str(now))

    for order in ['D', 'S', 'L', 'R']:
      result = command(length, now, order)
      if result < 0 or result > 10000:
        continue
      if not visited[result]:
        que.append((result, cmd+order))


for _ in range(int(input())):
  start, target = map(int, input().split())
  visited = [0] * 10001
  print(bfs(start, target))
  
