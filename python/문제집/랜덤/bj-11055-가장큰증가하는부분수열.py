import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
D = deepcopy(arr)
# D[i] = i까지 왔을 때, 합의 최대


for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            # D에 arr 원본 배열을 그대로 카피 했기 때문에
            # 이 문제는 해당 값 그 자체가 답이 될 수도있어서
            # i가 1~N까지 인덱스의 값을 잡고
            # j가 i번째 까지 순회하면서 현재 i가 위치한 값보다 큰 경우에만
            # 비교를 해서 D[i]의 값을 갱신한다.
            D[i] = max(arr[i] + D[j], D[i])

print(max(D))
