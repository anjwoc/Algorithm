import sys
input = sys.stdin.readline

'''
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
'''

for __ in range(int(input())):
    k = int(input())
    page = list(map(int, input().split()))

    dp = [[0]*k for _ in range(k)]
    for i in range(k-1):
        dp[i][i+1] = page[i] + page[i+1]  # 누적합
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + page[j]
    for i in dp:
        print(i)

    for d in range(2, k):  # diagonal
        for i in range(k-d):
            j = i+d
            print('k: %d, d: %d, i: %d, j: %d' % (k, d, i, j))
            print([dp[i][k] + dp[k+1][j] for k in range(i, j)])
            print('%d~%d + %d~%d' % (i, k, k+1, j))
            minimum = min([dp[i][k] + dp[k+1][j] for k in range(i, j)])
            dp[i][j] += minimum
            print('dp(%d, %d): %d' % (i, j, dp[i][j]))
            # print(dp[i])

    print(dp[0][k-1])
