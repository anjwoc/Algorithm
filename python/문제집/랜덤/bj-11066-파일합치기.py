import sys
input = sys.stdin.readline

'''
이 문제는 dp를 정의하는 부분이 어려움
유형 중 하나이기 때문에 풀어보지 않고 바로 떠올리기가 사실상 어려움
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
'''


def process():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    # dp[i][j]: i에서 j까지 합하는데 필요한 최소 비용
    # dp[i][k] + dp[k+1][j] + sum(arr[i] ~ arr[j])

    # sums[i]는 1번부터 i번까지의 누적합
    sums = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        sums[i] = sums[i-1] + arr[i]
    
    dp = [[0 for i in range(n+1)] for _ in range(n+1)]

    for i in range(2, n+1):
        # 첫 번째 반복문은 파일의 길이만큼 반복한다.
        # 부분 파일의 길이
        for j in range(1, n+2-i):
            # 시작점
            # j에서 시작해서 j+i-1은 j부터 i만큼의 길이인 애들 -1은 인덱스가 0부터 시작해서
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (sums[j+i-1] - sums[j-1])

    # for i in dp:
    #     print(i)
    print(dp[1][n])


for _ in range(int(input())):
    process()
