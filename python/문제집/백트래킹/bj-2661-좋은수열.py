import sys
input = sys.stdin.readline


def solve(idx):
    for i in range(1, (idx // 2) + 1):
        # print(s)
        # print('idx: %d, s[-%d:]: %s s[-2*%d: -%d]: %s' %
        #       (idx, i, s[-1:], i, i, s[-2*i: -i]))
        if s[-i:] == s[-2*i: -i]:
            return -1

    # base condition
    if idx == n:
        for i in range(n):
            print(s[i], end='')
        return 0

    for i in range(1, 4):
        s.append(i)
        if solve(idx+1) == 0:
            return 0
        s.pop()


s = []
n = int(input())
solve(0)
