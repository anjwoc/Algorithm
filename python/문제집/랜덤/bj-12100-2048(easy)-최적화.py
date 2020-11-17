import sys
from copy import deepcopy
input = sys.stdin.readline

# 4방향을 총 5번 움직일 수 있다면 총 4^5인 1024가 나온다.

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]


def rotate90(N, B):
    X = deepcopy(B)
    for i in range(N):
        for j in range(N):
            X[N-j-1][i] = B[i][j]
    return X


def convert(l):
    ll = [i for i in l if i]
    for i in range(len(ll)-1):
        if ll[i] == ll[i-1]:
            ll[i], ll[i+1] = ll[i]*2, 0
    ll = [i for i in ll if i]
    return ll + [0] * (len(l)-len(ll))


def dfs(N, B, cnt):
    ans = max([max(i) for i in B])
    if cnt == 0:
        return ans
    for _ in range(4):
        X = [convert(i) for i in B]
        if X != B:
            ans = max(ans, dfs(N, X, cnt-1))
        B = rotate90(N, B)
    return ans


print(dfs(N, maps, 5))
