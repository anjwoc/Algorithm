import sys
arr = []
for i in range(5):
    tmp = list(map(str, sys.stdin.readline().strip().split()))
    arr.append(tmp)
a = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n = 5
def solve(str, cnt, x, y):
    str += arr[x][y]
    if(cnt == 6):
        a.append(str)
        return
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx>=0 and nx<n and ny>=0 and ny<n):
                solve(str,cnt+1 ,nx, ny)
                    
            

for i in range(n):
    for j in range(n):        
        save = []
        string = ""
        solve(string, 1, i, j)

print(len(list(set(a))))
        



