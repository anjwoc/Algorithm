import sys
from copy import deepcopy
input = sys.stdin.readline

n, arr = int(input()), list(map(int, input().split()))
D = deepcopy(arr)
path = [i for i in range(n)]  # 경로 추적을 위한 배열
idx = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and D[i] < arr[i] + D[j]:
            D[i] = arr[i] + D[j]
            # 값을 갱신할 때의 어디서부터 온 인덱스인지를 가리키는 j 인덱스를 넣는다.
            path[i] = j

    if D[idx] < D[i]:
        # 최대값 인덱스를 저장하기 위해 사용
        idx = i

print(D[idx])  # 최대값 출력

while path[idx] != idx:
    print(arr[idx], sep=" ")
    # idx를 path[idx](이전 인덱스)로 갱신해준다.
    # 1 2 50 60 이면 idx가 4이고 path[idx]는 3이다.
    # arr[4] = 60 arr[3] = 50 path[idx]는 바로 이전의 값에 대한 인덱스
    idx = path[idx]

print(arr[idx])
