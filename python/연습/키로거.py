import sys

"""
1. 문자열 크기가 최대 1000000이므로 시뮬레이션 방식으로는 문제를 해결 못한다.
2. 스택을 활용하여 선형시간안에 문제를 풀수 있도록 알고리즘을 설계해야함

1) 스택 두 개를 만들고, 스택 두 개의 중간지점을 커서로 둔다.
2) 문자 입력: 왼쪽 스택에 원소를 삽입
3) - 입력: 왼쪽 스택에서 원소를 삭제
4) < 입력: 왼쪽 스택에서 오른쪽 스택으로 원소를 이동
5) > 입력: 오론쪽 스택에서 왼쪽스택으로 원소를 이동

내가 실수한 접근법: 스택을 두 개 사용한다는 접근까지는 맞았지만 커서를 인덱스로 활용하려하다보니
구현이 복잡해저 에러 발생
"""

input = lambda: sys.stdin.readline().strip()
n = int(input())

for _ in range(n):
    lstk = []
    rstk = []
    data = input()
    for i in data:
        if i == "-":
            if lstk:
                lstk.pop()
        elif i == "<":
            if lstk:
                rstk.append(lstk.pop())
        elif i == ">":
            if rstk:
                lstk.append(rstk.pop())
        else:
            lstk.append(i)
    lstk.extend(reversed(rstk))
    print("".join(lstk))
