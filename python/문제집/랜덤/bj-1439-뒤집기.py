import sys
input = sys.stdin.readline

s = list(input().strip())
ans = 0
for i in range(1, len(s)):
    # 바뀌는 구간 탐색
    if s[i] != s[i-1]:
        ans += 1

# (바뀌는 구간의 개수 + 1) // 2
print((ans + 1) // 2)
