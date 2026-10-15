# C. AVL 2. Вставка
import sys

input = sys.stdin.readline


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def h(node):
    if node is None:
        return 0
    return node.height


def update(node):
    node.height = max(h(node.left), h(node.right)) + 1


# bal(v) = h(R) - h(L)
def bal(node):
    return h(node.right) - h(node.left)


def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    update(a)
    update(b)
    return b


def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    update(a)
    update(b)
    return b


def balance(v):
    update(v)
    b = bal(v)
    if b == 2:
        if bal(v.right) < 0:
            v.right = rotate_right(v.right)
        return rotate_left(v)
    if b == -2:
        if bal(v.left) > 0:
            v.left = rotate_left(v.left)
        return rotate_right(v)
    return v


def add(node, x):
    if node is None:
        return Node(x)
    if x < node.key:
        node.left = add(node.left, x)
    elif x > node.key:
        node.right = add(node.right, x)
    else:
        return node
    # на обратном ходе рекурсии проверяем вершины от родителя нового листа до корня
    return balance(node)


def exists(node, x):
    while node is not None:
        if x == node.key:
            return True
        if x < node.key:
            node = node.left
        else:
            node = node.right
    return False


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
    elif cmd[0] == 'exists':
        if exists(root, int(cmd[1])):
            ans.append('YES')
        else:
            ans.append('NO')
    elif cmd[0] == 'root':
        if root is None:
            ans.append('Empty')
        else:
            ans.append(str(root.key))
    elif cmd[0] == 'height':
        ans.append(str(h(root)))
    elif cmd[0] == 'print':
        if root is None:
            ans.append('Empty')
        else:
            keys = []
            preorder(root, keys)
            ans.append(' '.join(keys))

print('\n'.join(ans))
