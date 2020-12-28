import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
for i in arr:
  # 총감독관이 감시 가능한 수를 뺀다.
  i -= b
  # 감독관 수 1 추가
  ans += 1

  # 아직 i의 값이 0보다 크다면 감시할 인원이 남은 경우
  if i > 0:
    # 부감독관이 가능한 경우를 나눈 몫을 추가하고
    ans += i//c
    # 나머지가 0이 아닌경우는 감시해야 할 인원이 남으므로 1추가한다.
    if not i % c == 0:
      ans += 1
  
print(ans)