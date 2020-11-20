import sys
input: lambda: sys.stdin.readline().strip()


def bfs(i, j, A):
    for x in range(3):
        for y in range(3):
            nx, ny = i + x, j + y
            A[nx][ny] ^= 1


n, m = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(n)]
B = [list(map(int, list(input()))) for _ in range(n)]


ans = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            bfs(i, j, A)
            ans += 1


if A != B:
    print(-1)
else:
    print(ans)
