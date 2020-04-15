import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 50


def fibo(n):
    global dp
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]


print(fibo(n))
