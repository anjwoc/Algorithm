import sys
input = sys.stdin.readline

# in operator를 사용하더라도 최악의 경우 O(n^2)
# N의 범위는 100,000 까지여서 100억번이 나오니 N^2은 불가능
# 시간 제한이 2초이니 러프하게 잡아도 1억번 안에 해결해야 함

n = int(input())
arr = dict()
for i in map(int, input().split()):
    arr[i] = True

int(input())

for data in map(int, input().split()):
    try:
        print(arr[data] and 1)
    except:
        print(0)
