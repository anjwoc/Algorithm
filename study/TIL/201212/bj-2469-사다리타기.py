import sys, string
input = sys.stdin.readline

alphabets = string.ascii_uppercase
k = int(input())
n = int(input())
alpha = list(alphabets[:k]) # A부터 순서대로 K개의 알파벳을 만든다.
ans = list(input().rstrip()) # 최종 순서
maps = [list(input().rstrip()) for _ in range(n)] # 사다리 맵

# ?가 있는 행의 인덱스
# qIdx = [i for i in range(n) if '?' in maps[i]][0] 
qIdx = [i for i in range(n) if maps[i][0] == '?'][0]

# ? 이전 사다리들을 탐색하며 '-'인 경우 사다리를 바꿔준다.
for i in range(qIdx):
  for j in range(k-1):
    if maps[i][j] == '-':
      alpha[j], alpha[j+1] = alpha[j+1], alpha[j]

# ? 이후 사다리들을 탐색하며 '-'인 경우 사다리를 바꿔준다.
# 순서는 가장 밑의 사다리부터 역순으로 탐색한다.
for i in range(n-1, qIdx, -1):
  for j in range(k-1):
    if maps[i][j] == '-':
      ans[j], ans[j+1] = ans[j+1], ans[j]

ret = ''
for i in range(k-1):
  if alpha[i] == ans[i]:
    ret += "*"
  elif alpha[i] == ans[i+1] and alpha[i+1] == ans[i] and(i==0 or ret[-1] == "*"):
    # ret의 마지막 문자가 * 이거나 첫 루프일 때만 실행하는 이유는 사다리가 연속해서 나올 수 없도록 하는 조건
    ret += "-"
    alpha[i], alpha[i+1] = alpha[i+1], alpha[i]
  else:
    ret = "x" * (k-1)
    break

print(ret)