import sys
input = sys.stdin.readline

'''
+, -, *, %
계산식의 진행은 연산자 우선순위를 무시하고 앞에서부터 진행
나눗셈은 몫만 취한다.
음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫만 취하고, 음수로 바꿔야 함
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가
최대인 것과 최소인 것을 구해라.
'''

def calc(num, idx, add, sub, mul, div):
  global n, minv, maxv
  if idx == n:
    maxv = max(maxv, num)
    minv = min(minv, num)
    return
  else:
    if add:
      calc(num + numbers[idx], idx+1, add-1, sub, mul, div)
    if sub:
      calc(num - numbers[idx], idx+1, add, sub-1, mul, div)
    if mul:
      calc(num * numbers[idx], idx+1, add, sub, mul-1, div)
    if div:
      calc(int(num / numbers[idx]), idx+1, add, sub, mul, div-1)
    


n = int(input())
numbers = list(map(int, input().split()))
op_number = list(map(int, input().split()))

maxv = -sys.maxsize-1
minv = sys.maxsize

calc(numbers[0], 1, *op_number)

print(maxv)
print(minv)