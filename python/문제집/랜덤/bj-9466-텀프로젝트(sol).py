import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v):
    global cnt
    visited[v] = True  # 방문 표시
    cycle.append(v)  # cycle에 추가
    number = A[v]  # 배열의 현재 인덱스 값

    if visited[number]:
        if number in cycle:
            cnt += len(cycle[cycle.index(number):])
        return
    else:
        dfs(number)


for _ in range(int(input())):
    n = int(input())
    A = [0] + list(map(int, input().split()))

    cnt = 0
    visited = [True] + [False] * n
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-cnt)
