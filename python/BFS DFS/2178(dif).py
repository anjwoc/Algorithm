import sys
def main():
    n, m = map(int, sys.stdin.readline().split())
    dist = [[0]*m for _ in range(m)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    maze  = [[0]*m for _ in range(n)]
    for i in range(n):
        tmp = sys.stdin.readline()
        for j in range(m):
            maze[i][j] = int(tmp[j])
                    
    dist[0][0] = 1
    queue = []
    queue.append((0,0))
    while(queue):
        x, y = queue.pop(0)
        if(x == n-1 and y == m-1):
            for i in range(n):
                print(dist[i])

            print(dist[x][y])
            sys.exit()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx >= 0 and ny >= 0 and nx < n and ny < m):    
                if(dist[nx][ny]==0 and maze[nx][ny]==1):
                    dist[nx][ny] = 1 + dist[x][y]
                    queue.append((nx, ny))
    
if __name__ == '__main__':
    main()


