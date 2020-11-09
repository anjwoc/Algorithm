import sys
n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 가로, 세로, 대각선의 idx를 각각 0, 1, 2로 설정.
table = [[[0]*3 for _ in range(n)] for _ in range(n)]
# 파이프의 오른쪽 끝만 도착하면 되기 때문에, 파이프 오른쪽을 기준으로 설정
table[0][1][0] = 1

print(maps)
# 첫 위치에서 가로로만 이동하는 방법의 개수
for x in range(2, n):
    if maps[0][x] == 0:
        table[0][x][0] = table[0][x-1][0]
# 이동하기
for y in range(n):
    # x는 idx 1에서부터 출발하고, x가 idx 1로 되돌아가는 방법은 없다.
    # 가로 -> 대각선 -> 세로를 최소한 한 번은 거쳐야 하기 때문
    for x in range(2, n):
        # 가로, 세로, 대각선 어디에서든 대각선으로 머리를 변경할 수 있다.
        # 대각선으로 이동할 수 있는 경우
        if maps[y][x] == maps[y][x-1] == maps[y-1][x] == 0:
            table[y][x][2] = table[y-1][x-1][0] + \
                table[y-1][x-1][1] + table[y-1][x-1][2]
        # 다음 칸으로 움직일 수 있는 경우
        if maps[y][x] == 0:
            # 가로로 이동하는 경우 = 대각선 -> 가로, 가로 -> 가로
            table[y][x][0] = table[y][x-1][2] + table[y][x-1][0]
            # 세로로 움직이는 경우 = 대각선 -> 세로, 세로 -> 세로
            table[y][x][1] = table[y-1][x][2] + table[y-1][x][1]


print(sum(table[-1][-1]))
