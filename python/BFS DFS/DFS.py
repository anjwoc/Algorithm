graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D', 'G'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['C'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
'''
DFS는 BFS와는 달리 현재 보는 칸이 시작점으로 부터 1만큼 떨어저 있다는 성질이 성립되지 않는다.
거리를 잴 때는 BFS를 사용해야 한다.
다차원 배열에서는 DFS를 사용할 일이 거의 없다. Flood fill 도 BFS로 구현이 가능하기 때문
'''

def bfs(graph, start):
    visited = []
    queue = [start]

    while(queue):
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while(stack):
        #Queue일때는 pop(0)으로 가장 최근에 들어간 원소를 뺀다.
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited
print(dfs(graph, 'A'))



