import sys
from itertools import permutations
input = sys.stdin.readline

'''
+, -, *, %
계산식의 진행은 연산자 우선순위를 무시하고 앞에서부터 진행
나눗셈은 몫만 취한다.
음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫만 취하고, 음수로 바꿔야 함
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가
최대인 것과 최소인 것을 구해라.
'''

def calc(number, operator):
  ans = number[0]

  for i in range(n-1):
    if operator[i] == '+':
      ans += number[i+1]
    elif operator[i] == '-':
      ans -= number[i+1]
    elif operator[i] == '*':
      ans *= number[i+1]
    elif operator[i] == '//':
      # if ans < 0:
      #   ans = -(ans)
      #   ans //= number[i+1]
      #   ans = -(ans)
      # else:
      #   ans //= number[i+1]
  return ans

n = int(input())
arr = list(map(int, input().split()))
ops = ["+", "-", "*", "//"]
op_number = list(map(int, input().split()))
operator = []

for i in range(4):
  if op_number[i] == 0:
    continue
  operator.extend([ops[i]] * op_number[i]) 
operator = set(permutations(operator, n-1))

min_value = sys.maxsize
max_value = -sys.maxsize-1

for op in operator:
  result = calc(arr, op)
  min_value = min(min_value, result)
  max_value = max(max_value, result)

print(max_value)
print(min_value)
  