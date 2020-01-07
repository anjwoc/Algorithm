import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# A에서 가장 작은수와 B에서 가장 큰수와 곱해야한다.
A = sorted(A)
B.sort()
B.reverse()

ans = 0
for i in range(len(A)):
    ans += A[i] * B[i]

print(ans)