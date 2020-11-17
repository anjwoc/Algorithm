import sys
from copy import deepcopy
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)

# 4방향을 총 5번 움직일 수 있다면 총 4^5인 1024가 나온다.

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]


def rotate90(n, B):
    # 외워야 함
    NB = deepcopy(B)
    for i in range(n):
        for j in range(n):
            NB[j][n-i-1] = B[i][j]
    return NB


def convert(lst, n):
    # 0이 아닌 숫자만 필터링
    new_list = [i for i in lst if i]

    for i in range(1, len(new_list)):
        # 1부터 순회해서 전값과 내값이 같으면
        if new_list[i-1] == new_list[i]:
            # 지금 값은 0으로 만들고 내 값은 2배를한다.
            # 2 2 2 2 => 4 0 4 0
            new_list[i-1] *= 2
            new_list[i] = 0
    # 이후에 다시 0을 제외한 리스트를 뽑고
    new_list = [i for i in new_list if i]
    # 리스트의 나머지 요소는 0으로 채운다.
    return new_list + [0] * (n-len(new_list))


def dfs(n, B, cnt):
    ans = max([max(i) for i in B])
    if cnt == 0:
        return ans
    for _ in range(4):
        X = [convert(i, n) for i in B]
        if X != B:
            ans = max(ans, dfs(n, X, cnt-1))
        B = rotate90(n, B)
    return ans


print(dfs(n, maps, 5))
