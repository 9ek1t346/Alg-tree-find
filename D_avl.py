# D. AVL 3. Полная реализация
import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    if node is None:
        return 0
    return node.height


def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1


# bal(v) = h(R) - h(L)
def get_balance(node):
    return get_height(node.right) - get_height(node.left)


def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    update_height(a)
    update_height(b)
    return b


def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    update_height(a)
    update_height(b)
    return b


# пересчитывает высоту вершины и, если |bal| = 2, делает повороты
# возвращает вершину, которая теперь стоит на месте v
def fix_balance(v):
    update_height(v)
    b = get_balance(v)
    if b == 2:
        if get_balance(v.right) < 0:
            v.right = rotate_right(v.right)
        return rotate_left(v)
    if b == -2:
        if get_balance(v.left) > 0:
            v.left = rotate_left(v.left)
        return rotate_right(v)
    return v


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node
    return fix_balance(node)


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def remove(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = remove(node.left, key)
    elif key > node.key:
        node.right = remove(node.right, key)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        # два ребенка: записываем в вершину минимум правого поддерева,
        # а саму вершину с этим минимумом удаляем из правого поддерева
        m = find_min(node.right)
        node.key = m.key
        node.right = remove(node.right, m.key)
    # балансируем все вершины на пути обратно к корню
    return fix_balance(node)


def contains(node, key):
    while node is not None:
        if key == node.key:
            return True
        if key < node.key:
            node = node.left
        else:
            node = node.right
    return False


# минимальный ключ >= x
def next_key(node, x):
    res = None
    while node is not None:
        if node.key >= x:
            res = node.key
            node = node.left
        else:
            node = node.right
    return res


# максимальный ключ <= x
def prev_key(node, x):
    res = None
    while node is not None:
        if node.key <= x:
            res = node.key
            node = node.right
        else:
            node = node.left
    return res


def preorder(node, res):
    if node is None:
        return
    res.append(str(node.key))
    preorder(node.left, res)
    preorder(node.right, res)


def main():
    input = sys.stdin.readline
    root = None
    ans = []
    q = int(input())
    for _ in range(q):
        cmd = input().split()
        if cmd[0] == 'add':
            root = insert(root, int(cmd[1]))
        elif cmd[0] == 'del':
            root = remove(root, int(cmd[1]))
        elif cmd[0] == 'exists':
            if contains(root, int(cmd[1])):
                ans.append('YES')
            else:
                ans.append('NO')
        elif cmd[0] == 'next':
            ans.append(str(next_key(root, int(cmd[1]))))
        elif cmd[0] == 'prev':
            ans.append(str(prev_key(root, int(cmd[1]))))
        elif cmd[0] == 'root':
            if root is None:
                ans.append('Empty')
            else:
                ans.append(str(root.key))
        elif cmd[0] == 'height':
            ans.append(str(get_height(root)))
        elif cmd[0] == 'print':
            if root is None:
                ans.append('Empty')
            else:
                keys = []
                preorder(root, keys)
                ans.append(' '.join(keys))
    print('\n'.join(ans))


if __name__ == '__main__':
    main()
