import sys
input = sys.stdin.readline
'''
N은 14보다 작거나 같은 정수
시간 복잡도는 4^14이지만 가지치기 될거를 고려하면 
최초에만 갈 수 있는 방향이 4방향이고 이후부터는 왔던 길로는 돌아갈 수 없기때문에
계속 3방향만 갈 수 있어서 건너 뛰거나 가지치기를 안해도 4 * 3^14 이다.
위 숫자는 대략 600만이여서 cpp의 경우 1초에 1억 파이썬의 경우 1초에 2천만~5천만으로 생각하면 넉넉하다.
'''
n, east, west, south, north = list(map(int, input().split()))
probs = [east/100, west/100, south/100, north/100]
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
ans = 0


def dfs(x, y, act, prob, visited):
    global ans
    if act == n:
        if len(set(visited)) == n+1:
            # 같은 곳을 방문하면 n+1보다 작아진다.
            ans += prob
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, act+1, prob*probs[i], visited)
            visited.pop()


dfs(0, 0, 0, 1, [(0, 0)])
print(ans)
