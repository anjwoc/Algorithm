import sys
input = sys.stdin.readline

# n, m = map(int, input().split())

def permutation(arr, r):
  arr = sorted(arr) # 정렬
  used = [False for _ in range(len(arr))] # 방문했는지 표시

  def generate(chosen, used):
    if len(chosen) == r: 
      # 고른 개수가 r과 같으면
      print(chosen)
      return
    for i in range(len(arr)):
      if not used[i]: # 방문 안했으면
        # arr[i]값을 추가하고 방문표시 하고 generate 함수 호출
        chosen.append(arr[i]) 
        used[i] = True
        generate(chosen, used)
        # 다시 다음 i값에서 재사용 해야하니까 False로 변경하고
        # chosen도 비워줘야하니 pop
        used[i] = False
        chosen.pop()
  generate([], used)

'''
1, 2, 3 들어오고 출력 리턴
방문 
'''


def combination(arr, r):
  arr = sorted(arr)

  def generate(chosen):
    if len(chosen) == r:
      print(chosen)
      return
    
    start = arr.index(chosen[-1]) + 1 if chosen else 0
    for nxt in range(start, len(arr)):
      chosen.append(arr[nxt])
      generate(chosen)
      chosen.pop()
  generate([])


permutation([1, 2, 3, 4], 2)