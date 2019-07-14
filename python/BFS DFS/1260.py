import sys
n, m, start = map(int, sys.stdin.readline().split())
graph = { }

for i in range(m):
    s, v = map(int, sys.stdin.readline().split())
    if(s not in graph.keys()):
        graph[s] = [v]
    else:
        graph[s].append(v) 


print(graph)



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



