from copy import deepcopy


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
questions = [tuple(map(int, input().split())) for _ in range(K)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
ans = 10000


def value(arr):
    return min([sum(i) for i in arr])


def convert(arr, qry):
    r, c, s = qry
    r, c = r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        nr, nc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                ndr, ndc = nr + dx[w], nc + dy[w]
                new_arr[ndr][ndc] = arr[nr][nc]
                nr, nc = ndr, ndc
    return new_arr


def dfs(arr, check):
    global ans
    if sum(check) == K:
        ans = min(ans, value(arr))
        return
    for i in range(K):
        if check[i]:
            continue
        new_arr = convert(arr, questions[i])
        check[i] = 1
        dfs(new_arr, check)
        check[i] = 0


dfs(A, [0 for i in range(K)])
print(ans)
