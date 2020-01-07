import sys
N, S = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

tmp = 0

def partial_sum(arr, a, b):
    arr = [0] + arr
    partial_sum = [0] * len(arr)

    for i in range(1, len(arr)):
        partial_sum[i] = partial_sum[i-1] + arr[i]

    partial_sum = partial_sum[1:]
    print("partial_sum : ", partial_sum)
    print("total_sum: ", partial_sum[-1])

    return partial_sum[b] - partial_sum[a-1]


scores = [100, 95, 80, 100, 70, 65]
partial_sum(scores, 3, 5) # 235