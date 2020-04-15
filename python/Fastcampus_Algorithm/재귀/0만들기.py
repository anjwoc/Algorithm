import sys
import copy

input = lambda: sys.stdin.readline().strip()
"""
3<=n<=9로 n의 범위가 작기때문에 완전탐색으로 해결 가능
"""


def recursive(arr, n):
    global op_list
    if len(arr) == n:
        op_list.append(copy.deepcopy(arr))
        return
    arr.append(" ")
    recursive(arr, n)
    arr.pop()

    arr.append("+")
    recursive(arr, n)
    arr.pop()

    arr.append("-")
    recursive(arr, n)
    arr.pop()


t = int(input())
for _ in range(t):
    op_list = []
    n = int(input())
    recursive([], n - 1)
    integers = [i for i in range(1, n + 1)]  # 수열
    for op in op_list:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + op[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()
