import sys
from collections import deque
input: lambda: sys.stdin.readline().strip()

n = int(input())
arr = input()

op = [0] * ((n-1) // 2)
lst = []


def go(idx, flag, hist):
    if idx == (n-1) // 2:
        lst.append(hist)
        return
    if flag:
        go(idx+1, False, hist+[0])
    else:
        go(idx+1, True, hist+[1])
        go(idx+1, True, hist+[0])


go(0, False, [])


def cal(a, b, operator):
    if operator == '*':
        return a*b
    elif operator == '+':
        return a+b
    elif operator == '-':
        return a-b


ans = -999999999

for case in lst:
    st = []
    i = 0

    while i < n:
        if i % 2 == 0:
            st.append(arr[i])
        else:
            if case[(i-1) // 2]:
                left = int(st.pop())
                right = int(arr[i+1])
                st.append(cal(left, right, arr[i]))
                i += 1
            else:
                st.append(arr[i])
        i += 1
    first = int(st.pop(0))
    for i in range(0, len(st), 2):
        first = cal(first, int(st[i+1]), st[i])

    ans = max(ans, first)

print(ans)
