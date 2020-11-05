import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data, left, right):
        self.parent = -1
        self.data = data
        self.left = left
        self.right = right


def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, x)
    if node.left != -1:
        in_order(tree[node.left], level+1)

    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1

    if node.right != -1:
        in_order(tree[node.right], level+1)


n = int(input())
tree = {}
level_min = [n]
level_max = [0]
level_depth = 1
x = 1
root = -1


for i in range(1, n+1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    data, left, right = map(int, input().split())
    tree[data].left = left
    tree[data].right = right

    if left != -1:
        tree[left].parent = data

    if right != -1:
        tree[right].parent = data

for i in range(1, n+1):
    if tree[i].parent == -1:
        root = i


in_order(tree[root], 1)

width = level_max[1] - level_min[1] + 1
level = 1

for i in range(2, level_depth + 1):
    w = level_max[i] - level_min[i] + 1

    if width < w:
        width = w
        level = i

print(level, width)
