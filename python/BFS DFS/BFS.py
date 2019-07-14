'''
append함수는 object를 맨 뒤에 추가한다.
extend함수는 iterable 객체(list, tuple, dictionary)의 엘리먼트들을 list에 appending 시킨다.
'''
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


def bfs(graph, start):
    visited = []
    queue = [start]
    
    while(queue):
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            print("graph[node] : "+str(graph[node]))
            queue.extend(graph[node])
    return visited

print(bfs(graph, 'A'))

def bfs_paths(graph, start, goal):
    result = []
    queue = [(start, [start, goal])]

    while(queue):
        #(node, [start, end])의 형태인 튜플이기 때문에 unpacking해서 나눠 들어간다.
        node, path = queue.pop(0)
        if(node == goal):
            result.append(path)
        else:
            for m in graph[node]:
                queue.append((m, path+[m]))
    return result

print(bfs_paths(graph, 'A', 'M'))


