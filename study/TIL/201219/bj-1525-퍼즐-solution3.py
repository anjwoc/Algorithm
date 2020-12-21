from collections import deque
import sys
input = sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
  que=deque([maps])
  visited = { maps: 0 }
  
  while que:
    v = que.popleft()
    step = visited.get(v)
    if v == '123456780':
      return visited[v]
    
    k = v.find('0')
    # x, y = divmod(k, 3) => divmod함수는 큰 숫자일때 효과적이다.
    x, y = k // 3, k % 3 # 3X3표일 때 x,y 좌표
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < 3 and 0 <= ny < 3:
        nk = nx*3 + ny # 3x3 표에서 x,y 좌표를 리스트로 바꿨을때의 위치
        lst = list(v)
        lst[k], lst[nk] = lst[nk], lst[k]
        S = ''.join(lst)
        
        if not visited.get(S): 
          visited[S] = step+1
          que.append(S)
          
  return -1

maps=''

for _ in range(3):
  maps+=''.join(input().split())

print(bfs())