import sys
import copy
 
input = sys.stdin.readline
 
def spreadVirus(_virusList, c_arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    spread_virus_count = 0
    global safe_area
 
    while _virusList:
        x, y = _virusList.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx and 0 <= ny and nx < n and ny < m:
                if c_arr[nx][ny] == 0:
                    c_arr[nx][ny] = 2
                    spread_virus_count += 1
                    _virusList.add((nx, ny))
    # 3 : 세운 벽의 수
    # 안전한 공간의 수를 반환
    return safe_area - spread_virus_count - 3
 
 
def setWall(start, wallCount):
    global maxVal
    global n
    global m
 
    # 벽을 다 세운 경우
    if wallCount == 0:
        copy_arr = copy.deepcopy(arr)
        copy_virusList = copy.deepcopy(virusList)
        # 바이러스를 퍼뜨린다.
        sCount = spreadVirus(copy_virusList, copy_arr)
        maxVal = max(sCount, maxVal)
        return
 
    # n번째 원소부터 루프를 돌린다
    for i in range(start, n*m):
        x = i // m # 몫
        y = i % m # 나머지
 
        if arr[x][y] == 0:
            arr[x][y] = 1 # 벽을 세운다
            setWall(i+1, wallCount - 1)
            arr[x][y] = 0 # 최근에 세운 벽을 초기화
 
 
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    posList = []
    virusList = set()
    arr = []
    maxVal = 0
    safe_area = 0
 
    for i in range(n):
        arr.append(list(map(int, input().strip().split())))
 
    for i in range(n):
        for j in range(m):
            v = arr[i][j]
            if v == 2:
                virusList.add((i,j))
            elif v == 0:
                safe_area += 1
    setWall(0, 3)
    print(maxVal)