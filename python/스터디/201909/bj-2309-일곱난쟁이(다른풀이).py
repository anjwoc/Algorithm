import sys
input = sys.stdin.readline

arr = sorted([int(input()) for _ in range(9)])
sums = sum(arr)

for i in range(9):
    for j in range(i+1, 9):
        if sums-arr[i]-arr[j] == 100:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    print(arr[k])
                    