import sys
arr = []
for i in range(5):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    arr.append(tmp)

print(arr)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n = 5
def solve(arr,cnt, x, y, a, save):
    if(cnt == 6):
        if(len(save) < 6):
            return
        if save not in a:
            a.append([save])
            save=[]
            
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx>=0 and nx<n and ny>=0 and ny<n):
                save.append(arr[nx][ny])
                solve(arr, cnt+1, nx, ny, a, save)
                    
            

for i in range(n):
    for j in range(n):
        a = []
        save = []
        #chk= [[False]*(n+1) for _ in range(n+1)]
        solve(arr, 0, i, j, a, save)

print(a)
    

        



