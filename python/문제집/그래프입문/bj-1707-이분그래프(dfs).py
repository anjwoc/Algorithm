import sys
sys.setrecursionlimit(100000)
input= lambda : sys.stdin.readline().strip()

tc = int(input())

def dfs(v,group):
  color[v] = group
  for i in adj[v]:
    # 여기서 False를 리턴하면 같은 그룹
    if color[i] == 0:
      # -group값을 넘겨줘서 color[v]에 할당되더라도 서로 다른 그룹임을 알수있다.
      if dfs(i, -group) is False:
        # 재귀적으로 호출해서 마지막까지 도달하고 False가 리턴된거면
        # 같은 컬러를 가진 그룹이 있어서 False가 리턴된 상황
        return False
    elif color[i] == color[v]:
      # 컬러가 이미 칠해저있다면 비교
      return False
  return True

while tc:
  tc -= 1
  v,e=map(int,input().split())
  adj=[[] for i in range(v+1)]
  color=[0]*(v+1)

  for i in range(e):
    # 인접리스트 초기화
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

  ans=True
  for i in range(1, v + 1):
    # 각 정점을 방문하며
    if color[i] == 0:
      # 현재 정점의 체크 값이 0이라면 dfs 순회
      if dfs(i, 1) is False:
        # 결과가 False가 나온다면 이분 그래프가 아님
        ans = False
        break

  print('YES' if ans else 'NO')