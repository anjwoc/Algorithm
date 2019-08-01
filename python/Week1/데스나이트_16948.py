import sys
n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
arr = [[0]*(n+1) for _ in range(n+1)]
check = [[False]*(n+1) for _ in range(n+1)]
ans = []
def solve(cnt, r, c):
    global ans
    queue = []
    queue.append((cnt, r, c))
    check[r][c] = True
    while(queue):
        cnt, r, c = queue.pop(0)
        if(r==r2 and c==c2):
            ans.append(cnt)
            return
        else:
            for i in range(6):
                nr = r+dx[i]
                nc = c+dy[i]
                if(nr>=0 and nr<n and nc>=0 and nc<n):
                    if(check[nr][nc] != True):
                        check[nr][nc] = True
                        queue.append((cnt+1, nr,nc))

solve(0, r1, c1)
if(ans == []):
    print("-1")
else:
    print(min(ans))
