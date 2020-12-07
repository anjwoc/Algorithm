import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def pre_order(node):
    # BAC
    print(node.data, end='')
    if node.left != '.':
        pre_order(arr[node.left])
    if node.right != '.':
        pre_order(arr[node.right])


def in_order(node):
    # ABC
    if node.left != '.':
        in_order(arr[node.left])
    print(node.data, end='')
    if node.right != '.':
        in_order(arr[node.right])


def post_order(node):
    # ACB
    if node.left != '.':
        post_order(arr[node.left])
    if node.right != '.':
        post_order(arr[node.right])
    print(node.data, end='')


n = int(input())
arr = {}
for _ in range(n):
    root, left, right = input().split()
    arr[root] = Node(root, left, right)

pre_order(arr['A'])
print()
in_order(arr['A'])
print()
post_order(arr['A'])
