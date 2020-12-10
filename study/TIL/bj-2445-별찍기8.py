import sys
input = sys.stdin.readline

n = int(input())

# 위 아래로 두 부분으로 나눠서 별을 찍는다.
# 가운데 중앙선을 기준으로 윗 부분
for i in range(1, n+1):
  # 첫 별을 찍는 삼각형으로 1~n개 순으로 늘어난다.
  print('*'*i, end='')
  # 가운데 공백으로 이뤄진 삼각형으로 홀수가 역순으로 찍히게 된다.
  # ...9, 7, 5, 3, 1
  print(' '*(2*(n-i)), end='')
  # 첫 삼각형과 동일
  print('*'*i)

# 아래 부분도 위의 방식과 동일.
for i in range(1, n+1):
  print('*'*(n-i), end='')
  print(' '*(2*i), end='')
  print('*'*(n-i))