import sys
input = sys.stdin.readline


def binary_search(start, end, target):
    if start > end:
        return 0
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


n = int(input())
arr = sorted(map(int, input().split()))

m = int(input())
cmp = list(map(int, input().split()))

for target in cmp:
    start = 0
    end = n-1
    print(binary_search(start, end, target))
