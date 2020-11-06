import sys
import copy
input: lambda: sys.stdin.readline().strip()


def solve(arr, cnt):
    if cnt == n-1:
        comb.append(copy.deepcopy(arr))
        return
    arr.append(' ')
    solve(arr, cnt+1)
    arr.pop()

    arr.append('+')
    solve(arr, cnt+1)
    arr.pop()

    arr.append('-')
    solve(arr, cnt+1)
    arr.pop()


for _ in range(int(input())):
    n = int(input())
    comb = []
    solve([], 0)

    for op in comb:
        string = ""
        for i in range(1, n):
            string += str(i) + op[i-1]

        string += str(n)
        x = string.replace(' ', '')
        if eval(x) == 0:
            print(string)
    print()
