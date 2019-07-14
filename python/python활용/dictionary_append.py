import sys
n, m, start = map(int, sys.stdin.readline().split())
graph = { }
#type은 int인지 str인지 맘대로 바꾸면 됌
for i in range(m):
    s, v = map(int, sys.stdin.readline().split())
    if(s not in graph.keys()):
        graph[s] = [v]
    else:
        graph[s].append(v) 
print(graph)

'''
input)
4 5 1
1 2
1 3
1 4
2 4
3 4
output)
{1: [2, 3, 4], 2: [4], 3: [4]}
'''
