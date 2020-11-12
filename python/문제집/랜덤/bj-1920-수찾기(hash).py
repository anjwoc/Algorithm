import sys
input = sys.stdin.readline

n = int(input())
arr = dict()
for num in map(int, input().split()):
    arr[num] = True

m = int(input())
for num in map(int, input().split()):
    try:
        print(arr[num] and 1)
    except:
        print(0)
