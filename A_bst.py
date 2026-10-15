# A. BST - дерево поиска без балансировки
import sys

# дерево может выродиться в цепочку из 1000 вершин, рекурсии нужен запас
sys.setrecursionlimit(10000)
input = sys.stdin.readline


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(node, x):
    if node is None:
        return Node(x)
    if x < node.key:
        node.left = add(node.left, x)
    elif x > node.key:
        node.right = add(node.right, x)
    return node


def delete(node, x):
    if node is None:
        return None
    if x < node.key:
        node.left = delete(node.left, x)
    elif x > node.key:
        node.right = delete(node.right, x)
    else:
        # лист или один ребенок
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        # два ребенка: берем минимум из правого поддерева
        m = node.right
        while m.left is not None:
            m = m.left
        node.key = m.key
        node.right = delete(node.right, m.key)
    return node


def exists(node, x):
    while node is not None:
        if x == node.key:
            return True
        if x < node.key:
            node = node.left
        else:
            node = node.right
    return False


def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


def preorder(node, res):
    if node is None:
        return
    res.append(str(node.key))
    preorder(node.left, res)
    preorder(node.right, res)


root = None
ans = []
q = int(input())
for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'add':
        root = add(root, int(cmd[1]))
    elif cmd[0] == 'del':
        root = delete(root, int(cmd[1]))
    elif cmd[0] == 'exists':
        if exists(root, int(cmd[1])):
            ans.append('YES')
        else:
            ans.append('NO')
    elif cmd[0] == 'height':
        ans.append(str(height(root)))
    elif cmd[0] == 'print':
        if root is None:
            ans.append('Empty')
        else:
            keys = []
            preorder(root, keys)
            ans.append(' '.join(keys))

print('\n'.join(ans))
