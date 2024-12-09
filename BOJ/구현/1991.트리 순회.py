import sys
input = sys.stdin.readline

def preorder_traversal(order):
    if order != '.':
        print(order, end='')
        preorder_traversal(tree[order][0])
        preorder_traversal(tree[order][1])

def inorder_traversal(order):
    if order != '.':
        inorder_traversal(tree[order][0])
        print(order, end='')
        inorder_traversal(tree[order][1])

def postorder_traversal(order):
    if order != '.':
        postorder_traversal(tree[order][0])
        postorder_traversal(tree[order][1])
        print(order, end='')

n = int(input())
tree = {}
for _ in range(n):
    parent, *child = input().split()
    tree[parent] = child
preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')