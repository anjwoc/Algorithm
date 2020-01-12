import sys
input = sys.stdin.readline

def permutaion(arr, r):
  arr = sorted(arr)
  visited = [False for _ in range(len(arr))]

  def generate(chosen, visited):
    if len(chosen) == r:
      print(*chosen)
      return
    for i in range(len(arr)):
      if not visited[i] and (i==0 or arr[i-1] != arr[i] or visited[i-1]):
        chosen.append(arr[i])
        visited[i] = True
        generate(chosen, visited)
        visited[i] = False
        chosen.pop()
        
  generate([], visited)

n, m = map(int, input().split())
tmp = [i for i in range(1, n+1)]  

permutaion(tmp, m)
