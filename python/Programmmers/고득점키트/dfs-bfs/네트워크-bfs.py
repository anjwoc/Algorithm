def solution(n=3, computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]):
    ans = 0

    def bfs(node, visited):
        que = [node]
        visited[node] = 1
        while que:
            v = que.pop(0)
            for i in range(n):
                if computers[v][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    que.append(i)
        return visited

    visited = [0 for i in range(n)]
    for i in range(n):
        try:
            visited = bfs(visited.index(0), visited)
            ans += 1
        except:
            break
    return ans


print(solution())
