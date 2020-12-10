import sys
input = sys.stdin.readline

n = int(input())

# 1~n까지 반복
for i in range(1, n+1):
  # 첫 공백은 n부터 0까지의 순서의 개수로 찍힌다.
  print(' '*(n-i), end='')
  # *은 1 3 5 7 ... 로 홀수로 늘어나면서 찍힌다.
  print('*'*(2*i-1))
