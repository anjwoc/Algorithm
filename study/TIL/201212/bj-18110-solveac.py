import sys
input = sys.stdin.readline

def round2(x):
  # python의 내장 round함수는 5사5입법이 적용된 반올림이여서 4사5입 방식을 구현해야 통과가 가능하다.
  # 5사5입의 경우 0.5, 1.5의 경우 0, 1의 결과가 나온다.
  return int(x) + (1 if x - int(x) >= 0.5 else 0)

n = int(input())
if n==0:
  print(0)
  exit(0)
arr = sorted([int(input()) for _ in range(n)])
cut = round2(n * 0.15)
arr = arr[cut: n-cut]
print(round2(sum(arr)/len(arr)))