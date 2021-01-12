from collections import deque


def move(p1, p2, maps):
    ret = []
    y, x = 0, 1
    x1, y1 = p1
    x2, y2 = p2
    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in delta:
        nxt1 = (p1[y] + dy, p1[x] + dx)
        nxt2 = (p2[y] + dy, p2[x] + dx)

        if maps[nxt1[y]][nxt1[x]] == 0 and maps[nxt2[y]][nxt2[x]] == 0:
            ret.append((nxt1, nxt2))

    # 회전
    if p1[y] == p2[y]:  # 가로 방향
        up, down = -1, 1
        for d in [up, down]:
            if maps[p1[y] + d][p1[x]] == 0 and maps[p2[y] + d][p2[x]] == 0:
                ret.append((p1, (p1[y] + d, p1[x])))
                ret.append((p2, (p2[y] + d, p2[x])))
    else:
        left, right = -1, 1
        for d in [left, right]:
            if maps[p1[y]][p1[x] + d] == 0 and maps[p2[y]][p2[x] + d] == 0:
                ret.append(((p1[y], p1[x] + d), p1))
                ret.append(((p2[y], p2[x] + d), p2))
    return ret


def solution(board):
    ans = 0
    n = len(board)
    maps = [[1] * (n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            maps[i+1][j+1] = board[i][j]

    que = deque([((1, 1), (1, 2), 0)])
    check = set([((1, 1), (1, 2))])

    while que:
        p1, p2, cnt = que.popleft()
        if p1 == (n, n) or p2 == (n, n):
            return cnt
        for nxt in move(p1, p2, maps):
            if nxt not in check:
                que.append((*nxt, cnt+1))
                check.add(nxt)

    return ans
