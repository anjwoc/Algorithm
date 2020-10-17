import sys
from itertools import combinations
input: lambda: sys.stdin.readline().strip()


def dfs(n):
    global length, ans

    if n == length-1:
        for i in ans:
            print(i, end=" ")
        exit(0)

    num = 0
    s = ""
    for i in range(n, n+1, 1):
        num = int(s + str(i))

        if num > max_num:
            continue
        if arr[num] == 1:
            continue
        ans.append(num)
        arr[num] = 1
        dfs(i+1)
        arr[num] = 0
        ans.pop()


char = list(input())
arr = [0]*51
ans = []
length = len(char)
max_num = 0
if length > 9:
    max_num = length-9
    max_num /= 2
    max_num += 9
else:
    max_num = length

dfs(0)
