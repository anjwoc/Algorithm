import sys
input: lambda: sys.stdin.readline().strip()


def flip(x, y):
    for i in range(3):
        for j in range(3):
            nx, ny = x+i, y+j
            # XOR 연산
            A[nx][ny] ^= 1


n, m = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(n)]
B = [list(map(int, list(input()))) for _ in range(n)]


ans = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            ans += 1


# 파이써닉하게 출력
print(ans if A == B else -1)
