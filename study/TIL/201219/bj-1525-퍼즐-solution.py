import sys
from collections import deque
input = sys.stdin.readline

def solve():
  que = deque([maps])
  visited = {maps:0}
  
  while que:
    table = que.popleft()
    step = visited.get(table)
    zero = table.index('0')
 
    if table == '123456780':
      return step
    
    i = zero//3 # row 
    # zero index - (3 * (zero index // 3))
    # zero index를 3으로 나눈 몫을 3곱한 값을 i에서 뺀다.
    # 0 1 2의 숫자가 반복된다.
    j = zero - 3*(zero//3)

    step += 1
    lst = list(table)
    if i > 0: # move UP
      lst[zero], lst[zero-3] = lst[zero-3], lst[zero]
      S = ''.join(lst)
      if not visited.get(S):
        visited[S] = step
        que.append(S)
      lst[zero], lst[zero-3] = lst[zero-3], lst[zero]
 
    if i < 2: # move DOWN
      # 2 이상이면 +3을 했을 때 범위에서 벗어난다.
      # i=1까지가 012345
      lst[zero], lst[zero+3] = lst[zero+3], lst[zero]
      S = ''.join(lst)
      if not visited.get(S):
        visited[S] = step
        que.append(S)
      lst[zero], lst[zero+3] = lst[zero+3], lst[zero]
    
    if j > 0: # move LEFT
      # 0인 경우 가장 왼쪽에 위치해서 이동 불가
      lst[zero], lst[zero-1] = lst[zero-1], lst[zero]
      S = ''.join(lst)
      if not visited.get(S):
        visited[S] = step
        que.append(S)
      lst[zero], lst[zero-1] = lst[zero-1], lst[zero]
      
    if j < 2: # move RIGHT
      # 2이상 인 경우 오른쪽으로 이동 불가
      lst[zero], lst[zero+1] = lst[zero+1], lst[zero]
      S = ''.join(lst)
      if not visited.get(S):
        visited[S] = step
        que.append(S)
      lst[zero], lst[zero+1] = lst[zero+1], lst[zero]
 
  return -1

maps = ""
for _ in range(3):
  maps += ''.join(input().split())


print(solve())