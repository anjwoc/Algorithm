import sys
input = sys.stdin.readline

'''
조합은 순서에 영향이 없고
대표만 뽑는 경우의 수
1,2가 나왔으면 2,1은 안됨
'''
def combination(arr, r):
  arr = sorted(arr)
  visited = [False for _ in range(len(arr))]
  def generate(chosen):
    if len(chosen) == r:
      print(*chosen)
      return
    
    #만약 start가 chosen이 비어있으면 0을 넣는다.
    #그런 경우가 아니면 chosen의 마지막 값에 1을 더한 값으로 시작
    start = arr.index(chosen[-1]) + 1 if chosen else 0
    
    for nxt in range(start, len(arr)):
      if not visited[nxt] and (nxt==0 or arr[nxt-1] != arr[nxt] or visited[nxt-1]):
        chosen.append(arr[nxt])
        generate(chosen)
        chosen.pop()

generate([])


n, m = map(int, input().split())
tmp = [i for i in range(1, n+1)]  

permutaion(tmp)
