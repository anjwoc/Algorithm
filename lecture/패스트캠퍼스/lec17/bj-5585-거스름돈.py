import sys

input = sys.stdin.readline

n = 1000 - int(input())
rotations = (500, 100, 50, 10, 5, 1)

cnt = 0
for i in rotations:
    if i > n:
        continue
    cnt += n // i
    n = n % i

print(cnt)
