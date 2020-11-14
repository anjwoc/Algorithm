import sys
input = sys.stdin.readline


def bfs(x, y, A):
    for i in range(3):
        for j in range(3):
            nx, ny = i + x, j + y
            A[nx][ny] ^= 1  # XOR


n, m = map(int, input().split())
A = [list(map(int, list(input().strip()))) for _ in range(n)]
B = [list(map(int, list(input().strip()))) for _ in range(n)]

ans = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            bfs(i, j, A)
            ans += 1

print(-1 if A != B else ans)
