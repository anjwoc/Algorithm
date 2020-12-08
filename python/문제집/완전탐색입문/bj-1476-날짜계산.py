import sys
input = sys.stdin.readline

limits = [15, 28, 19]
e, s, m = map(int, input().split())

a,b,c, = 1,1,1

ans = 1
while True:
    if (a, b, c) == (e, s, m):
        print(ans)
        break
    a += 1
    b += 1
    c += 1
    ans += 1
    if a > limits[0]:
        a = 1
    if b > limits[1]:
        b = 1
    if c > limits[2]:
        c = 1

