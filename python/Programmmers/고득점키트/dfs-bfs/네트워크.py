def solution(n=3, computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        print(computers, visited, start)
        while stack:
            cur = stack.pop()
            print("cur: %d" % (cur))
            if visited[cur] == 0:
                print("visitied[cur]: %d, cur: %d" % (visited[cur], cur))
                visited[cur] = 1
                print("1로 바뀜")
            for i in range(len(computers)):
                # pop한 정점과 연결되어있고 방문하지 않은곳 stack에 저장
                print(
                    "computers[cur][i]: %d visited[i]: %d"
                    % (computers[cur][i], visited[i]),
                    end="  ",
                )
                if computers[cur][i] == 1 and visited[i] == 0:
                    # stack에 저장하고나면 해당정점과 다시 pop하면서 정점과 연결된 곳을 모두 방문함
                    stack.append(i)
                    print(stack)

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    return answer


print(solution())
