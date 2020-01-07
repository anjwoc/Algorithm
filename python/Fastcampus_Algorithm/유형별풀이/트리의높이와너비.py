import sys

class Node:
  def __init__(self, number, Lnode, Rnode):
    self.parent = -1
    self.number = number
    self.Lnode = Lnode
    self.Rnode = Rnode

def in_order(node, level):
  global level_depth, x
  level_depth = max(level_depth, level)
  if node.Lnode != -1:
    in_order(tree[node.Lnode], level+1)
  level_min[level] = min(level_min[level], x)
  level_max[level] = max(level_max[level], x)
  x += 1
  if node.Rnode != -1:
    in_order(tree[node.Rnode], level+1)

n = int(input())
tree = {}
level_min = [n]
level_max = [0]
root = -1
x = 1
level_depth = 1

for i in range(1, n+1):
  tree[i] = Node(i, -1, -1)
  level_min.append(n)
  level_max.append(0)

for _ in range(n):
  number, Lnode, Rnode = map(int, sys.stdin.readline().split())
  tree[number].Lnode = Lnode
  tree[number].Rnode = Rnode
  if Lnode != -1:
    tree[Lnode].parent = number
  if Rnode != -1:
    tree[Rnode].parent = number

for i in range(1, n+1):
  if tree[i].parent == -1:
    root = i

in_order(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1):
  width = level_max[i] - level_min[i] + 1
  if result_width < width:
    result_level = i
    result_width = width

print(result_level, result_width)
