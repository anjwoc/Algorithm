import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

lmax = arr[0]
rmax = arr[-1]
cnt = 1
cnt2 = 1
for i in range(1, n):
    if lmax < arr[i]:
        cnt += 1
        lmax = max(lmax, arr[i])

for i in range(n-1, -1, -1):
    if rmax < arr[i]:
        cnt2 += 1
        rmax = max(rmax, arr[i])

if cnt == n:
    print(cnt)
    print(1)
elif cnt == 1:
    print(1)
    print(cnt2)
else:
    print(cnt)
    print(cnt2)
