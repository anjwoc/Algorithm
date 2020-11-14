import sys
input = sys.stdin.readline

S = list(input().rstrip())
c1 = 0
c2 = 0

# 1번풀이
if S[0] == '1':
    c1 += 1
else:
    c2 += 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            c1 += 1
        else:
            c2 += 1

print(min(c1, c2))


# 2번 풀이
ans = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        ans += 1

# (바뀌는 구간의 개수+1) // 2
print((ans+1) // 2)
