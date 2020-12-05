import sys
input = sys.stdin.readline
n, m = map(int, input().split())

'''
가장 헤맨 부분은 반드시 문제에서 적어도 N개라고 했지 반드시 N개라고 하지 않았다.
N개를 사도록 로직을 작성해서 오답이 발생함
1) n이 6이상
 - 아래 두 값을 더한다.
 - 패키지만 사는경우, 최소 패키지 가격과 최소 낱개 가격을 같이 구매하는 경우 중 작은 값 * (n을 6으로 나눈 몫)
 - 낱개 최소 가격 * (n을 6으로 나눈 나머지), 패키지 최소 가격
2) 6 미만
 - 낱개 최소 가격 * (n을 6으로 나눈 나머지), 패키지 최소 가격
'''

brand = []
for _ in range(m):
  package, solo = map(int, input().split())
  brand.append((package, solo, solo*6))

min_one = min(brand, key=lambda x: x[1])[1]
min_package = min(brand, key=lambda x: x[0])[0]
min_six = min(brand, key=lambda x: x[2])[2]

if n>=6:
  print(min(min_package, min_six)*(n//6) + min(min_one*(n%6), min_package))
else:
  print(min(min_one*(n%6), min_package))
