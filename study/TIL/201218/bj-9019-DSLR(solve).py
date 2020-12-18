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


def bfs(start, target):
  que = deque([(start, '')])
  visited[start] = 1

  while que:
    now, cmd = que.popleft()
    if now == target:
      return cmd
    
    length = len(str(now))

    # D Command
    t = (now*2)%10000
    if not visited[t]:
      visited[t] = 1
      que.append((t, cmd + 'D'))

    # S Command
    t = (now-1)%10000
    if not visited[t]:
      visited[t] = 1
      que.append((t, cmd + 'S'))
    
    # L Command
    if length != 4:
      t = now*10
    else:
      t, d = divmod(now, 10**(length-1))
      t += (d*10)
    if not visited[t]:
      visited[t] = 1
      que.append((t, cmd+'L'))

    # R Command
    if length == 1:
      t = now * 1000
    else:
      t, d = divmod(now, 10)
      t += (d*1000)
    if not visited[t]:
      visited[t] = 1
      que.append((t, cmd + 'R'))

for _ in range(int(input())):
  start, target = map(int, input().split())
  visited = [0] * 10001
  print(bfs(start, target))
  
