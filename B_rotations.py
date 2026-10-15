# B. AVL 1. Вращения
import sys

sys.setrecursionlimit(10000)


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


def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    return b


def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    return b


# спускаемся до вершины с ключом x, поворачиваем ее
# и возвращаем новый корень поддерева, чтобы родитель перецепил ссылку
def rotate(node, x, side):
    if node.key == x:
        if side == 'left':
            return rotate_left(node)
        return rotate_right(node)
    if x < node.key:
        node.left = rotate(node.left, x, side)
    else:
        node.right = rotate(node.right, x, side)
    return node


def preorder(node, res):
    if node is None:
        return
    res.append(str(node.key))
    preorder(node.left, res)
    preorder(node.right, res)


data = sys.stdin.read().split()
n = int(data[0])
root = None
for i in range(1, n + 1):
    root = add(root, int(data[i]))

m = int(data[n + 1])
pos = n + 2
ans = []
for _ in range(m):
    side = data[pos]
    x = int(data[pos + 1])
    pos += 2
    root = rotate(root, x, side)
    keys = []
    preorder(root, keys)
    ans.append(' '.join(keys))

print('\n'.join(ans))
