import sys
from collections import deque
input = sys.stdin.readline

# 버튼 A or B
# A -> N이 1 증가
# B -> (N*2) => (result) => str(int(str(result)[:1])-1) + str(result[1:])


def bfs():
    que = deque()
    que.append(n)
    dist[n] = 0
    while que:
        x = que.popleft()
        if dist[x] > t:
            break
        if x == g:
            print(dist[x])
            return

        dx = [(x+1), (x*2)]
        for i in range(2):
            nx = dx[i]
            if nx > 99999:
                continue

            if i and x:
                # i가 1인 경우에만 조건에 들어옴(B버튼)
                # 1의 자리면 1을 빼고, 10의자리면 10을 뺀다.
                nx -= 10**(len(str(nx))-1)
            if dist[nx] == -1:
                que.append(nx)
                dist[nx] = dist[x]+1
    print("ANG")


n, t, g = map(int, input().split())
dist = [-1] * 100000
bfs()
