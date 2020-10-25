import sys
# import heapq
input: lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    m = int(input().rstrip())
    print((m+1)//2)
    n = int(m / 10)
    n = (m % 10) != 0 and n + 1 or n
    arr = []
    for __ in range(n):
        arr.extend(list(map(int, input().split())))

    for i in range(1, len(arr)+1):
        tmp = sorted(arr[:i])
        if (i+1) % 2 == 0:
            if i == m-1:
                print(tmp[i//2], end='\n')
            else:
                print(tmp[i//2], end=' ')
