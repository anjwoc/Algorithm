import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 그래프 싸이클 여부 판단 문제

def dfs(x):
  global ans
  visited[x] = True
  # 사이클을 이루는 팀을 확인하기 위함
  cycle.append(x)
  number = A[x]

  '''
  예를 들어
  5->1
  1->2
  2->3
  3->4
  4->1
  위와 같은 상황이면 재귀를 타면서 visited에 5, 1, 2, 3, 4, 1 순으로 찍히게 된다.
  visited를 이용해서 다시 1이 왔을때 1의 인덱스를 찾고 1인덱스부터
  마지막까지 배열을 추출하면 사이클을 이룬 부분만 나온다.  
  '''

  if visited[number]:
    if number in cycle:
      # 사이클이 되는 구간부터만 팀을 이룬다.
      ans += len(cycle[cycle.index(number):])
    return
  else:
    dfs(number)

for _ in range(int(input())):
  n = int(input())
  A = [0] + list(map(int, input().split()))
  visited = [True] + [False] * n
  ans = 0

  for i in range(1, n + 1):
    if not visited[i]:
      cycle = []
      dfs(i)
  print(n - ans)