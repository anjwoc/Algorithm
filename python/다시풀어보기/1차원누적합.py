import sys
input = sys.stdin.readline

# 1차원 누적합
arr = list(range(10))
ans = [0]*10
for i in range(1, 10):
    ans[i] = ans[i-1] + arr[i]

print(ans)
