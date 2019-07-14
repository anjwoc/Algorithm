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
DFS�� BFS�ʹ� �޸� ���� ���� ĭ�� ���������� ���� 1��ŭ ������ �ִٴ� ������ �������� �ʴ´�.
�Ÿ��� �� ���� BFS�� ����ؾ� �Ѵ�.
������ �迭������ DFS�� ����� ���� ���� ����. Flood fill �� BFS�� ������ �����ϱ� ����
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
        #Queue�϶��� pop(0)���� ���� �ֱٿ� �� ���Ҹ� ����.
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited
print(dfs(graph, 'A'))



