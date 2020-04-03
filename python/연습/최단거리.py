def path_finder(area):
    n = len(area)
    dp = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range]
    dp[0][0] = 0
    dp[0][1] = 1
    dp[1][0] = 1
    que = []
    dx = (-1, 0, 0, 1)
    dy = (1, 0, 0, -1)

    x, y = 0, 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dp
            print()

    return  # total levels climbed


area = "\n".join(["000", "000", "000"])
path_finder(area)
