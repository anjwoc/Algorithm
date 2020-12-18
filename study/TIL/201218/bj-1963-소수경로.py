import sys
from collections import deque
input = sys.stdin.readline

def primes(n):
  # O(nlog(logn))
  P = [1] * n
  m = int(n ** 0.5)

  for i in range(2, m+1):
    t = 2
    while i*t < n:
      # i값의 t의 배수가 n보다 작을 때까지 모두 소수가 아니므로 0으로 바꾼다.
      P[i*t] = 0
      t += 1
  return P

prime = primes(10001)

'''
3
1033 8179
1373 8017
1033 1033
'''

def bfs():
  que = deque([(start, 0)])
  visited = [False] * (10001)

  while que:
    now, step = que.popleft()
    if now == target:
      return step
    
    cur = str(now)
    step += 1

    for i in range(4):
      # 총 4자리므로 4번 반복
      for j in map(str, range(10)):
        # 1~9까지의 숫자를 반복하며 넣어본다.
        # 넣어서 소수이고 방문하지 않았으면 방문표시를 하고 큐에 넣는다.
        if i == 0 and j == '0':
          # 첫 자리는 0이면 안된다.
          continue
        num = int(cur[:i] + j + cur[i+1:])
        
        if prime[num] and not visited[num]:
          visited[num] = True
          que.append((num, step))
  

for _ in range(int(input())):
  start, target = map(int, input().split())
  print(bfs())