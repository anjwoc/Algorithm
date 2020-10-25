import sys
input: lambda: sys.stdin.readline().strip()
'''
복습 때 놓친 부분
'''

for _ in range(int(input())):
    arr = list(input())
    st1 = []
    st2 = []
    for i in range(len(arr)):
        data = arr[i]
        if data == '<':
            if st1:
                st2.append(st1.pop())
        elif data == '>':
            if st2:
                st1.append(st2.pop())
        elif data == '-':
            if st1:
                st1.pop()
        else:
            st1.append(data)
    st1.extend(reversed(st2))
    print(''.join(st1))
